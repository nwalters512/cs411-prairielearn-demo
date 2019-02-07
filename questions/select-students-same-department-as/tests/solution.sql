SELECT FirstName 
FROM   Students 
WHERE  Department IN (SELECT Department 
                      FROM   Students 
                      WHERE  FirstName = 'Evan')
