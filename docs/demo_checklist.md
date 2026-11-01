# VANTARA – Final Demonstration Checklist

## 1. Before the Demonstration
- [ ] Open the VANTARA project in VS Code.
- [ ] Activate the Python virtual environment.
- [ ] Confirm all required datasets are present.
- [ ] Confirm trained model files are present.
- [ ] Run the automated tests.
- [ ] Start the API and Streamlit dashboard.

## 2. Dashboard Demonstration
- [ ] Open the Overview page.
- [ ] Explain the dataset and key business metrics.
- [ ] Show Customer Segmentation.
- [ ] Demonstrate the customer segment filter.
- [ ] Explain the Churn Analysis page.
- [ ] Show CLV Analysis and explain the 90-day revenue target.
- [ ] Show Model Performance and compare the models.
- [ ] Demonstrate SHAP and LIME explainability.
- [ ] Make a sample prediction on the Churn Prediction page.

## 3. API Demonstration
- [ ] Open http://127.0.0.1:8000/docs.
- [ ] Show the GET / endpoint.
- [ ] Show the POST /predict/churn endpoint.
- [ ] Submit sample customer data.
- [ ] Explain the returned churn prediction and probability.

## 4. Technical Explanation
- [ ] Explain data cleaning.
- [ ] Explain RFM feature engineering.
- [ ] Explain the churn prediction target.
- [ ] Explain the train/test split.
- [ ] Compare ANN and XGBoost results.
- [ ] Explain K-Means clustering.
- [ ] Explain model explainability.
- [ ] Discuss project limitations.

## 5. Testing Evidence
- [ ] Show the passing pytest results.
- [ ] Show the test report if generated.
- [ ] Show the project health report.
- [ ] Show the project documentation.

## 6. Final Submission
- [ ] Confirm README.md exists.
- [ ] Confirm docs folder is complete.
- [ ] Confirm requirements.txt exists.
- [ ] Confirm GitHub repository is updated.
- [ ] Keep a backup of the project.
- [ ] Prepare screenshots of important dashboard pages.

## Important Recorded Results
- Cleaned records: 779,425
- Identified customers: 5,878
- Best recorded churn F1-score: 80.16% (ANN)
- K-Means silhouette score: 0.4322
- Latest recorded automated tests: 8 passed

## Presentation Reminder
Explain what each feature does, why it is useful to a retail business, and what its limitations are.
