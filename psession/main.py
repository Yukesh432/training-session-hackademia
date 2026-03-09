from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

from .preprocessing import preprocess_single_input

model = joblib.load("psession/cereal_model.pkl")
scaler = joblib.load("psession/scaler.pkl")
label_encoder = joblib.load("psession/label_encoder.pkl")

app = FastAPI()


class Item(BaseModel):
    name: str
    calories: float
    protein: float
    fat: float
    sodium: float
    fiber: float
    carbo: float
    sugars: float
    potass: float
    weight: float
    cups: float
    shelf: int
    type: str
    vitamins: float
    mfr: str


@app.post("/predict")
async def predict(item: Item):

    df = pd.DataFrame([item.dict()])

    processed_df = preprocess_single_input(df, scaler, label_encoder, model)

    prediction = model.predict(processed_df)

    return {"prediction": float(prediction[0])}