-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT state_id, name
FROM cities
WHERE state_id =
	(SELECT id
	FROM state
	WHERE name = 'California')
ORDER BY id ASC;;
