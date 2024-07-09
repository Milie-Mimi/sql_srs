SELECT store_id,
COALESCE(product_name, 'TOTAL MAGASIN') AS product_name,
SUM(amount) as sum_amount
FROM redbull
GROUP BY
GROUPING SETS ((store_id, product_name), store_id)
ORDER BY store_id