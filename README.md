# Customer Order Analytics

## Project Description
This project involves building an end-to-end data engineering pipeline using SQL to analyze customer orders for a fictional e-commerce company. The pipeline extracts data from CSV files, transforms it, and loads it into a PostgreSQL database. Finally, analytical reports are generated to derive business insights.

## Project Structure
- **data/**: Contains the source CSV files.
- **etl/**: Contains Python scripts for the ETL process.
  - `extract.py`: Extract data from CSV files.
  - `transform.py`: Transform the data (cleaning, normalization, and integration).
  - `load.py`: Load the transformed data into a PostgreSQL database.
- **sql/**: Contains SQL scripts for creating tables and generating reports.
  - `create_tables.sql`: SQL script to create database tables.
  - `queries.sql`: SQL queries for analytical reports.

## How to Run
1. Clone the repository.
2. Install the required Python packages: `pandas`, `sqlalchemy`, `psycopg2`.
3. Set up a PostgreSQL database and update the connection details in the `load.py` script.
4. Run the ETL process:
   ```bash
   python etl/extract.py
   python etl/transform.py
   python etl/load.py
