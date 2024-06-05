SELECT *
FROM df_customers
LEFT JOIN df_stores
USING(customer_id)
LEFT JOIN df_store_products
USING(store_id)
FULL OUTER JOIN df_products
USING(product_id)