# Stocks ETL Pipeline (Airflow + Docker + PostgreSQL)

End-to-end ETL pipeline that extracts stock market data from the Alpha Vantage API, transforms it using Python, and loads it into PostgreSQL, orchestrated with Apache Airflow and fully containerized using Docker Compose.

--- 

## Overview

This project demonstrates a production-style data pipeline that automates the ingestion, transformation, and storage of financial market data.

It is designed with modular components, reproducibility, and workflow orchestration in mind.

## Architecture

**Data Flow:**

```
Alpha Vantage API -> Extract (Python) -> Transform -> Load -> PostgreSQL -> Airflow Scheduling
```

**Core Components:**

- Airflow DAGs for orchestration
- Python-based ETL modules
- PostgreSQL for structured storage
- Docker Compose for multi-service setup

## Tech Stack

- Python
- Apache Airflow
- PostgreSQL
- Docker & Docker Compose
- REST APIs (Alpha Vantage)
- SQL

## Project Structure

``
├── dags/                  # Airflow DAGs
│   └── etlstocks.py
│
├── src/                  # ETL logic
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── __init__.py
│
├── include/              # Constants / configs
│   └── constants.py
│
├── tests/                # Unit tests (in progress)
│   └── dags/
│
├── files/                # Sample API responses
│   └── response.json
│
├── Dockerfile
├── docker.compose.yml
├── requirements.txt
├── packages.txt
├── .dockerignore
├── .gitignore
└── README.md
``

## Features

- End-to-end ETL pipeline for financial data
- API-based data ingestion (Alpha Vantage)
- Data transformation and cleaning in Python
- PostgreSQL integration for structured storage
- Airflow DAG for scheduled pipeline execution
- Fully containerized environment using Docker Compose
- Modular architecture separating extract, transform, and load layers

## Setup & Installation

1. Clone the repository

``
git clone https://github.com/TheDucky-2/Stocks-ETL-Pipeline.git
``
cd stock-etl-pipeline

2. Set up environment variables

Create a .env file:

ALPHA_VANTAGE_API_KEY=your_api_key
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=stocks
3. Run with Docker Compose
docker-compose up --build
4. Access Airflow
Web UI: http://localhost:8080
Default login depends on your Airflow config
Airflow DAG

The DAG (etlstocks.py) performs:

Extract stock data from API
Transform raw JSON into structured format
Load processed data into PostgreSQL

Scheduled execution ensures automated updates.

Testing

Basic DAG integrity tests are included under tests/.
More unit tests for ETL modules will be added.

Future Improvements
Add data validation layer (schema enforcement)
Implement retries + failure alerting
Add Redis caching layer
Cloud deployment (AWS/GCP)
Monitoring & logging improvements
Expand test coverage for ETL modules
What This Project Demonstrates
Backend engineering skills
Data pipeline design
Workflow orchestration (Airflow)
Database design (PostgreSQL)
Containerized systems (Docker)
API integration
Modular system architecture