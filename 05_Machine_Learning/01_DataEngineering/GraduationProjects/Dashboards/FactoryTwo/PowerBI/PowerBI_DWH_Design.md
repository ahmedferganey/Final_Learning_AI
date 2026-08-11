# Kandil Glass — Power BI Design on the Data Warehouse
**Version:** 1.0  
**Source:** DWH star schema (v3.2) fed by the 4 role-based Excel templates  
**Target:** Power BI Desktop / Service (Import mode recommended for Phase 1)

---

## 1. Purpose

This document defines how Power BI should be built on top of the Kandil Glass Data Warehouse so that:

- Reports use a single governed model (no direct Excel connections in production reports).
- Measures are defined once and reused across all pages.
- The model matches the confirmed business rules (Loss % of Design Output, hourly defects, etc.).
- The design is ready to move later to SSAS Tabular with minimal change.

---

## 2. Data Source & Connection

| Item | Recommendation |
|------|----------------|
| Source | SQL Server Data Warehouse (star schema) |
| Mode | **Import** (Phase 1) |
| Gateway | On-premises data gateway if DWH is on-prem |
| Refresh | Daily after SSIS load (e.g. 06:00) |
| Future | Switch dataset to SSAS Tabular when ready; visuals stay the same |

**Do not** connect Power BI reports directly to the Excel files or to Staging in production. Excel → Staging → DWH → Power BI.

---

## 3. Tables to Bring into the Model

### Dimensions (all)

| DWH Table | Power BI Name | Role |
|-----------|---------------|------|
| DIM_DATE | Date | Date dimension (mark as Date table) |
| DIM_HOUR | Hour | Hour of day (0–23) for defect analysis |
| DIM_FACTORY | Factory | Plant |
| DIM_LINE | Line | Production line (21–25) |
| DIM_SHIFT | Shift | AM / PM |
| DIM_CREW | Crew | A / B / C |
| DIM_PRODUCTIONCASE | Production Case | Normal / Trial / Reworking |
| DIM_CUSTOMER | Customer | Customer master |
| DIM_PRODUCT | Product | Product master |
| DIM_ORDER | Order | Order master |
| DIM_JOBCHANGETYPE | Job Change Type | Small / Medium / Big / Process |
| DIM_LOSSCATEGORY | Loss Category | 11 loss types + Total Reject |
| DIM_DEFECT | Defect | Defect names |
| DIM_REWORKSTATUS | Rework Status | Hold / Resorted / Move to Cullet |
| DIM_DOWNTIMEREASON | Downtime Reason | HE / CE / Palletizer reasons |

### Facts

| DWH Table | Power BI Name | Grain |
|-----------|---------------|-------|
| FACT_PRODUCTION | Production | Line + Date + Shift + Order |
| FACT_LOSSESOUTPUT | Losses Output | Line + Date + Shift + Order + Loss Category |
| FACT_JOBCHANGE | Job Change | One changeover event |
| FACT_DEFECTSAMPLING | Defect Sampling | Line + Date + Order + Hour + Defect |
| FACT_REWORK | Rework | Line + Date + Shift + Order + Status |

---

## 4. Relationships (Star Schema)

```
Date[DateKey]          → Production[DateKey]
Date[DateKey]          → Losses Output[DateKey]
Date[DateKey]          → Job Change[DateKey]
Date[DateKey]          → Defect Sampling[DateKey]
Date[DateKey]          → Rework[DateKey]

Hour[HourKey]          → Defect Sampling[HourKey]

Factory[FactoryKey]    → Production, Losses Output, Job Change, Defect Sampling, Rework
Line[LineKey]          → Production, Losses Output, Job Change, Defect Sampling, Rework
Shift[ShiftKey]        → Production, Losses Output, Job Change, Defect Sampling, Rework
Crew[CrewKey]          → Production, Job Change
Production Case[CaseKey] → Production
Order[OrderKey]        → Production, Losses Output, Job Change (From/To), Defect Sampling, Rework
Job Change Type[JobChangeTypeKey] → Job Change
Loss Category[LossCategoryKey] → Losses Output
Defect[DefectKey]      → Defect Sampling
Rework Status[ReworkStatusKey] → Rework
Downtime Reason[DowntimeReasonKey] → Job Change (HE / CE / Palletizer reason keys)

Customer[CustomerKey]  → Product[CustomerKey]
Product[ProductKey]    → Order[ProductKey]
```

**Cross-filter direction:** Single (dimension → fact) for all relationships.  
**Date table:** Mark `Date` as the official Date table in Power BI.

---

## 5. Core Measures (DAX)

Copy these into the model (preferably in a dedicated Measures table).

### Production

```dax
Actual Pack = SUM ( Production[ActualPack] )

Design Output = SUM ( Production[DesignOutput] )

Total Hold = SUM ( Production[TotalHold] )

Working Hours = SUM ( Production[WorkingHours] )

Pack Efficiency % = 
DIVIDE ( [Actual Pack], [Design Output] )
```

### Losses (confirmed business rules)

```dax
Loss Percent = SUM ( 'Losses Output'[LossPercent] )

Total Losses % = 
CALCULATE (
    SUM ( 'Losses Output'[LossPercent] ),
    NOT ( 'Loss Category'[CategoryName] = "Total Reject" )
)

Loss Quantity = SUM ( 'Losses Output'[ComputedValue] )
-- ComputedValue already = LossPercent × DesignOutput (populated by SSIS)

Total Reject Qty = 
CALCULATE (
    SUM ( 'Losses Output'[ComputedValue] ),
    'Loss Category'[CategoryName] = "Total Reject"
)

Loss Rate vs Design % = 
DIVIDE ( [Loss Quantity], [Design Output] )
```

### Defects (hourly sampling)

```dax
Defect Quantity = SUM ( 'Defect Sampling'[Quantity] )

Total Samples = SUM ( 'Defect Sampling'[TotalSamples] )

Defect Rate % = 
DIVIDE ( [Defect Quantity], [Total Samples] )
```

### Rework

```dax
Reworked Units = SUM ( Rework[ReworkedUnits] )

Rework Rate % = 
DIVIDE ( [Reworked Units], [Actual Pack] )
```

### Job Change

```dax
Total Job Change Hours = SUM ( 'Job Change'[TotalJobChangeLosses_Hrs] )

Avg Job Change Hours = AVERAGE ( 'Job Change'[TotalJobChangeLosses_Hrs] )
```

### FPY (near-term win)

```dax
FPY % = 
DIVIDE ( [Actual Pack], [Actual Pack] + [Total Reject Qty] + [Total Hold] )
```

---

## 6. Suggested Report Pages

| Page | Audience | Key Visuals |
|------|----------|-------------|
| **1. Executive Overview** | Plant Head / Management | Actual Pack vs Design Output (trend), Pack Efficiency %, Total Losses %, Defect Rate %, FPY % |
| **2. Production by Line** | Supervisors | Matrix: Line × Date — Actual Pack, Design Output, Efficiency %, Hold |
| **3. Losses Analysis** | Process Engineers | Stacked bar / waterfall of the 11 loss categories; Total Losses % trend; Loss Quantity vs Design Output |
| **4. Job Change Performance** | Supervisors / Process | Duration vs Target (T1/T2); reasons breakdown (HE / CE / Palletizer); count of changes by type |
| **5. Quality — Defects** | Quality | Defect Rate % by Hour (line chart); Defect Pareto; heatmap Line × Hour |
| **6. Rework** | Quality / Production | Reworked Units by Status; trend; rate vs Pack |
| **7. Line Comparison** | Management | Clustered bar: Efficiency, Losses %, Defect Rate side-by-side for lines 21–25 |

---

## 7. Slicers (common across pages)

- Date (range or relative)
- Factory
- Line
- Shift
- Crew
- Production Case
- Order / Product / Customer (as needed)

Use a **sync slicer** pane so filters stay consistent across pages.

---

## 8. Mapping from Excel Workbooks → Model

| Excel Workbook | Feeds DWH Facts | Used in Power BI pages |
|----------------|-----------------|------------------------|
| 01_MasterData | All dimensions | Slicers + drill-through |
| 02_Supervisor_Log | Production, Job Change | Pages 1, 2, 4, 7 |
| 03_Process_Losses | Losses Output | Pages 1, 3, 7 |
| 04_Quality_Log | Defect Sampling, Rework | Pages 1, 5, 6 |

---

## 9. Row-Level Security (optional, later)

| Role | Filter |
|------|--------|
| Plant Manager | No filter (all lines) |
| Line Supervisor | `Line[LineNumber] IN { their lines }` |
| Quality | No line filter (or all lines) — focus on defect/rework pages |

Implement in Power BI (or later in SSAS) with AD groups.

---

## 10. Implementation Checklist

1. Connect Power BI Desktop to DWH (Import).
2. Select only the dimension and fact tables listed above.
3. Create relationships exactly as in Section 4.
4. Mark Date as Date table.
5. Create a Measures table and paste the DAX from Section 5.
6. Hide technical key columns (…Key) from Report view.
7. Build pages 1–3 first (highest value).
8. Validate numbers against a known Excel day (e.g. 2026-07-28 sample).
9. Publish to Power BI Service + schedule refresh after SSIS.
10. Later: point the same report at SSAS Tabular when the semantic layer is ready.

---

## 11. Design Principles (do not break)

- **No direct Excel connections** in published reports.
- **No calculated columns** for KPIs that belong as measures.
- **One Date table** shared by all facts.
- **Loss % of Design Output** and **Total Losses % = sum of 11 categories** stay consistent with the locked business rules.
- Keep the model star-shaped — avoid many-to-many or bi-directional filters unless absolutely required.

---

*This design is the contract between the DWH and Power BI. Any change to grain or measures should be updated here first.*
