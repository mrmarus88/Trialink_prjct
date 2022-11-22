DELETE
	main_table
FROM  
	main_table
LEFT OUTER JOIN 
	(SELECT MIN(id) AS id, DataBase_name FROM main_table GROUP BY DataBase_name) AS tmp
ON 
	main_table.id = tmp.id 
WHERE
	tmp.id IS NULL