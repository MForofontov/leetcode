SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) OVER (ORDER BY id) AS prev_num_1,
           LAG(num, 2) OVER (ORDER BY id) AS prev_num_2
    FROM Logs
) AS temp
WHERE num = prev_num_1 AND num = prev_num_2;
