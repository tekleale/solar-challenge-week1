import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from app.utils import load_data, create_time_series_plot, create_distribution_plot

st.set_page_config(layout="wide", page_title="Solar Radiation Dashboard")
st.title("🌞 Solar Radiation Dashboard")

# Sidebar controls
st.sidebar.header("Controls")
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
variable = st.sidebar.selectbox("Select Variable", ["GHI", "DNI", "DHI", "Tamb", "RH", "WS"])
time_period = st.sidebar.selectbox("Select Time Period", ["All", "Daily", "Monthly"])

try:
    # Load data
    df = load_data(country)
    
    # Overview section
    st.header(f"Solar Radiation Analysis for {country}")
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Mean GHI", f"{df['GHI'].mean():.2f} W/m²")
    col2.metric("Max GHI", f"{df['GHI'].max():.2f} W/m²")
    col3.metric("Mean Temp", f"{df['Tamb'].mean():.2f} °C")
    col4.metric("Mean Wind Speed", f"{df['WS'].mean():.2f} m/s")
    
    # Time-series plot
    st.subheader(f"{variable} Time Series for {country}")
    fig1 = create_time_series_plot(df, variable, time_period)
    st.pyplot(fig1)
    
    # Distribution plot
    st.subheader(f"Distribution of {variable}")
    fig2 = create_distribution_plot(df, variable)
    st.pyplot(fig2)
    
    # Correlation heatmap
    st.subheader("Correlation Matrix")
    corr_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
    corr = df[corr_cols].corr()
    fig3, ax3 = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)
    
    # Data table
    st.subheader("Data Sample")
    st.dataframe(df.head(10))
    
except FileNotFoundError:
    st.error("Data not found for selected country. Please make sure the data files are in the correct location.")
except Exception as e:
    st.error(f"An error occurred: {e}")
