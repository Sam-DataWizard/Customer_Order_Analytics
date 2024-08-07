import pandas as pd
from sqlalchemy import create_engine

# Load transformed data
transformed_data = pd.read_csv('../data/transformed_data.csv')

# Load data into PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/ecommerce')
transformed_data.to_sql('order_analysis', engine, if_exists='replace', index=False)
