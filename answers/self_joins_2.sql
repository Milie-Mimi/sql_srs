SELECT customer_id,
df1.order_id AS first_order,
df1.date AS date_first_order,
df2.order_id AS second_order,
df2.date as date_next_order
FROM sales AS df1
LEFT JOIN sales AS df2
USING(customer_id)
WHERE (df1.order_id != df2.order_id)
AND (date_next_order - date_first_order = 1)