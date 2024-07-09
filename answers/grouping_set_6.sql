SELECT
    COALESCE(type_contrat, 'TOTAL') AS type_contrat,
    COALESCE(type_acte, 'TOTAL') AS type_acte,
    SUM(montant_rembourse)
FROM sante
GROUP BY CUBE (type_contrat, type_acte)
ORDER BY type_contrat, type_acte