import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
 
def load_data_to_snowflake(file_path, table_name, connection_params):
    df = pd.read_csv(file_path)
    conn = snowflake.connector.connect(
        user=connection_params['user'],
        password=connection_params['password'],
        account=connection_params['account'],
        warehouse=connection_params['warehouse'],
        database=connection_params['database'],
        schema=connection_params['schema']
    )
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name)
    conn.close()
    return success, nchunks, nrows
 
if __name__ == "__main__":
    # Example loading data to Snowflake
    file_path = "transformed_data.csv"
    table_name = "WEATHER_DATA"
    connection_params = {
        'user': 'YOUR_USERNAME', 
        'password': 'YOUR_PASSWORD',
        'account': 'YOUR_ACCOUNT',
        'warehouse': 'WEATHER_WAREHOUSE',
        'database': 'WEATHER_DATABASE',
        'schema': 'WEATHER_SCHEMA'
    }
    success, nchunks, nrows = load_data_to_snowflake(file_path, table_name, connection_params)
    print(f"Data loaded successfully: {success}, Number of chunks: {nchunks}, Number of rows: {nrows}")
