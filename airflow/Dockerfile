FROM apache/airflow:2.5.1

# Switch to root user to install additional packages if needed
USER root

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user to install Python packages
USER airflow

# Install psycopg2
RUN pip install psycopg2-binary

# Copy DAGs directory into the container
COPY dags /opt/airflow/dags
