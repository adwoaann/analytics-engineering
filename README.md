# Analytics Engineering Project: OpenWeatherMap to Snowflake Dashboard

## Purpose of Project
This project demonstrates an end-to-end data pipeline for extracting weather data, transforming it using Python, loading it into Snowflake and visualizing it through Power BI.the whole process is auntomated using apache airflow and run in a dockerized environment.


## Requirements
1. Docker
2. Python 
3. Snowflake Account
4. Airflow
5. Power BI Desktop
6. OpenWeatherMap API Key

# Docker Setup
1. Ensure Docker is installed on your machine

# Python Environment Setup
1. Install Python packages

# Snowflake Setup
1.Create a Snowflakes account
2. Create a Warehouse
3. Create a Database
4. Create a Schema
5. Create a Table

# Airflow DAG Setup
1. Access the Airflow webserver at http://localhost:8080

# Power BI Visualization
1. Connect Power BI to Snowflake


## Usage Instructions
# Run the ETL Script:
docker exec -it your_container_name python src/weather_etl.py

# Airflow DAG Setup:
1. Access the Airflow webserver at http://localhost:8080.
2. Trigger the DAG weather_data_pipeline to run the ETL process daily.

# Power BI Visualization:
Connect Power BI to Snowflake:
1. Open Power BI Desktop.
2. Click on Get Data and select Snowflake.
3. Enter your Snowflake connection details and load the weather_data table.
4. Create visualizations like line charts for temperature trends, pie charts for weather conditions, etc.

## Data Flow
Extract: Fetch data from OpenWeatherMap API using Python.
Transform: Clean and transform data using Pandas.
Load: Insert data into Snowflake.
Automate: Use Apache Airflow to automate the ETL process.
Visualize: Create dashboards in Power BI.


