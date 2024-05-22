-- display score and name from table second_table
-- if name is null will not be display
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
