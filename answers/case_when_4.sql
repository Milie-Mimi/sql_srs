WITH salary_range AS (
    SELECT
        department,
        wage,
        CASE
            WHEN wage <= 50000 THEN 'Low'
            WHEN wage < 90000 THEN 'Medium'
            ELSE 'High'
        END AS salary_range
    FROM salaires)

SELECT department, salary_range , AVG(wage) AS average_salary, COUNT(*) AS count
FROM salary_range
GROUP BY department, salary_range