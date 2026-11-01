# VANTARA – Customer Intelligence Platform

**An AI-powered retail analytics platform for customer behavior analysis, churn prediction, and customer segmentation.**

## 1. Project Overview

VANTARA is a customer intelligence platform developed to help retail businesses understand customer purchasing behavior, identify customers at risk of churn, estimate future customer revenue, and discover valuable customer segments.

## 2. Project Objectives

- Analyze customer purchasing patterns.
- Predict customer churn using machine learning.
- Estimate future 90-day customer revenue.
- Segment customers based on purchasing behavior.
- Detect unusual customer activity.
- Explain machine learning predictions.
- Provide an interactive analytics dashboard.

## 3. Dataset

**Dataset:** UCI Online Retail II

- Cleaned transaction records: 779,425
- Identified customers: 5,878
- Unique products: 4,631
- Countries: 41
- Recorded revenue: £17,374,804.27

**Dataset Citation:**

Chen, D. (2012). *Online Retail II* [Dataset]. UCI Machine Learning Repository.

## 4. Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- TensorFlow and Keras
- XGBoost
- SHAP and LIME
- FastAPI
- Streamlit
- PostgreSQL integration groundwork

## 5. Machine Learning Models

### Churn Prediction
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Support Vector Machine
- Artificial Neural Network (ANN)

### Other Analytics
- K-Means clustering
- DBSCAN clustering
- CLV proxy regression
- LSTM purchase sequence modeling
- Autoencoder anomaly detection

## 6. Best Recorded Churn Model

**Artificial Neural Network (ANN)**

| Metric | Score |
|---|---:|
| Accuracy | 76.63% |
| Precision | 77.13% |
| Recall | 83.44% |
| F1-score | 80.16% |

K-Means silhouette score: **0.4322**

## 7. Main Application Features

- Customer Intelligence Dashboard
- Customer Segmentation
- Churn Analysis
- Future Revenue Analysis
- Model Performance Comparison
- SHAP and LIME Explainability
- Individual Customer Churn Prediction
- FastAPI Prediction Endpoint

## 8. How to Run the Project

### Step 1: Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 2: Start the FastAPI backend

```powershell
uvicorn api.main:app --reload --port 8000
```

API documentation: http://127.0.0.1:8000/docs

### Step 3: Start the Streamlit dashboard

Open another terminal:

```powershell
streamlit run frontend/app.py
```

Dashboard: http://localhost:8501

### Alternative: Start both services

```powershell
.\start_vantara.ps1
```

## 9. Run Automated Tests

```powershell
$env:PYTHONPATH = (Get-Location).Path
pytest -v
```

Latest recorded result: **8 tests passed.**

## 10. Project Limitations

- Future 90-day revenue is used as a CLV proxy, not true lifetime customer value.
- Cancelled invoices and non-positive transactions were excluded from the modeling dataset.
- LSTM evaluation requires further leakage-safe validation.
- Model performance should be monitored using newer customer data.

## 11. Project Structure

```text
vantara-customer-intelligence/
├── api/
├── config/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── docs/
├── frontend/
├── models_artifacts/
├── notebooks/
├── reports/
├── src/
├── tests/
├── requirements.txt
├── README.md
└── start_vantara.ps1
```

## 12. Conclusion

VANTARA combines data analytics, machine learning, customer segmentation, explainable AI, and interactive visualization to support smarter retail business decisions.