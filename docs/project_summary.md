# Vantara Customer Intelligence Platform – Project Summary

## Project Objective
To analyze retail customer behavior and build predictive models that support customer retention and business decision-making.

## Dataset
UCI Online Retail II dataset (Dataset ID: 502).

## Data Processing
- Loaded and combined both Excel sheets.
- Removed duplicates and invalid transaction records.
- Handled missing customer information.
- Created a cleaned dataset of 779,425 records.

## Feature Engineering
- RFM metrics
- Customer behavioral features
- Purchase frequency and monetary value
- Average order value and basket size
- Customer segmentation labels

## Machine Learning
- Churn classification using six models.
- ANN achieved the highest F1 score: 80.16%.
- CLV regression for future 90-day revenue.
- K-Means and DBSCAN segmentation.

## Deep Learning
- ANN churn prediction.
- LSTM purchase sequence modeling.
- Autoencoder anomaly detection.

## Explainability
- SHAP
- LIME
- Partial Dependence

## Application
- Streamlit dashboard
- FastAPI prediction service
- PostgreSQL integration
- Docker configuration

## Conclusion
Vantara combines customer analytics, machine learning, deep learning and visualization into a customer intelligence platform. Further model validation and deployment testing are required before production use.
