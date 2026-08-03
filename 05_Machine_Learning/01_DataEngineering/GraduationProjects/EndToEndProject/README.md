# AdventureWorks Data Warehouse & Power BI Analytics

End-to-end **Data Warehouse** solution built from the AdventureWorks sample database, designed for analytical reporting in **Power BI**.

This project demonstrates a complete dimensional modeling + ETL workflow: extracting transactional data with **SSIS**, transforming it into a star schema, loading it into a dedicated Data Warehouse, and preparing it for business intelligence and visualization.

---

## Table of Contents

1. [Project Goal](#-project-goal)
2. [Architecture Overview](#-architecture-overview)
3. [What Was Implemented](#-what-was-implemented)
4. [SSIS ETL Package – Full Implementation Guide](#-ssis-etl-package--full-implementation-guide)
5. [SSAS Tabular Semantic Layer – Implementation Guide](#-ssas-tabular-semantic-layer--implementation-guide)
6. [Tech Stack](#-tech-stack)
7. [Project Structure](#-project-structure)
8. [How to Run](#-how-to-run)
9. [Example Insights You Can Build in Power BI](#-example-insights-you-can-build-in-power-bi)
10. [Troubleshooting](#-troubleshooting)
11. [Skills Demonstrated](#-skills-demonstrated)
12. [Possible Next Steps](#-possible-next-steps-future-improvements)
13. [Author](#-author)

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
   SSAS Tabular Model (Semantic Layer)
   • Relationships, hierarchies, DAX measures
   • Row-Level Security, single reusable source of truth
          │
          ▼
     Power BI Desktop / Service
   (Live Connection to SSAS, or direct Import from the DWH)
   (Dashboards + Scheduled Refresh / SSAS Processing)
```

> The SSAS layer is an **optional enterprise-style extension**. Power BI can also connect straight to `AdventureWorksDWH` (Import mode) without SSAS in between — that's the simpler path used earlier in this project. SSAS is added when you want one governed semantic model reused across multiple reports, centralized DAX measures, and Row-Level Security enforced outside of Power BI itself.

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

### 5. Semantic Layer with SSAS (Optional Extension)
- SSAS Tabular model built on top of `AdventureWorksDWH`
- Centralizes relationships, hierarchies, and DAX measures in one governed model
- Row-Level Security defined once and enforced for every report that connects to it
- Power BI connects live to this model instead of (or in addition to) importing the DWH directly

### 6. Design Principles Applied
- Clear definition of **fact grain**
- Denormalized dimensions for easy filtering and hierarchies
- Separation of concerns (Source → ETL → DWH → Semantic Layer → BI)
- Ready for Power BI relationships and DAX measures
- Production-oriented ETL with SSIS
- Single semantic source of truth via SSAS (avoids duplicated measures across reports)

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
## 🧊 SSAS Tabular Semantic Layer – Implementation Guide

This section documents how an **Analysis Services Tabular model** was added on top of `AdventureWorksDWH`, sitting between the warehouse and Power BI as a governed semantic layer.

### Why add SSAS here

| Without SSAS (Power BI Import only) | With SSAS Tabular |
|---|---|
| Each `.pbix` has its own copy of measures/relationships | One model, reused by every report via **Live Connection** |
| RLS defined per Power BI file | RLS defined once, centrally, in the model |
| Data duplicated into every report's cache | Single source of truth; reports query the model live |
| Fine for one dashboard / one developer | Better fit for multiple reports, multiple authors, larger data volumes |

For a portfolio project, adding this layer demonstrates understanding of enterprise BI architecture, not just report-building.

### Prerequisites

- **SQL Server Analysis Services (Tabular mode)** instance installed and running
- Visual Studio + **SQL Server Data Tools (SSDT)** with the *Analysis Services* project template (installed via the Visual Studio Installer → Individual Components → "SQL Server Analysis Services projects", or the standalone SSDT installer)
- `AdventureWorksDWH` already populated by the SSIS package
- Enough permissions to deploy a database to the SSAS instance

### Step 1 — Create a new Analysis Services Tabular project

1. Open Visual Studio → **Create a new project**.
2. Search for **Analysis Services Tabular Project** → select it → **Next**.
3. Name it `AdventureWorks_DWH_SSAS`, choose a short local path, click **Create**.
4. When prompted, choose the **Compatibility Level** matching your SSAS server version (e.g. 1600 for SQL Server 2022) and select the **Workspace server** (usually your local SSAS instance or an integrated workspace).

### Step 2 — Import data from the Data Warehouse

1. In Solution Explorer, right-click the model → **Import from Data Source** (or **Model** menu → **Import from Data Source**).
2. Choose **SQL Server** as the source type.
3. Server name: your SQL Server instance; Database: `AdventureWorksDWH`.
4. In the table selection screen, check: `FactSales`, `DimCustomer`, `DimProduct`, `DimTerritory`, and your date table (`DateTable`, per the fix applied earlier in the Power BI section).
5. Click **Load** to import the data into the model's in-memory storage (VertiPaq).

### Step 3 — Build relationships

1. Switch to **Diagram View** (View menu → Diagram View, or the icon in the bottom-right).
2. Drag to connect:
   - `DateTable[Date]` → `FactSales[OrderDate]`
   - `DimCustomer[CustomerID]` → `FactSales[CustomerID]`
   - `DimProduct[ProductID]` → `FactSales[ProductID]`
   - `DimTerritory[TerritoryID]` → `FactSales[TerritoryID]`
3. Each relationship defaults to One (dimension) → Many (fact), Single cross-filter direction — leave these as-is unless a specific visual requires bi-directional filtering.

### Step 4 — Mark the Date table

1. Right-click `DateTable` in Diagram View → **Mark as Date Table**.
2. Select the `Date` column.
3. This enables time-intelligence DAX functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, etc.) inside the model itself.

### Step 5 — Build measures

1. Switch to **Data View** (or Diagram View — measures can be added from the measure grid under any table).
2. Click into the empty measure grid area below `FactSales` and add each measure (one cell per measure):

```dax
Total Revenue = SUM(FactSales[LineTotal])
Total Quantity = SUM(FactSales[OrderQty])
Order Count = DISTINCTCOUNT(FactSales[SalesOrderID])
Avg Order Value = DIVIDE([Total Revenue], [Order Count])
YTD Revenue = TOTALYTD([Total Revenue], DateTable[Date])
PY Revenue = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DateTable[Date]))
Revenue YoY % = DIVIDE([Total Revenue] - [PY Revenue], [PY Revenue])
```

3. Format each measure (Properties pane → Format → Currency / Whole Number / Percentage as appropriate) so every report connecting to this model inherits correct formatting automatically.

### Step 6 — Build hierarchies (optional but recommended)

1. In Diagram View, on `DimProduct`, select `Category` and `SubCategory` and `ProductName` together (Ctrl-click) → right-click → **Create Hierarchy**. Name it `Product Hierarchy`.
2. On `DateTable`, create a `Calendar Hierarchy`: `Year` → `Quarter` → `Month` → `Date`.
3. These hierarchies let report authors drill down without manually building them in every report.

### Step 7 — Row-Level Security (optional)

1. **Model** menu → **Roles** → **New**.
2. Name the role (e.g. `TerritoryManagers`), set **Read** permission.
3. On the **Row Filters** tab, select `DimTerritory` and add a DAX filter, e.g.:

```dax
[TerritoryName] = USERNAME()
```

(or a lookup table mapping usernames to allowed territories, for a real-world setup).
4. Assign Active Directory users/groups to this role after deployment (SSMS → Roles → Membership), or map them in Power BI Service under **Security** for the dataset.

### Step 8 — Deploy the model to the SSAS server

1. Right-click the project → **Properties**.
2. Set **Server**: your SSAS instance name; **Database**: `AdventureWorks_DWH_SSAS`.
3. Right-click the project → **Deploy**.
4. Visual Studio builds the model and pushes it to the SSAS server, then processes it (loads data into memory).

### Step 9 — Connect Power BI to the model (Live Connection)

1. In Power BI Desktop → **Get Data** → **SQL Server Analysis Services database**.
2. Server: your SSAS instance; Database: `AdventureWorks_DWH_SSAS`.
3. Choose **Connect live** (not Import).
4. Power BI now shows the model's tables, hierarchies, and measures directly — no local data copy, no need to rebuild measures in Power BI.

### Step 10 — Keep the model refreshed after each SSIS load

Since Power BI is now live-connected, the SSAS model itself needs reprocessing after every SSIS run — Power BI's own "scheduled refresh" doesn't apply in Live Connection mode.

1. Add a step to the daily pipeline: after the SSIS job finishes, trigger an **Analysis Services Processing Task**.
2. Easiest approach: create a small SSIS package (or a step in the existing one) using the **Analysis Services Processing Task** control-flow item, pointed at the `AdventureWorks_DWH_SSAS` database, mode **Process Full**.
3. Add this task to the same SQL Server Agent job (or a follow-on job scheduled a few minutes after the ETL job), so the sequence is: `SSIS ETL load → SSAS Process Full → data live for all connected reports`.

---

## ⚠️ Troubleshooting & Lessons Learned (SSAS Setup)

During the SSAS Tabular implementation, several real-world infrastructure issues were encountered. This section documents the **problems, root causes, and resolutions**.

### 🔴 Issue 1 — SSAS Service Fails to Start

**Symptom**
- SSAS service starts and immediately stops
- Visual Studio error: `localhost was not found`

**Root Cause**
- Service account changed to a custom user (`BS`)
- Missing permissions on SSAS directories

**Solution**
1. Grant **Full Control** to the service account on:
   ```
   C:\Program Files\Microsoft SQL Server\MSAS17.MSSQLSERVER\
   ```
2. Ensure the account has **"Log on as a service"** rights
3. Restart SSAS service

---

### 🔴 Issue 2 — Cryptographic Key Regeneration

**Symptom**
```
Successfully generated server Gen2 cryptokey file...
Any existing databases ... will have their cryptkeys corrupt
```

**Root Cause**
- Changing the service account invalidated encryption keys
- SSAS could not decrypt existing metadata

**Impact**
- Existing SSAS databases became unusable

**Solution**
- Accept key regeneration
- Proceed with system database reset (see Issue 3)

---

### 🔴 Issue 3 — Corrupted SSAS System Database (Critical)

**Symptom**
```
System.0.asm.xml
Input past end of file
```

**Root Cause**
- System database corruption due to encryption mismatch

**Solution**
1. Stop SSAS service
2. Navigate to:
   ```
   C:\Program Files\Microsoft SQL Server\MSAS17.MSSQLSERVER\OLAP\Data\
   ```
3. Delete or rename:
   ```
   System.0.asm.xml
   System.1.asm.xml
   ```
   (or reset the entire `Data` folder)
4. Restart SSAS service

**Result**
- SSAS recreates system database automatically
- Service starts successfully

---

### 🔴 Issue 4 — Visual Studio Cannot Connect to SSAS

**Symptom**
```
localhost was not found
```

**Root Cause**
- SSAS service was not running

**Solution**
- Ensure SSAS is running
- Verify project property:
  ```
  Workspace Server = localhost
  ```

---

## 🧠 Key Lessons Learned

- SSAS is **highly sensitive to service account changes**
- Encryption keys are tied to the service identity
- Changing accounts without preparation can:
  - Corrupt cryptographic keys
  - Break system databases
- The folder:
  ```
  OLAP\Data
  ```
  is **critical for SSAS startup**
- Fastest recovery path in many cases:
  ```
  Reset system database → Restart SSAS → Redeploy model
  ```

---

## ✅ Final Outcome

- SSAS running successfully in **Tabular mode**
- Visual Studio connects without errors
- Model deployment and processing work correctly
- Power BI connects via **Live Connection**
```


---

## 🛠️ Tech Stack

- **SQL Server** + SQL Server Management Studio (SSMS)
- **SQL Server Integration Services (SSIS)**
- **SQL Server Analysis Services (SSAS Tabular)** — semantic layer, DAX measures, RLS *(optional extension)*
- **SQL Server Data Tools (SSDT)** / Visual Studio
- **T-SQL** (table creation, transformations)
- **DAX** (Tabular model measures, time intelligence)
- **AdventureWorks** sample database (source)
- **Dimensional Modeling** (Star Schema / Kimball)
- **Power BI Desktop** + Power BI Service (reporting, Live Connection & scheduled refresh)
- **SQL Server Agent** (for scheduling the SSIS package and SSAS processing)

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
├── SSAS/                                     ← (optional) Semantic layer
│   └── AdventureWorks_DWH_SSAS/              ← Tabular model project (.smproj, .bim)
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

### 3. (Optional) SSAS Semantic Layer
1. Build and deploy the Tabular model as described in the [SSAS Tabular Semantic Layer guide](#-ssas-tabular-semantic-layer--implementation-guide) above.
2. Add an Analysis Services Processing Task to run after the SSIS load so the model reflects the latest data daily.

### 4. Power BI
1. Connect **Power BI Desktop** to either:
   - `AdventureWorksDWH` directly (**Import** mode), or
   - the deployed **SSAS Tabular model** (**Connect live**), if the optional semantic layer was built.
2. If connecting directly to the DWH, create relationships:
   - `FactSales[CustomerID]` → `DimCustomer[CustomerID]`
   - `FactSales[ProductID]` → `DimProduct[ProductID]`
   - `FactSales[OrderDate]` → `DateTable[Date]`
   - `FactSales[TerritoryID]` → `DimTerritory[TerritoryID]`
3. Build measures (examples) — already provided by the model if using Live Connection to SSAS:
   - Total Revenue = `SUM(FactSales[LineTotal])`
   - Total Quantity = `SUM(FactSales[OrderQty])`
   - Order Count = `DISTINCTCOUNT(FactSales[SalesOrderID])`
4. Publish to **Power BI Service**:
   - **Import mode**: configure **Scheduled Refresh** (use an On-premises Data Gateway if SQL Server is on-premises).
   - **Live Connection to SSAS**: no Power BI–side refresh needed — freshness is driven by the SSAS Processing Task in the pipeline instead.

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
| **Power BI shows stale data after a Live Connection to SSAS** | Live Connection reads whatever is currently processed in the SSAS model — refreshing in Power BI does nothing on its own | Reprocess the SSAS database (Process Full) after each SSIS load; add this as an Analysis Services Processing Task in the daily job |
| **Time-intelligence measures return blank or mirrored values in SSAS/Power BI** | The date table isn't marked as a date table, or a measure still references an old/unmarked date table | Confirm **Mark as Date Table** is applied to the correct table, and check every measure's formula references that same table (not a leftover one) |
| **SSAS deployment fails with a compatibility-level error** | The Tabular project's compatibility level doesn't match the target SSAS server version | Project properties → set **Compatibility Level** to match the server (check the server version in SSMS → Object Explorer properties) |

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
- **SSAS Tabular model development** (relationships, hierarchies, DAX measures, RLS)
- Understanding of semantic-layer architecture and Live Connection vs. Import in Power BI
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
- Perspectives in the SSAS model for role-specific views (e.g. Sales-only, Finance-only)
- Automate SSAS Process Full via an XMLA script/Agent job instead of a manual step
- Deploy the SSAS model to Azure Analysis Services or Power BI Premium/Fabric semantic models

---

## 👤 Author

Built as a hands-on project to demonstrate end-to-end Data Warehouse design, SSIS ETL development, an optional SSAS semantic layer, and Power BI readiness.

Feel free to fork, improve, or use as a learning reference.