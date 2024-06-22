-- Create a warehouse
CREATE WAREHOUSE IF NOT EXISTS WEATHER_WAREHOUSE
  WITH WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;
 
-- Create a database
CREATE DATABASE IF NOT EXISTS WEATHER_DATABASE;
 
-- Create a schema
CREATE SCHEMA IF NOT EXISTS WEATHER_SCHEMA;
 
-- Create a table
CREATE TABLE IF NOT EXISTS WEATHER_SCHEMA.WEATHER_DATA (
    id STRING,
    name STRING,
    coord_lat FLOAT,
    coord_lon FLOAT,
    weather_main STRING,
    weather_description STRING,
    main_temp FLOAT,
    main_feels_like FLOAT,
    main_temp_min FLOAT,
    main_temp_max FLOAT,
    main_pressure INT,
    main_humidity INT,
    visibility INT,
    wind_speed FLOAT,
    wind_deg INT,
    clouds_all INT,
    dt INT,
    sys_country STRING,
    sys_sunrise INT,
    sys_sunset INT,
    timezone INT,
    cod INT
);
