import pandas as pd
from pathlib import Path

def test_cleaned_data_exists():
    assert Path("data/processed/cleaned_retail_data.csv").exists()

def test_customer_features_exist():
    assert Path("data/processed/customer_features.csv").exists()

def test_churn_dataset_exists():
    assert Path("data/processed/churn_dataset.csv").exists()

def test_cleaned_data_quality():
    df = pd.read_csv("data/processed/cleaned_retail_data.csv")

    assert not df.empty
    assert df["Customer ID"].notna().all()
    assert (df["Quantity"] > 0).all()
    assert (df["Price"] > 0).all()
    assert not df.duplicated().any()

def test_churn_labels():
    df = pd.read_csv("data/processed/churn_dataset.csv")

    assert set(df["Churn"].unique()).issubset({0, 1})
    assert not df["Churn"].isna().any()
