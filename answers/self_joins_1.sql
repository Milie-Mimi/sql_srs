WITH employee_manager AS
    (SELECT le.employee_id,
    le.employee_name,
    le.manager_id,
    re.employee_name AS n1_employee_name,
    re.manager_id AS n1_manager_id
    FROM employees le
    LEFT JOIN employees re
    ON le.manager_id = re.employee_id)


SELECT *
FROM employee_manager
LEFT JOIN employees re
ON employee_manager.n1_manager_id = re.employee_id