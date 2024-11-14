WITH RankedSalaries AS (
    SELECT 
        departmentId,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM 
        Employee
    GROUP BY 
        departmentId, salary
),
HighEarners AS (
    SELECT 
        e.id AS EmployeeID,
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department
    FROM 
        Employee e
    JOIN 
        RankedSalaries rs ON e.departmentId = rs.departmentId AND e.salary = rs.salary
    JOIN 
        Department d ON e.departmentId = d.id
    WHERE 
        rs.salary_rank <= 3
)
SELECT 
    Department, Employee, Salary
FROM 
    HighEarners
ORDER BY 
    Department, Salary DESC;


