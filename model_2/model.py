# Librerias externas (Opcional)
from pickle import load
from pandas import DataFrame, concat, get_dummies

import os

# Paquetes del proyecto (Necesario)
from prediction_request import PredictionRequest
from utils import transform_to_dataframe

# Librerias importadas
from pickle import load
import pandas as pd
import numpy as np


# Importacion de modelos y pipelines de procesamiento de datos
folder_dir = os.path.dirname(__file__)  # Ruta de la carpeta de este arcivo

# importacion del modelo
model = load(open(os.path.join(folder_dir, 'model_xgboost.pkl'), 'rb'))
# importacion del pipeline
scaler = load(open(os.path.join(folder_dir, 'scaler.pkl'), 'rb'))

# Columnas usadas en procesamiento (sin importancia)
columnas = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Delta 15 N (o/oo)',
                         'Delta 13 C (o/oo)', 'Flipper Length (mm)', 'Body Mass (g)', 'Clutch Completion', 'Sex', 'Island']


# procesamiento de los datos (Necesario)
def preprocessing_data(request: PredictionRequest):

    """Aplica el pipeline de procesamiento sobre el JSON de la peticion

    Args:
        request (PredictionRequest): JSON de entrada a la API
    """

    trans_df = transform_to_dataframe(request) # Convierte el json a un DataFrame (Necesario)
    # A eleccion propia lo que quieran hacer en el resto de la funcion
    df = DataFrame(columns=columnas)
    df = concat([df, get_dummies(trans_df)], ignore_index=True)[
        columnas].fillna(0)
    return scaler.transform(df)



class Clasificador():
    # Constructor de la clase que acepta un DataFrame como argumento
    def __init__(self, new_data: pd.DataFrame):
        self.model = load(open('model_xgboost.pkl', 'rb'))  # Modelo Importado
        self.columnas = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Delta 15 N (o/oo)',
                         'Delta 13 C (o/oo)', 'Flipper Length (mm)', 'Body Mass (g)', 'Clutch Completion', 'Sex', 'Island']
        self.new_data = new_data  # Almacena el nuevo DataFrame

    def one_hot_function(self,data, column_name,target_categories = ['A', 'B', 'C', 'D']):

    # Crear un DataFrame con las columnas dummy
       dummy_columns = pd.DataFrame(index=data.index)
       for category in target_categories:
            dummy_column_name = f"{column_name}_{category}"
        # Codificación para cada categoría
            dummy_columns[dummy_column_name] = (data[column_name] == category).astype(int)

    # Concatenar las columnas dummy al DataFrame original
       data_encoded = pd.concat([data, dummy_columns], axis=1)
       del(data_encoded[column_name])
       return(data_encoded)

    def preproc(self):
        # Procesamiento de los datos utilizando el DataFrame almacenado

        df = self.new_data.loc[:, self.columnas]
        df["Body_Mass_ln"] = np.where(np.log(df['Body Mass (g)']) == np.nan, 0, np.log(df['Body Mass (g)']))
        df["Flipper_Length_ln"] = np.where(np.log(df['Flipper Length (mm)']) == np.nan, 0, np.log(df['Flipper Length (mm)']))
        col_one_hot = ['Island', "Clutch Completion", 'Sex']
        df = df.dropna()


        dfa_1 = self.one_hot_function(df.loc[:,["Sex"]],"Sex", ["MALE","FEMALE"])
        dfa_2 = self.one_hot_function(df.loc[:,["Clutch Completion"]],"Clutch Completion", ["Yes","No"])
        dfa_3 = self.one_hot_function(df.loc[:,["Island"]],"Island", ["Biscoe","Torgersen","Dream"])
        df_concatenado = pd.concat([df,dfa_1, dfa_2, dfa_3], axis=1)
        df_final = df_concatenado.loc[:,['Culmen Length (mm)', 'Culmen Depth (mm)', 'Delta 15 N (o/oo)',
       'Delta 13 C (o/oo)', 'Body_Mass_ln', 'Flipper_Length_ln',
       'Island_Biscoe', 'Island_Dream', 'Island_Torgersen',
       'Clutch Completion_No', 'Clutch Completion_Yes', 'Sex_FEMALE',
       'Sex_MALE']]
        return(df_final)

    def predict(self):
        """
        Realiza la predicción utilizando el DataFrame almacenado.
        """

        prediction = self.model.predict(self.preproc())
        reemplazos = {0: 'Adelie Penguin (Pygoscelis adeliae)', 1: 'Chinstrap penguin (Pygoscelis antarctica)', 2: 'Gentoo penguin (Pygoscelis papua)'}

        # Comprensión de lista para reemplazar los valores
        prediction_f = [reemplazos[valor] for valor in prediction]

        return list(prediction_f)






# Prediccion (Necesario)
def get_prediction(request: PredictionRequest) -> list[str]:

    """Genera la prediccion a partir de la peticion en formato JSON

    Args:
        request (PredictionRequest): JSON de entrada a la API

    Returns:
        list[str]: Lista de strings con las predicciones generadas
    """

    data_to_predict = preprocessing_data(request) # Preprocesamiento (Necesario) 
    # A eleccion propia lo que quieran hacer en el resto de la funcion
    prediction = model.predict(data_to_predict)
    return list(prediction) # Debe entregar una lista de strings con las predicciones
