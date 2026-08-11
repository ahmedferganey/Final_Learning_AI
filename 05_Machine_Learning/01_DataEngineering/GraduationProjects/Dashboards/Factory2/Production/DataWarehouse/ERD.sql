-- ============================================================================
-- Kandil Glass — Production Data Platform
-- DATA WAREHOUSE — v3.2
-- ============================================================================
-- Changes in v3.2 (vs v3.1):
--   1. Loss formula locked:
--        ComputedValue = LossPercent × DesignOutput
--        Total Losses % = SUM(LossPercent) across the 11 categories (measure only)
--   2. Comments updated to reflect confirmed business rules
--   3. Version aligned with Staging v2.2
-- ============================================================================

-- ===================== 1. CONFORMED DIMENSIONS =====================

CREATE TABLE [DIM_FACTORY] (
    [FactoryKey]     INT IDENTITY(1,1) NOT NULL,
    [FactoryCode]    VARCHAR(50) NOT NULL,
    [FactoryName]    NVARCHAR(150) NOT NULL,
    CONSTRAINT [PK_DIM_FACTORY] PRIMARY KEY CLUSTERED ([FactoryKey])
);

CREATE TABLE [DIM_DATE] (
    [DateKey]        INT NOT NULL,               -- YYYYMMDD
    [FullDate]       DATE NOT NULL,
    [Year]           INT NOT NULL,
    [Month]          INT NOT NULL,
    [Day]            INT NOT NULL,
    [WeekdayName]    VARCHAR(20) NOT NULL,
    [WeekOfYear]     INT NOT NULL,
    CONSTRAINT [PK_DIM_DATE] PRIMARY KEY CLUSTERED ([DateKey])
);

CREATE TABLE [DIM_HOUR] (
    [HourKey]       INT NOT NULL,               -- 0 to 23
    [HourNumber]    INT NOT NULL,
    [HourLabel]     VARCHAR(10) NOT NULL,       -- '00:00', '01:00', ...
    [HourLabel12]   VARCHAR(10) NOT NULL,       -- '12 AM', '1 AM', ...
    [ShiftGroup]    VARCHAR(10) NULL,           -- 'AM' / 'PM'
    CONSTRAINT [PK_DIM_HOUR] PRIMARY KEY CLUSTERED ([HourKey])
);

CREATE TABLE [DIM_LINE] (
    [LineKey]            INT IDENTITY(1,1) NOT NULL,
    [FactoryKey]         INT NOT NULL,
    [LineNumber]         INT NOT NULL,
    [MachineName]        NVARCHAR(100) NULL,
    [SectionsCount]      INT NULL,
    [DesignCyclesPerMin] DECIMAL(10,2) NULL,
    [FurnaceID]          VARCHAR(50) NULL,
    [EffectiveFrom]      DATE NOT NULL,
    [EffectiveTo]        DATE NULL,
    [IsCurrent]          CHAR(1) NOT NULL DEFAULT 'Y',
    CONSTRAINT [PK_DIM_LINE] PRIMARY KEY CLUSTERED ([LineKey]),
    CONSTRAINT [FK_DIM_LINE_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey])
);

CREATE TABLE [DIM_SHIFT] (
    [ShiftKey]   INT IDENTITY(1,1) NOT NULL,
    [ShiftCode]  VARCHAR(10) NOT NULL,          -- AM / PM
    CONSTRAINT [PK_DIM_SHIFT] PRIMARY KEY CLUSTERED ([ShiftKey])
);

CREATE TABLE [DIM_CREW] (
    [CrewKey]    INT IDENTITY(1,1) NOT NULL,
    [CrewCode]   VARCHAR(10) NOT NULL,          -- A / B / C
    CONSTRAINT [PK_DIM_CREW] PRIMARY KEY CLUSTERED ([CrewKey])
);

CREATE TABLE [DIM_PRODUCTIONCASE] (
    [CaseKey]    INT IDENTITY(1,1) NOT NULL,
    [CaseName]   NVARCHAR(50) NOT NULL,         -- Normal / Trial / Reworking
    CONSTRAINT [PK_DIM_PRODUCTIONCASE] PRIMARY KEY CLUSTERED ([CaseKey])
);

CREATE TABLE [DIM_CUSTOMER] (
    [CustomerKey]   INT IDENTITY(1,1) NOT NULL,
    [CustomerCode]  VARCHAR(50) NOT NULL,
    [CustomerName]  NVARCHAR(150) NOT NULL,
    [CountryType]   NVARCHAR(50) NULL,         -- Local / Export
    CONSTRAINT [PK_DIM_CUSTOMER] PRIMARY KEY CLUSTERED ([CustomerKey])
);

CREATE TABLE [DIM_PRODUCT] (
    [ProductKey]    INT IDENTITY(1,1) NOT NULL,
    [CustomerKey]   INT NOT NULL,
    [ProductCode]   VARCHAR(50) NOT NULL,
    [ProductName]   NVARCHAR(150) NOT NULL,
    [Category]      NVARCHAR(50) NULL,         -- Jar / Bottle
    CONSTRAINT [PK_DIM_PRODUCT] PRIMARY KEY CLUSTERED ([ProductKey]),
    CONSTRAINT [FK_DIM_PRODUCT_CUSTOMER] FOREIGN KEY ([CustomerKey]) REFERENCES [DIM_CUSTOMER]([CustomerKey])
);

CREATE TABLE [DIM_ORDER] (
    [OrderKey]          INT IDENTITY(1,1) NOT NULL,
    [ProductKey]        INT NOT NULL,
    [OrderNumber]       VARCHAR(50) NOT NULL,
    [TotalMoltenUnits]  DECIMAL(18,2) NULL,
    CONSTRAINT [PK_DIM_ORDER] PRIMARY KEY CLUSTERED ([OrderKey]),
    CONSTRAINT [FK_DIM_ORDER_PRODUCT] FOREIGN KEY ([ProductKey]) REFERENCES [DIM_PRODUCT]([ProductKey])
);

CREATE TABLE [DIM_JOBCHANGETYPE] (
    [JobChangeTypeKey]  INT IDENTITY(1,1) NOT NULL,
    [TypeName]          NVARCHAR(50) NOT NULL,  -- Small / Medium / Big / Process
    [TargetT1_Hrs]      DECIMAL(8,2) NULL,
    [TargetT2_Hrs]      DECIMAL(8,2) NULL,
    CONSTRAINT [PK_DIM_JOBCHANGETYPE] PRIMARY KEY CLUSTERED ([JobChangeTypeKey])
);

CREATE TABLE [DIM_LOSSCATEGORY] (
    [LossCategoryKey]       INT IDENTITY(1,1) NOT NULL,
    [ParentLossCategoryKey] INT NULL,
    [CategoryName]          NVARCHAR(100) NOT NULL,
    [CategoryLevel]         NVARCHAR(50) NULL,
    CONSTRAINT [PK_DIM_LOSSCATEGORY] PRIMARY KEY CLUSTERED ([LossCategoryKey]),
    CONSTRAINT [FK_DIM_LOSSCATEGORY_PARENT] FOREIGN KEY ([ParentLossCategoryKey])
        REFERENCES [DIM_LOSSCATEGORY]([LossCategoryKey])
);

CREATE TABLE [DIM_DEFECT] (
    [DefectKey]     INT IDENTITY(1,1) NOT NULL,
    [DefectName]    NVARCHAR(100) NOT NULL,
    [Severity]      NVARCHAR(50) NULL,
    CONSTRAINT [PK_DIM_DEFECT] PRIMARY KEY CLUSTERED ([DefectKey])
);

CREATE TABLE [DIM_REWORKSTATUS] (
    [ReworkStatusKey]   INT IDENTITY(1,1) NOT NULL,
    [StatusName]        NVARCHAR(50) NOT NULL,  -- Hold / Resorted / Move to Cullet
    CONSTRAINT [PK_DIM_REWORKSTATUS] PRIMARY KEY CLUSTERED ([ReworkStatusKey])
);

CREATE TABLE [DIM_DOWNTIMEREASON] (
    [DowntimeReasonKey] INT IDENTITY(1,1) NOT NULL,
    [ReasonName]        NVARCHAR(150) NOT NULL,
    [AppliesTo]         VARCHAR(20) NOT NULL, -- 'HE' / 'CE' / 'Palletizer'
    CONSTRAINT [PK_DIM_DOWNTIMEREASON] PRIMARY KEY CLUSTERED ([DowntimeReasonKey])
);

-- ===================== 2. FACT TABLES =====================

CREATE TABLE [FACT_JOBCHANGE] (
    [JobChangeKey]              INT IDENTITY(1,1) NOT NULL,
    [DateKey]                   INT NOT NULL,
    [FactoryKey]                INT NOT NULL,
    [LineKey]                   INT NOT NULL,
    [ShiftKey]                  INT NOT NULL,
    [CrewKey]                   INT NOT NULL,
    [FromOrderKey]              INT NULL,
    [ToOrderKey]                INT NOT NULL,
    [JobChangeTypeKey]          INT NOT NULL,
    [HE_DowntimeReasonKey]      INT NULL,
    [CE_LossesReasonKey]        INT NULL,
    [PalletizerReasonKey]       INT NULL,
    [MechanicalWorkT1_Hrs]      DECIMAL(8,2) NULL,
    [FormingTimeT2_Hrs]         DECIMAL(8,2) NULL,
    [TrialLosses_Hrs]           DECIMAL(8,2) NULL,
    [CE_Losses_Hrs]             DECIMAL(8,2) NULL,
    [HE_Downtime_Hrs]           DECIMAL(8,2) NULL,
    [PalletizerLosses_Hrs]      DECIMAL(8,2) NULL,
    [TotalJobChangeLosses_Hrs]  AS (
        ISNULL([MechanicalWorkT1_Hrs],0) + ISNULL([FormingTimeT2_Hrs],0) +
        ISNULL([TrialLosses_Hrs],0) + ISNULL([CE_Losses_Hrs],0) +
        ISNULL([HE_Downtime_Hrs],0) + ISNULL([PalletizerLosses_Hrs],0)
    ) PERSISTED,
    CONSTRAINT [PK_FACT_JOBCHANGE] PRIMARY KEY CLUSTERED ([JobChangeKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_CREW] FOREIGN KEY ([CrewKey]) REFERENCES [DIM_CREW]([CrewKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_FROMORDER] FOREIGN KEY ([FromOrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_TOORDER] FOREIGN KEY ([ToOrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_TYPE] FOREIGN KEY ([JobChangeTypeKey]) REFERENCES [DIM_JOBCHANGETYPE]([JobChangeTypeKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_HE_REASON] FOREIGN KEY ([HE_DowntimeReasonKey]) REFERENCES [DIM_DOWNTIMEREASON]([DowntimeReasonKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_CE_REASON] FOREIGN KEY ([CE_LossesReasonKey]) REFERENCES [DIM_DOWNTIMEREASON]([DowntimeReasonKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_PALLETIZER_REASON] FOREIGN KEY ([PalletizerReasonKey]) REFERENCES [DIM_DOWNTIMEREASON]([DowntimeReasonKey])
);

CREATE TABLE [FACT_PRODUCTION] (
    [ProductionKey]         INT IDENTITY(1,1) NOT NULL,
    [DateKey]               INT NOT NULL,
    [FactoryKey]            INT NOT NULL,
    [LineKey]               INT NOT NULL,
    [ShiftKey]              INT NOT NULL,
    [CrewKey]               INT NOT NULL,
    [OrderKey]              INT NOT NULL,
    [CaseKey]               INT NOT NULL,
    [NoSections]            INT NULL,
    [NoCavities]            INT NULL,
    [DesignedCyclesPerMin]  DECIMAL(10,2) NULL,
    [DesignedCutsPerHour]   DECIMAL(10,2) NULL,
    [WorkingHours]          DECIMAL(6,2) NULL,
    [DesignOutput]          DECIMAL(18,2) NULL,
    [ActualPack]            DECIMAL(18,2) NULL,
    [TotalHold]             DECIMAL(18,2) NULL,
    CONSTRAINT [PK_FACT_PRODUCTION] PRIMARY KEY CLUSTERED ([ProductionKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_CREW] FOREIGN KEY ([CrewKey]) REFERENCES [DIM_CREW]([CrewKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_ORDER] FOREIGN KEY ([OrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_PRODUCTION_CASE] FOREIGN KEY ([CaseKey]) REFERENCES [DIM_PRODUCTIONCASE]([CaseKey])
);

-- Locked business rules:
--   LossPercent     = raw % from LossesLog (of Design Output)
--   ComputedValue   = LossPercent × DesignOutput   (populated by SSIS)
--   Total Losses %  = SUM(LossPercent)             (SSAS / Power BI measure only)
CREATE TABLE [FACT_LOSSESOUTPUT] (
    [LossOutputKey]     INT IDENTITY(1,1) NOT NULL,
    [DateKey]           INT NOT NULL,
    [FactoryKey]        INT NOT NULL,
    [LineKey]           INT NOT NULL,
    [ShiftKey]          INT NOT NULL,
    [OrderKey]          INT NOT NULL,
    [LossCategoryKey]   INT NOT NULL,
    [LossPercent]       DECIMAL(9,6) NULL,
    [ComputedValue]     DECIMAL(18,4) NULL,  -- = LossPercent × DesignOutput
    CONSTRAINT [PK_FACT_LOSSESOUTPUT] PRIMARY KEY CLUSTERED ([LossOutputKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_ORDER] FOREIGN KEY ([OrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_CATEGORY] FOREIGN KEY ([LossCategoryKey]) REFERENCES [DIM_LOSSCATEGORY]([LossCategoryKey])
);

CREATE TABLE [FACT_DEFECTSAMPLING] (
    [DefectSamplingKey] INT IDENTITY(1,1) NOT NULL,
    [DateKey]           INT NOT NULL,
    [FactoryKey]        INT NOT NULL,
    [LineKey]           INT NOT NULL,
    [OrderKey]          INT NOT NULL,
    [HourKey]           INT NOT NULL,
    [ShiftKey]          INT NOT NULL,
    [DefectKey]         INT NOT NULL,
    [TotalSamples]      INT NOT NULL,
    [Quantity]          DECIMAL(18,2) NOT NULL,
    CONSTRAINT [PK_FACT_DEFECTSAMPLING] PRIMARY KEY CLUSTERED ([DefectSamplingKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_ORDER] FOREIGN KEY ([OrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_HOUR] FOREIGN KEY ([HourKey]) REFERENCES [DIM_HOUR]([HourKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_DEFECTSAMPLING_DEFECT] FOREIGN KEY ([DefectKey]) REFERENCES [DIM_DEFECT]([DefectKey])
);

CREATE TABLE [FACT_REWORK] (
    [ReworkKey]             INT IDENTITY(1,1) NOT NULL,
    [DateKey]               INT NOT NULL,
    [FactoryKey]            INT NOT NULL,
    [LineKey]               INT NOT NULL,
    [ShiftKey]              INT NOT NULL,
    [OrderKey]              INT NOT NULL,
    [ReworkStatusKey]       INT NOT NULL,
    [PalletsCount]          INT NULL,
    [ArticlesPerPallet]     DECIMAL(10,2) NULL,
    [ReworkedUnits]         AS (ISNULL([PalletsCount],0) * ISNULL([ArticlesPerPallet],0)) PERSISTED,
    CONSTRAINT [PK_FACT_REWORK] PRIMARY KEY CLUSTERED ([ReworkKey]),
    CONSTRAINT [FK_FACT_REWORK_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_REWORK_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_REWORK_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_REWORK_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_REWORK_ORDER] FOREIGN KEY ([OrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_REWORK_STATUS] FOREIGN KEY ([ReworkStatusKey]) REFERENCES [DIM_REWORKSTATUS]([ReworkStatusKey])
);
