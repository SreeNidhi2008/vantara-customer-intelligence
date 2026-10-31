# Vantara – Model Evaluation Report

## 1. Churn Prediction Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| ANN | 76.63% | 77.13% | 83.44% | 80.16% |
| XGBoost | 75.21% | 75.30% | 83.61% | 79.24% |
| Random Forest | 75.02% | 77.38% | 78.93% | 78.15% |
| Decision Tree | 73.13% | 74.30% | 80.27% | 77.17% |
| Logistic Regression | 73.04% | 75.61% | 77.26% | 76.43% |
| SVM | 72.66% | 78.66% | 70.90% | 74.58% |

## 2. Best Churn Model

The Artificial Neural Network achieved the highest F1 score of 80.16% among the compared models.

## 3. Customer Segmentation

K-Means clustering:
- Number of clusters: 5
- Silhouette score: 0.4322
- Customers analyzed: 5,878

## 4. CLV Regression

The initial Random Forest regression model achieved:
- MAE: 599.72
- RMSE: 5,653.76
- R²: 0.0244

The target represents future 90-day revenue, not actual lifetime customer value.

## 5. Explainability

The project uses:
- SHAP for global feature importance.
- LIME for individual customer explanations.
- Partial Dependence for feature effect analysis.

## 6. Conclusion

The ANN achieved the strongest churn classification F1 score in the current comparison. The CLV regression model requires further improvement. Segmentation and explainability provide additional insight into customer behavior.

## 7. Evaluation Limitations

Results depend on the selected dataset, preprocessing, feature selection and train-test split. Further validation is required before production deployment.
