from pandas import DataFrame

from prediction_request import PredictionRequest


def transform_to_dataframe(request: PredictionRequest) -> DataFrame:

    """Transforma la peticion (El JSON de entrada a la API) en un Dataframe

    Args:
        request (PredictionRequest): JSON de entrada a la API

    Returns:
        DataFrame: DataFrame con la info de la peticion
    """

    # La peticion se convierte a DataFrame
    trans_df = DataFrame([request.model_dump()]) 
    # Se actualiza las columnas para que tengan los nombres del Dataframe Original
    trans_df.columns = ["studyName", "Sample Number", "Region", "Island", "Stage",
                        "Individual ID", "Clutch Completion", "Date Egg", "Culmen Length (mm)",
                        "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)", "Sex",
                        "Delta 15 N (o/oo)", "Delta 13 C (o/oo)", "Comments"]
    return trans_df
