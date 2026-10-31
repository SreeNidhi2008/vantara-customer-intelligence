from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = FastAPI(
    title="Vantara Customer Intelligence API",
    description="Customer churn prediction using ANN",
    version="2.0.0"
)

# Load the best-performing ANN model and its scaler
model = load_model("models_artifacts/ann_churn.keras")
scaler = joblib.load("models_artifacts/ann_scaler.pkl")

class CustomerData(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float
    Average_Order_Value: float
    Customer_Lifetime_Days: float

@app.get("/")
def home():
    return {
        "message": "Vantara Customer Intelligence API",
        "model": "Artificial Neural Network",
        "status": "Running"
    }

@app.post("/predict/churn")
def predict_churn(customer: CustomerData):

    data = np.array([[
        customer.Recency,
        customer.Frequency,
        customer.Monetary,
        customer.Average_Order_Value,
        customer.Customer_Lifetime_Days
    ]])

    scaled_data = scaler.transform(data)

    probability = float(model.predict(scaled_data, verbose=0)[0][0])
    prediction = 1 if probability >= 0.5 else 0

    return {
        "model": "ANN",
        "churn_prediction": "Churned" if prediction == 1 else "Active",
        "churn_probability": round(probability, 4)
    }
