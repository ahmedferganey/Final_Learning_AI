

/* Create DIMENSION: Product*/
SELECT 
    p.ProductID,
    p.Name AS ProductName,
    pc.Name AS Category,
    ps.Name AS SubCategory
INTO DimProduct
FROM AdventureWorks2025.Production.Product p
LEFT JOIN AdventureWorks2025.Production.ProductSubcategory ps
    ON p.ProductSubcategoryID = ps.ProductSubcategoryID
LEFT JOIN AdventureWorks2025.Production.ProductCategory pc
    ON ps.ProductCategoryID = pc.ProductCategoryID;