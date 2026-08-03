# Kandil Glass — Role-Based Excel Workbooks Design
**Version:** 1.0  
**Decision:** Split into multiple role-based workbooks (confirmed)

---

## Workbook Map

| # | Workbook File Name | Owner / Role | Sheets Inside | Staging Target |
|---|--------------------|--------------|---------------|----------------|
| 1 | `01_MasterData.xlsx` | Planning / Sales / IT | Customers, Products, Orders, JobChangeTypes, Lines, Lookups | STG_CUSTOMER, STG_PRODUCT, STG_ORDER, STG_JOBCHANGETYPE + all REF_ |
| 2 | `02_Supervisor_Log.xlsx` | Production Supervisors / Shift Leaders | JobChange, DailyProduction | STG_JOBCHANGE, STG_PRODUCTION |
| 3 | `03_Process_Losses.xlsx` | Process Engineers | LossesOutput | STG_LOSSESOUTPUT |
| 4 | `04_Quality_Log.xlsx` | Quality team | SamplingDefectLog, Rework | STG_SAMPLINGDEFECTLOG, STG_REWORK |

---

## Detailed Sheet Contents

### 1. 01_MasterData.xlsx (Planning / IT)

| Sheet | Key Columns |
|-------|-------------|
| Customers | CustomerCode, CustomerName, CountryType |
| Products | ProductCode, ProductName, Category, CustomerCode |
| Orders | OrderNumber, ProductCode, CustomerCode, TotalMoltenUnits |
| JobChangeTypes | JobChangeTypeName, TargetT1_Hrs, TargetT2_Hrs |
| Lines | FactoryCode, LineNumber, LineStatus |
| Lookups (hidden or protected) | Shift, Crew, ProductionCase, ReworkStatus, DefectName, DowntimeReasons (HE/CE/Palletizer), CountryType, ProductCategory |

### 2. 02_Supervisor_Log.xlsx (Production Supervisors)

| Sheet | Key Columns |
|-------|-------------|
| JobChange | FactoryCode, LineNumber, EventDate, ShiftCode, CrewCode, FromOrderNumber, ToOrderNumber, JobChangeTypeName, MechanicalWorkT1_Hrs, FormingTimeT2_Hrs, TrialLosses_Hrs, HE_Downtime_Hrs, HE_DowntimeReason, CE_Losses_Hrs, CE_LossesReason, PalletizerLosses_Hrs, PalletizerReason, Notes |
| DailyProduction | FactoryCode, EventDate, ShiftCode, CrewCode, LineNumber, OrderNumber, CaseName, NoSections, NoCavities, DesignedCyclesPerMin, DesignedCutsPerHour, WorkingHours, DesignOutput, ActualPack, TotalHold |

### 3. 03_Process_Losses.xlsx (Process Engineers)

| Sheet | Key Columns |
|-------|-------------|
| LossesOutput | FactoryCode, LineNumber, EventDate, ShiftCode, OrderNumber, TotalReject_Value, FixedLosses, ISLosses, HotEndConveyerLosses, StuckDownLosses, LehrLosses, Evo16Losses, Evo12Losses, Evo5Losses, SanliLosses, VisualLosses, PalletizerLosses |

> Note: Keep Excel column names **without** `_Pct`. SSIS maps them to Staging `_Pct` columns.

### 4. 04_Quality_Log.xlsx (Quality)

| Sheet | Key Columns |
|-------|-------------|
| SamplingDefectLog | FactoryCode, LineNumber, EventDate, OrderNumber, HourNumber, ShiftCode, TotalSamples, DefectName, Quantity |
| Rework | FactoryCode, LineNumber, EventDate, ShiftCode, OrderNumber, ReworkStatusName, PalletsCount, ArticlesPerPallet |

---

## File Naming & OneDrive Convention

```
/OneDrive/KandilGlass/ProductionData/
    ├── Master/
    │     └── 01_MasterData.xlsx
    ├── Daily/
    │     ├── 02_Supervisor_Log_YYYYMMDD.xlsx
    │     ├── 03_Process_Losses_YYYYMMDD.xlsx
    │     └── 04_Quality_Log_YYYYMMDD.xlsx
    └── Archive/
```

- Daily files are saved with the date in the file name.
- SSIS / scheduled agent watches the `Daily` folder on OneDrive.
- After successful load, files are moved to `Archive`.

---

## Rules for All Workbooks

1. One row = one event. No merged cells, no totals inside detail.
2. Fixed headers (never rename columns).
3. Dropdowns for every coded field (sourced from MasterData Lookups).
4. Real Excel dates.
5. Raw data only — no KPI formulas.
6. Header row frozen + AutoFilter on.
7. Protect sheets (unlock only input cells).

---

## Load Order (SSIS)

1. `01_MasterData.xlsx` → dimensions / REF tables  
2. `02_Supervisor_Log.xlsx` → JobChange + Production  
3. `03_Process_Losses.xlsx` → Losses (unpivot)  
4. `04_Quality_Log.xlsx` → DefectSampling + Rework  
