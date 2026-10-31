import streamlit as st

# VANTARA CUSTOM THEME
st.markdown("""
<style>
.stApp {
    background: #F4F7FB;
    color: #172B4D;
}

[data-testid="stSidebar"] {
    background: #10243A;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

h1, h2, h3 {
    color: #10243A;
    font-weight: 700;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #E2EAF2;
    box-shadow: 0 3px 12px rgba(16, 36, 58, 0.06);
}

[data-testid="stMetricLabel"] {
    color: #64748B;
}

[data-testid="stMetricValue"] {
    color: #087E8B;
    font-weight: 700;
}

.stButton > button {
    background: #087E8B;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 18px;
}

.stButton > button:hover {
    background: #06636D;
    color: white;
}

hr {
    border-color: #DCE5EF;
}

/* VANTARA OVERVIEW POLISH */
h1 {
    font-size: 2.5rem !important;
    letter-spacing: -1.2px;
    margin-bottom: 8px;
}

h2 {
    font-size: 1.55rem !important;
    margin-top: 24px;
}

[data-testid="stMetric"] {
    min-height: 125px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-radius: 16px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(16, 36, 58, 0.10);
}

[data-testid="stMetricLabel"] p {
    font-size: 0.9rem;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    font-size: 2rem;
}

[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E2EAF2;
    border-radius: 14px;
    padding: 10px;
}


/* VANTARA SIDEBAR DESIGN */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10243A 0%, #183B50 100%);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    color: #FFFFFF !important;
    font-size: 1.8rem !important;
    letter-spacing: 1px;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #C5D8E5 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(255,255,255,0.05);
    border-radius: 9px;
    padding: 8px 12px;
    margin-bottom: 6px;
    transition: background 0.2s ease;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(8,126,139,0.45);
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.2);
}


/* VANTARA BRAND IDENTITY */
[data-testid="stAppViewContainer"] .main .block-container {
    padding-top: 2rem;
    max-width: 1450px;
}

[data-testid="stAppViewContainer"] h1:first-of-type {
    border-bottom: 3px solid #087E8B;
    padding-bottom: 14px;
    margin-bottom: 12px;
}

[data-testid="stAppViewContainer"] h2 {
    border-left: 4px solid #087E8B;
    padding-left: 12px;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
    letter-spacing: 2px;
    color: #FFFFFF !important;
}


/* VANTARA PREDICTION FORM */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #FFFFFF;
    border: 1px solid #D5E1EA;
    border-radius: 10px;
}

[data-testid="stNumberInput"] button {
    color: #087E8B;
}

[data-testid="stForm"] {
    background: #FFFFFF;
    padding: 24px;
    border: 1px solid #E2EAF2;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(16,36,58,0.05);
}

[data-testid="stFormSubmitButton"] button {
    background: #087E8B;
    color: #FFFFFF;
    border-radius: 10px;
    border: none;
    font-weight: 700;
    min-height: 45px;
}

[data-testid="stFormSubmitButton"] button:hover {
    background: #06636D;
    color: #FFFFFF;
}


/* VANTARA MODEL PERFORMANCE */
[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #DCE5EF;
    border-radius: 14px;
    overflow: hidden;
}

[data-testid="stTable"] {
    background: #FFFFFF;
    border-radius: 14px;
}

[data-testid="stProgressBar"] > div > div {
    background-color: #087E8B;
}

[data-testid="stCaptionContainer"] {
    color: #64748B;
}


/* VANTARA EXPLAINABILITY */
[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid #E2EAF2;
    background: #FFFFFF;
    padding: 8px;
}

[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #E2EAF2;
    border-radius: 12px;
    margin-bottom: 10px;
}

[data-testid="stInfo"],
[data-testid="stSuccess"],
[data-testid="stWarning"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

import pandas as pd
import os

st.set_page_config(
    page_title="Vantara | Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("Vantara Customer Intelligence Platform")
st.caption("Customer Behaviour Analytics & Prediction Dashboard")

# Load datasets
customers = pd.read_csv("data/processed/customer_features.csv")
churn = pd.read_csv("data/processed/churn_dataset.csv")
clv = pd.read_csv("data/processed/clv_dataset.csv")
segments = pd.read_csv("data/processed/customer_segments.csv")
comparison = pd.read_csv("reports/churn_model_comparison.csv")

# Sidebar
st.sidebar.title("Vantara")
page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Customer Segmentation",
        "Churn Analysis",
        "CLV Analysis",
        "Model Performance",
        "Explainability",
        "Churn Prediction"
    ]
)

# OVERVIEW
if page == "Overview":
    st.header("Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", f"{len(customers):,}")
    col2.metric("Churn Rate", f"{churn['Churn'].mean() * 100:.1f}%")
    col3.metric("Total Revenue", f"£{customers['Monetary'].sum():,.0f}")
    col4.metric("Customer Segments", customers["Customer_Segment"].nunique())

    st.subheader("Customer Segment Distribution")

    segment_counts = customers["Customer_Segment"].value_counts()
    st.bar_chart(segment_counts)

    st.subheader("Churn Distribution")
    churn_counts = churn["Churn"].value_counts()
    churn_counts.index = ["Active" if i == 0 else "Churned" for i in churn_counts.index]
    st.bar_chart(churn_counts)

# CUSTOMER SEGMENTATION
elif page == "Customer Segmentation":
    st.header("Customer Segmentation")

    segment_counts = customers["Customer_Segment"].value_counts()

    st.subheader("Customer Distribution")
    st.bar_chart(segment_counts)

    st.subheader("Segment Revenue")

    revenue = customers.groupby("Customer_Segment")["Monetary"].sum()
    st.bar_chart(revenue)

    st.subheader("Customer Records")
    st.dataframe(customers, use_container_width=True)

# CHURN ANALYSIS
elif page == "Churn Analysis":
    st.header("Customer Churn Analysis")

    col1, col2 = st.columns(2)

    col1.metric(
        "Churned Customers",
        f"{(churn['Churn'] == 1).sum():,}"
    )

    col2.metric(
        "Active Customers",
        f"{(churn['Churn'] == 0).sum():,}"
    )

    st.subheader("Churn Distribution")
    st.bar_chart(churn["Churn"].value_counts())

    st.subheader("Churn Dataset")
    st.dataframe(churn, use_container_width=True)

# CLV ANALYSIS
elif page == "CLV Analysis":
    st.header("Customer Lifetime Value Analysis")

    col1, col2 = st.columns(2)

    col1.metric(
        "Average Predicted 90-Day Revenue",
        f"£{clv['Future_90_Day_Revenue'].mean():,.2f}"
    )

    col2.metric(
        "Customers with Future Revenue",
        f"{(clv['Future_90_Day_Revenue'] > 0).sum():,}"
    )

    st.subheader("Future 90-Day Revenue Distribution")
    st.bar_chart(
        clv["Future_90_Day_Revenue"].clip(upper=10000)
    )

    st.caption("Revenue values are actual future 90-day revenue labels used to train the baseline CLV model, not individual model predictions.")

# MODEL PERFORMANCE
elif page == "Model Performance":
    st.header("Churn Model Performance")

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("F1 Score Comparison")

    chart_data = comparison.set_index("Model")[["F1 Score"]]
    st.bar_chart(chart_data)

    best_model = comparison.sort_values(
        "F1 Score", ascending=False
    ).iloc[0]

    st.success(
        f"Best model: {best_model['Model']} "
        f"(F1 Score: {best_model['F1 Score']:.4f})"
    )

# EXPLAINABILITY
elif page == "Explainability":
    st.header("Model Explainability")

    charts = {
        "SHAP Summary": "reports/figures/shap_summary.png",
        "SHAP Feature Importance": "reports/figures/shap_feature_importance.png",
        "LIME Customer Explanation": "reports/figures/lime_customer_explanation.png"
    }

    for title, path in charts.items():
        st.subheader(title)

        if os.path.exists(path):
            st.image(path, use_container_width=True)
        else:
            st.warning(f"Chart not found: {path}")

st.sidebar.markdown("---")
st.sidebar.caption("Vantara Customer Intelligence Platform")







