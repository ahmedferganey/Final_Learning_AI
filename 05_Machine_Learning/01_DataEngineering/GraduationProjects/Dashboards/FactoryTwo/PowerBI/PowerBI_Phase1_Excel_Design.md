# Kandil Glass — Power BI Phase 1 Design
## Direct from Excel Templates (Fast Delivery)

**Version:** 1.0  
**Goal:** Deliver working dashboards quickly from the 4 role-based Excel workbooks  
**Later:** Switch the same reports to DWH / SSAS with minimal rework  

---

## 1. Strategy

| Phase | Source | Purpose |
|-------|--------|---------|
| **Phase 1 (now)** | 4 Excel workbooks on OneDrive | Fast dashboards, validate KPIs |
| **Phase 2 (next)** | Staging → SSIS → DWH → Power BI | Automated, historical, governed |

**Rule:** Shape the Excel model in Power Query so it already looks like the future DWH star schema. Same table names, same measure names → easy migration later.

---

## 2. Source Files

| File | Location | Role |
|------|----------|------|
| `01_MasterData.xlsx` | OneDrive `/Master/` | Dimensions + lookups |
| `02_Supervisor_Log_YYYYMMDD.xlsx` | OneDrive `/Daily/` | JobChange + DailyProduction |
| `03_Process_Losses_YYYYMMDD.xlsx` | OneDrive `/Daily/` | LossesOutput (wide) |
| `04_Quality_Log_YYYYMMDD.xlsx` | OneDrive `/Daily/` | SamplingDefectLog + Rework |

**Power BI connection:**  
Get Data → Excel Workbook (or Folder connector on `/Daily/` for automatic combine of dated files).

---

## 3. Power Query — Target Tables

Create these queries. Name them exactly as below (matches future DWH names).

### 3.1 Dimension-style tables (from MasterData)

| Query Name | Source Sheet | Notes |
|------------|--------------|-------|
| Customer | Customers | Remove blank rows |
| Product | Products | |
| Order | Orders | Rename TotalMoltenUnits if needed |
| Job Change Type | JobChangeTypes | |
| Line | Lines | |
| Shift | Lookups (Shift column) | Distinct list → AM, PM |
| Crew | Lookups (Crew column) | Distinct list → A, B, C |
| Production Case | Lookups | Normal, Trial, Reworking |
| Rework Status | Lookups | Hold, Resorted, Move to Cullet |
| Defect | Lookups (DefectName) | |
| Downtime Reason | Lookups (HE / CE / Palletizer columns) | Unpivot or create separate small tables if needed |
| Loss Category | Hard-code or from a small reference list | 11 categories + Total Reject |

### 3.2 Fact-style tables

| Query Name | Source | Power Query actions |
|------------|--------|---------------------|
| **Production** | DailyProduction sheet | Keep columns. Ensure EventDate is Date type. Add DateKey = EventDate if useful. |
| **Job Change** | JobChange sheet | Keep columns. EventDate → Date. |
| **Losses Output** | LossesOutput sheet | **Unpivot** the 11 % columns (see §4). Keep TotalReject_Value as separate logic or as its own category row. |
| **Defect Sampling** | SamplingDefectLog sheet | Keep. HourNumber as Whole Number (0–23). |
| **Rework** | Rework sheet | Keep. Optional: add ReworkedUnits = PalletsCount × ArticlesPerPallet as a column. |

---

## 4. Critical Power Query Step — Unpivot Losses

**Source columns (wide):**  
`FixedLosses, ISLosses, HotEndConveyerLosses, StuckDownLosses, LehrLosses, Evo16Losses, Evo12Losses, Evo5Losses, SanliLosses, VisualLosses, PalletizerLosses`

**Steps:**
1. Select the 11 percentage columns.
2. Transform → Unpivot Columns.
3. Rename:
   - `Attribute` → `CategoryName` (or map to clean names)
   - `Value` → `LossPercent`
4. Keep: FactoryCode, LineNumber, EventDate, ShiftCode, OrderNumber, TotalReject_Value, CategoryName, LossPercent.

**Optional — add Total Reject as a row:**  
Append a row (or separate query) where CategoryName = "Total Reject" and LossPercent = null, and a Quantity column = TotalReject_Value.

**Clean CategoryName mapping (recommended):**

| Excel Attribute | Clean CategoryName |
|-----------------|--------------------|
| FixedLosses | Fixed Losses |
| ISLosses | IS Losses |
| HotEndConveyerLosses | Hot End Conveyer Losses |
| StuckDownLosses | Stuck Down Losses |
| LehrLosses | Lehr Losses |
| Evo16Losses | Evo16 Losses |
| Evo12Losses | Evo12 Losses |
| Evo5Losses | Evo5 Losses |
| SanliLosses | Sanli Losses |
| VisualLosses | Visual Losses |
| PalletizerLosses | Palletizer Losses |

---

## 5. Date Table

Create a simple Date table in Power Query or DAX:

```dax
Date = 
ADDCOLUMNS (
    CALENDAR ( DATE(2025,1,1), DATE(2027,12,31) ),
    "Year", YEAR ( [Date] ),
    "Month", MONTH ( [Date] ),
    "MonthName", FORMAT ( [Date], "MMM" ),
    "WeekdayName", FORMAT ( [Date], "ddd" )
)
```

Mark as Date table. Relate `Date[Date]` to:
- Production[EventDate]
- Job Change[EventDate]
- Losses Output[EventDate]
- Defect Sampling[EventDate]
- Rework[EventDate]

---

## 6. Relationships (Phase 1 model)

```
Date[Date]              → Production[EventDate]
Date[Date]              → Job Change[EventDate]
Date[Date]              → Losses Output[EventDate]
Date[Date]              → Defect Sampling[EventDate]
Date[Date]              → Rework[EventDate]

Line[LineNumber]        → Production[LineNumber]          (and other facts)
Shift[ShiftCode]        → Production[ShiftCode]           (and other facts)
Crew[CrewCode]          → Production[CrewCode]
Production Case[CaseName] → Production[CaseName]
Order[OrderNumber]      → Production[OrderNumber]         (and other facts)
Job Change Type[JobChangeTypeName] → Job Change[JobChangeTypeName]
Loss Category[CategoryName] → Losses Output[CategoryName]
Defect[DefectName]      → Defect Sampling[DefectName]
Rework Status[StatusName] → Rework[ReworkStatusName]
```

Use **single** cross-filter direction (dimension → fact).  
If Line/Shift exist only as columns on facts (no separate dim tables yet), you can still build; add proper dim tables as soon as possible for cleaner slicers.

---

## 7. Core Measures (same names as future DWH model)

### Production measures

```dax
Actual Pack = SUM ( DailyProduction_Fact[ActualPack] )

Design Output = SUM ( DailyProduction_Fact[DesignOutput] )

Total Hold = SUM ( DailyProduction_Fact[TotalHold] )

Working Hours = SUM ( DailyProduction_Fact[WorkingHours] )

Pack Efficiency % = 
DIVIDE ( [Actual Pack], [Design Output] )

Hold Rate % = 
DIVIDE ( [Total Hold], [Design Output] )

Designed Cuts Per Hour = 
AVERAGE ( DailyProduction_Fact[DesignedCutsPerHour] )
```
### Losses measures

```dax
Loss Percent = SUM ( LossesOutput_Fact[LossPercent] )

Total Losses % = 
CALCULATE (
    SUM ( LossesOutput_Fact[LossPercent] ),
    NOT ( LossesOutput_Fact[CategoryName] = "Total Reject" )
)

// Quantity lost (approx) = % × Design Output at same Line/Date/Shift/Order
Loss Quantity = 
SUMX (
    LossesOutput_Fact,
    VAR pct = LossesOutput_Fact[LossPercent]
    VAR des =
        LOOKUPVALUE (
            DailyProduction_Fact[DesignOutput],
            DailyProduction_Fact[EventDate], LossesOutput_Fact[EventDate],
            DailyProduction_Fact[LineNumber], LossesOutput_Fact[LineNumber],
            DailyProduction_Fact[ShiftCode], LossesOutput_Fact[ShiftCode],
            DailyProduction_Fact[OrderNumber], LossesOutput_Fact[OrderNumber]
        )
    RETURN pct * des
)

Total Reject Qty = SUM ( LossesOutput_Fact[TotalReject_Value] )

Loss Rate vs Design % = 
DIVIDE ( [Loss Quantity], [Design Output] )
```
### Job Change measures

```dax
Mechanical Work T1 Hrs = SUM ( JobChange_Fact[MechanicalWorkT1_Hrs] )

Forming Time T2 Hrs = SUM ( JobChange_Fact[FormingTimeT2_Hrs] )

Trial Losses Hrs = SUM ( JobChange_Fact[TrialLosses_Hrs] )

HE Downtime Hrs = SUM ( JobChange_Fact[HE_Downtime_Hrs] )

CE Losses Hrs = SUM ( JobChange_Fact[CE_Losses_Hrs] )

Palletizer Losses Hrs = SUM ( JobChange_Fact[PalletizerLosses_Hrs] )

Total Job Change Hours = 
[Mechanical Work T1 Hrs] + [Forming Time T2 Hrs] + [Trial Losses Hrs] +
[HE Downtime Hrs] + [CE Losses Hrs] + [Palletizer Losses Hrs]

Job Change Count = COUNTROWS ( JobChange_Fact )

Avg Job Change Hours = 
DIVIDE ( [Total Job Change Hours], [Job Change Count] )
```

### Quality – Defect measures

```dax
Defect Quantity = SUM ( SamplingDefectLog_Fact[Quantity] )

Total Samples = SUM ( SamplingDefectLog_Fact[TotalSamples] )

Defect Rate % = 
DIVIDE ( [Defect Quantity], [Total Samples] )

Defect Event Count = COUNTROWS ( SamplingDefectLog_Fact )
```

### Rework measures

```dax
Pallets Count = SUM ( Rework_Fact[PalletsCount] )

Reworked Units = 
SUMX (
    Rework_Fact,
    Rework_Fact[PalletsCount] * Rework_Fact[ArticlesPerPallet]
)

Rework Rate % = 
DIVIDE ( [Reworked Units], [Actual Pack] )

Rework Event Count = COUNTROWS ( Rework_Fact )
```

### Combined / KPI measures

```dax
FPY % = 
DIVIDE (
    [Actual Pack],
    [Actual Pack] + [Total Reject Qty] + [Total Hold]
)

Net Good Output = [Actual Pack]   // alias if useful

Production vs Target Gap = [Design Output] - [Actual Pack]
```

> **Note:** In Phase 2 (DWH), `ComputedValue` is pre-calculated by SSIS. In Phase 1 we approximate it with `SUMX` + `LOOKUPVALUE`. When you migrate, replace `Loss Quantity` with `SUM ( 'Losses Output'[ComputedValue] )`.

---

## 8. Suggested First Dashboards (build in this order)

| # | Page | Priority | Key visuals |
|---|------|----------|-------------|
| 1 | **Executive Overview** | Highest | Cards: Actual Pack, Design Output, Pack Efficiency %, Total Losses %, Defect Rate %, FPY %. Trend line for Pack vs Design. |
| 2 | **Production by Line** | High | Matrix Line × Date: Actual Pack, Design Output, Efficiency %, Hold. Slicers: Date, Shift, Crew. |
| 3 | **Losses Analysis** | High | Stacked bar of 11 categories; Total Losses % trend; table of Loss Quantity by category. |
| 4 | **Quality – Defects** | Medium | Defect Rate % by Hour; Pareto of DefectName; Line × Hour heatmap. |
| 5 | **Job Change** | Medium | Hours by type; reason breakdown; count of changes. |
| 6 | **Rework** | Lower | Reworked Units by Status; rate vs Pack. |

---

## 9. Slicers (common)

- Date (range)
- Line (21–25)
- Shift (AM / PM)
- Crew (A / B / C)
- Order / Product / Customer (optional)

Sync slicers across pages.

---

## 10. Refresh Options (Phase 1)

| Option | How | Pros | Cons |
|--------|-----|------|------|
| **A. Manual** | User clicks Refresh in Desktop / Service | Simple | Easy to forget |
| **B. OneDrive + Scheduled refresh** | Publish dataset; files live on OneDrive; Service refreshes on schedule | Automatic | Needs Power BI Pro + OneDrive path stable |
| **C. Folder combine** | Get Data → Folder on `/Daily/`; combine dated files | History grows automatically | Slightly more Power Query work |

**Recommended:** Option B or C.

---

## 11. Migration Path to Phase 2 (DWH)

When Staging + SSIS + DWH are live:

1. Create a **new** Power BI dataset connected to the DWH (or switch source of existing dataset).
2. Keep the **same table names** and **same measure names**.
3. Point visuals at the new dataset (or rebind).
4. Replace Phase-1 `Loss Quantity` (SUMX/LOOKUPVALUE) with `SUM ( ComputedValue )`.
5. Remove Excel connections.

Most report pages should keep working with little or no visual redesign.

---

## 12. Phase 1 Checklist

- [ ] Connect to the 4 Excel templates (Master + Daily files)
- [ ] Build dimension queries (Customer, Product, Order, Line, Shift, …)
- [ ] Build Production, Job Change, Rework, Defect Sampling queries
- [ ] **Unpivot** LossesOutput → Losses Output (tall)
- [ ] Create Date table and relationships
- [ ] Paste core measures (Section 7)
- [ ] Build Executive Overview + Production by Line + Losses Analysis
- [ ] Validate one known day (e.g. 2026-07-28) against Excel numbers
- [ ] Publish to Power BI Service
- [ ] Set refresh schedule (OneDrive)
- [ ] Share with stakeholders and collect feedback

---

## 13. Design Rules (do not break)

1. Use only the 4 standardized templates — no old ad-hoc Excel files.
2. Unpivot Losses in Power Query (never leave them wide in the model).
3. Keep measure names identical to the future DWH model.
4. One Date table shared by all facts.
5. No KPI formulas inside the Excel files themselves.
6. Document any temporary Phase-1 approximations (e.g. Loss Quantity via LOOKUPVALUE).

---

*Phase 1 gets value in front of users quickly. Phase 2 hardens the platform. This design keeps both aligned.*
