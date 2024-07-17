from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import logging
import psycopg2

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fetch_and_store_data():
    # Fetch data from the Random User API
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        person = response.json()['results'][0]
        first_name = person['name']['first']
        last_name = person['name']['last']
        email = person['email']
        gender = person['gender']
        dob = person['dob']['date']
        nationality = person['nat']
        
        logging.info(f"Fetched person: {first_name} {last_name}, {email}, {gender}, {dob}, {nationality}")
        
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname='apidata',
            user='airflow',
            password='airflow',
            host='postgres',
            port='5432'
        )
        cursor = conn.cursor()
        
        # Insert data into the users table
        insert_query = """
        INSERT INTO users (first_name, last_name, email, gender, dob, nationality)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (first_name, last_name, email, gender, dob, nationality))
        conn.commit()
        
        cursor.close()
        conn.close()
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")

with DAG('fetch_and_store_data_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    fetch_and_store_task = PythonOperator(
        task_id='fetch_and_store_data',
        python_callable=fetch_and_store_data,
    )

    fetch_and_store_task
