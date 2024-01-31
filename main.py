from fastapi import FastAPI
from pydantic import BaseModel
from pickle import load
import pandas as pd


model = load(open('model.pkl', 'rb'))
scaler = load(open('scaler.pkl', 'rb'))

columnas = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)',
            'Island_Biscoe', 'Island_Dream', 'Island_Torgersen', 'Sex_FEMALE']


class PredictionRequest(BaseModel):
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


class PredictionResponse(BaseModel):
    specie: list[str]


def transform_to_dataframe(request: PredictionRequest):
    trans_df = pd.DataFrame([request.model_dump()])
    trans_df.columns = ["studyName", "Sample Number", "Region", "Island", "Stage",
                        "Individual ID", "Clutch Completion", "Date Egg", "Culmen Length (mm)",
                        "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)", "Sex",
                        "Delta 15 N (o/oo)", "Delta 13 C (o/oo)", "Comments"]
    return trans_df


def prerprocessing_data(request: PredictionRequest):
    trans_df = transform_to_dataframe(request)
    df = pd.DataFrame(columns=columnas)
    df = pd.concat([df, pd.get_dummies(trans_df)],
                   ignore_index=True)[columnas].fillna(0)
    return scaler.transform(df)


def get_prediction(request: PredictionRequest) -> str:
    data_to_predict = prerprocessing_data(request)
    prediction = model.predict(data_to_predict)
    return list(prediction)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict", response_model=list[str])
def predict(request: PredictionRequest) -> list[str]:
    return get_prediction(request)
