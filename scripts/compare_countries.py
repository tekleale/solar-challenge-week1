import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

def load_country_data(countries=['benin', 'sierra_leone', 'togo']):
    """
    Load data for multiple countries
    
    Parameters:
    -----------
    countries : list
        List of country names
        
    Returns:
    --------
    dict
        Dictionary with country names as keys and dataframes as values
    """
    data = {}
    for country in countries:
        try:
            file_path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
            df = pd.read_csv(file_path)
            data[country] = df
        except FileNotFoundError:
            print(f"Data file for {country} not found.")
    return data

def create_comparison_boxplots(data, metrics=['GHI', 'DNI', 'DHI']):
    """
    Create boxplots comparing metrics across countries
    
    Parameters:
    -----------
    data : dict
        Dictionary with country names as keys and dataframes as values
    metrics : list
        List of metrics to compare
        
    Returns:
    --------
    list
        List of matplotlib figures
    """
    figures = []
    
    for metric in metrics:
        # Create a dataframe for the metric
        df_metric = pd.DataFrame()
        
        for country, df in data.items():
            if metric in df.columns:
                temp_df = pd.DataFrame({
                    'Country': country,
                    metric: df[metric]
                })
                df_metric = pd.concat([df_metric, temp_df])
        
        # Create boxplot
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='Country', y=metric, data=df_metric, ax=ax)
        ax.set_title(f'Comparison of {metric} across Countries')
        ax.set_ylabel(f"{metric} ({'W/m²' if metric in ['GHI','DNI','DHI'] else '°C' if metric == 'Tamb' else '%' if metric == 'RH' else 'm/s'})")
        
        figures.append(fig)
    
    return figures

def create_summary_table(data, metrics=['GHI', 'DNI', 'DHI']):
    """
    Create a summary table comparing metrics across countries
    
    Parameters:
    -----------
    data : dict
        Dictionary with country names as keys and dataframes as values
    metrics : list
        List of metrics to compare
        
    Returns:
    --------
    pandas.DataFrame
        Summary table
    """
    summary = []
    
    for metric in metrics:
        for country, df in data.items():
            if metric in df.columns:
                summary.append({
                    'Country': country,
                    'Metric': metric,
                    'Mean': df[metric].mean(),
                    'Median': df[metric].median(),
                    'Std Dev': df[metric].std(),
                    'Min': df[metric].min(),
                    'Max': df[metric].max()
                })
    
    return pd.DataFrame(summary)

def run_statistical_tests(data, metrics=['GHI', 'DNI', 'DHI']):
    """
    Run statistical tests to compare metrics across countries
    
    Parameters:
    -----------
    data : dict
        Dictionary with country names as keys and dataframes as values
    metrics : list
        List of metrics to compare
        
    Returns:
    --------
    dict
        Dictionary with test results
    """
    results = {}
    
    for metric in metrics:
        # Extract data for each country
        country_data = []
        country_names = []
        
        for country, df in data.items():
            if metric in df.columns:
                country_data.append(df[metric].dropna())
                country_names.append(country)
        
        # Run ANOVA if we have data for at least 2 countries
        if len(country_data) >= 2:
            try:
                f_stat, p_value = stats.f_oneway(*country_data)
                results[metric] = {
                    'test': 'ANOVA',
                    'f_statistic': f_stat,
                    'p_value': p_value,
                    'countries': country_names
                }
            except:
                # If ANOVA fails, try Kruskal-Wallis test
                try:
                    h_stat, p_value = stats.kruskal(*country_data)
                    results[metric] = {
                        'test': 'Kruskal-Wallis',
                        'h_statistic': h_stat,
                        'p_value': p_value,
                        'countries': country_names
                    }
                except:
                    results[metric] = {
                        'test': 'Failed',
                        'error': 'Could not run statistical tests',
                        'countries': country_names
                    }
    
    return results

if __name__ == "__main__":
    # Load data for all countries
    countries = ['benin', 'sierra_leone', 'togo']
    data = load_country_data(countries)
    
    # Create comparison boxplots
    figures = create_comparison_boxplots(data)
    
    # Create summary table
    summary = create_summary_table(data)
    print(summary)
    
    # Run statistical tests
    results = run_statistical_tests(data)
    for metric, result in results.items():
        print(f"\nResults for {metric}:")
        for key, value in result.items():
            print(f"  {key}: {value}")
