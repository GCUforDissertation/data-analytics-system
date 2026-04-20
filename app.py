import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Integrated Data Analytics System", layout="wide")
st.sidebar.title("📊 Navigation")
st.sidebar.info("""
Integrated Data Analytics System  

Group 79 Project  
""")

st.sidebar.markdown("### Instructions")
st.sidebar.write("Upload a CSV file to begin analysis.")
st.markdown("""
<style>
.header-box {
    background: linear-gradient(90deg, #2c3e50, #3498db);
    padding: 20px;
    border-radius: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-box">
    <h1>📊 Integrated Data Analytics System</h1>
    <p>Group 79 – Data Analytics Project</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
### Welcome 👋  

**Group 79 – Data Analytics Project**

This platform helps you perform data analysis easily by:
- Uploading datasets
- Cleaning data
- Visualising trends
- Generating insights
""")

st.markdown("---")

st.markdown("### 🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.info("📁 Upload CSV Data\n\nEasily upload datasets for analysis.")

    st.info("🧹 Data Cleaning\n\nAutomatic handling of missing values.")

with col2:
    st.info("📈 Visualisation\n\nInteractive charts and trends.")

    st.info("🤖 Insights\n\nAutomated summary statistics.")
    
st.markdown("## 🔍 How to Use This System")

st.success("""
1. Upload your dataset (CSV format)  
2. Explore raw and cleaned data  
3. View visualisations and trends  
4. Analyse automated insights  
""")
st.markdown("---")  
# Upload file
st.markdown("## 📤 Upload Your Dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if not uploaded_file:
    st.warning("⚠️ Please upload a CSV file to begin analysis.")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data Preview")
    st.write(df)

    # Data preprocessing
    df_clean = df.dropna()

    st.subheader("🧹 Cleaned Data")
    st.write(df_clean)

    # Visualisation
    st.subheader("📊 Data Visualisation")
    numeric_cols = df_clean.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:
        st.line_chart(df_clean[numeric_cols])

      # Insight generation
    st.subheader("🤖 Automated Insights")

    st.write("Summary Statistics:")
    st.write(df_clean.describe())

    if len(numeric_cols) > 0:
        max_col = numeric_cols[0]
        st.write(f"Highest value in {max_col}: ", df_clean[max_col].max())
        st.write(f"Lowest value in {max_col}: ", df_clean[max_col].min())