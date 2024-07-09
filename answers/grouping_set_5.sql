SELECT type_contrat, type_acte, groupe_age, SUM(montant_rembourse)
FROM sante
GROUP BY ROLLUP (type_contrat, type_acte, groupe_age)
ORDER BY type_contrat, type_acte, groupe_age