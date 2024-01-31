# Librerias externas (Opcional)
from pickle import load
from pandas import DataFrame, concat, get_dummies

import os

# Paquetes del proyecto (Necesario)
from prediction_request import PredictionRequest
from utils import transform_to_dataframe

# Importacion de modelos y pipelines de procesamiento de datos
folder_dir = os.path.dirname(__file__)  # Ruta de la carpeta de este arcivo

# importacion del modelo
model = load(open(os.path.join(folder_dir, 'model.pkl'), 'rb'))
# importacion del pipeline
scaler = load(open(os.path.join(folder_dir, 'scaler.pkl'), 'rb'))

# Columnas usadas en procesamiento (sin importancia)
columnas = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)',
            'Island_Biscoe', 'Island_Dream', 'Island_Torgersen', 'Sex_FEMALE']


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
