
from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel, Field


# Locate saved model
ROOT_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = (
    ROOT_DIR
    / "models"
    / "house_price_pipeline.joblib"
)

# Load model once when application starts
model = joblib.load(MODEL_PATH)

# Create FastAPI application
app = FastAPI(
    title="House Price Prediction API",
    description="ML model served using FastAPI",
    version="1.0.0"
)


# Define input schema
class HouseFeatures(BaseModel):

    MedInc: float = Field(gt=0)
    HouseAge: float = Field(gt=0)
    AveRooms: float = Field(gt=0)
    AveBedrms: float = Field(gt=0)
    Population: float = Field(gt=0)
    AveOccup: float = Field(gt=0)
    Latitude: float = Field(ge=-90, le=90)
    Longitude: float = Field(ge=-180, le=180)


# Health endpoint
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


# Prediction endpoint
@app.post("/predict")
def predict_house_price(features: HouseFeatures):

    input_data = pd.DataFrame(
        [features.model_dump()]
    )

    prediction = model.predict(input_data)[0]

    return {
        "predicted_value_100k_usd": round(float(prediction), 4),
        "predicted_value_usd": round(float(prediction) * 100000, 2),
        "currency": "USD"
    }
