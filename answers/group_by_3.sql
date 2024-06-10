WITH customer_sales AS (
    SELECT client, SUM(montant) AS tot_sales
    FROM ventes
    GROUP BY client
),

avg_customer_sales AS (
    SELECT MEAN(tot_sales)
    FROM customer_sales
)


SELECT client, SUM(montant) AS tot_sales
FROM ventes
GROUP BY client
HAVING tot_sales > (SELECT * FROM avg_customer_sales)