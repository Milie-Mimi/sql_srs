SELECT
store_id,
SUM(amount) FILTER(WHERE product_name = 'redbull') as redbull_amount,
SUM(amount)
FROM redbull
GROUP BY store_id
ORDER BY SUM(amount) DESC