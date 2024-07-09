SELECT year, COALESCE(region, 'TOTAL') AS region, SUM(population) AS sum_pop
FROM datapop
GROUP BY
GROUPING SETS((year, region), year)
ORDER BY region, year