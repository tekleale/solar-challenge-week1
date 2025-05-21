import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(country):
    """
    Load data for a specific country
    
    Parameters:
    -----------
    country : str
        Name of the country (Benin, Sierra Leone, or Togo)
        
    Returns:
    --------
    pandas.DataFrame
        Cleaned data for the specified country
    """
    file_path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
    df = pd.read_csv(file_path)
    
    # Convert timestamp to datetime if it exists
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
    return df

def create_time_series_plot(df, variable, time_period='All'):
    """
    Create a time series plot for a specific variable
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Data frame containing the data
    variable : str
        Variable to plot
    time_period : str
        Time period to plot (All, Daily, Monthly)
        
    Returns:
    --------
    matplotlib.figure.Figure
        Time series plot
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Set the index to timestamp for time series plotting
    if 'Timestamp' in df.columns:
        df = df.set_index('Timestamp')
    
    # Resample based on time period
    if time_period == 'Daily':
        data = df[variable].resample('D').mean()
    elif time_period == 'Monthly':
        data = df[variable].resample('M').mean()
    else:
        data = df[variable]
    
    # Plot the data
    data.plot(ax=ax)
    
    # Set labels and title
    ax.set_ylabel(f"{variable} ({'W/m²' if variable in ['GHI','DNI','DHI'] else '°C' if variable == 'Tamb' else '%' if variable == 'RH' else 'm/s'})")
    ax.set_title(f"{variable} over time")
    
    return fig

def create_distribution_plot(df, variable):
    """
    Create a distribution plot for a specific variable
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Data frame containing the data
    variable : str
        Variable to plot
        
    Returns:
    --------
    matplotlib.figure.Figure
        Distribution plot
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create histogram with KDE
    sns.histplot(df[variable], kde=True, ax=ax)
    
    # Add mean and median lines
    mean_val = df[variable].mean()
    median_val = df[variable].median()
    
    ax.axvline(mean_val, color='r', linestyle='--', label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='g', linestyle='-.', label=f'Median: {median_val:.2f}')
    
    # Set labels and title
    ax.set_xlabel(variable)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {variable}')
    ax.legend()
    
    return fig
