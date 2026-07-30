%% Kandil Glass — Production Data Platform
%% STAGING LAYER ERD — Final Aligned Version (optimized for SSIS → DWH)
%% Principles:
%%   - Natural keys only
%%   - One table ≈ one Excel form / source
%%   - Full load metadata on every table
%%   - All codes needed for DWH lookups are present
%%   - Clear 1:1 or simple path to each Fact table

erDiagram

    %% ===================== TRANSACTIONAL STAGING TABLES =====================

    STG_JOBCHANGE {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus "New / Processed / Error"
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        varchar ShiftCode "AM / PM"
        varchar CrewCode "A / B / C"
        varchar FromOrderNumber "nullable"
        varchar ToOrderNumber
        varchar JobChangeTypeName "Small / Medium / Big / Process"
        decimal MechanicalWorkT1_Hrs
        decimal FormingTimeT2_Hrs
        decimal TrialLosses_Hrs
        decimal CE_Losses_Hrs
        decimal HE_Downtime_Hrs
        decimal PalletizerLosses_Hrs
        decimal ExtraT1_Hrs
        decimal ExtraT2_Hrs
        nvarchar Notes
    }

    STG_PRODUCTION {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        varchar ShiftCode
        varchar CrewCode
        varchar OrderNumber
        varchar CaseName "Normal / Trial / Reworking"
        decimal DesignedCutsPerHour
        decimal ActualPack
        decimal TotalReject
        decimal TotalResort
        decimal TotalHold
    }

    STG_LOSSESOUTPUT {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        varchar ShiftCode
        %% Wide format — SSIS will UNPIVOT these into FACT_LOSSESOUTPUT
        decimal ActualPack_Value
        decimal TotalReject_Value
        decimal TotalResort_Value
        decimal TotalHold_Value
        decimal HE_Losses_Value
        decimal CE_Entry_Value
        decimal LehrEntry_Value
        decimal GobCuts_Value
        %% ... add all remaining ~25 loss category columns here (same naming pattern)
        %% Example: decimal ColdEnd_Reject_Value, decimal HotEnd_Reject_Value, etc.
    }

    STG_DEFECTLOG {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus               -- New / Processed / Error
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        int      HourNumber              -- 0 to 23  (or 1-24 depending on your preference)
        varchar ShiftCode
        varchar DefectName
        varchar ZoneName
        decimal Quantity
        CONSTRAINT [PK_STG_DEFECTLOG] PRIMARY KEY ([LoadID])  -- or composite if needed
    }

    STG_REWORK {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        varchar ShiftCode
        varchar OrderNumber
        varchar ReworkStatusName "Hold / Resorted / Move to Cullet"
        int PalletsCount
        decimal ArticlesPerPallet
    }

    STG_LINECONFIG {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar FactoryCode
        int LineNumber
        date EventDate
        int SectionNumber
        int CavitiesActive
        varchar CaseName "Normal / Trial / Reworking"
    }

    %% ===================== MASTER DATA STAGING (new – critical for clean ETL) =====================

    STG_ORDER {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar OrderNumber
        varchar ProductCode
        varchar CustomerCode
        decimal TotalMoltenUnits
    }

    STG_PRODUCT {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar ProductCode
        varchar ProductName
        varchar Category "Jar / Bottle"
        varchar CustomerCode
    }

    STG_CUSTOMER {
        int LoadID PK
        varchar SourceFileName
        datetime LoadTimestamp
        varchar RowStatus
        varchar ErrorMessage
        varchar CustomerCode
        nvarchar CustomerName
        varchar CountryType "Local / Export"
    }

    %% ===================== REFERENCE / VALIDATION LISTS =====================

    REF_LINE {
        varchar FactoryCode PK
        int LineNumber PK
        varchar LineStatus "Active / Inactive"
    }

    REF_JOBCHANGETYPE {
        varchar JobChangeTypeName PK
        decimal TargetT1_Hrs
        decimal TargetT2_Hrs
    }

    REF_LOSSCATEGORY {
        varchar CategoryName PK
        varchar ParentCategoryName
    }

    REF_DEFECT {
        varchar DefectName PK
        varchar Severity
    }

    REF_REJECTIONZONE {
        varchar ZoneName PK
    }

    REF_REWORKSTATUS {
        varchar StatusName PK
    }

    REF_PRODUCTIONCASE {
        varchar CaseName PK
    }

    %% ===================== VALIDATION LINKS (informational) =====================

    REF_LINE ||--o{ STG_JOBCHANGE : "validates"
    REF_LINE ||--o{ STG_PRODUCTION : "validates"
    REF_LINE ||--o{ STG_LOSSESOUTPUT : "validates"
    REF_LINE ||--o{ STG_DEFECTLOG : "validates"
    REF_LINE ||--o{ STG_REWORK : "validates"
    REF_LINE ||--o{ STG_LINECONFIG : "validates"

    REF_JOBCHANGETYPE ||--o{ STG_JOBCHANGE : "validates"
    REF_DEFECT ||--o{ STG_DEFECTLOG : "validates"
    REF_REJECTIONZONE ||--o{ STG_DEFECTLOG : "validates"
    REF_REWORKSTATUS ||--o{ STG_REWORK : "validates"
    REF_PRODUCTIONCASE ||--o{ STG_PRODUCTION : "validates"
    REF_PRODUCTIONCASE ||--o{ STG_LINECONFIG : "validates"