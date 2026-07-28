
/* Create DIMENSION: Customer*/
SELECT 
    c.CustomerID,
    p.FirstName + ' ' + p.LastName AS FullName
INTO DimCustomer
FROM AdventureWorks2025.Sales.Customer c
JOIN AdventureWorks2025.Person.Person p
    ON c.PersonID = p.BusinessEntityID;
