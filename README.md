# 🌍 International Debt Analysis

## 📖 Overview
The **International Debt Analysis** project is a full-stack data analytics pipeline and interactive dashboard. It is designed to extract, clean, and visualize complex global debt data, allowing users to interactively explore economic indicators and country-level financial burdens. 

By connecting a native Python web application directly to a relational database, this project demonstrates end-to-end data handling—from raw CSV cleaning to live SQL querying and dynamic visual storytelling.

## ⚡ Key Features
* **Interactive Multi-Page Dashboard:** A user-friendly Streamlit interface featuring a main global command center and a dedicated analytical reporting page.
* **Live Database Connection:** Data is queried in real-time from a PostgreSQL database using `psycopg2` and `SQLAlchemy`, ensuring the dashboard always reflects the most up-to-date structural data.
* **Dynamic Visualizations:** Utilizes Plotly to render interactive choropleth maps, donut charts, treemaps, and historical area charts that respond instantly to user filters.
* **Automated Data Cleaning:** Includes robust Python scripts to handle missing values, correct strict data types (e.g., converting scientific notation to large integers/numerics), and prepare data for SQL ingestion.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Database:** PostgreSQL, pgAdmin
* **Database Drivers:** SQLAlchemy, psycopg2
* **Web Framework:** Streamlit
* **Data Visualization:** Plotly Express

## 📊 Analytical Scope
The application includes a dedicated analytics engine capable of answering complex financial questions, including:
1. Finding the top 5 indicators contributing most to global debt.
2. Calculating the percentage contribution of each country to total global debt.
3. Identifying the top 3 countries for specific debt indicators.
4. Displaying the top 10 countries with the highest overall debt.
5. Calculating historical averages and analyzing debt distribution.

## 📁 Project Structure
```text
International_Debt_Analysis/
│
├── 1_🌍_Dashboard.py               # Main Streamlit application and KPI command center
├── Data_Cleanning.py               # Python script for raw data processing and formatting
├── requirements.txt                # Project dependencies
├── .gitignore                      # Git exclusion rules (protects .venv and passwords)
│
├── pages/                          # Streamlit multi-page routing directory
│   └── 2_📊_Analytical_Questions.py # SQL-driven Q&A reporting dashboard
│
└── Cleaned_Datasets/               # Output directories for processed CSVs
    ├── AllCountries_DATA.csv
    ├── CountriesMeta_DATA.csv
    └── SeriesMeta_DATA.csv
