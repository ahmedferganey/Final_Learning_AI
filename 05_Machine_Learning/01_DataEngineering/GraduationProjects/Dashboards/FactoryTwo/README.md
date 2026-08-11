# Kandil Glass — Production Data Platform
## Excel → Staging DB → SSIS → Data Warehouse → SSAS → Power BI

**Version:** 3.1  
**Status:** Staging + DWH DDL built and grounded in `System.xlsx`. Excel entry system exists (`System.xlsx`, 10 sheets). SSIS packages not yet built. SSAS semantic layer planned.  
**Owner:** Kandil Glass — Production & BI Team  
**Production lines in scope:** 21, 22, 23, 24, 25 (Factory `KG01`)

---

## 0. Version History

| Version | Change |
|---|---|
| 1.0 | Initial architecture draft based on two original raw Excel exports |
| 2.0 | Business Logic Document formalized; ERD v2 with 6 modeling gaps resolved |
| 3.0 | Redesigned against actual working Excel system (`System.xlsx`). Corrected loss categories, defect grain, line-config granularity. Separated confirmed architecture from future scope. |
| **3.1 (current)** | Integration check completed (System.xlsx ↔ Staging ↔ DWH). SSAS added to target architecture as the enterprise semantic / OLAP layer between DWH and Power BI. Open gaps documented. |

---

## 1. Why This Project Exists

Production data (job changes, losses, output, defects, rework) is captured manually in Excel by shift/line teams. This works for daily shop-floor use, but creates problems for company-wide reporting:

- Every file has a slightly different structure → nothing combines automatically.
- History is scattered across daily/weekly files instead of one trusted source.
- Power BI reports break every time someone changes a column name or layout.
- There is no single definition of "a line," "a shift," "a loss category," or "a defect."

**Goal:** Keep Excel as the *data entry tool* people already know, but stop treating Excel files as the *system of record*.

```
Operators enter data → Excel System (System.xlsx / future standardized templates)
                              ↓ (daily load)
                        Staging Database          ← CONFIRMED, DDL built
                              ↓ (SSIS ETL)
                        Data Warehouse (star)     ← CONFIRMED, DDL built
                              ↓
                        SSAS Tabular / Multidimensional  ← PLANNED (semantic layer)
                              ↓
                        Power BI (dashboards + self-service)
```

---

## 2. Architecture Overview

| Layer | Purpose | Status |
|---|---|---|
| **1. Data Entry** | Shift / Quality / Process teams enter daily data | ✅ Exists — `System.xlsx` (10 sheets) |
| **2. Staging DB** | Raw daily landing zone (one table ≈ one Excel sheet) | ✅ DDL built |
| **3. ETL** | Clean, unpivot, resolve surrogate keys, apply business rules | ⏳ Not yet built |
| **4. Data Warehouse (DWH)** | Governed star schema, full history | ✅ DDL built |
| **5. SSAS (Semantic Layer)** | Centralized measures, hierarchies, KPIs, security, performance | 💡 Planned |
| **6. Reporting** | Dashboards, self-service analytics | ⏳ Not yet built |

**Design principle:** Excel stays simple. Staging is a faithful copy. All business logic, calculations, and KPI definitions live in SSIS → DWH → SSAS, never in Excel formulas.

---

## 3. Source / Data Entry Layer (`System.xlsx`)

| Sheet | Feeds Staging | Grain |
|---|---|---|
| Customers | `STG_CUSTOMER` | One customer |
| Products | `STG_PRODUCT` | One product |
| JobChangeTypes | `STG_JOBCHANGETYPE` | One job-change type + targets |
| OrderLog | `STG_ORDER` | One order |
| JobChangeLog | `STG_JOBCHANGE` | One changeover event |
| DailyProdLog | `STG_PRODUCTION` | Line + Date + Shift + Order |
| LossesLog | `STG_LOSSESOUTPUT` | Line + Date + Shift + Order (11 flat % categories + TotalReject) |
| SamplingDefectLog | `STG_SAMPLINGDEFECTLOG` | Line + Date + Order + **Hour** + Defect (+ TotalSamples) |
| ReworkLog | `STG_REWORK` | Line + Date + Shift + Order + Status |
| DataValidation | powers `REF_*` tables & Excel dropdowns | — |

### Key Rules for Data Entry
- One row = one event. No merged cells, no totals inside detail data.
- Fixed headers matching staging tables.
- Dropdowns for every coded field.
- Real Excel dates.
- Raw data only — no KPI formulas inside the entry workbook.

---

## 4. Staging Database — Confirmed Design

**Philosophy:** Natural keys only, one table ≈ one Excel sheet, full load metadata (`LoadID`, `SourceFileName`, `LoadTimestamp`, `RowStatus`, `ErrorMessage`) on every table.

**Master data:** `STG_CUSTOMER`, `STG_PRODUCT`, `STG_JOBCHANGETYPE`, `STG_ORDER`  
**Transactional:** `STG_JOBCHANGE`, `STG_PRODUCTION`, `STG_LOSSESOUTPUT`, `STG_SAMPLINGDEFECTLOG`, `STG_REWORK`  
**Reference lists:** `REF_FACTORY`, `REF_LINE`, `REF_JOBCHANGETYPE`, `REF_LOSSCATEGORY`, `REF_DEFECT`, `REF_REWORKSTATUS`, `REF_PRODUCTIONCASE`, `REF_DOWNTIMEREASON`

**Intentionally removed (no source support):**
- `STG_LINECONFIG` → folded into `STG_PRODUCTION` as `NoSections` / `NoCavities`
- `REF_REJECTIONZONE` → no Zone field exists in SamplingDefectLog

---

## 5. Data Warehouse — Confirmed Design

**Conformed dimensions:**  
`DIM_FACTORY`, `DIM_DATE`, `DIM_HOUR`, `DIM_LINE` (SCD2), `DIM_SHIFT`, `DIM_CREW`, `DIM_PRODUCTIONCASE`, `DIM_CUSTOMER`, `DIM_PRODUCT`, `DIM_ORDER`, `DIM_JOBCHANGETYPE`, `DIM_LOSSCATEGORY` (11 flat categories), `DIM_DEFECT`, `DIM_REWORKSTATUS`, `DIM_DOWNTIMEREASON`

**Fact tables:**

| Fact | Grain | Notes |
|---|---|---|
| `FACT_JOBCHANGE` | One changeover event | From/To Order + 3 reason FKs (HE / CE / Palletizer) |
| `FACT_PRODUCTION` | Line + Date + Shift + Order | Includes `NoSections`, `NoCavities`, `WorkingHours`, `DesignOutput` |
| `FACT_LOSSESOUTPUT` | Line + Date + Shift + Order + LossCategory | `LossPercent` + `ComputedValue` (formula still open) |
| `FACT_DEFECTSAMPLING` | Line + Date + Order + **Hour** + Defect | Separate fact — has `TotalSamples` denominator |
| `FACT_REWORK` | Line + Date + Shift + Order + Status | `ReworkedUnits` persisted computed column |

---

## 6. Integration Check Summary (System.xlsx ↔ Staging ↔ DWH)

| Area | Status | Notes |
|---|---|---|
| Master data path (Customer → Product → Order) | ✅ Aligned | Clean |
| Job Change + Downtime Reasons | ✅ Aligned | 3 reason FKs correctly modeled |
| Production | ⚠️ Gap | `FactoryCode` missing in DailyProdLog source — Staging allows NULL, SSIS must default |
| Losses (11 categories) | ⚠️ Naming + formula | Excel names ≠ Staging `_Pct` names; % meaning still open |
| Defect Sampling (hourly) | ✅ Aligned | Correctly separated into its own fact with `DIM_HOUR` |
| Rework | ✅ Aligned | Clean |
| Line Config | ✅ Correctly folded | No per-section source data exists |
| Zone on defects | ✅ Correctly removed | No Zone field in source |

**Priority fixes before SSIS build:**
1. Confirm the business meaning of each LossesLog percentage (blocks `ComputedValue` and all Losses KPIs).
2. Add `FactoryCode` to DailyProdLog (or document the SSIS default rule permanently).
3. Publish an explicit column-mapping table for the Losses unpivot (Excel name → Staging name → `DIM_LOSSCATEGORY`).

---

## 7. SSIS ETL Responsibilities (Not Yet Built)

- Load each Excel sheet → matching staging table with full audit columns.
- Validate codes against `REF_` / `DIM_` tables; log and quarantine bad rows.
- Unpivot `STG_LOSSESOUTPUT` (11 percentage columns → tall `FACT_LOSSESOUTPUT` rows).
- Resolve natural keys → surrogate keys for every fact.
- SCD Type 2 on `DIM_LINE` when attributes change.
- Upsert master data (`DIM_CUSTOMER`, `DIM_PRODUCT`, `DIM_ORDER`, `DIM_JOBCHANGETYPE`).
- Populate `DIM_HOUR` (0–23) once.

**Suggested package order:**  
Master Data → JobChange → Production → Losses (unpivot) → DefectSampling → Rework

---

## 8. SSAS Semantic Layer (Planned)

SSAS sits **between the Data Warehouse and Power BI**. It is the enterprise semantic / OLAP layer.

### Why SSAS is in scope
- Centralized, version-controlled DAX (or MDX) measures — single definition of Efficiency %, Defect Rate, Loss %, FPY, etc.
- Hierarchies (Date, Loss Category, Product, Line) available to every report.
- Row-level security by role (Plant Manager, Line Supervisor, Quality, etc.) enforced once.
- Better query performance and scale as history grows across 5 lines and multiple years.
- Power BI (and Excel, Reporting Services, etc.) connect to one trusted model instead of each developer reinventing measures.

### Recommended approach
| Choice | Recommendation | Reason |
|---|---|---|
| Model type | **Tabular** (DAX) | Faster to develop, native for Power BI, sufficient for current grain |
| Deployment | SQL Server Analysis Services (on-prem) or Azure Analysis Services / Fabric | Match existing SQL Server footprint |
| Source | DirectQuery or Import from DWH star schema | Import preferred initially for performance |
| Security | Roles mapped to AD groups | Plant / Line / Quality visibility |

### Core measures to implement in SSAS (once DWH is live)
- Actual Pack, Design Output, Working Hours
- Efficiency % / Performance %
- Total Reject, Loss % by category
- Defect Rate % = Quantity / TotalSamples (from `FACT_DEFECTSAMPLING`)
- Job Change duration vs Target (T1 / T2)
- Reworked Units, Rework rate
- FPY (First Pass Yield) — derivable from existing Production + Rework data

### What SSAS does **not** replace
- Staging and DWH remain the system of record.
- SSIS remains responsible for cleaning and key resolution.
- Power BI remains the primary visualization and self-service tool.

---

## 9. Daily Operational Flow (Target)

1. Shift / Quality / Process staff fill `System.xlsx` (or future role-based templates).
2. File saved to agreed shared location (mechanism TBD).
3. Scheduled job loads new data into Staging.
4. SSIS transforms Staging → DWH.
5. SSAS model processes (full or incremental).
6. Power BI datasets refresh from SSAS (or directly from DWH during early phases).
7. Rejected rows reviewed by data owner.

---

## 10. Open Decisions Still Needed

1. **Loss percentage formula** — Is each of the 11 percentages a share of `TotalReject_Value`, of `DesignOutput`, of working time, or something else? Blocks all Losses KPIs.
2. **`FactoryCode` on DailyProdLog** — Add to source sheet or permanently default in SSIS?
3. **File delivery mechanism** — Shared folder, SharePoint, Teams, or email-in?
4. **Final Defect Name & Downtime Reason lists** — currently draft values pending QA / Production sign-off.
5. **SSAS timing** — Build SSAS immediately after first DWH load, or run Power BI directly on DWH for 1–2 months first?
6. **One workbook vs multiple role-based workbooks** — operational preference still open.

---

## 11. Master Data Governance

- One owner per dimension list (Line, Shift, Job Change Type, Loss Category, Defect, Rework Status, Downtime Reason).
- New codes are added to `REF_` / `DIM_` tables **first**, then appear in Excel dropdowns — never the reverse.
- Living Data Dictionary: source column → staging column → DWH column → SSAS measure / Power BI field.

---

## 12. Proposed Future Scope (Not Yet Designed)

| Idea | Prerequisite |
|---|---|
| Downtime tracking (start/end timestamps) | New Excel log + new fact table |
| Machine-level detail (finer than Line) | Business decision + source data |
| Full OEE (Availability / Performance / Quality) | Requires downtime tracking first |
| FPY | Achievable now from existing facts — near-term win |
| Row-Level Security | Implement in SSAS (or Power BI) once model exists |

**Recommendation:** Deliver FPY and basic RLS as soon as the core pipeline + SSAS model are live. Defer full OEE / machine-level until dedicated data capture exists.

---

## 13. Next Steps

1. Close the open decisions in Section 10 (Loss % formula is highest priority).
2. Fix the small source gaps (`FactoryCode`, naming consistency).
3. Build SSIS packages in dependency order.
4. Populate DWH and validate with sample data from `System.xlsx`.
5. Design and deploy SSAS Tabular model (measures, hierarchies, roles).
6. Connect Power BI to SSAS and deliver first production dashboards.
7. Revisit future-scope items (OEE, machine-level) once the core platform is stable.

---

*This README is the single source of truth for the architecture. Any change to grain, keys, Excel structure, or semantic-layer scope must be reflected here first.*
