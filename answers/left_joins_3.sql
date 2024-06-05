SELECT *
FROM customers
LEFT JOIN orders
USING(customer_id)
LEFT JOIN order_details
USING(order_id)
LEFT JOIN products
USING(product_id)