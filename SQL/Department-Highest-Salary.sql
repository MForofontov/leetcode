SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
INNER JOIN 
    Department d
ON 
    e.departmentId = d.id
WHERE 
    e.salary = (
        SELECT 
            MAX(e2.salary)
        FROM 
            Employee e2
        WHERE 
            e2.departmentId = e.departmentId
    );
