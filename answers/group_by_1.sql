SELECT COALESCE(neighborhood, 'inconnu'), MEAN(price) AS avg_price, COUNT(*) AS nb_ventes
FROM ventes_immo
GROUP BY neighborhood
ORDER BY avg_price desc