# Kandil Glass — Business Logic Document
## Production Data Platform (Excel → Staging → SSIS → DWH → Power BI)

**Version:** 2.0
**Scope:** Multi-factory capable | Detailed design for **Factory 2**
**Sources:** Job Change Log + Losses & Output Log
**Status:** ERD finalized (v2) — ready for physical DDL and Excel template design
**Companion file:** `Kandil_Glass_ERD_v2_FINAL.mermaid` (visual ERD matching this document)

---

## 0. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | Initial draft | Core entities, grains, dimensions defined. 6 open modeling gaps identified during ERD design. |
| 2.0 | Current | All 6 modeling gaps resolved (see **Section 12 — Design Decision Log**). `Dim_ProductionCase`, `Dim_ReworkStatus` added. `Fact_Rework` and `Fact_LineConfig_Daily` added. `Fact_JobChange` and `Fact_LossesOutput` grains updated. |

---

## 1. Purpose of this Document

This document captures **all business rules, entities, relationships, grains, and measures** so that:

- Excel templates are designed correctly
- Staging tables match the Excel structure
- SSIS transformations follow the same logic
- Data Warehouse (star schema) stores the correct grain and keys
- Power BI measures are calculated consistently

Everything in this document must be reflected across **all layers**.

---

## 2. High-Level Business Context

### 2.1 Multi-Factory Reality
- The company has **multiple factories**.
- Each factory has its own products, line numbers, and slight process differences.
- The **Data Warehouse must store data for all factories**.
- Dimension tables will have a `FactoryKey` / `FactoryCode` so reports can be filtered by factory or combined.

**Current focus:** Factory 2 (detailed below). Other factories will follow the same pattern.

### 2.2 Factory 2 Physical Layout
- **1 Furnace**
- Furnace feeds **5 Distributors**
- Each Distributor feeds **1 Press / IS Machine** → **5 production lines** (currently identified as Lines 21–25)
- Each machine has a **custom number of Sections**
- Each Section can run **1, 2, or 3 cavities** depending on:
  - Product design
  - Whether the line is in **Normal Production** or **Trial**
  - Temporary decisions (e.g., a cavity is taken out because of high reject rate)

> **v2.0 note:** Cavity/section configuration is now formally modeled as a daily snapshot fact table, `Fact_LineConfig_Daily` — see Section 7.5 and Decision #4.

### 2.3 Workforce & Shifts (Factory 2)
- Two main shifts: **AM** and **PM**
- Workers are divided into **3 groups: A, B, C**
- Group assignment rotates according to workforce planning (Group A can work AM one week, PM another week, etc.)
- Therefore the system must capture both:
  - **Shift** (AM / PM)
  - **Crew / Group** (A / B / C)

---

## 3. Core Business Entities

| Entity              | Description                                                                 | Key Attributes                                      |
|---------------------|-----------------------------------------------------------------------------|-----------------------------------------------------|
| Factory             | Physical plant                                                              | FactoryCode, FactoryName                            |
| Line / Machine      | One of the 5 press machines                                                 | LineNumber (21-25), MachineName, Sections, DesignCyclesPerMin |
| Product             | Finished glass container                                                    | ProductCode, ProductName, Category (Jar / Bottle), Customer |
| Customer            | Buyer of the product                                                        | CustomerCode, CustomerName, Country (Local / Export) |
| Order               | Production order linked to a product                                        | OrderNumber, ProductCode, TotalMoltenUnits          |
| Job Change Type     | Classification of changeover                                                | Small / Medium / Big / Process Change + Target T1/T2 hours |
| Loss Category       | Standardized list of time & quality losses (aggregate KPI hierarchy)        | Category → Sub-category hierarchy                   |
| Defect              | Quality defect                                                              | DefectName, Severity (Critical / Major / Minor)     |
| Rejection Zone      | Physical location where a **specific defect** was detected                  | Hot End / Lehr / Cold End / Section / etc.          |
| **Production Case** *(new v2.0)* | Classifies the operating mode of a line on a given day/shift          | CaseName: Normal Production / Trial / Reworking     |
| **Rework Status** *(new v2.0)*   | Outcome status of reworked goods                                       | StatusName: Hold / Resorted / Move to Cullet        |

> **v2.0 scope clarification (Decision #5):** `Loss Category` is the master list of the ~30 named aggregate metrics (e.g., "HE Losses," "Section 03 Stops") used for time/quantity KPI reporting. `Rejection Zone` is a **separate, narrower-purpose** dimension used only alongside a specific `Defect` record, to say where *that particular occurrence* was physically caught — independent of which aggregate Loss Category metric it may also roll into. These are not the same hierarchy and are not merged.

---

## 4. Three Production Cases (Critical Business Rule)

On any line, on any day/shift, the work falls into **exactly one** of these three cases:

| Case              | Description                                                                 | What we record |
|-------------------|-----------------------------------------------------------------------------|----------------|
| **1. Normal Production** | Stable production of a product                                              | Designed speed vs Actual output, rejections, defects |
| **2. Trial**            | Testing a new product, machine modification, or product redesign            | Trial time losses + units lost during trial |
| **3. Reworking**        | Reprocessing previously produced goods                                      | Number of pallets × articles per pallet → total units reworked. Status after rework: **Hold / Resorted / Move to Cullet** |

**Important:** Reworked quantity is always a **subset** of the total molten units produced for that Order.

> **v2.0 update (Decision #2 & #3):** This case classification is now formally modeled as `Dim_ProductionCase`, attached to `Fact_Production` and `Fact_LineConfig_Daily`. Case 3 (Reworking) is captured in its own fact table, `Fact_Rework` (Section 7.4), rather than folded into `Fact_Production`, because its grain (Order + Rework Status, with pallets/articles math) is structurally different from normal production rows.

---

## 5. Designed vs Actual Production (Normal Production)

For every machine we store **design parameters**:

- Design Cycles (cuts) per minute
- Design number of cavities
- Number of sections

**Theoretical (Designed) output formula:**

Designed Cuts per Hour = Cycles_per_min × Cavities × Sections × 60

**Actual output** is measured and split into:
- Accepted (Packed)
- Rejected
- To be Reworked

We always compare **Actual Pack** vs **Designed Output** to calculate efficiency.

---

## 6. Losses – Two Perspectives

### 6.1 Time Losses (mainly from Job Change / Changeover domain)

| # | Loss Type                    | Description                                      | Related to          |
|---|------------------------------|--------------------------------------------------|---------------------|
| 1 | Trial Losses                 | Time spent on trial runs                         | Trial case          |
| 2 | T1 Losses (Mechanical/Setup) | Mechanical work and setup time                   | Job Change          |
| 3 | T2 Losses (Forming/Process)  | Forming process adjustment time                  | Job Change          |
| 4 | CE Losses (Cold End)         | Time lost at inspection / packing area           | Job Change          |
| 5 | Palletizer Losses            | Time lost at palletizing station                 | Job Change          |
| 6 | HE Breakdown Losses          | Hot End machine breakdown time                   | Job Change          |
| 7 | Extra T1 Losses              | Unplanned setup time beyond T1 target            | Job Change          |
| 8 | Extra T2 Losses              | Unplanned forming time beyond T2 target          | Job Change          |
| 9 | **Total Job Change Losses**  | SUM of all the above                             | Calculated          |

Job Change Type (Small / Medium / Big / Process) has **target T1 and T2 hours**.
We compare actual T1/T2 against the target.

> **v2.0 update (Decision #6):** A changeover is inherently a switch *from* one product/order *to* another. `Fact_JobChange` now carries both `FromOrderKey` (nullable — no prior order on a line's first-ever changeover or after a shutdown) and `ToOrderKey` (the incoming order, part of the fact's grain). This enables changeover-time matrix reporting (e.g., "Product A → B changeovers take longer than A → C").

### 6.2 Defect / Quality Losses (mainly from Losses & Output domain)

Defects are classified by **Severity**:
- Critical
- Major
- Minor

Every defect name belongs to **only one** severity.

**Rejection Zones** (where the defect is detected):

| Zone              | Examples of metrics                                      |
|-------------------|----------------------------------------------------------|
| Hot End           | HE Conv., HE Losses, HE Reject                           |
| Lehr Zone         | Lehr Entry, Lehr Losses, Lehr Pack                       |
| Cold End          | CE Entry, CE Losses, MNR Losses                          |
| IS Machine        | Section 01–10 defects, Total Section Stops, Stuck & Down |
| Quality Categories| Total Reject, Total Resort, Total Hold, Visual           |
| Secondary Losses  | Gob Cuts, Pallet In, Total EVO12/16/5, Total SanLi        |

> **v2.0 update (Decision #1):** `Defect` and `Rejection Zone` are now formally linked into the star schema as **nullable foreign keys directly on `Fact_LossesOutput`** (`DefectKey`, `RejectionZoneKey`) rather than left unattached. Rows representing aggregate metrics (e.g., "HE Losses = 38,233") leave these two keys null. Rows representing an actual defect occurrence populate both keys. This keeps one fact table serving both levels of detail instead of fragmenting the domain into multiple fact tables.

---

## 7. Grain Definitions (Very Important for DWH)

### 7.1 Fact_JobChange
**Grain:** One row = one changeover / job-change event
**Natural Key:** Date + Factory + Line + Shift + ToOrder + JobChangeType

**Keys:**
- DateKey, FactoryKey, LineKey, ShiftKey, CrewKey
- **FromOrderKey** *(nullable — v2.0 addition, Decision #6)*
- **ToOrderKey** *(v2.0 rename of "Order/Product" — part of grain, Decision #6)*
- JobChangeTypeKey

**Measures (hours):**
- MechanicalWorkT1_Hrs
- FormingTimeT2_Hrs
- TrialLosses_Hrs
- CE_Losses_Hrs
- HE_Downtime_Hrs
- PalletizerLosses_Hrs
- ExtraT1_Hrs
- ExtraT2_Hrs
- TotalJobChangeLosses_Hrs (calculated)

### 7.2 Fact_LossesOutput
**Grain:** One row = Factory + Line + Date + Shift + Loss/Output Category [+ Defect + Rejection Zone, when applicable]
(After unpivoting the wide Excel structure)

**Keys:**
- DateKey, FactoryKey, LineKey, ShiftKey, LossCategoryKey
- **DefectKey** *(nullable — v2.0 addition, Decision #1)*
- **RejectionZoneKey** *(nullable — v2.0 addition, Decision #1; populated only alongside DefectKey)*

**Measures:**
- Value (pieces or hours depending on the category)
- Percent (recommended to calculate in Power BI, not store)

### 7.3 Fact_Production
**Grain:** One row = Factory + Line + Date + Shift + Order/Product [+ Production Case]

**Keys:**
- DateKey, FactoryKey, LineKey, ShiftKey, CrewKey, OrderKey
- **CaseKey** *(nullable-no — required — v2.0 addition, Decision #3: Normal / Trial / Reworking)*

**Measures:**
- DesignedCutsPerHour
- ActualPack
- TotalReject
- TotalResort
- TotalHold
- Efficiency % (calculated)

### 7.4 Fact_Rework *(new in v2.0 — Decision #2)*
**Grain:** One row = Factory + Line + Date + Shift + Order + Rework Status

**Keys:**
- DateKey, FactoryKey, LineKey, ShiftKey, OrderKey, ReworkStatusKey

**Measures:**
- PalletsCount
- ArticlesPerPallet
- ReworkedUnits (calculated = PalletsCount × ArticlesPerPallet)
- **Business rule:** ReworkedUnits must always be ≤ the parent Order's TotalMoltenUnits (see Section 9, Rule 5)

### 7.5 Fact_LineConfig_Daily *(new in v2.0 — Decision #4)*
**Grain:** One row = Line + Date + Section Number
**Type:** Daily snapshot fact (not a Type-2 dimension attribute — see Decision #4 rationale)

**Keys:**
- DateKey, LineKey, CaseKey (Normal / Trial)

**Measures:**
- SectionNumber
- CavitiesActive

---

## 8. Conformed Dimensions (Shared across all facts)

| Dimension              | Purpose                                      | SCD Type Recommendation |
|------------------------|-----------------------------------------------|-------------------------|
| Dim_Factory            | Multi-factory support                        | Type 1                  |
| Dim_Date               | Calendar                                     | Type 1                  |
| Dim_Line               | Line 21-25 + attributes (sections, design cycles, furnace) | Type 2 (history) |
| Dim_Shift              | AM / PM                                      | Type 1                  |
| Dim_Crew               | Group A / B / C                              | Type 1                  |
| Dim_Product            | ProductCode → Category (Jar/Bottle), Customer| Type 2                  |
| Dim_Customer           | Customer master                              | Type 2                  |
| Dim_Order              | OrderNumber + Product + TotalMoltenUnits     | Type 2                  |
| Dim_JobChangeType      | Small/Medium/Big/Process + Target T1/T2      | Type 1                  |
| Dim_LossCategory       | Hierarchical (Category → Sub-category); master list of aggregate KPI metrics | Type 1 or Type 2 |
| Dim_Defect             | DefectName + Severity (Critical/Major/Minor) | Type 1                  |
| Dim_RejectionZone      | Physical zone tied to specific defect occurrences only (see Section 3 scope note) | Type 1 |
| **Dim_ProductionCase** *(new v2.0)* | Normal / Trial / Reworking — used on Fact_Production and Fact_LineConfig_Daily | Type 1 |
| **Dim_ReworkStatus** *(new v2.0)*  | Hold / Resorted / Move to Cullet — used on Fact_Rework | Type 1 |

> **Why `Fact_LineConfig_Daily` instead of Type-2 `Dim_Line` for cavity/section changes (Decision #4):** cavity configuration can change daily or even mid-shift. Versioning the entire `Dim_Line` record on every such change would produce excessive near-duplicate dimension rows. A daily snapshot fact is the standard modeling pattern for fast-changing configuration data like this.

---

## 9. Key Business Rules for ETL / SSIS

1. **Never store free-text reasons** → map everything to standardized dimension codes via dropdowns in Excel.
2. **Unpivot** the wide Losses file into long format (Category | Value).
3. **Split composite keys** (e.g., Date+Line) into separate fields.
4. **Calculate Total Job Change Losses** = sum of all individual time losses.
5. **Rework quantity** must always be ≤ Total Molten Units of the Order (enforced in `Fact_Rework`, validated against `Dim_Order.TotalMoltenUnits`).
6. **Percent columns** should not be stored in the fact table — calculate in Power BI or a DWH view.
7. **Cavity / Section configuration** is captured daily in `Fact_LineConfig_Daily` (see Decision #4) — **not** versioned into `Dim_Line`.
8. All dimensions must be loaded **before** facts (lookup surrogate keys).
9. *(new v2.0)* **`DefectKey` and `RejectionZoneKey` on `Fact_LossesOutput` are populated together or not at all** — a row either represents an aggregate category metric (both null) or a specific defect occurrence (both populated). ETL must reject/flag rows where only one of the two is populated.
10. *(new v2.0)* **`Fact_JobChange.FromOrderKey` may be null** only for a line's first recorded changeover or its first changeover after an extended shutdown; SSIS should flag (not silently null) any other missing `FromOrderKey` for review.

---

## 10. Open Decisions Still Needed

1. Final shift standard (AM/PM + Crew A/B/C confirmed?). — *(Confirmed in v1.0 discussion; formally modeled as `Dim_Shift` + `Dim_Crew`.)*
2. Exact list of standardized Loss Categories and Defect Names (to be locked as master data).
3. Product master source (does a clean ProductCode list already exist?).
4. How files will be delivered daily (shared folder / SharePoint / Teams).
5. ~~Whether we need a separate Fact_Production or can derive everything from the two existing facts.~~ — **Resolved in v2.0:** yes, `Fact_Production` is a separate fact table, and `Fact_Rework` is also separate (see Section 12, Decisions #2 and #3 context).

---

## 11. Alignment Checklist (All Layers Must Follow This Document)

| Layer              | Must implement                                      |
|--------------------|-----------------------------------------------------|
| Excel Templates    | Dropdowns from master lists, one row = one event, no totals |
| Staging DB         | Exact copy of cleaned Excel structure + Load metadata |
| SSIS               | Unpivot, cleanse, key lookup, apply rules above, plus v2.0 rules 9–10 |
| Data Warehouse     | Star schema with the grains and dimensions defined, including `Fact_Rework` and `Fact_LineConfig_Daily` |
| Power BI           | Measures calculated from the facts, never hard-coded|

---

## 12. Design Decision Log (ERD v2.0)

These six modeling gaps were identified during ERD design (v1 draft) and formally resolved here. This log is the audit trail for *why* the schema looks the way it does — future changes to these decisions should be recorded as new dated entries below, not by silently editing the tables above.

| # | Gap Identified | Decision | Rationale |
|---|---|---|---|
| 1 | `Dim_Defect` and `Dim_RejectionZone` were defined but not linked to any fact table's grain | Added `DefectKey` and `RejectionZoneKey` as **nullable FKs directly on `Fact_LossesOutput`** | Keeps one fact table for the whole Losses & Output domain instead of fragmenting it into a separate defect-detail fact. Aggregate metric rows leave the keys null; defect-occurrence rows populate both. |
| 2 | Case 3 "Reworking" (pallets/articles/status) had no defined fact table | Created a **dedicated `Fact_Rework`** table | Rework has a different grain (Order + Rework Status) than Production or Losses/Output; forcing it into an existing table would leave those columns mostly null everywhere else. |
| 3 | "Production Case" (Normal/Trial/Reworking) wasn't listed as a dimension anywhere | Added `Dim_ProductionCase`; attached to `Fact_Production` and `Fact_LineConfig_Daily` only (not `Fact_JobChange`, which already has an explicit `TrialLosses_Hrs` measure) | Avoids redundant tagging where the case is already implied by an existing measure. |
| 4 | Cavity/Section configuration changes daily; no table was defined for it | Modeled as a **separate daily snapshot fact, `Fact_LineConfig_Daily`**, rather than a Type-2 attribute on `Dim_Line` | Daily/intra-shift changes would explode a Type-2 `Dim_Line` into excessive near-duplicate versions. A snapshot fact is the standard pattern for fast-changing configuration data. |
| 5 | `Dim_LossCategory` and `Dim_RejectionZone` appeared to describe the same hierarchy (both organized by Hot End / Cold End / Lehr / etc.) | **Kept both dimensions, scoped differently**: `Dim_LossCategory` = master list of aggregate KPI metrics; `Dim_RejectionZone` = physical location tied only to specific defect occurrences | The aggregate metrics already encode zone in their names (HE Losses, CE Losses), but a specific defect can be caught in varying zones across occurrences — an orthogonal fact that a merged hierarchy would not represent correctly. |
| 6 | `Fact_JobChange`'s grain only referenced one Order/Product, but a changeover is inherently a switch between two products | Added both **`FromOrderKey` (nullable)** and **`ToOrderKey`** (grain-defining) | Enables changeover-time matrix analysis (e.g., "A→B changeovers take longer than A→C") that a single-order grain could not support. |

---

**End of Business Logic Document (v2.0)**

This document is now the **single source of truth**, together with `Kandil_Glass_ERD_v2_FINAL.mermaid`.
Any change in business rules or schema design must be recorded here first (with a new dated entry in Section 12 if it revises a prior decision), then reflected in Excel, SSIS, and DWH.