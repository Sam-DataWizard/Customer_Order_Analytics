import pandas as pd

# Extract data from CSV files
customers = pd.read_csv('../data/customers.csv')
orders = pd.read_csv('../data/orders.csv')
products = pd.read_csv('../data/products.csv')

# Save extracted data to CSV for verification
customers.to_csv('../data/extracted_customers.csv', index=False)
orders.to_csv('../data/extracted_orders.csv', index=False)
products.to_csv('../data/extracted_products.csv', index=False)
