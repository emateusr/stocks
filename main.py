from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

class ApiInput(BaseModel):
    features: List[float] 

class ApiOutput(BaseModel):
    forecast: float 

app = FastAPI()

try:
    model = joblib.load("model.joblib")
except FileNotFoundError:
    print("Error: 'model.joblib' no se encontró en el servidor.")

@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    forecast = model.predict([data.features])[0]
    return ApiOutput(forecast=forecast)
