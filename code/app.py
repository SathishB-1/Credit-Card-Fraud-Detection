import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraud Detection Data Viewer", layout="wide")

# Title
st.title("Credit Card Transactions - Fraud Detection Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load data
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Basic statistics
    st.subheader("Dataset Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transactions", len(df))
        st.metric("Fraudulent Transactions", df['is_fraud'].sum())
    with col2:
        st.metric("Unique Merchants", df['merchant'].nunique())
        st.metric("Total Amount ($)", round(df['amt'].sum(), 2))

    # Fraud analysis
    st.subheader("Fraud vs Non-Fraud Transactions")
    fraud_counts = df['is_fraud'].value_counts().rename(index={0: 'Not Fraud', 1: 'Fraud'})
    st.bar_chart(fraud_counts)

    # Geographic info (optional map)
    if 'lat' in df.columns and 'long' in df.columns:
        st.subheader("Transaction Locations")

        # Rename 'long' to 'lon' for Streamlit compatibility
        df_map = df.rename(columns={'long': 'lon'})
        st.map(df_map[['lat', 'lon']])
    else:
        st.warning("No geographic data available for mapping.")
else:
    st.info("Please upload a CSV file to begin.")
