CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS INT AS $$
DECLARE
    result INT;
BEGIN
    -- Check if N is valid
    IF N < 1 THEN
        RETURN NULL;
    END IF;

    -- Query to get the Nth highest salary
    SELECT salary INTO result
    FROM (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N-1
    ) AS subquery;

    -- Return the result
    RETURN result;
END;
$$ LANGUAGE plpgsql;