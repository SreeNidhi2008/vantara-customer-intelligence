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
    with st.expander("Dataset Information"):
        st.write("Dataset: UCI Online Retail II")
        st.write("Cleaned transaction records: 779,425")
        st.write("Identified customers: 5,878")
        st.write("Countries represented: 41")
        st.write("Period: December 2009 ? December 2011")

    st.caption("AI-powered customer analytics | Retail intelligence | Data-driven decisions")

    st.header("Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", f"{len(customers):,}")
    col2.metric("Churn Rate", f"{churn['Churn'].mean() * 100:.1f}%")
    col3.metric("Total Revenue", f"£{customers['Monetary'].sum():,.0f}")
    col4.metric("Customer Segments", customers["Customer_Segment"].nunique())


    st.subheader("Revenue Insights")
    revenue_cols = st.columns(2)
    revenue_cols[0].metric(
        "Average Revenue per Customer",
        f"?{customers['Monetary'].mean():,.2f}"
    )
    revenue_cols[1].metric(
        "Median Revenue per Customer",
        f"?{customers['Monetary'].median():,.2f}"
    )

    st.metric(
        "Average Order Value",
        f"?{customers['Average_Order_Value'].mean():,.2f}"
    )


    st.metric(
        "Average Orders per Customer",
        f"{customers['Frequency'].mean():.1f}"
    )

    st.subheader("Customer Segment Distribution")

    segment_counts = customers["Customer_Segment"].value_counts()
    st.bar_chart(segment_counts, horizontal=True)

    st.subheader("Churn Distribution")
    churn_counts = churn["Churn"].value_counts()
    churn_counts.index = ["Active" if i == 0 else "Churned" for i in churn_counts.index]
    st.bar_chart(churn_counts)

# CUSTOMER SEGMENTATION
elif page == "Customer Segmentation":
    st.header("Customer Segmentation")
    top_customer = customers.loc[customers["Monetary"].idxmax()]
    st.metric(
        "Highest Value Customer ID",
        str(int(top_customer["Customer ID"])),
        f"?{top_customer['Monetary']:,.2f} revenue"
    )

    metric_cols = st.columns(3)
    metric_cols[0].metric("Total Customers", f"{len(customers):,}")
    metric_cols[1].metric("Number of Segments", customers["Customer_Segment"].nunique())
    metric_cols[2].metric("Average Customer Revenue", f"?{customers['Monetary'].mean():,.2f}")

    st.info(
        "Customers are grouped by purchasing behaviour, "
        "recency, frequency and monetary value."
    )


    segment_counts = customers["Customer_Segment"].value_counts()

    st.subheader("Customer Distribution")
    st.bar_chart(segment_counts)


    st.subheader("Top 10 Highest Revenue Customers")
    top_customers = customers.nlargest(10, "Monetary")[
        ["Customer ID", "Monetary", "Frequency", "Customer_Segment"]
    ]
    st.dataframe(top_customers, width="stretch", hide_index=True)

    st.subheader("Segment Revenue")

    st.caption("Revenue contribution by customer segment")


    revenue = customers.groupby("Customer_Segment")["Monetary"].sum()
    st.bar_chart(revenue, horizontal=True)

    st.subheader("Customer Records")
    selected_segments = st.multiselect(
        "Filter by Customer Segment",
        options=sorted(customers["Customer_Segment"].dropna().unique()),
        default=sorted(customers["Customer_Segment"].dropna().unique())
    )

    filtered_customers = customers[
        customers["Customer_Segment"].isin(selected_segments)
    ]


    search_id = st.text_input("Search Customer ID")
    if search_id.strip():
        filtered_customers = filtered_customers[
            filtered_customers["Customer ID"].astype(str).str.contains(
                search_id.strip(), case=False, na=False
            )
        ]
        st.caption(f"Search results: {len(filtered_customers):,}")
    st.dataframe(filtered_customers, width="stretch")

    st.caption(f"Showing {len(filtered_customers):,} customers")

    st.download_button(
        "Download Customer Data (CSV)",
        customers.to_csv(index=False).encode("utf-8"),
        "vantara_customer_data.csv",
        "text/csv"
    )


# CHURN ANALYSIS
elif page == "Churn Analysis":
    st.header("Customer Churn Analysis")

    with st.expander("Churn Dataset Details"):
        st.write(f"Customers in churn dataset: {len(churn):,}")
        st.write(f"Active customers: {(churn['Churn'] == 0).sum():,}")
        st.write(f"Churned customers: {(churn['Churn'] == 1).sum():,}")
        st.write("Churn label: No purchase in the future 90-day window.")

    churn_rate = churn["Churn"].mean() * 100
    active_rate = 100 - churn_rate
    rate_cols = st.columns(2)
    rate_cols[0].metric("Churn Rate", f"{churn_rate:.1f}%")
    rate_cols[1].metric("Active Rate", f"{active_rate:.1f}%")

    st.caption(
        "Churn identifies customers who made no purchase "
        "during the defined future 90-day observation window."
    )

    st.metric("Overall Churn Rate", f"{churn['Churn'].mean() * 100:.1f}%")


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
    churn_labels = churn["Churn"].map({
        0: "Active",
        1: "Churned"
    }).value_counts()

    st.bar_chart(churn_labels)


    st.subheader("Customer Status Percentages")
    status_percentages = (
        churn["Churn"].map({0: "Active", 1: "Churned"})
        .value_counts(normalize=True) * 100
    )
    st.bar_chart(status_percentages)

    st.subheader("Churn Dataset")

    churn_filter = st.selectbox(
        "Filter Customer Status",
        ["All", "Active", "Churned"]
    )

    filtered_churn = churn.copy()
    if churn_filter == "Active":
        filtered_churn = churn[ churn["Churn"] == 0 ]
    elif churn_filter == "Churned":
        filtered_churn = churn[ churn["Churn"] == 1 ]

    st.dataframe(filtered_churn, width="stretch")
    st.caption(f"Showing {len(filtered_churn):,} records")

    st.download_button(
        "Download Churn Dataset (CSV)",
        churn.to_csv(index=False).encode("utf-8"),
        "vantara_churn_data.csv",
        "text/csv"
    )


# CLV ANALYSIS
elif page == "CLV Analysis":
    st.header("Customer Lifetime Value Analysis")
    zero_revenue = (clv["Future_90_Day_Revenue"] == 0).sum()
    st.metric("Customers with No Future 90-Day Revenue", f"{zero_revenue:,}")
    st.caption("These customers had no recorded revenue in the future 90-day target window.")

    clv_col1, clv_col2 = st.columns(2)

    clv_col1.metric(
        "Median Future Revenue",
        f"?{clv['Future_90_Day_Revenue'].median():,.2f}"
    )

    clv_col2.metric(
        "Highest Future Revenue",
        f"?{clv['Future_90_Day_Revenue'].max():,.2f}"
    )

    st.info(
        "This analysis uses historical customer behaviour "
        "to examine revenue generated over a future 90-day period. "
        "It is a revenue proxy, not full lifetime value."
    )

    st.metric(
        "Average Actual Future 90-Day Revenue",
        f"?{clv['Future_90_Day_Revenue'].mean():,.2f}"
    )


    col1, col2 = st.columns(2)

    col1.metric(
        "Average Actual Future 90-Day Revenue",
        f"£{clv['Future_90_Day_Revenue'].mean():,.2f}"
    )

    col2.metric(
        "Customers with Future Revenue",
        f"{(clv['Future_90_Day_Revenue'] > 0).sum():,}"
    )


    st.download_button(
        "Download CLV Dataset (CSV)",
        clv.to_csv(index=False).encode("utf-8"),
        "vantara_clv_dataset.csv",
        "text/csv"
    )
    st.subheader("Future 90-Day Revenue Distribution")
    st.bar_chart(
        clv["Future_90_Day_Revenue"].clip(upper=10000)
    )

    st.caption("Revenue values are actual future 90-day revenue labels used to train the baseline CLV model, not individual model predictions.")

# MODEL PERFORMANCE
elif page == "Model Performance":
    st.header("Churn Model Performance")
    best_f1 = comparison["F1 Score"].max()
    st.metric("Best F1 Score", f"{best_f1:.4f}")

    summary_cols = st.columns(2)
    summary_cols[0].metric("Models Compared", f"{len(comparison):,}")
    summary_cols[1].metric("Average F1 Score", f"{comparison['F1 Score'].mean():.3f}")

    st.subheader("Best Performing Model")

    leaderboard = comparison.sort_values(
        "F1 Score", ascending=False
    ).reset_index(drop=True)

    st.success(
        f"Top model: {leaderboard.iloc[0]['Model']} "
        f"| F1 Score: {leaderboard.iloc[0]['F1 Score']:.4f}"
    )


    st.dataframe(
        comparison,
        width="stretch",
        hide_index=True
    )
    st.download_button(
        "Download Model Comparison (CSV)",
        comparison.to_csv(index=False).encode("utf-8"),
        "vantara_model_comparison.csv",
        "text/csv"
    )



    st.caption(
        "Use F1 Score alongside precision, recall and accuracy "
        "when comparing models on the imbalanced churn dataset."
    )


    st.subheader("Precision vs Recall")
    precision_recall = comparison.set_index("Model")[["Precision", "Recall"]]
    st.bar_chart(precision_recall, horizontal=True)

    st.subheader("F1 Score Comparison")

    selected_metric = st.selectbox(
        "Choose Evaluation Metric",
        ["F1 Score", "Accuracy", "Precision", "Recall"]
    )
    chart_data = comparison.set_index("Model")[[selected_metric]]
    st.bar_chart(chart_data, horizontal=True)
    st.caption(
        "F1 Score balances precision and recall. "
        "A higher score indicates a better balance between the two."
    )


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
            st.image(path, width="stretch")
        else:
            st.warning(f"Chart not found: {path}")

st.sidebar.markdown("---")
st.sidebar.caption("Vantara Customer Intelligence Platform")



# VANTARA LIGHT CHART THEME
import matplotlib.pyplot as plt
import plotly.io as pio

pio.templates.default = "plotly_white"

plt.rcParams["figure.facecolor"] = "#F4F7FB"
plt.rcParams["axes.facecolor"] = "#FFFFFF"
plt.rcParams["axes.edgecolor"] = "#DCE5EF"
plt.rcParams["axes.labelcolor"] = "#172B4D"
plt.rcParams["xtick.color"] = "#172B4D"
plt.rcParams["ytick.color"] = "#172B4D"
plt.rcParams["text.color"] = "#172B4D"



# PROJECT INFORMATION
with st.expander("About Vantara Customer Intelligence Platform"):
    st.markdown("""
    **Vantara Retail Solutions**

    An intelligent customer analytics platform designed to:

    - Analyse customer purchasing behaviour
    - Identify customers at risk of churn
    - Estimate future customer revenue
    - Segment customers based on behaviour
    - Explain machine learning predictions

    **Dataset:** UCI Online Retail II

    **Technologies:** Python, Pandas, Scikit-learn,
    TensorFlow, FastAPI and Streamlit.
    """)


# VANTARA FOOTER
st.divider()
st.markdown(
    "<div style='text-align:center;color:#718096;padding:12px;'>"
    "<b>VANTARA</b> | Customer Intelligence Platform<br>"
    "Turning retail data into actionable customer insights"
    "</div>",
    unsafe_allow_html=True
)
