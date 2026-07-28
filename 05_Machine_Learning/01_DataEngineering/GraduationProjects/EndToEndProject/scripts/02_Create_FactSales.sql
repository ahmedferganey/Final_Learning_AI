

/* Create FACT TABLE*/
SELECT 
    sod.SalesOrderID,
    sod.SalesOrderDetailID,
    soh.OrderDate,
    soh.CustomerID,
    soh.TerritoryID,
    sod.ProductID,
    sod.OrderQty,
    sod.UnitPrice,
    sod.LineTotal
INTO FactSales
FROM AdventureWorks2025.Sales.SalesOrderDetail sod
JOIN AdventureWorks2025.Sales.SalesOrderHeader soh
    ON sod.SalesOrderID = soh.SalesOrderID;