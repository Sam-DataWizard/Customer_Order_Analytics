-- Total Sales per Month
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_sales
FROM
    order_analysis
GROUP BY
    month
ORDER BY
    month;

-- Top 10 Customers by Sales
SELECT
    customer_name,
    SUM(amount) AS total_sales
FROM
    order_analysis
GROUP BY
    customer_name
ORDER BY
    total_sales DESC
LIMIT 10;

-- Most Popular Products
SELECT
    product_name,
    COUNT(order_id) AS total_orders
FROM
    order_analysis
GROUP BY
    product_name
ORDER BY
    total_orders DESC
LIMIT 10;
