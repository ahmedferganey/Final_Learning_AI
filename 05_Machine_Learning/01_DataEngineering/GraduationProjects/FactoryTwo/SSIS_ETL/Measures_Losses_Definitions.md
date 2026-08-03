# Kandil Glass — Losses & Related Measures
**Version:** 1.0  
**Status:** Locked (based on confirmed business rules)

---

## Confirmed Business Rules

| Rule | Definition |
|------|------------|
| Loss % base | Each of the 11 percentages is a **% of Design Output** |
| ComputedValue | `LossPercent × DesignOutput` |
| Total Losses % | `SUM` of the 11 percentage columns |
| TotalReject | Absolute quantity (not a %) — stored as its own category row or used directly |

---

## 1. SSIS Transformation Logic (Losses)

### Unpivot map (Excel → Staging → DWH)

| Excel Column (LossesOutput sheet) | Staging Column | DIM_LOSSCATEGORY.CategoryName |
|-----------------------------------|----------------|-------------------------------|
| TotalReject_Value | TotalReject_Value | Total Reject |
| FixedLosses | FixedLosses_Pct | Fixed Losses |
| ISLosses | ISLosses_Pct | IS Losses |
| HotEndConveyerLosses | HotEndConveyerLosses_Pct | Hot End Conveyer Losses |
| StuckDownLosses | StuckDownLosses_Pct | Stuck Down Losses |
| LehrLosses | LehrLosses_Pct | Lehr Losses |
| Evo16Losses | Evo16Losses_Pct | Evo16 Losses |
| Evo12Losses | Evo12Losses_Pct | Evo12 Losses |
| Evo5Losses | Evo5Losses_Pct | Evo5 Losses |
| SanliLosses | SanliLosses_Pct | Sanli Losses |
| VisualLosses | VisualLosses_Pct | Visual Losses |
| PalletizerLosses | PalletizerLosses_Pct | Palletizer Losses |

### ComputedValue population (SSIS)

After unpivot, for every loss-category row (except Total Reject):

```text
ComputedValue = LossPercent × DesignOutput
```

Where `DesignOutput` is looked up from `FACT_PRODUCTION` (or `STG_PRODUCTION`) on the same:

`FactoryCode + LineNumber + EventDate + ShiftCode + OrderNumber`

For the **Total Reject** row:
- `LossPercent` = NULL
- `ComputedValue` = `TotalReject_Value` (absolute quantity)

---

## 2. DAX Measures (Power BI / SSAS Tabular)

```dax
-- Base
Actual Pack =
SUM ( FACT_PRODUCTION[ActualPack] )

Design Output =
SUM ( FACT_PRODUCTION[DesignOutput] )

Total Hold =
SUM ( FACT_PRODUCTION[TotalHold] )

Working Hours =
SUM ( FACT_PRODUCTION[WorkingHours] )

-- Losses
Loss Percent :=
SUM ( FACT_LOSSESOUTPUT[LossPercent] )

Total Losses % :=
CALCULATE (
    SUM ( FACT_LOSSESOUTPUT[LossPercent] ),
    NOT ( DIM_LOSSCATEGORY[CategoryName] = "Total Reject" )
)

Loss Quantity (Computed) :=
SUM ( FACT_LOSSESOUTPUT[ComputedValue] )

Total Reject Qty :=
CALCULATE (
    SUM ( FACT_LOSSESOUTPUT[ComputedValue] ),
    DIM_LOSSCATEGORY[CategoryName] = "Total Reject"
)

-- Efficiency / Yield style
Pack Efficiency % :=
DIVIDE ( [Actual Pack], [Design Output] )

Loss Rate vs Design % :=
DIVIDE ( [Loss Quantity (Computed)], [Design Output] )

-- Defect Sampling
Defect Quantity :=
SUM ( FACT_DEFECTSAMPLING[Quantity] )

Total Samples :=
SUM ( FACT_DEFECTSAMPLING[TotalSamples] )

Defect Rate % :=
DIVIDE ( [Defect Quantity], [Total Samples] )

-- Rework
Reworked Units :=
SUM ( FACT_REWORK[ReworkedUnits] )

-- Job Change
Total Job Change Hours :=
SUM ( FACT_JOBCHANGE[TotalJobChangeLosses_Hrs] )
```

---

## 3. Example (from your sample data)

Given:
- DesignOutput = 432,000
- FixedLosses = 2.00% → ComputedValue = 0.02 × 432,000 = **8,640**
- ISLosses = 1.00% → 4,320
- … (all 11 categories)
- Sum of the 11 % = **6.44%**
- Total Losses Quantity ≈ 0.0644 × 432,000 ≈ **27,821** pieces

---

## 4. Implementation Notes

- Store only `LossPercent` and `ComputedValue` in the fact table.
- Never store Total Losses % as a column — always calculate it as a measure.
- DesignOutput must be available at the same grain (Line + Date + Shift + Order) for the multiplication to be correct.
- If a Losses row has no matching Production row, `ComputedValue` should be left NULL and logged as a data-quality issue.
