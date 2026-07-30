use AdventureWorksDWH
-- DimProduct PK
IF NOT EXISTS (
    SELECT 1 FROM sys.key_constraints 
    WHERE name = 'PK_DimProduct'
)
ALTER TABLE DimProduct
ADD CONSTRAINT PK_DimProduct PRIMARY KEY (ProductID);


-- DimCustomer PK
IF NOT EXISTS (
    SELECT 1 FROM sys.key_constraints 
    WHERE name = 'PK_DimCustomer'
)
ALTER TABLE DimCustomer
ADD CONSTRAINT PK_DimCustomer PRIMARY KEY (CustomerID);


-- DimTerritory PK
IF NOT EXISTS (
    SELECT 1 FROM sys.key_constraints 
    WHERE name = 'PK_DimTerritory'
)
ALTER TABLE DimTerritory
ADD CONSTRAINT PK_DimTerritory PRIMARY KEY (TerritoryID);


-- DimDate PK
IF NOT EXISTS (
    SELECT 1 FROM sys.key_constraints 
    WHERE name = 'PK_DimDate'
)
ALTER TABLE DimDate
ADD CONSTRAINT PK_DimDate PRIMARY KEY (Date);



-- FactSales PK (Composite Key)
IF NOT EXISTS (
    SELECT 1 FROM sys.key_constraints 
    WHERE name = 'PK_FactSales'
)
ALTER TABLE FactSales
ADD CONSTRAINT PK_FactSales 
PRIMARY KEY (SalesOrderID, SalesOrderDetailID);



-- Product FK
IF NOT EXISTS (
    SELECT 1 FROM sys.foreign_keys 
    WHERE name = 'FK_Fact_Product'
)
ALTER TABLE FactSales
ADD CONSTRAINT FK_Fact_Product
FOREIGN KEY (ProductID)
REFERENCES DimProduct(ProductID);


-- Customer FK
IF NOT EXISTS (
    SELECT 1 FROM sys.foreign_keys 
    WHERE name = 'FK_Fact_Customer'
)
ALTER TABLE FactSales
ADD CONSTRAINT FK_Fact_Customer
FOREIGN KEY (CustomerID)
REFERENCES DimCustomer(CustomerID);


-- Territory FK
IF NOT EXISTS (
    SELECT 1 FROM sys.foreign_keys 
    WHERE name = 'FK_Fact_Territory'
)
ALTER TABLE FactSales
ADD CONSTRAINT FK_Fact_Territory
FOREIGN KEY (TerritoryID)
REFERENCES DimTerritory(TerritoryID);


-- Date FK
IF NOT EXISTS (
    SELECT 1 FROM sys.foreign_keys 
    WHERE name = 'FK_Fact_Date'
)
ALTER TABLE FactSales
ADD CONSTRAINT FK_Fact_Date
FOREIGN KEY (OrderDate)
REFERENCES DimDate(Date);