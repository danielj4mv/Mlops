from fastapi import FastAPI  # Para crear el API

from prediction_request import PredictionRequest
import model_1.model
import model_2.model


app = FastAPI(docs_url="/")  # Creacion del app
app.title = "Clasificador de especies de pingunos"
app.version = "0.0.1"


@app.post("/predict", response_model=list[str], tags=["Modelo_1"])
def predict(request: PredictionRequest) -> list[str]:
    """Predice la especie del pinguino a partir de la peticiopn en formato JSON usando el Modelo 1

    Args:
        request (PredictionRequest): JSON de entrada a la API

    Returns:
        list[str]: Lista de strings con las predicciones generadas
    """
    return model_1.model.get_prediction(request)


@app.post("/predict-alt", response_model=list[str], tags=["Modelo_2"])
def predict(request: PredictionRequest) -> list[str]:
    """Predice la especie del pinguino a partir de la peticiopn en formato JSON usando el Modelo 2

    Args:
        request (PredictionRequest): JSON de entrada a la API

    Returns:
        list[str]: Lista de strings con las predicciones generadas
    """
    return model_2.model.get_prediction(request)
