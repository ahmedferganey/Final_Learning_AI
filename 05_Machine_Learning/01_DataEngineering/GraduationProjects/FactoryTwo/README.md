# Kandil Glass — Production Data Platform
## Excel → Staging DB → SSIS → Data Warehouse → Power BI

**Status:** Design Complete (Aligned Staging + DWH) — Ready for Implementation  
**Owner:** Kandil Glass — Production & BI Team  
**Production lines in scope:** 21, 22, 23, 24, 25  
**Last updated:** July 2026

---

## 1. Why this project exists

Today, production data (job changes, losses, output, defects, rework, line configuration) is captured manually in Excel by shift/line teams. This works for daily shop-floor use, but creates serious problems for company-wide reporting:

- Every file has a slightly different structure → nothing can be combined automatically.
- History is scattered across daily/weekly files instead of one trusted source.
- Power BI reports break every time someone changes a column name or layout.
- There is no single definition of “a line”, “a shift”, “a loss category”, “a job-change type”, or “a defect”.

**Goal:** Keep Excel as the *data entry tool* people already know, but stop treating Excel files as the *system of record*.

```plaintext
Operators enter data → Standardized Excel Templates (multiple workbooks)
↓
Staging Database (raw, auditable)
↓ (SSIS ETL: clean, validate, unpivot, surrogate keys)
Data Warehouse (Star Schema)
↓
Power BI (single source of truth)
```


---

## 2. Architecture Overview

| Layer | Purpose | Technology |
|-------|---------|------------|
| **1. Data Entry** | Shift / Quality / Process teams enter data | 7 standardized Excel workbooks (locked structure + dropdowns) |
| **2. Staging DB** | Daily raw landing zone (one table ≈ one Excel form) | SQL Server Staging schema |
| **3. ETL** | Clean, unpivot, lookup keys, apply business rules | SSIS packages |
| **4. Data Warehouse** | Governed star schema + full history | SQL Server DWH |
| **5. Reporting** | Dashboards, KPIs, self-service | Power BI |

**Design principle:** Excel stays simple and disposable. All smart logic (unpivoting, key resolution, calculated measures) lives in SSIS / DWH / Power BI.

---

## 3. Excel Data Entry Layer (Multiple Workbooks)

We use **multiple specialized workbooks** (recommended for real factory use):

| # | Workbook | Who uses it | Staging Table |
|---|----------|-------------|---------------|
| 1 | `01_MasterData.xlsx` | Planning / Sales / IT | STG_CUSTOMER, STG_PRODUCT, STG_ORDER + all REF_ tables |
| 2 | `02_JobChangeLog.xlsx` | Production Supervisors | STG_JOBCHANGE |
| 3 | `03_DailyProduction.xlsx` | Production Supervisors | STG_PRODUCTION |
| 4 | `04_LossesAndOutput.xlsx` | Process Engineers | STG_LOSSESOUTPUT (wide → unpivoted in SSIS) |
| 5 | `05_DefectLog.xlsx` | Quality team | STG_DEFECTLOG (**hourly** per machine) |
| 6 | `06_ReworkLog.xlsx` | Quality / Production | STG_REWORK |
| 7 | `07_LineConfig.xlsx` | Process / Technical | STG_LINECONFIG |

### Key rules for all templates
- One row = one event / transaction
- No merged cells, no totals inside detail data
- Fixed headers matching the Staging tables
- Dropdowns (Data Validation) for all coded fields
- Real Excel dates
- Raw data only (no KPI formulas)
- Header row frozen + AutoFilter enabled
- Color coding: Yellow = dropdown, Green = date, Light blue = number

---

## 4. Staging Database Design

**Philosophy:**
- Natural keys only
- One table ≈ one Excel form
- Full load metadata on every table (`LoadID`, `SourceFileName`, `LoadTimestamp`, `RowStatus`, `ErrorMessage`)
- Minimal FK enforcement (validation happens in SSIS)

### Main Staging Tables
- `STG_JOBCHANGE`
- `STG_PRODUCTION`
- `STG_LOSSESOUTPUT` (wide format)
- `STG_DEFECTLOG` ← **includes `HourNumber` (0–23)** for hourly defect recording per machine
- `STG_REWORK`
- `STG_LINECONFIG`
- `STG_CUSTOMER` / `STG_PRODUCT` / `STG_ORDER`

### Reference Tables (for dropdowns & light validation)
- `REF_LINE`, `REF_JOBCHANGETYPE`, `REF_LOSSCATEGORY`
- `REF_DEFECT`, `REF_REJECTIONZONE`, `REF_REWORKSTATUS`, `REF_PRODUCTIONCASE`

---

## 5. Data Warehouse (Star Schema)

### Conformed Dimensions
- `DIM_DATE`
- `DIM_HOUR` ← **new** (0–23) to support hourly defect analysis
- `DIM_FACTORY`
- `DIM_LINE` (SCD Type 2)
- `DIM_SHIFT`
- `DIM_CREW`
- `DIM_PRODUCTIONCASE`
- `DIM_CUSTOMER`
- `DIM_PRODUCT`
- `DIM_ORDER`
- `DIM_JOBCHANGETYPE`
- `DIM_LOSSCATEGORY` (self-referencing hierarchy)
- `DIM_DEFECT`
- `DIM_REJECTIONZONE`
- `DIM_REWORKSTATUS`

### Fact Tables
| Fact Table | Grain | Source |
|------------|-------|--------|
| `FACT_JOBCHANGE` | One job change event | STG_JOBCHANGE |
| `FACT_PRODUCTION` | Line + Date + Shift + Order | STG_PRODUCTION |
| `FACT_LOSSESOUTPUT` | Line + Date + Shift (+ Hour for defects) + LossCategory / Defect | STG_LOSSESOUTPUT + STG_DEFECTLOG |
| `FACT_REWORK` | Line + Date + Shift + Order + Status | STG_REWORK |
| `FACT_LINECONFIG_DAILY` | Line + Date + Section | STG_LINECONFIG |

**Important design decision (Defects):**  
`FACT_LOSSESOUTPUT` contains a nullable `HourKey`.  
- Shift-level loss metrics → `HourKey = NULL`  
- Hourly defect records → `HourKey` is populated (0–23)

---

## 6. SSIS ETL Responsibilities

- Load Excel → Staging (with audit columns)
- Validate codes against REF_ / DIM_ tables
- Unpivot `STG_LOSSESOUTPUT` (wide → tall)
- Map hourly defects from `STG_DEFECTLOG` into `FACT_LOSSESOUTPUT` (with `HourKey`)
- Resolve all natural keys → surrogate keys
- Handle SCD Type 2 on `DIM_LINE`
- Upsert master data (`DIM_CUSTOMER`, `DIM_PRODUCT`, `DIM_ORDER`)
- Log rejects and row counts for every package

---

## 7. Daily Operational Flow

1. Teams fill the relevant Excel workbook during / after the shift.
2. Files are saved to the agreed shared folder (or SharePoint).
3. Automated process loads files into Staging DB.
4. SSIS packages run (nightly or per-shift) → transform Staging → DWH.
5. Power BI dataset refreshes every morning.
6. Rejected rows are reviewed by the data owner.

---

## 8. Master Data Governance

- One owner per dimension list.
- New codes must be added to Master Data / REF_ tables **first**, then they appear in Excel dropdowns.
- Maintain a living Data Dictionary.
- Never allow free-text entry for coded fields.

---

## 9. Project Phases

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 0 — Foundation | Data dictionary, open decisions, dimension lists | Done |
| 1 — Excel Templates | 7 standardized workbooks | Done (templates ready) |
| 2 — Staging DB | Create all STG_ + REF_ tables | Ready to build |
| 3 — DWH Design | Full star schema + DIM_HOUR | Ready to build |
| 4 — SSIS ETL | Packages for all domains | Next |
| 5 — Power BI Model | Semantic model + core dashboards | Next |
| 6 — Rollout & Governance | Training + ownership | Later |
| 7 — Scale | Add more domains (quality, maintenance, etc.) | Future |

---

## 10. Key Design Decisions Already Taken

| Topic | Decision |
|-------|----------|
| Excel approach | Multiple specialized workbooks (not one big file) |
| Defect recording | **Hourly per machine/line** |
| Defect storage in DWH | Inside `FACT_LOSSESOUTPUT` using nullable `HourKey` + `DIM_HOUR` |
| Losses format | Keep wide in Excel → Unpivot in SSIS |
| Production metrics | Dedicated `STG_PRODUCTION` / `FACT_PRODUCTION` |
| Order / Product / Customer | Full master data path in Staging + DWH |
| Line history | SCD Type 2 on `DIM_LINE` |
| Calculated fields | Stored as persisted computed columns only when useful (e.g. TotalJobChangeLosses_Hrs, ReworkedUnits). All KPIs otherwise calculated in Power BI |

---

## 11. Next Immediate Steps

1. Review and approve the 7 Excel templates.
2. Create Staging database + tables (including `HourNumber` in `STG_DEFECTLOG`).
3. Create DWH database + full star schema (including `DIM_HOUR`).
4. Build SSIS packages in this order:
   - Master Data load
   - Job Change
   - Daily Production
   - Losses (unpivot)
   - Defects (hourly)
   - Rework
   - Line Config
5. Build first Power BI dataset and dashboard.

---

*This README is the single source of truth for the architecture. Any change to grain, keys, or Excel structure must be reflected here first.*