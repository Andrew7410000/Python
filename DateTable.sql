/* Generate Date Table */

-- Declare start and end dates
DECLARE @StartDate DATE = '2020-01-01';
DECLARE @EndDate DATE = '2030-12-31';

-- Common Table Expressions (CTEs) to generate series of numbers and dates

--CTE to generate 10 rows with 1 as a value
WITH GenerateSeries_10 AS (
    SELECT
        1 AS Number
    FROM 
        (VALUES (1), (1),(1),(1),(1),(1),(1),(1),(1),(1)) AS T(ColName)
)

--CTE to generate 100 rows with 1 as a value
, GenerateSeries_100 AS (
    SELECT
        1 AS Number
    FROM
        GenerateSeries_10 AS T1 CROSS JOIN GenerateSeries_10 AS T2
)

--CTE to generate date values between StartDate and EndDate
, GenertaeSeriesDate AS (
    SELECT
        TOP(DATEIF(DAY, @StartDate, @EndDate) + 1)
        CONVERT(
            DATE
            , DATEADD(DAY, ROW_NUMBER() OVER(ORDER BY(SELECT NULL)) - 1, @StartDate)
        ) AS DATE 
    FROM 
        GenerateSeries_100 AS T1 CROSS JOIN GenerateSeries_100 AS T2
)

-- CTE to structure the date table with essential date-related information
, DateTable AS (
    SELECT
        DATE
        , YEAR(DATE) AS Year
        , DATENAME(QUARTER, DATE) AS Quarter 
        , MONTH (DATE) AS MonthNum
        , DATENAME (MONTH, DATE) AS MonthName
        , DAY(Date) AS Day
        , DATENAME(WEEK, DATE) AS WeekNum
        , DATENAME(WEEKDAY, DATE) AS WeekDay
        , DATENAME(DAYOFYEAR, DATE) AS DayOfYear
        , IIF(DATENAME(WEEKDAY, DATE) IN ('Saturday', 'Sunday'), 1, 0) AS IsWeekEnd
    FROM
        GenerateSeriesDate
)

SELECT * FROM DateTable