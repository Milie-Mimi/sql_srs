SELECT COALESCE(neighborhood, 'inconnu'), MEAN(price) AS avg_price
FROM ventes_immo
GROUP BY neighborhood
ORDER BY avg_price desc