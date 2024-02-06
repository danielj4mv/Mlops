# Librerias externas (Opcional)
from pickle import load
from pandas import DataFrame, concat, get_dummies
import numpy as np

import os

# Paquetes del proyecto (Necesario)
from prediction_request import PredictionRequest
from utils import transform_to_dataframe


# Importacion de modelos y pipelines de procesamiento de datos
folder_dir = os.path.dirname(__file__)  # Ruta de la carpeta de este arcivo

# importacion del modelo
model = load(open(os.path.join(folder_dir, 'model_xgboost.pkl'), 'rb'))

# Columnas usadas en procesamiento (sin importancia)
columnas = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Delta 15 N (o/oo)',
            'Delta 13 C (o/oo)', 'Flipper Length (mm)', 'Body Mass (g)', 'Clutch Completion', 'Sex', 'Island']


def one_hot_function(data, column_name, target_categories=['A', 'B', 'C', 'D']):
    dummy_columns = DataFrame(index=data.index)
    for category in target_categories:
        dummy_column_name = f"{column_name}_{category}"
    # Codificación para cada categoría
        dummy_columns[dummy_column_name] = (
            data[column_name] == category).astype(int)

# Concatenar las columnas dummy al DataFrame original
    data_encoded = concat([data, dummy_columns], axis=1)
    del (data_encoded[column_name])
    return (data_encoded)  # procesamiento de los datos (Necesario)


def preprocessing_data(request: PredictionRequest):
    """Aplica el pipeline de procesamiento sobre el JSON de la peticion

    Args:
        request (PredictionRequest): JSON de entrada a la API
    """

    # Convierte el json a un DataFrame (Necesario)
    df = transform_to_dataframe(request)
    # A eleccion propia lo que quieran hacer en el resto de la funcion
    df = df[columnas]
    df["Body_Mass_ln"] = np.where(np.log(df['Body Mass (g)']) == np.nan, 0, np.log(df['Body Mass (g)']))
    df["Flipper_Length_ln"] = np.where(np.log(df['Flipper Length (mm)']) == np.nan, 0, np.log(df['Flipper Length (mm)']))
    col_one_hot = ['Island', "Clutch Completion", 'Sex']
    df = df.dropna()

    dfa_1 = one_hot_function(df.loc[:,["Sex"]],"Sex", ["MALE","FEMALE"])
    dfa_2 = one_hot_function(df.loc[:,["Clutch Completion"]],"Clutch Completion", ["Yes","No"])
    dfa_3 = one_hot_function(df.loc[:,["Island"]],"Island", ["Biscoe","Torgersen","Dream"])
    df_concatenado = concat([df,dfa_1, dfa_2, dfa_3], axis=1)
    df_final = df_concatenado.loc[:,['Culmen Length (mm)', 'Culmen Depth (mm)', 'Delta 15 N (o/oo)',
    'Delta 13 C (o/oo)', 'Body_Mass_ln', 'Flipper_Length_ln',
    'Island_Biscoe', 'Island_Dream', 'Island_Torgersen',
    'Clutch Completion_No', 'Clutch Completion_Yes', 'Sex_FEMALE',
    'Sex_MALE']]
    return(df_final)


# Prediccion (Necesario)
def get_prediction(request: PredictionRequest) -> list[str]:
    """Genera la prediccion a partir de la peticion en formato JSON

    Args:
        request (PredictionRequest): JSON de entrada a la API

    Returns:
        list[str]: Lista de strings con las predicciones generadas
    """

    data_to_predict = preprocessing_data(request)  # Preprocesamiento (Necesario)
    # A eleccion propia lo que quieran hacer en el resto de la funcion
    prediction = model.predict(data_to_predict)
    reemplazos = {0: 'Adelie Penguin (Pygoscelis adeliae)', 1: 'Chinstrap penguin (Pygoscelis antarctica)', 2: 'Gentoo penguin (Pygoscelis papua)'}
    prediction_f = [reemplazos[valor] for valor in prediction]
    # Debe entregar una lista de strings con las predicciones

    return list(prediction_f)
