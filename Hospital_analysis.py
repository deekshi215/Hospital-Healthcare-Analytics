#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


# load the dataset
from pathlib import Path

file_path = Path(
    r"C:\Users\drdee\OneDrive\Desktop\Hospital Healthcare Analytics\hospital_admissions_cleaned.csv"

)

df = pd.read_csv(file_path)


# In[9]:


# check number of rows and columns
print("Rows and columns:", df.shape)


# In[10]:


# check the first five rows
df.head()


# In[11]:


# check all column names
df.columns.tolist()


# In[12]:


# check data types
df.dtypes


# In[13]:


# check missing values
df.isnull().sum()


# In[14]:


# check duplicate rows
df.duplicated().sum()


# In[15]:


# standardize column names 
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

print(df.columns.tolist())


# In[16]:


# convert dates and numeric columns
date_columns = ["admission_date", "discharge_date"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(
            df[col],
            errors="coerce",
            dayfirst=True
        )

numeric_columns = [
    "age",
    "length_of_stay_days",
    "billing_amount",
    "patient_satisfaction"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.dtypes)


# In[19]:


# identify invalid records
if "age" in df.columns:
    invalid_age = df[
        (df["age"] < 0) | (df["age"] > 120)
    ]

    print("Invalid ages:", len(invalid_age))

if "length_of_stay_days" in df.columns:
    invalid_stay = df[
        df["length_of_stay_days"] < 0
    ]

    print("Negative length of stay:", len(invalid_stay))

if "billing_amount" in df.columns:
    invalid_billing = df[
        df["billing_amount"] < 0
    ]

    print("Negative billing amounts:", len(invalid_billing))

if "admission_date" in df.columns:
    invalid_dates = df[df["admission_date"].isna()]

    print("Missing or invalid admission dates:", len(invalid_dates))

if {"admission_date", "discharge_date"}.issubset(df.columns):
    invalid_date_order = df[
        df["admission_date"].notna()
        & df["discharge_date"].notna()
        & (df["discharge_date"] < df["admission_date"])
    ]

    print("Discharge before admission:", len(invalid_date_order))


# In[21]:


# calculate the main hospital KPIs
print("Total admissions:", len(df))

if "patient_id" in df.columns:
    print("Unique patients:", df["patient_id"].nunique())

if "length_of_stay_days" in df.columns:
    valid_stay = df.loc[
        df["length_of_stay_days"] >= 0,
        "length_of_stay_days"
    ]

    print("Average length of stay:", round(valid_stay.mean(), 2))

if "billing_amount" in df.columns:
    valid_billing = df.loc[
        df["billing_amount"] >= 0,
        "billing_amount"
    ]

    print("Total billing:", round(valid_billing.sum(), 2))
    print("Average billing:", round(valid_billing.mean(), 2))

if "department" in df.columns:
    print("\nAdmissions by department:")
    print(df["department"].value_counts(dropna=False))


# In[22]:


# calculate the 30-day readmission rate
if "is_readmission_30d" in df.columns:
    status = (
        df["is_readmission_30d"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    valid_status = status.isin(
        ["true", "false", "yes", "no", "1", "0"]
    )

    readmitted = status.isin(["true", "yes", "1"])

    readmission_rate = (
        readmitted[valid_status].mean() * 100
        if valid_status.any()
        else np.nan
    )

    print(
        "Readmission rate (%):",
        round(readmission_rate, 2)
        if pd.notna(readmission_rate)
        else "No valid readmission records"
    )

    print("\nReadmission status counts:")
    print(status.value_counts(dropna=False))


# In[23]:


# analyze monthly admissions
if {"admission_month", "admission_date"}.issubset(df.columns):
    monthly_admissions = (
        df.dropna(subset=["admission_date"])
        .groupby("admission_month")
        .size()
        .sort_index()
    )

    print(monthly_admissions)


# In[27]:


# plot monthly hospital admissions
if "admission_month" in df.columns:
    monthly_admissions = (
        df.dropna(subset=["admission_date"])
        .groupby("admission_month")
        .size()
        .sort_index()
    )

    monthly_admissions.index = monthly_admissions.index.astype(str)

    monthly_admissions.plot(
        kind="line",
        marker="o",
        figsize=(12, 5)
    )

    plt.title("Monthly Hospital Admissions")
    plt.xlabel("Admission Month")
    plt.ylabel("Number of Admissions")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# In[25]:


# department wise performance
if "department" in df.columns:
    department_analysis = df.groupby("department").agg(
        total_admissions=("department", "size")
    )

    if "length_of_stay_days" in df.columns:
        department_analysis["avg_length_of_stay"] = (
            df.groupby("department")["length_of_stay_days"].mean().round(2)
        )

    if "billing_amount" in df.columns:
        department_analysis["total_billing"] = (
            df.groupby("department")["billing_amount"].sum().round(2)
        )

    print(department_analysis.sort_values(
        "total_admissions", ascending=False
    ))


# In[26]:


# average patient satisfaction by department
if {"department", "patient_satisfaction"}.issubset(df.columns):
    satisfaction_analysis = (
        df.groupby("department")
        .agg(
            avg_satisfaction=("patient_satisfaction", "mean"),
            recorded_scores=("patient_satisfaction", "count")
        )
        .round(2)
        .sort_values("avg_satisfaction", ascending=False)
    )

    print(satisfaction_analysis)


# In[ ]:




