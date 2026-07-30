-- ============================================================================
-- Kandil Glass — Production Data Platform
-- DWH LAYER — Final Aligned Version (optimized for SSIS from Staging)
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
    [CategoryLevel]         NVARCHAR(50) NULL,  -- Zone-level / Category / Sub-category
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

CREATE TABLE [DIM_REJECTIONZONE] (
    [RejectionZoneKey]  INT IDENTITY(1,1) NOT NULL,
    [ZoneName]          NVARCHAR(100) NOT NULL,
    CONSTRAINT [PK_DIM_REJECTIONZONE] PRIMARY KEY CLUSTERED ([RejectionZoneKey])
);

CREATE TABLE [DIM_REWORKSTATUS] (
    [ReworkStatusKey]   INT IDENTITY(1,1) NOT NULL,
    [StatusName]        NVARCHAR(50) NOT NULL,  -- Hold / Resorted / Move to Cullet
    CONSTRAINT [PK_DIM_REWORKSTATUS] PRIMARY KEY CLUSTERED ([ReworkStatusKey])
);

CREATE TABLE [DIM_HOUR] (
    [HourKey]       INT NOT NULL,               -- 0 to 23
    [HourNumber]    INT NOT NULL,               -- 0 to 23
    [HourLabel]     VARCHAR(10) NOT NULL,       -- '00:00', '01:00', ...
    [HourLabel12]   VARCHAR(10) NOT NULL,       -- '12 AM', '1 AM', ...
    [ShiftGroup]    VARCHAR(10) NULL,          -- 'AM' / 'PM' (optional helper)
    CONSTRAINT [PK_DIM_HOUR] PRIMARY KEY CLUSTERED ([HourKey])
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
    [MechanicalWorkT1_Hrs]      DECIMAL(8,2) NULL,
    [FormingTimeT2_Hrs]         DECIMAL(8,2) NULL,
    [TrialLosses_Hrs]           DECIMAL(8,2) NULL,
    [CE_Losses_Hrs]             DECIMAL(8,2) NULL,
    [HE_Downtime_Hrs]           DECIMAL(8,2) NULL,
    [PalletizerLosses_Hrs]      DECIMAL(8,2) NULL,
    [ExtraT1_Hrs]               DECIMAL(8,2) NULL,
    [ExtraT2_Hrs]               DECIMAL(8,2) NULL,
    [TotalJobChangeLosses_Hrs]  AS (
        ISNULL([MechanicalWorkT1_Hrs],0) + ISNULL([FormingTimeT2_Hrs],0) +
        ISNULL([TrialLosses_Hrs],0) + ISNULL([CE_Losses_Hrs],0) +
        ISNULL([HE_Downtime_Hrs],0) + ISNULL([PalletizerLosses_Hrs],0) +
        ISNULL([ExtraT1_Hrs],0) + ISNULL([ExtraT2_Hrs],0)
    ) PERSISTED,
    CONSTRAINT [PK_FACT_JOBCHANGE] PRIMARY KEY CLUSTERED ([JobChangeKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_CREW] FOREIGN KEY ([CrewKey]) REFERENCES [DIM_CREW]([CrewKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_FROMORDER] FOREIGN KEY ([FromOrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_TOORDER] FOREIGN KEY ([ToOrderKey]) REFERENCES [DIM_ORDER]([OrderKey]),
    CONSTRAINT [FK_FACT_JOBCHANGE_TYPE] FOREIGN KEY ([JobChangeTypeKey]) REFERENCES [DIM_JOBCHANGETYPE]([JobChangeTypeKey])
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
    [DesignedCutsPerHour]   DECIMAL(10,2) NULL,
    [ActualPack]            DECIMAL(18,2) NULL,
    [TotalReject]           DECIMAL(18,2) NULL,
    [TotalResort]           DECIMAL(18,2) NULL,
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

CREATE TABLE [FACT_LOSSESOUTPUT] (
    [LossOutputKey]     INT IDENTITY(1,1) NOT NULL,
    [DateKey]           INT NOT NULL,
    [FactoryKey]        INT NOT NULL,
    [LineKey]           INT NOT NULL,
    [ShiftKey]          INT NOT NULL,
    [LossCategoryKey]   INT NOT NULL,
    [DefectKey]         INT NULL,               -- only when coming from STG_DEFECTLOG
    [RejectionZoneKey]  INT NULL,               -- only when coming from STG_DEFECTLOG
    [Value]             DECIMAL(18,4) NOT NULL,
    CONSTRAINT [PK_FACT_LOSSESOUTPUT] PRIMARY KEY CLUSTERED ([LossOutputKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_HOUR] FOREIGN KEY ([HourKey]) REFERENCES [DIM_HOUR]([HourKey]),   -- NEW
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_FACTORY] FOREIGN KEY ([FactoryKey]) REFERENCES [DIM_FACTORY]([FactoryKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_SHIFT] FOREIGN KEY ([ShiftKey]) REFERENCES [DIM_SHIFT]([ShiftKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_CATEGORY] FOREIGN KEY ([LossCategoryKey]) REFERENCES [DIM_LOSSCATEGORY]([LossCategoryKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_DEFECT] FOREIGN KEY ([DefectKey]) REFERENCES [DIM_DEFECT]([DefectKey]),
    CONSTRAINT [FK_FACT_LOSSESOUTPUT_ZONE] FOREIGN KEY ([RejectionZoneKey]) REFERENCES [DIM_REJECTIONZONE]([RejectionZoneKey])
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

CREATE TABLE [FACT_LINECONFIG_DAILY] (
    [LineConfigKey]     INT IDENTITY(1,1) NOT NULL,
    [DateKey]           INT NOT NULL,
    [LineKey]           INT NOT NULL,
    [SectionNumber]     INT NOT NULL,
    [CavitiesActive]    INT NOT NULL,
    [CaseKey]           INT NOT NULL,
    CONSTRAINT [PK_FACT_LINECONFIG_DAILY] PRIMARY KEY CLUSTERED ([LineConfigKey]),
    CONSTRAINT [FK_FACT_LINECONFIG_DATE] FOREIGN KEY ([DateKey]) REFERENCES [DIM_DATE]([DateKey]),
    CONSTRAINT [FK_FACT_LINECONFIG_LINE] FOREIGN KEY ([LineKey]) REFERENCES [DIM_LINE]([LineKey]),
    CONSTRAINT [FK_FACT_LINECONFIG_CASE] FOREIGN KEY ([CaseKey]) REFERENCES [DIM_PRODUCTIONCASE]([CaseKey])
);