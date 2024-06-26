SELECT *,
       CASE
           WHEN department == 'SALES' THEN wage * 1.1
           WHEN department == 'HR' THEN wage * 1.05
           WHEN department == 'IT' THEN wage * 1.03
           ELSE wage
       END AS wage_after_increase
FROM salaires