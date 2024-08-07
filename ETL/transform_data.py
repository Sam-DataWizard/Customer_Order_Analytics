import pandas as pd

# Load extracted data
customers = pd.read_csv('../data/extracted_customers.csv')
orders = pd.read_csv('../data/extracted_orders.csv')
products = pd.read_csv('../data/extracted_products.csv')

# Data Cleaning: Handle missing values and duplicates
customers.dropna(inplace=True)
orders.dropna(inplace=True)
products.dropna(inplace=True)

# Data Normalization: Standardize date formats
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Data Integration: Merge datasets
orders_customers = pd.merge(orders, customers, on='customer_id', how='inner')
orders_customers_products = pd.merge(orders_customers, products, on='product_id', how='inner')

# Save transformed data to CSV for verification
orders_customers_products.to_csv('../data/transformed_data.csv', index=False)
