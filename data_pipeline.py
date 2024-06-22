import requests
import pandas as pd
import json
from sqlalchemy import create_engine
 
def fetch_data_from_api(api_url, cities, api_key):
    data = []
    for city in cities:
        params = {"q": city, "appid": api_key}
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data.append(response.json())
        else:
            print(f"Failed to fetch data for {city}")
    return pd.json_normalize(data)
 
def load_data(file_path, file_type):
    if file_type == "csv":
        return pd.read_csv(file_path)
    elif file_type == "json":
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.json_normalize(data)
    elif file_type == "parquet":
        return pd.read_parquet(file_path)
    elif file_type == "database":
        engine = create_engine(file_path)
        return pd.read_sql("SELECT * FROM weather_data", engine)
 
def transform_data(df):
    # Perform data cleaning and transformation
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip().str.lower()
    return df
 
def save_data(df, output_path):
    df.to_csv(output_path, index=False)
 
if __name__ == "__main__":

    api_url = "http://api.openweathermap.org/data/2.5/weather"
    cities = ["ACCRA", "KUMASI", "SEKONDI-TAKORADI", "CAPE COAST", "TAMALE",
          "SUNYANI", "BOLGATANGA", "WA", "HO", "KOFORIDUA", "TEMA", "TARKWA"]
    api_key = "c283c8ba01e59454956a44953170df18"
    api_df = fetch_data_from_api(api_url, cities, api_key)
    # Transform and save data
    transformed_df = transform_data(api_df)
    save_data(transformed_df, "transformed_data.csv")