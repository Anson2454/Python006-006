-- INNER JOIN 
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;

--INNER JOIN RESULT:
table1.id   table1.name     table2.id   table2.name 
1           table1_table2   1           table1_table2

