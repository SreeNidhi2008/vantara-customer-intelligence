# VANTARA – Project Demonstration Guide

## 1. Introduction
VANTARA is an AI-powered Customer Intelligence Platform designed to help retail businesses understand customer behavior, identify churn risk, segment customers, and estimate future revenue.

## 2. Dataset
- Dataset: UCI Online Retail II
- Original records: 1,067,371
- Cleaned records: 779,425
- Identified customers after cleaning: 5,878
- Countries: 41
- Period: December 2009 to December 2011

## 3. Data Processing
Explain how missing customer IDs, duplicate records, cancelled invoices, invalid quantities, and invalid prices were handled.

## 4. Customer Analytics
Demonstrate:
- Recency: how recently a customer purchased
- Frequency: how often a customer purchased
- Monetary: how much a customer spent
- RFM-based customer segments
- Customer purchasing behavior

## 5. Churn Prediction
Explain that customers without a purchase in the future 90-day window are labelled as churned.

Best recorded model: ANN
- Accuracy: 76.63%
- Precision: 77.13%
- Recall: 83.44%
- F1 Score: 80.16%

## 6. Customer Segmentation
Demonstrate the rule-based customer segments and K-Means clustering.
Recorded K-Means silhouette score: 0.4322.

## 7. Revenue Estimation
Explain that the regression model estimates future 90-day customer revenue. This is not true lifetime customer value.

## 8. Explainable AI
Demonstrate SHAP global feature importance and the LIME explanation for one customer prediction.

## 9. Additional AI Components
Introduce the LSTM purchase-sequence model and autoencoder anomaly detection. Do not claim performance results unless you have measured them.

## 10. Technology Stack
Python, Pandas, Scikit-learn, TensorFlow, XGBoost, SHAP, LIME, FastAPI, and Streamlit.

## 11. Limitations
- Historical dataset may not represent current retail behavior.
- Churn is defined using a 90-day future observation window.
- Future 90-day revenue is not lifetime value.
- Model predictions are estimates, not guarantees.
- Some customers have insufficient purchase history to calculate purchase intervals.

## 12. Conclusion
VANTARA demonstrates how retail transaction data can be transformed into customer insights and predictive analytics that support data-driven business decisions.
