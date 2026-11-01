import pandas as pd
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_api_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running"

def test_churn_prediction():
    df = pd.read_csv("data/processed/churn_dataset.csv")
    customer = df.iloc[0]

    payload = {
        "Recency": float(customer["Recency"]),
        "Frequency": float(customer["Frequency"]),
        "Monetary": float(customer["Monetary"]),
        "Average_Order_Value": float(customer["Average_Order_Value"]),
        "Customer_Lifetime_Days": float(customer["Customer_Lifetime_Days"])
    }

    response = client.post("/predict/churn", json=payload)

    assert response.status_code == 200

    result = response.json()
    assert result["model"] == "ANN"
    assert result["churn_prediction"] in ["Active", "Churned"]
    assert 0 <= result["churn_probability"] <= 1

