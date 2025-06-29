-- Lists all records of the table second_table without rows where name is NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
