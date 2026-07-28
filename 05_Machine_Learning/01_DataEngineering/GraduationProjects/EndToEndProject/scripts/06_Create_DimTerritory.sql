
/* (Optional but recommended) Territory*/
SELECT 
    TerritoryID,
    Name AS TerritoryName,
    CountryRegionCode
INTO DimTerritory
FROM AdventureWorks2025.Sales.SalesTerritory;

