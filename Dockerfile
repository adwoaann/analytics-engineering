# Use the official Airflow image
FROM apache/airflow:2.1.2
 
# Install additional dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
 
# Copy your scripts to the container
COPY . /opt/airflow/
 
# Set the working directory
WORKDIR /opt/airflow