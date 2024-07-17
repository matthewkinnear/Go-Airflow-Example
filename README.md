# Random Person API Data Storage

## Overview

This project demonstrates how to fetch data from the Random User API and store it in a PostgreSQL database using Go, Docker, and Apache Airflow.

## Project Structure
///
 airflow
    dags
       example_dag.py
    Dockerfile
 go-app
    main.go
    Dockerfile
 config
    airflow.cfg
 docker-compose.yml
///
## Components

- **Go Application**: Triggers the Airflow DAG.
- **Airflow DAG**: Fetches data from the Random User API and stores it in the PostgreSQL database.
- **PostgreSQL Database**: Stores the fetched data.

## Usage

1. Build and start the Docker containers.
2. Access the Airflow web interface at \http://localhost:8080\.
3. Enable and trigger the \etch_and_store_data_dag\ DAG.

## Technologies

- Go
- Docker
- Apache Airflow
- PostgreSQL

