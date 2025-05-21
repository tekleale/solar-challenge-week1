import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("🌞 Solar Radiation Dashboard")

# Sidebar controls
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
variable = st.sidebar.selectbox("Select Variable", ["GHI", "DNI", "DHI", "Tamb"])

@st.cache_data
def load_data(country):
    return pd.read_csv(f"data/processed/{country.lower().replace(' ', '_')}_clean.csv")

try:
    df = load_data(country)
    
    # Time-series plot
    st.subheader(f"{variable} Time Series for {country}")
    fig1, ax1 = plt.subplots(figsize=(12, 4))
    df.set_index("Timestamp")[variable].plot(ax=ax1)
    plt.ylabel(f"{variable} ({'W/m²' if variable in ['GHI','DNI','DHI'] else '°C'})")
    st.pyplot(fig1)
    
    # Distribution plot
    st.subheader(f"Distribution of {variable}")
    fig2, ax2 = plt.subplots()
    sns.histplot(df[variable], kde=True, ax=ax2)
    st.pyplot(fig2)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    col1.metric("Mean", f"{df[variable].mean():.2f}")
    col2.metric("Median", f"{df[variable].median():.2f}")
    col3.metric("Std Dev", f"{df[variable].std():.2f}")
    
except FileNotFoundError:
    st.error("Data not found for selected country")