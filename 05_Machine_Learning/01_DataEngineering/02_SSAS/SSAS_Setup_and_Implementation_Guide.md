# SSAS Multidimensional Project Setup & Implementation Guide

This document provides a complete, end-to-end, step-by-step technical guide for configuring SQL Server Analysis Services (SSAS), connecting SQL Server Data Tools (SSDT) / Visual Studio, and building and deploying an Analysis Services Multidimensional Cube.

---

## Technical Environment Summary

| Component | Standard Configuration / Value |
| :--- | :--- |
| **SQL Server Engine Instance** | `DESKTOP-R0FEFQL` (Default Instance / `localhost`) |
| **Analysis Services Engine** | `DESKTOP-R0FEFQL` (SSAS Multidimensional Mode) |
| **Database Engine Service Account** | Local Windows User (`.\BS`) |
| **Authentication Protocol** | Windows NT Integrated Security |
| **Source Relational DWH** | `AdventureWorksDW` |
| **SSAS Project Name** | `AdvenCubeSSAS` |

---

## Section 1: Pre-requisites & Service Configuration

Before launching Visual Studio, ensure that the underlying SQL Server services and network protocols are properly started and enabled.

### 1.1 Verifying SQL Server Services (`services.msc`)
1. Press `Win + R`, type `services.msc`, and press **Enter**.
2. Locate the following services and ensure their startup and running states:
   - **SQL Server (MSSQLSERVER)**: Status = `Running`, Startup Type = `Automatic`.
   - **SQL Server Analysis Services (MSSQLSERVER)**: Status = `Running`, Startup Type = `Automatic`.
   - **SQL Server Browser**: Status = `Running`, Startup Type = `Automatic`.

> **Note on Service Accounts:** If services run under a local account (e.g., `.\BS`), ensure that this user account has proper read permissions on the target database engine and administrative rights on SSAS.

### 1.2 Configuring Network Protocols (SQL Server Configuration Manager)
1. Open **SQL Server Configuration Manager**.
2. Expand **SQL Server Network Configuration** $ightarrow$ Click **Protocols for MSSQLSERVER**.
3. Enable the following protocols:
   - **Shared Memory**: `Enabled`
   - **TCP/IP**: `Enabled`
4. If TCP/IP was previously disabled, restart the **SQL Server (MSSQLSERVER)** service for changes to take effect.

---

## Section 2: Data Source & Data Source View (DSV) Setup

### 2.1 Establishing the Data Source Connection
1. In Visual Studio, open your SSAS project (`AdvenCubeSSAS`).
2. In **Solution Explorer**, right-click **Data Sources** $ightarrow$ Select **New Data Source...**
3. Click **Next** $ightarrow$ Click **New...** to create a connection string.
4. Configure the **Connection Manager** dialog:
   - **Provider**: `Microsoft OLE DB Driver for SQL Server` (or `MSOLEDBSQL`).
   - **Server or file name**: `DESKTOP-R0FEFQL` (or `.` / `localhost`). Do **not** append instance suffixes like `\BS` if running on the default instance.
   - **Log on to the server**: Select **Use Windows NT Integrated Security**.
   - **Initial catalog**: Select `AdventureWorksDW`.
5. Click **Test Connection** to confirm connectivity, then click **OK**.
6. Click **Next**, and on the **Impersonation Information** page:
   - Select **Use the credentials of the current user** (or **Use the service account**).
7. Name the Data Source (e.g., `AdventureWorks DWH`) and click **Finish**.

### 2.2 Building the Data Source View (DSV)
1. In **Solution Explorer**, right-click **Data Source Views** $ightarrow$ Select **New Data Source View...**
2. Click **Next**, select the `AdventureWorks DWH` data source, and click **Next**.
3. In the **Select Tables and Views** window, select the following tables from **Available objects** and move them to **Included objects**:
   - `FactSales` (Fact Table)
   - `DimDate` (Dimension Table)
   - `DimProduct` (Dimension Table)
   - `DimCustomer` (Dimension Table)
   - `DimTerritory` (Dimension Table)
4. Click **Next**, name the Data Source View `AdventureWorksDWH`, and click **Finish**.
5. Double-click `AdventureWorksDWH.dsv` to inspect the schema diagram. Ensure foreign key relationship lines connect `FactSales` to each `Dim*` table.

---

## Section 3: Dimension Design

Each dimension table must be wrapped in an Analysis Services Dimension object defining its surrogate keys and attributes.

### 3.1 Creating `DimDate`
1. Right-click **Dimensions** $ightarrow$ **New Dimension...** $ightarrow$ Click **Next**.
2. Select **Use an existing table** $ightarrow$ Click **Next**.
3. Set **Main table**: `DimDate`.
4. Set **Key columns**: `Date` (or `DateKey`).
5. Click **Next**. Select attributes to expose for analysis (e.g., `CalendarYear`, `CalendarQuarter`, `MonthNumberOfYear`, `EnglishMonthName`).
6. Name the dimension `DimDate` (or `Date`) and click **Finish**.

### 3.2 Creating Additional Dimensions
Repeat the Dimension Wizard process for the remaining entity tables:

* **Product Dimension (`DimProduct`)**:
  - **Main Table**: `DimProduct`
  - **Key Column**: `ProductKey`
  - **Attributes**: `EnglishProductName`, `Color`, `StandardCost`, `ListPrice`
* **Customer Dimension (`DimCustomer`)**:
  - **Main Table**: `DimCustomer`
  - **Key Column**: `CustomerKey`
  - **Attributes**: `FirstName`, `LastName`, `Gender`, `EmailAddress`
* **Territory Dimension (`DimTerritory`)**:
  - **Main Table**: `DimTerritory`
  - **Key Column**: `SalesTerritoryKey` (or `TerritoryID`)
  - **Attributes**: `SalesTerritoryRegion`, `SalesTerritoryCountry`, `SalesTerritoryGroup`

---

## Section 4: Cube Building & Measure Configuration

### 4.1 Constructing the Cube
1. In **Solution Explorer**, right-click **Cubes** $ightarrow$ Select **New Cube...**
2. Click **Next** $ightarrow$ Choose **Use existing tables** $ightarrow$ Click **Next**.
3. Under **Measure Group Tables**, check **`FactSales`** $ightarrow$ Click **Next**.
4. Select measures for aggregation (e.g., `SalesAmount`, `OrderQuantity`, `UnitPrice`, `ExtendedAmount`).
5. Check all previously created dimensions (`DimDate`, `DimProduct`, `DimCustomer`, `DimTerritory`) to attach them to the cube.
6. Name the cube `AdventureWorksCube` and click **Finish**.

---

## Section 5: Deployment & Processing

### 5.1 Project Deployment Settings
1. In **Solution Explorer**, right-click the project root (`AdvenCubeSSAS`) $ightarrow$ Select **Properties**.
2. Under **Configuration Properties**, click **Deployment**.
3. Configure target properties:
   - **Server**: `DESKTOP-R0FEFQL` (or `localhost`)
   - **Database**: `AdvenCubeSSAS`
   - **Processing Option**: `Do Full`
4. Click **OK**.

### 5.2 Building, Deploying, and Processing
1. In the top toolbar, click **Build** $ightarrow$ **Deploy AdvenCubeSSAS**.
2. Monitor the **Deployment Progress** window until deployment completes successfully.
3. If processing is required post-deployment:
   - Right-click the project or cube in **Solution Explorer** $ightarrow$ Select **Process**.
   - Click **Run** in the Process Database dialog.
   - Confirm status reads **Process succeeded**.

---

## Section 6: Validation & Data Browsing

1. Double-click `AdventureWorksCube.cube` in **Solution Explorer**.
2. Switch to the **Browser** tab at the top of the designer window.
3. Expand **Measures** and drag `Sales Amount` into the central matrix workspace.
4. Expand **DimDate** and drag `Calendar Year` into the row area.
5. Expand **DimTerritory** and drag `Sales Territory Country` into the column area.
6. Execute the query to verify that multidimensional aggregation slices are calculated accurately across all dimensions.
