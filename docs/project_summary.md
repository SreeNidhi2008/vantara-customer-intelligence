# VANTARA – Customer Intelligence Platform

## 1. Project Overview
VANTARA is a customer intelligence platform designed to analyze retail purchasing behavior, identify customers at risk of churn, estimate future customer revenue, and discover customer segments.

## 2. Dataset
- Source: UCI Machine Learning Repository
- Dataset: Online Retail II
- Cleaned transaction records: 779,425
- Identified customers: 5,878
- Products: 4,631
- Countries: 41
- Total recorded revenue: £17,374,804.27

Citation:
Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository.

## 3. Data Processing
- Removed duplicate records.
- Handled missing customer IDs and descriptions.
- Excluded cancelled invoices from the modeling dataset.
- Removed non-positive quantities and prices.
- Created revenue and customer-level behavioral features.

## 4. Machine Learning
Churn prediction models:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Support Vector Machine
- Artificial Neural Network

Best recorded churn model:
- ANN
- Accuracy: 76.63%
- Precision: 77.13%
- Recall: 83.44%
- F1-score: 80.16%

## 5. Customer Segmentation
- RFM-based customer segments
- K-Means clustering
- DBSCAN clustering
- K-Means silhouette score: 0.4322

## 6. Advanced Analytics
- Customer Lifetime Value proxy using future 90-day revenue
- LSTM purchase sequence modeling
- Autoencoder-based anomaly detection
- SHAP and LIME explainability

## 7. Application
- Streamlit customer intelligence dashboard
- FastAPI churn prediction endpoint
- PostgreSQL integration groundwork
- Automated test suite
- Docker configuration (optional; not required to run the application)

## 8. Testing
Latest recorded automated test result:
- 8 tests passed
- 0 tests failed

## 9. Limitations
- Future 90-day revenue is a CLV proxy, not true lifetime value.
- Return records were excluded from the modeling dataset.
- LSTM evaluation requires further leakage-safe validation.
- Model performance should be monitored on newer retail data.

## 10. Conclusion
VANTARA combines customer analytics, machine learning, explainability, and an interactive dashboard to support data-driven retail decisions.
