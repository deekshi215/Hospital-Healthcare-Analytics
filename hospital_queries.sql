CREATE DATABASE hospital_analytics;
USE hospital_analytics;

-- Check the imported data
SELECT COUNT(*) AS total_rows
FROM hospital_admissions_cleaned;

SELECT *
FROM hospital_admissions_cleaned
LIMIT 10;

DESCRIBE hospital_admissions_cleaned;

-- Overall hospital KPIs
SELECT
    COUNT(*) AS total_admissions,
    COUNT(DISTINCT Patient_ID) AS unique_patients,
    ROUND(AVG(Length_of_Stay_Days), 2)
        AS average_length_of_stay,
    ROUND(SUM(Billing_Amount), 2) AS total_billing,
    ROUND(AVG(Billing_Amount), 2) AS average_billing
FROM hospital_admissions_cleaned;

-- Admissions by department
SELECT
    Department,
    COUNT(*) AS total_admissions,
    ROUND(AVG(Length_of_Stay_Days), 2)
        AS average_stay_days,
    ROUND(SUM(Billing_Amount), 2) AS total_billing
FROM hospital_admissions_cleaned
GROUP BY Department
ORDER BY total_admissions DESC;

-- Monthly admission trends
SELECT
    DATE_FORMAT(Admission_Date, '%Y-%m') AS admission_month,
    COUNT(*) AS total_admissions,
    ROUND(SUM(Billing_Amount), 2) AS total_billing
FROM hospital_admissions_cleaned
WHERE Admission_Date IS NOT NULL
GROUP BY DATE_FORMAT(Admission_Date, '%Y-%m')
ORDER BY admission_month;

-- Count TRUE and FALSE readmission records
SELECT
    Is_Readmission_30D,
    COUNT(*) AS record_count
FROM hospital_admissions_cleaned
GROUP BY Is_Readmission_30D;

-- Readmission rate
SELECT
    COUNT(*) AS total_admissions,
    SUM(
        CASE
            WHEN LOWER(CAST(Is_Readmission_30D AS CHAR)) = 'true'
            THEN 1
            ELSE 0
        END
    ) AS readmission_admissions,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN LOWER(CAST(Is_Readmission_30D AS CHAR)) = 'true'
                THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS readmission_rate_pct
FROM hospital_admissions_cleaned;

-- Department-wise readmission rates
SELECT
    Department,
    COUNT(*) AS total_admissions,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Is_Readmission_30D IN (1, '1', 'Yes', 'yes')
                THEN 1 ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS readmission_rate_pct
FROM hospital_admissions_cleaned
GROUP BY Department
ORDER BY readmission_rate_pct DESC;

-- Admissions by admission type
SELECT
    Admission_Type,
    COUNT(*) AS total_admissions,
    ROUND(AVG(Length_of_Stay_Days), 2)
        AS average_stay_days,
    ROUND(AVG(Billing_Amount), 2) AS average_billing
FROM hospital_admissions_cleaned
GROUP BY Admission_Type
ORDER BY total_admissions DESC;

-- Age-group analysis
SELECT
    CASE
        WHEN Age < 18 THEN 'Under 18'
        WHEN Age BETWEEN 18 AND 35 THEN '18-35'
        WHEN Age BETWEEN 36 AND 50 THEN '36-50'
        WHEN Age BETWEEN 51 AND 65 THEN '51-65'
        WHEN Age > 65 THEN 'Over 65'
        ELSE 'Unknown'
    END AS age_group,
    COUNT(*) AS total_admissions,
    ROUND(AVG(Length_of_Stay_Days), 2)
        AS average_stay_days,
    ROUND(AVG(Billing_Amount), 2) AS average_billing
FROM hospital_admissions_cleaned
GROUP BY age_group
ORDER BY total_admissions DESC;

-- Highest-billing admissions
SELECT
    Admission_ID,
    Department,
    Diagnosis,
    Admission_Date,
    Billing_Amount
FROM hospital_admissions_cleaned
WHERE Billing_Amount IS NOT NULL
ORDER BY Billing_Amount DESC
LIMIT 10;

-- Patient satisfaction by department
SELECT
    Department,
    COUNT(Patient_Satisfaction) AS responses,
    ROUND(AVG(Patient_Satisfaction), 2)
        AS average_satisfaction
FROM hospital_admissions_cleaned
GROUP BY Department
ORDER BY average_satisfaction DESC;

-- Data-quality exceptions
SELECT *
FROM hospital_admissions_cleaned
WHERE
    Admission_ID IS NULL
    OR Admission_Date IS NULL
    OR Age < 0
    OR Length_of_Stay_Days < 0
    OR Billing_Amount < 0;