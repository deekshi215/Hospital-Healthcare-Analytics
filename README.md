# Hospital & Healthcare Operations Analytics

## Problem Statement

This project analyzes hospital admissions, patient demographics, department-wise patient volumes, billing, length of stay, and 30-day readmissions to understand hospital operations and performance.

The dashboard helps identify admission trends, monitor healthcare costs, evaluate hospital resource utilization, and understand readmission patterns. It enables stakeholders to explore key operational metrics and make data-driven decisions to improve hospital efficiency and patient care.

## Tools & Technologies Used

- Microsoft Excel (Data Inspection & Cleaning)
- Python (Data Cleaning & Preprocessing)
- Pandas
- MySQL Workbench (SQL Analysis)
- Power BI Desktop (Dashboard & Visualization)
- Power Query (Data Transformation)
- DAX (KPI Calculations)
- GitHub

## Steps Followed

**Step 1: Load the Dataset**

The hospital healthcare dataset was imported from a CSV file containing patient information, admission details, medical information, billing amounts, and readmission indicators.

**Step 2: Data Inspection and Cleaning using Excel**

The dataset was inspected to identify data-quality issues:

- Checked missing and blank values
- Verified admission and discharge date formats
- Checked Age and Billing Amount data types
- Identified invalid or negative values for review
- Checked inconsistent category values
- Preserved the original raw dataset

The cleaned data was prepared for further analysis while avoiding the removal of valid repeat hospital admissions.

**Step 3: Data Cleaning using Python**

Python and Pandas were used to prepare the dataset for analysis:

- Standardized column names and data types
- Handled missing values
- Checked duplicate records
- Converted date columns into datetime format
- Validated admission and discharge dates
- Created derived fields such as Length of Stay, Admission Month, and Age Group where required

**Step 4: SQL Analysis using MySQL Workbench**

The cleaned dataset was imported into MySQL for structured analysis.

SQL queries were used to calculate:

- Total hospital admissions
- Average length of stay
- Department-wise admission counts
- Admission type distribution
- Total and average billing amounts
- 30-day readmission counts and rates
- Monthly admission trends

**Step 5: Data Transformation using Power Query**

The cleaned dataset was loaded into Power BI.

- Verified column data types
- Checked date and numeric fields
- Prepared fields for analysis
- Ensured consistent categories and structured data

**Step 6: KPI Metrics**

Key performance indicators were created using DAX measures:

- Total Admissions
- Average Length of Stay
- Total Billing Amount
- Average Billing Amount
- Readmission Admissions
- Readmission Rate (%)

These metrics provide a high-level overview of hospital operations and performance.

**Step 7: Patient and Admission Analysis**

Visualizations were created to analyze:

- Admissions by Age Group
- Admissions by Gender
- Admissions by Admission Type
- Admissions by Medical Condition
- Department-wise Patient Volumes

**Step 8: Billing Analysis**

Billing performance was analyzed using:

- Total Billing Amount
- Average Billing Amount
- Billing by Department
- Billing by Medical Condition
- Monthly Billing Trends, where applicable

**Step 9: Hospital Efficiency and Readmission Analysis**

The dashboard was designed to explore operational performance through:

- Average Length of Stay
- Length of Stay by Department
- Monthly Admission Trends
- 30-Day Readmission Counts
- Readmission Rate (%)

These metrics help identify operational patterns and areas that may require further investigation.

**Step 10: Interactive Filters**

Slicers were added to allow users to explore the dashboard by relevant categories, including:

- Admission Type
- Gender
- Age Group
- Department
- Medical Condition
- Admission Month

The available filters depend on the fields included in the final dashboard.

**Step 11: Dashboard Design**

An interactive Power BI dashboard was developed with KPI cards, charts, and filters to present hospital operational insights in a clear and accessible format.

## Dataset

The dataset used for this project is a hospital healthcare admissions dataset containing patient demographics, admission details, medical conditions, billing information, and readmission indicators.

The dataset was prepared and cleaned before being used for SQL analysis and Power BI visualization.

**Dataset files:**

- `healthcare_dataset.csv` — Original dataset
- `hospital_admissions_cleaned.csv` — Cleaned dataset used for analysis

## SQL Analysis

MySQL Workbench was used to query the cleaned hospital dataset and calculate operational metrics.

The analysis covers admissions, length of stay, billing, admission categories, and 30-day readmissions.

## Python Analysis

Python and Pandas were used for data cleaning, validation, preprocessing, and exploratory data analysis.

The Python workflow helped prepare the dataset for reliable reporting and visualization.

## Power BI Project File

The interactive hospital analytics dashboard was created using Microsoft Power BI Desktop.

**File:**

- `Hospital_Healthcare_Analytics.pbix`

Download the Power BI file from this repository and open it using Microsoft Power BI Desktop to explore the dashboard.

## Dashboard Screenshots

Add your actual Power BI dashboard screenshots below to showcase the completed project.

### Page 1 — Hospital Overview

![Hospital Overview Dashboard](images/hospital_overview.png)

### Page 2 — Patient and Admission Analysis

![Patient and Admission Analysis](images/patient_admission_analysis.png)

### Page 3 — Billing Analysis

![Billing Analysis](images/billing_analysis.png)

## Key Insights

The dashboard provides insights into hospital operations through admission patterns, patient demographics, billing performance, length of stay, and readmissions.

The main areas of analysis include:

### Admission Trends

- Identify changes in admission volumes over time.
- Compare admissions across different admission types.
- Understand patient distribution by age group and gender.

### Hospital Efficiency

- Monitor average length of stay.
- Compare operational patterns across departments.
- Identify areas that may require additional investigation.

### Billing Performance

- Evaluate total and average billing amounts.
- Compare billing across medical conditions and departments.
- Explore changes in billing patterns over time.

### Readmission Analysis

- Track admissions flagged as 30-day readmissions.
- Calculate the readmission rate using the available readmission indicator.
- Identify patterns that may warrant further clinical or operational investigation.

## Conclusion

The Hospital & Healthcare Operations Analytics project demonstrates how Excel, Python, SQL, and Power BI can be used together to transform healthcare data into meaningful operational insights.

By analyzing admissions, patient demographics, billing, length of stay, and readmissions, the project provides a structured view of hospital performance and demonstrates practical data analytics skills.

This project showcases skills in data cleaning, data validation, SQL querying, KPI development, data visualization, and interactive dashboard design, with a focus on healthcare analytics.
