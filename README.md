# Solar Challenge Week 1

This repository contains the analysis of solar farm data from Benin, Sierra Leone, and Togo. The project includes exploratory data analysis (EDA), cross-country comparison, and an interactive dashboard.

## Project Structure

```
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── app.py
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone.ipynb
│   ├── togo_eda.ipynb
│   └── cross_country_analysis.ipynb
├── requirements.txt
├── scripts/
│   ├── __init__.py
│   └── README.md
├── src/
│   └── __init__.py
└── tests/
    ├── __init__.py
    └── README.md
```

## Environment Setup

To set up the environment for this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Data Analysis

The project includes EDA for three countries:
- Benin
- Sierra Leone
- Togo

Each notebook contains:
- Summary statistics
- Missing value analysis
- Outlier detection
- Time series analysis
- Correlation analysis
- Wind and distribution analysis
- Temperature analysis

## Dashboard

The project includes a Streamlit dashboard for interactive visualization of the data. To run the dashboard:

```
streamlit run app.py
```

## Contributors

- Your Name