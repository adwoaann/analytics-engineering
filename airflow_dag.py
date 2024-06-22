from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from data_pipeline import fetch_data_from_api, transform_data, save_data
from data_loading import load_data_to_snowflake
 
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}
 
dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='A simple data pipeline',
    schedule_interval='@daily',
)
 
def fetch_transform_save_data(**kwargs):
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    cities = ["ACCRA", "KUMASI", "SEKONDI-TAKORADI", "CAPE COAST", "TAMALE",
          "SUNYANI", "BOLGATANGA", "WA", "HO", "KOFORIDUA", "TEMA", "TARKWA"]
    api_key = "YOUR_API_KEY"
    api_df = fetch_data_from_api(api_url, cities, api_key)
    transformed_df = transform_data(api_df)
    save_data(transformed_df, "transformed_data.csv")
 
def load_to_snowflake(**kwargs):
    file_path = "transformed_data.csv"
    table_name = "weather_data"
    connection_params = {
        'user': 'HMENSAH',
        'password': 'Alister@2023',
        'account': 'YOUR_ACCOUNT',
        'warehouse': 'WEATHER_WAREHOUSE',
        'database': 'WEATHER_DATABASE',
        'schema': 'WEATHER_SCHEMA'
    }
    load_data_to_snowflake(file_path, table_name, connection_params)
 
fetch_transform_save_task = PythonOperator(
    task_id='fetch_transform_save_data',
    python_callable=fetch_transform_save_data,
    dag=dag,
)
 
load_to_snowflake_task = PythonOperator(
    task_id='load_to_snowflake',
    python_callable=load_to_snowflake,
    dag=dag,
)
 
fetch_transform_save_task >> load_to_snowflake_task