import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "Model", "linear_regression_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "Model", "scaler.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# FastAPI app
app = FastAPI(title="Manufacturing Output Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    injection_temperature: float
    injection_pressure: float
    cycle_time: float
    cooling_time: float
    material_viscosity: float
    ambient_temperature: float
    machine_age: float
    operator_experience: float
    hours_since_last_maintenance: float
    temperature_pressure_ratio: float
    total_cycle_time: float
    efficiency_score: float
    machine_utilization: float

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[
        data.injection_temperature,
        data.injection_pressure,
        data.cycle_time,
        data.cooling_time,
        data.material_viscosity,
        data.ambient_temperature,
        data.machine_age,
        data.operator_experience,
        data.hours_since_last_maintenance,
        data.temperature_pressure_ratio,
        data.total_cycle_time,
        data.efficiency_score,
        data.machine_utilization
    ]])
    
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    return {"predicted_hours": float(prediction[0])}