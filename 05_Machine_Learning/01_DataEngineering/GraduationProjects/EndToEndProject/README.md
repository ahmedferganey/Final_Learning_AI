# AdventureWorks Data Warehouse & Power BI Analytics

End-to-end **Data Warehouse** solution built from the AdventureWorks sample database, designed for analytical reporting in **Power BI**.

This project demonstrates a complete dimensional modeling + ETL workflow: extracting transactional data with **SSIS**, transforming it into a star schema, loading it into a dedicated Data Warehouse, and preparing it for business intelligence and visualization.

---

## Table of Contents

1. [Project Goal](#-project-goal)
2. [Architecture Overview](#-architecture-overview)
3. [What Was Implemented](#-what-was-implemented)
4. [SSIS ETL Package – Full Implementation Guide](#-ssis-etl-package--full-implementation-guide)
5. [Tech Stack](#-tech-stack)
6. [Project Structure](#-project-structure)
7. [How to Run](#-how-to-run)
8. [Example Insights You Can Build in Power BI](#-example-insights-you-can-build-in-power-bi)
9. [Troubleshooting](#-troubleshooting)
10. [Skills Demonstrated](#-skills-demonstrated)
11. [Possible Next Steps](#-possible-next-steps-future-improvements)
12. [Author](#-author)

---

## 🎯 Project Goal

Build a clean, analytics-ready **Data Warehouse** that enables fast and flexible sales analysis in Power BI (revenue, quantity, customers, products, territories, and time trends).

The solution follows **Kimball dimensional modeling** best practices and uses **SQL Server Integration Services (SSIS)** for reliable, schedulable data integration — making it production-oriented and easy to extend.

---

## 🏗️ Architecture Overview

```
AdventureWorks (OLTP Source)
          │
          ▼
   SSIS Package (ETL)
   • Truncate target tables (Full Refresh)
   • Extract data from source
   • Load into Star Schema
          │
          ▼
AdventureWorksDWH (Star Schema)
   ├── FactSales          ← Central fact table (order line grain)
   ├── DimCustomer
   ├── DimProduct
   ├── DimDate
   └── DimTerritory
          │
          ▼
     Power BI Desktop / Service
   (Relationships + Measures + Dashboards + Scheduled Refresh)
```

**Star Schema Design**
- One central **Fact** table containing the measurable events
- Surrounding **Dimension** tables providing descriptive context
- Simple one-to-many relationships ideal for Power BI

**ETL Layer (SSIS)**
- Handles the initial full-load of all Fact and Dimension tables
- Scheduled with SQL Server Agent to run daily
- Supports restartability (Truncate → Load pattern)
- Structured to be upgraded later to an incremental load pattern

---

## 📦 What Was Implemented

### 1. Data Warehouse Database
- Created dedicated database: `AdventureWorksDWH`
- Completely separated from the transactional `AdventureWorks` source

### 2. Fact Table – `FactSales`
- Grain: **one row = one sales order line**
- Contains key measures: `OrderQty`, `UnitPrice`, `LineTotal`
- Includes foreign keys to all dimensions (`CustomerID`, `ProductID`, `TerritoryID`, `OrderDate`)
- Built by joining `SalesOrderHeader` + `SalesOrderDetail`

### 3. Dimension Tables

| Dimension        | Key Columns                                    | Purpose                          |
|-------------------|------------------------------------------------|-----------------------------------|
| **DimCustomer**   | CustomerID, FullName                           | Customer analysis & filtering     |
| **DimProduct**    | ProductID, ProductName, Category, SubCategory  | Product hierarchy & performance   |
| **DimDate**       | Date, Year, Month, MonthName                   | Time-based analysis (YTD, trends) |
| **DimTerritory**  | TerritoryID, TerritoryName, CountryRegionCode  | Regional / geographic analysis    |

### 4. ETL Process with SSIS
- SSIS package extracts data from `AdventureWorks`
- Truncates and reloads the star schema tables (Full Refresh pattern)
- Designed to run on a schedule (daily) via SQL Server Agent
- Prepares clean data for Power BI consumption

### 5. Design Principles Applied
- Clear definition of **fact grain**
- Denormalized dimensions for easy filtering and hierarchies
- Separation of concerns (Source → ETL → DWH → BI)
- Ready for Power BI relationships and DAX measures
- Production-oriented ETL with SSIS

---

## 🔧 SSIS ETL Package – Full Implementation Guide

This section documents, step by step, how the `AdventureWorks_DWH_ETL.dtsx` package was built. It follows a **Full Refresh** pattern: truncate every target table, then reload it from the source.

### Prerequisites

- SQL Server with Integration Services installed
- Visual Studio + SQL Server Data Tools (SSDT), or the "SQL Server Integration Services Projects" extension
- `AdventureWorks` source database restored
- `AdventureWorksDWH` database and all target tables already created (via the `scripts/` folder)
- A **short** project path (avoid deeply nested folders such as OneDrive paths — Windows path-length limits can break SSIS builds). Recommended: `C:\Dev\AdventureWorks_DWH_ETL` or `C:\Projects\AdventureWorks_DWH_ETL`

### Step 1 — Create the SSIS Project

1. Open Visual Studio → **Create a new project**.
2. Search for **Integration Services Project** → select it → **Next**.
3. Name it `AdventureWorks_DWH_ETL`, choose a short local path, and click **Create**.
4. Rename the default `Package.dtsx` to `AdventureWorks_DWH_ETL.dtsx`.

### Step 2 — Create Connection Managers

Two OLE DB connections are required:

| Connection Name                  | Points to             | Role        |
|-----------------------------------|------------------------|-------------|
| `localhost.AdventureWorks2025`    | AdventureWorks (OLTP) | Source      |
| `LocalHost.AdventureWorksDWH`     | AdventureWorksDWH      | Destination |

Steps:
1. Right-click the Connection Managers area → **New OLE DB Connection…**
2. Click **New…**, choose the OLE DB provider (Microsoft OLE DB Driver for SQL Server), set the server name and select the database.
3. Test the connection → **OK**, and name it clearly (as above).
4. Repeat for the destination connection.

### Step 3 — Control Flow: Truncate Tasks (Full Refresh)

Add five **Execute SQL Task** components, connected to `LocalHost.AdventureWorksDWH`:

| Task Name              | SQL Statement                     |
|------------------------|------------------------------------|
| Truncate FactSales     | `TRUNCATE TABLE FactSales;`        |
| Truncate DimCustomer   | `TRUNCATE TABLE DimCustomer;`      |
| Truncate DimProduct    | `TRUNCATE TABLE DimProduct;`       |
| Truncate DimDate       | `TRUNCATE TABLE DimDate;`          |
| Truncate DimTerritory  | `TRUNCATE TABLE DimTerritory;`     |

Connect them in sequence using green (success) precedence constraints:

```
Truncate FactSales → Truncate DimCustomer → Truncate DimProduct → Truncate DimDate → Truncate DimTerritory
```

### Step 4 — Data Flow: Load FactSales

Add a **Data Flow Task** named `Load FactSales`, connected after the last Truncate task.

**OLE DB Source** (`localhost.AdventureWorks2025`, SQL command):
```sql
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
FROM Sales.SalesOrderDetail sod
INNER JOIN Sales.SalesOrderHeader soh
    ON sod.SalesOrderID = soh.SalesOrderID;
```

**OLE DB Destination** (`LocalHost.AdventureWorksDWH`):
- Data access mode: **Table or view – fast load**
- Table: `FactSales`
- Mappings verified in the **Mappings** tab

### Step 5 — Data Flow: Load Dimension Tables

Four additional Data Flow Tasks are added after `Load FactSales`, executed in order:

```
Load FactSales → Load DimCustomer → Load DimProduct → Load DimDate → Load DimTerritory
```

**Load DimCustomer**
```sql
SELECT 
    c.CustomerID,
    p.FirstName + ' ' + p.LastName AS FullName
FROM Sales.Customer c
INNER JOIN Person.Person p 
    ON c.PersonID = p.BusinessEntityID;
```

**Load DimProduct**
```sql
SELECT 
    p.ProductID,
    p.Name AS ProductName,
    pc.Name AS Category,
    ps.Name AS SubCategory
FROM Production.Product p
LEFT JOIN Production.ProductSubcategory ps 
    ON p.ProductSubcategoryID = ps.ProductSubcategoryID
LEFT JOIN Production.ProductCategory pc 
    ON ps.ProductCategoryID = pc.ProductCategoryID;
```

**Load DimDate**
```sql
SELECT DISTINCT
    OrderDate AS [Date],
    YEAR(OrderDate) AS [Year],
    MONTH(OrderDate) AS [Month],
    DATENAME(MONTH, OrderDate) AS MonthName
FROM Sales.SalesOrderHeader;
```

**Load DimTerritory**
```sql
SELECT 
    TerritoryID,
    Name AS TerritoryName,
    CountryRegionCode
FROM Sales.SalesTerritory;
```

Each Data Flow uses the same pattern: OLE DB Source (SQL command) → OLE DB Destination (Table or view – fast load) → the matching dimension table.

> **Note — Identity column fix:** `DimTerritory.TerritoryID` is an identity column in the target table, which by default blocks inserts of explicit ID values. Fixed by opening the `Load DimTerritory` OLE DB Destination and enabling **Keep Identity** under the fast-load options, so the original `TerritoryID` values from AdventureWorks are preserved instead of being auto-generated.

### Step 6 — Final Control Flow

```
1. Truncate FactSales
2. Truncate DimCustomer
3. Truncate DimProduct
4. Truncate DimDate
5. Truncate DimTerritory
6. Load FactSales          (Data Flow)
7. Load DimCustomer        (Data Flow)
8. Load DimProduct         (Data Flow)
9. Load DimDate            (Data Flow)
10. Load DimTerritory      (Data Flow)
```

### Step 7 — Test the Package

1. Execute the package in Visual Studio (F5 or **Start**).
2. All ten tasks should turn green in order.
3. Verify row counts in SSMS:
```sql
USE AdventureWorksDWH;
GO
SELECT COUNT(*) AS FactSales_Count     FROM FactSales;
SELECT COUNT(*) AS DimCustomer_Count   FROM DimCustomer;
SELECT COUNT(*) AS DimProduct_Count    FROM DimProduct;
SELECT COUNT(*) AS DimDate_Count       FROM DimDate;
SELECT COUNT(*) AS DimTerritory_Count  FROM DimTerritory;
```
All counts should be greater than zero.

### Step 8 — Deploy to the SSIS Catalog

1. Right-click the project in Solution Explorer → **Deploy**.
2. Select **SSIS in SQL Server** → **Next**.
3. Choose the destination server (e.g. `localhost`), authentication, and a catalog folder (e.g. `AdventureWorks`).
4. Review and click **Deploy**.

The package is then stored at: `SSISDB → AdventureWorks → Projects → AdventureWorks_DWH_ETL`.

### Step 9 — Schedule with SQL Server Agent

1. Confirm **SQL Server Agent** is running in SSMS (Object Explorer → right-click → **Start** if stopped).
2. Expand **SQL Server Agent → Jobs** → right-click → **New Job…**
3. **General** page: name it `Daily AdventureWorks DWH Refresh`.
4. **Steps** page → **New…**:
   - Type: `SQL Server Integration Services Package`
   - Package source: `SSIS Catalog`
   - Server: `localhost`
   - Package: select the deployed package
5. **Schedules** page → **New…**: Recurring, Daily, e.g. `02:00:00`.
6. Click **OK** to save the job.
7. Test it: right-click the job → **Start Job at Step…**, then check **View History** to confirm success.

---

## 🛠️ Tech Stack

- **SQL Server** + SQL Server Management Studio (SSMS)
- **SQL Server Integration Services (SSIS)**
- **SQL Server Data Tools (SSDT)** / Visual Studio
- **T-SQL** (table creation, transformations)
- **AdventureWorks** sample database (source)
- **Dimensional Modeling** (Star Schema / Kimball)
- **Power BI Desktop** + Power BI Service (reporting & scheduled refresh)
- **SQL Server Agent** (for scheduling the SSIS package)

---

## 📂 Project Structure

```
AdventureWorks-DWH/
├── README.md
├── scripts/
│   ├── 01_Create_Database.sql
│   ├── 02_Create_FactSales.sql
│   ├── 03_Create_DimCustomer.sql
│   ├── 04_Create_DimProduct.sql
│   ├── 05_Create_DimDate.sql
│   └── 06_Create_DimTerritory.sql
├── SSIS/
│   └── AdventureWorks_DWH_ETL.dtsx          ← Main SSIS package
│   └── (optional) Project deployment files
└── PowerBI/
    └── AdventureWorks_Sales_Dashboard.pbix  ← (optional)
```

---

## 🚀 How to Run

### 1. Prepare the Source & Target
1. Restore or attach the **AdventureWorks** database.
2. Run the SQL scripts in order (`01` → `06`) to create the empty star schema tables in `AdventureWorksDWH`.

### 2. SSIS Package
1. Open the SSIS project/package in **Visual Studio / SSDT** (see the [SSIS ETL Package section](#-ssis-etl-package--full-implementation-guide) above for the full build walkthrough).
2. Configure the connection managers:
   - Source → AdventureWorks
   - Destination → AdventureWorksDWH
3. Execute the package (or deploy it to the SSIS Catalog).
4. (Recommended) Create a **SQL Server Agent Job** to run the package daily.

### 3. Power BI
1. Connect **Power BI Desktop** to `AdventureWorksDWH`.
2. Create relationships:
   - `FactSales[CustomerID]` → `DimCustomer[CustomerID]`
   - `FactSales[ProductID]` → `DimProduct[ProductID]`
   - `FactSales[OrderDate]` → `DimDate[Date]`
   - `FactSales[TerritoryID]` → `DimTerritory[TerritoryID]`
3. Build measures (examples):
   - Total Revenue = `SUM(FactSales[LineTotal])`
   - Total Quantity = `SUM(FactSales[OrderQty])`
   - Order Count = `DISTINCTCOUNT(FactSales[SalesOrderID])`
4. Publish to **Power BI Service** and configure **Scheduled Refresh**  
   (use On-premises Data Gateway if SQL Server is on-premises).

---

## 📊 Example Insights You Can Build in Power BI

- Revenue by Year / Month / Territory
- Top products and categories
- Customer performance
- Sales trends over time
- Geographic analysis (maps)

---

## 🩹 Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| **Path length warning when creating the project** | Deeply nested OneDrive/GitHub folder path exceeds Windows path limits | Create the project in a short path (e.g. `C:\Dev\AdventureWorks_DWH_ETL`), then move it into the repo folder afterward |
| **"Failure inserting into the read-only column 'TerritoryID'"** | `TerritoryID` is an IDENTITY column in `DimTerritory`, blocking explicit inserts | In the OLE DB Destination for `Load DimTerritory`, enable **Keep Identity** under fast-load options (or drop/recreate the table without IDENTITY) |
| **Data Flow column mapping errors** | Source and destination column names/types don't align | Re-open the Data Flow → OLE DB Destination → **Mappings** tab and re-map manually |
| **"SQLServerAgent is not currently running so it cannot be notified of this action" when starting a job** | The SQL Server Agent service is stopped | In SSMS Object Explorer, right-click **SQL Server Agent** → **Start**; if it doesn't appear, start the *SQL Server Agent* Windows service from Services (services.msc) or SQL Server Configuration Manager |
| **Can't find OLE DB Source / Destination in the Toolbox** | Components are grouped under different sections or not shown by default | Use the SSIS Toolbox search box and type `OLE DB`, or expand **Other Sources** / **Other Destinations** |

---

## 💡 Skills Demonstrated

- Dimensional modeling (Star Schema)
- Fact & Dimension table design
- **SSIS package development** (Extract – Transform – Load)
- ETL orchestration and scheduling
- T-SQL data transformation
- Understanding of OLTP vs OLAP
- Preparing data for Power BI / BI tools
- End-to-end data pipeline (Source → DWH → Visualization)
- Diagnosing and resolving real SSIS deployment/runtime issues
- Clean project documentation & structure

---

## 🔮 Possible Next Steps (Future Improvements)

- Incremental load pattern (watermark / control table) inside SSIS
- Full continuous Date dimension (calendar table)
- Surrogate keys
- Slowly Changing Dimensions (SCD Type 1 / Type 2) in SSIS
- Staging area + error handling & logging
- Additional facts (e.g. Inventory, Purchasing)
- Row-level security and performance optimization
- Deployment to Azure (Azure Data Factory or Azure SSIS IR) + Power BI Service
- CI/CD for SSIS packages
- Email notifications on SQL Server Agent job failure

---

## 👤 Author

Built as a hands-on project to demonstrate end-to-end Data Warehouse design, SSIS ETL development, and Power BI readiness.

Feel free to fork, improve, or use as a learning reference.