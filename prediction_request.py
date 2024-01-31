from pydantic import BaseModel


class PredictionRequest(BaseModel):

    """
        Clase con el formato de las peticiones a la API
    """
    
    # definicion de los campos del json de entrada (los que tienen asignado None son opcionales)
    study_name: str = None
    sample_number: int = None
    region: str = None
    island: str
    stage: str = None
    individual_id: str = None
    clutch_completion: str = None
    date_egg: str = None
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass: float
    sex: str
    delta_15_N: float = None
    delta_13_C: float = None
    comments: str = None

    class Config:
        # definicion de un ejemplo para probar rapidamente el funcionamiento del API
        json_schema_extra = {
            "example": {"study_name": "PAL0708",
                        "sample_number": 1,
                        "region": "Anvers",
                        "island": "Torgersen",
                        "stage": "Adult, 1 Egg Stage",
                        "individual_id": "N1A1",
                        "clutch_completion": "Yes",
                        "date_egg": "11\/11\/07",
                        "culmen_length_mm": 39.1,
                        "culmen_depth_mm": 18.7,
                        "flipper_length_mm": 181.0,
                        "body_mass": 3750.0,
                        "sex": "MALE",
                        "delta_15_N": 8.94956,
                        "delta_13_C": -24.69454,
                        "comments": "Not enough blood for isotopes."
                        }
        }
