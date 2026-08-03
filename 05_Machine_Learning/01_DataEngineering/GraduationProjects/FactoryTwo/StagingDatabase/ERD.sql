-- ============================================================================
-- Kandil Glass — Production Data Platform
-- STAGING DATABASE — v2.2
-- ============================================================================
-- Design principles:
--   - Natural keys only (SSIS resolves surrogate keys on load to DWH)
--   - One staging table per Excel sheet / role-based workbook
--   - Full load metadata on every table
--
-- Changes in v2.2 (vs v2.1):
--   1. STG_PRODUCTION.FactoryCode → NOT NULL (Excel DailyProdLog now has the column)
--   2. Loss % formula locked: ComputedValue = LossPercent × DesignOutput (documented)
--   3. Total Losses % = SUM of the 11 percentage columns (measure only)
--   4. JobChangeType official value = 'Process' (not 'Process Change')
-- ============================================================================

-- ============================================================================
-- 1. MASTER DATA STAGING
-- ============================================================================

CREATE TABLE [STG_CUSTOMER] (
    [LoadID]          INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]  VARCHAR(255) NOT NULL,
    [LoadTimestamp]   DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]       VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]    NVARCHAR(500) NULL,
    [CustomerCode]    VARCHAR(50) NOT NULL,
    [CustomerName]    NVARCHAR(150) NOT NULL,
    [CountryType]     VARCHAR(50) NULL, -- 'Local' / 'Export'
    CONSTRAINT [PK_STG_CUSTOMER] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

CREATE TABLE [STG_PRODUCT] (
    [LoadID]          INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]  VARCHAR(255) NOT NULL,
    [LoadTimestamp]   DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]       VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]    NVARCHAR(500) NULL,
    [ProductCode]     VARCHAR(50) NOT NULL,
    [ProductName]     NVARCHAR(150) NOT NULL,
    [Category]        VARCHAR(50) NULL, -- 'Jar' / 'Bottle'
    [CustomerCode]    VARCHAR(50) NOT NULL,
    CONSTRAINT [PK_STG_PRODUCT] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

CREATE TABLE [STG_JOBCHANGETYPE] (
    [LoadID]            INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]    VARCHAR(255) NOT NULL,
    [LoadTimestamp]     DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]         VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]      NVARCHAR(500) NULL,
    [JobChangeTypeName] VARCHAR(50) NOT NULL, -- 'Small' / 'Medium' / 'Big' / 'Process'
    [TargetT1_Hrs]      DECIMAL(8, 2) NULL,
    [TargetT2_Hrs]      DECIMAL(8, 2) NULL,
    CONSTRAINT [PK_STG_JOBCHANGETYPE] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

CREATE TABLE [STG_ORDER] (
    [LoadID]            INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]    VARCHAR(255) NOT NULL,
    [LoadTimestamp]     DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]         VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]      NVARCHAR(500) NULL,
    [OrderNumber]       VARCHAR(50) NOT NULL,
    [ProductCode]       VARCHAR(50) NOT NULL,
    [CustomerCode]      VARCHAR(50) NOT NULL,
    [TotalMoltenUnits]  DECIMAL(18, 2) NULL, -- Packed + Rejected + Hold
    CONSTRAINT [PK_STG_ORDER] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

-- ============================================================================
-- 2. TRANSACTIONAL STAGING TABLES
-- ============================================================================

CREATE TABLE [STG_JOBCHANGE] (
    [LoadID]                INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]        VARCHAR(255) NOT NULL,
    [LoadTimestamp]         DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]             VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]          NVARCHAR(500) NULL,
    [FactoryCode]           VARCHAR(50) NOT NULL,
    [LineNumber]            INT NOT NULL,
    [EventDate]             DATE NOT NULL,
    [ShiftCode]             VARCHAR(10) NOT NULL,
    [CrewCode]              VARCHAR(10) NOT NULL,
    [FromOrderNumber]       VARCHAR(50) NULL,
    [ToOrderNumber]         VARCHAR(50) NOT NULL,
    [JobChangeTypeName]     VARCHAR(50) NOT NULL,
    [MechanicalWorkT1_Hrs]  DECIMAL(8, 2) NULL,
    [FormingTimeT2_Hrs]     DECIMAL(8, 2) NULL,
    [TrialLosses_Hrs]       DECIMAL(8, 2) NULL,
    [HE_Downtime_Hrs]       DECIMAL(8, 2) NULL,
    [HE_DowntimeReason]     NVARCHAR(150) NULL,
    [CE_Losses_Hrs]         DECIMAL(8, 2) NULL,
    [CE_LossesReason]       NVARCHAR(150) NULL,
    [PalletizerLosses_Hrs]  DECIMAL(8, 2) NULL,
    [PalletizerReason]      NVARCHAR(150) NULL,
    [Notes]                 NVARCHAR(500) NULL,
    CONSTRAINT [PK_STG_JOBCHANGE] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

-- FactoryCode is now required (Excel DailyProdLog has the column).
CREATE TABLE [STG_PRODUCTION] (
    [LoadID]                INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]        VARCHAR(255) NOT NULL,
    [LoadTimestamp]         DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]             VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]          NVARCHAR(500) NULL,
    [FactoryCode]           VARCHAR(50) NOT NULL,
    [EventDate]             DATE NOT NULL,
    [ShiftCode]             VARCHAR(10) NOT NULL,
    [CrewCode]              VARCHAR(10) NOT NULL,
    [LineNumber]            INT NOT NULL,
    [OrderNumber]           VARCHAR(50) NOT NULL,
    [CaseName]              VARCHAR(50) NOT NULL, -- 'Normal' / 'Trial' / 'Reworking'
    [NoSections]            INT NULL,
    [NoCavities]            INT NULL,
    [DesignedCyclesPerMin]  DECIMAL(10, 2) NULL,
    [DesignedCutsPerHour]   DECIMAL(10, 2) NULL,
    [WorkingHours]          DECIMAL(6, 2) NULL,
    [DesignOutput]          DECIMAL(18, 2) NULL, -- DesignedCutsPerHour × WorkingHours
    [ActualPack]            DECIMAL(18, 2) NULL,
    [TotalHold]             DECIMAL(18, 2) NULL,
    CONSTRAINT [PK_STG_PRODUCTION] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

-- Excel → Staging column map (SSIS unpivot reference):
--   FixedLosses           → FixedLosses_Pct
--   ISLosses              → ISLosses_Pct
--   HotEndConveyerLosses  → HotEndConveyerLosses_Pct
--   StuckDownLosses       → StuckDownLosses_Pct
--   LehrLosses            → LehrLosses_Pct
--   Evo16Losses           → Evo16Losses_Pct
--   Evo12Losses           → Evo12Losses_Pct
--   Evo5Losses            → Evo5Losses_Pct
--   SanliLosses           → SanliLosses_Pct
--   VisualLosses          → VisualLosses_Pct
--   PalletizerLosses      → PalletizerLosses_Pct
--   TotalReject_Value     → TotalReject_Value
-- Locked formula: ComputedValue = LossPercent × DesignOutput
-- Total Losses % = SUM of the 11 _Pct columns (measure only)
CREATE TABLE [STG_LOSSESOUTPUT] (
    [LoadID]                    INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]            VARCHAR(255) NOT NULL,
    [LoadTimestamp]             DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]                 VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]              NVARCHAR(500) NULL,
    [FactoryCode]               VARCHAR(50) NOT NULL,
    [LineNumber]                INT NOT NULL,
    [EventDate]                 DATE NOT NULL,
    [ShiftCode]                 VARCHAR(10) NOT NULL,
    [OrderNumber]               VARCHAR(50) NOT NULL,
    [TotalReject_Value]         DECIMAL(18, 2) NULL,
    [FixedLosses_Pct]           DECIMAL(9, 6) NULL,
    [ISLosses_Pct]              DECIMAL(9, 6) NULL,
    [HotEndConveyerLosses_Pct]  DECIMAL(9, 6) NULL,
    [StuckDownLosses_Pct]       DECIMAL(9, 6) NULL,
    [LehrLosses_Pct]            DECIMAL(9, 6) NULL,
    [Evo16Losses_Pct]           DECIMAL(9, 6) NULL,
    [Evo12Losses_Pct]           DECIMAL(9, 6) NULL,
    [Evo5Losses_Pct]            DECIMAL(9, 6) NULL,
    [SanliLosses_Pct]           DECIMAL(9, 6) NULL,
    [VisualLosses_Pct]          DECIMAL(9, 6) NULL,
    [PalletizerLosses_Pct]      DECIMAL(9, 6) NULL,
    CONSTRAINT [PK_STG_LOSSESOUTPUT] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

CREATE TABLE [STG_SAMPLINGDEFECTLOG] (
    [LoadID]          INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]  VARCHAR(255) NOT NULL,
    [LoadTimestamp]   DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]       VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]    NVARCHAR(500) NULL,
    [FactoryCode]     VARCHAR(50) NOT NULL,
    [LineNumber]      INT NOT NULL,
    [EventDate]       DATE NOT NULL,
    [OrderNumber]     VARCHAR(50) NOT NULL,
    [HourNumber]      INT NOT NULL, -- 0-23
    [ShiftCode]       VARCHAR(10) NOT NULL,
    [TotalSamples]    INT NOT NULL,
    [DefectName]      VARCHAR(100) NOT NULL,
    [Quantity]        DECIMAL(18, 2) NOT NULL,
    CONSTRAINT [PK_STG_SAMPLINGDEFECTLOG] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

CREATE TABLE [STG_REWORK] (
    [LoadID]              INT IDENTITY(1,1) NOT NULL,
    [SourceFileName]      VARCHAR(255) NOT NULL,
    [LoadTimestamp]       DATETIME2 NOT NULL DEFAULT GETDATE(),
    [RowStatus]           VARCHAR(20) NOT NULL DEFAULT 'New',
    [ErrorMessage]        NVARCHAR(500) NULL,
    [FactoryCode]         VARCHAR(50) NOT NULL,
    [LineNumber]          INT NOT NULL,
    [EventDate]           DATE NOT NULL,
    [ShiftCode]           VARCHAR(10) NOT NULL,
    [OrderNumber]         VARCHAR(50) NOT NULL,
    [ReworkStatusName]    VARCHAR(50) NOT NULL, -- 'Hold' / 'Resorted' / 'Move to Cullet'
    [PalletsCount]        INT NULL,
    [ArticlesPerPallet]   DECIMAL(10, 2) NULL,
    CONSTRAINT [PK_STG_REWORK] PRIMARY KEY CLUSTERED ([LoadID] ASC)
);

-- ============================================================================
-- 3. REFERENCE / VALIDATION LISTS
-- ============================================================================

CREATE TABLE [REF_FACTORY] (
    [FactoryCode]   VARCHAR(50) NOT NULL,
    CONSTRAINT [PK_REF_FACTORY] PRIMARY KEY CLUSTERED ([FactoryCode] ASC)
);

CREATE TABLE [REF_LINE] (
    [FactoryCode]   VARCHAR(50) NOT NULL,
    [LineNumber]    INT NOT NULL,
    [LineStatus]    VARCHAR(20) NULL, -- 'Active' / 'Inactive'
    CONSTRAINT [PK_REF_LINE] PRIMARY KEY CLUSTERED ([FactoryCode] ASC, [LineNumber] ASC)
);

CREATE TABLE [REF_JOBCHANGETYPE] (
    [JobChangeTypeName] VARCHAR(50) NOT NULL, -- official values: Small, Medium, Big, Process
    CONSTRAINT [PK_REF_JOBCHANGETYPE] PRIMARY KEY CLUSTERED ([JobChangeTypeName] ASC)
);

CREATE TABLE [REF_LOSSCATEGORY] (
    [CategoryName]        VARCHAR(100) NOT NULL,
    [ParentCategoryName]  VARCHAR(100) NULL,
    CONSTRAINT [PK_REF_LOSSCATEGORY] PRIMARY KEY CLUSTERED ([CategoryName] ASC)
);

CREATE TABLE [REF_DEFECT] (
    [DefectName]  VARCHAR(100) NOT NULL,
    [Severity]    VARCHAR(50) NULL,
    CONSTRAINT [PK_REF_DEFECT] PRIMARY KEY CLUSTERED ([DefectName] ASC)
);

CREATE TABLE [REF_REWORKSTATUS] (
    [StatusName]  VARCHAR(50) NOT NULL,
    CONSTRAINT [PK_REF_REWORKSTATUS] PRIMARY KEY CLUSTERED ([StatusName] ASC)
);

CREATE TABLE [REF_PRODUCTIONCASE] (
    [CaseName]  VARCHAR(50) NOT NULL,
    CONSTRAINT [PK_REF_PRODUCTIONCASE] PRIMARY KEY CLUSTERED ([CaseName] ASC)
);

CREATE TABLE [REF_DOWNTIMEREASON] (
    [ReasonName]  VARCHAR(150) NOT NULL,
    [AppliesTo]   VARCHAR(20) NOT NULL, -- 'HE' / 'CE' / 'Palletizer'
    CONSTRAINT [PK_REF_DOWNTIMEREASON] PRIMARY KEY CLUSTERED ([ReasonName] ASC, [AppliesTo] ASC)
);
