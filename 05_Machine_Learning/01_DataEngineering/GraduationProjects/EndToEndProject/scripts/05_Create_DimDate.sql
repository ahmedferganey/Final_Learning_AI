


/* Create DIMENSION: Date*/
SELECT DISTINCT
    OrderDate AS Date,
    YEAR(OrderDate) AS Year,
    MONTH(OrderDate) AS Month,
    DATENAME(MONTH, OrderDate) AS MonthName
INTO DimDate
FROM AdventureWorks2025.Sales.SalesOrderHeader;
