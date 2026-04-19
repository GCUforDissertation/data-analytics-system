import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Integrated Data Analytics System")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.write(df)

    # Data preprocessing
    df_clean = df.dropna()

    st.subheader("Cleaned Data")
    st.write(df_clean)

    # Visualisation
    st.subheader("Data Visualisation")
    numeric_cols = df_clean.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:
        st.line_chart(df_clean[numeric_cols])

    # Insight generation
    st.subheader("Automated Insights")

    st.write("Summary Statistics:")
    st.write(df_clean.describe())

    if len(numeric_cols) > 0:
        max_col = numeric_cols[0]
        st.write(f"Highest value in {max_col}: ", df_clean[max_col].max())
        st.write(f"Lowest value in {max_col}: ", df_clean[max_col].min())