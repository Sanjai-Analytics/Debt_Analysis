import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extras import RealDictCursor

@st.cache_resource
def init_connection():
    try:
        return psycopg2.connect(
            host="localhost",
            user="postgres",     
            password="your_password",  
            database="Debt_Analysis",   
            port="5432"
        )
    except Exception as e:
        st.error(f"Error connecting to PostgreSQL: {e}")
        return None

conn = init_connection()
cursor = conn.cursor(cursor_factory=RealDictCursor)

report_option = st.selectbox(
    "Choose Analytics Questions:",
    options= [
    "Select a question...",
    "1. Find the top 5 indicators contributing most to global debt.",
    "2. Calculate percentage contribution of each country to total global debt.",
    "3. Identify the top 3 countries for each indicator based on debt.",
    "4. Find the total debt for each country.",
    "5. Display the top 10 countries with the highest total debt.",
    "6. Find the average debt per country.",
    "7. Retrieve all distinct country names from the dataset.",
    "8. Count the total number of countries." 
])
if report_option == "1. Find the top 5 indicators contributing most to global debt.":
    st.subheader("Top 5 Indicators")
    cursor.execute(f"""SELECT series_name AS "Indicator", SUM(debt_value) AS "Total Debt"
    FROM ALLCountries_DATA
    GROUP BY series_name
    ORDER BY "Total Debt" DESC
    LIMIT 5;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "2. Calculate percentage contribution of each country to total global debt.":
    st.subheader("Percentage contribution of each country")
    cursor.execute(f"""SELECT country_name, 
    SUM(debt_value) AS country_total,
    ROUND((SUM(debt_value) / (SELECT SUM(debt_value) FROM ALLCountries_DATA) * 100), 4) AS percentage_contribution
    FROM ALLCountries_DATA
    GROUP BY country_name
    ORDER BY percentage_contribution DESC;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "3. Identify the top 3 countries for each indicator based on debt.":
    st.subheader("Top 3 countries for each indicator based on debt")
    cursor.execute(f"""
    WITH RankedDebt AS (
    SELECT country_name, series_name, SUM(debt_value) AS total_debt,
    DENSE_RANK() OVER(PARTITION BY series_name ORDER BY SUM(debt_value) DESC) as rank
    FROM ALLCountries_DATA
    GROUP BY country_name, series_name)
    SELECT series_name, country_name, total_debt
    FROM RankedDebt
    WHERE rank <= 3;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "4. Find the total debt for each country.":
    st.subheader("Total debt for each country")
    cursor.execute(f"""
    SELECT country_name, SUM(debt_value) AS total_debt
    FROM ALLCountries_DATA
    GROUP BY country_name
    ORDER BY total_debt DESC;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "5. Display the top 10 countries with the highest total debt.":
    st.subheader("Top 10 countries with the highest total debt.")
    cursor.execute(f"""
    SELECT country_name, SUM(debt_value) AS total_debt
    FROM ALLCountries_DATA
    GROUP BY country_name
    ORDER BY total_debt DESC
    LIMIT 10;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "6. Find the average debt per country.":
    st.subheader("The average debt.")
    cursor.execute(f"""
    SELECT country_name, AVG(debt_value) AS average_debt
    FROM ALLCountries_DATA
    GROUP BY country_name
    ORDER BY average_debt DESC;""")
elif report_option == "7. Retrieve all distinct country names from the dataset.":
    st.subheader("Country names.")
    cursor.execute(f"""
    SELECT DISTINCT country_name
    FROM ALLCountries_DATA
    ORDER BY country_name;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)
elif report_option == "8. Count the total number of countries.":
    st.subheader("The Total number of countries.")
    cursor.execute(f"""
    SELECT COUNT(DISTINCT country_name) AS total_countries
    FROM ALLCountries_DATA;""")
    data = cursor.fetchall()
    st.dataframe(data, use_container_width=True)

       






