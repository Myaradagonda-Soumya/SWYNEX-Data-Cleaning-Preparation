# SWYNEX – Data Cleaning & Preparation

## 📌 Task 1

This project is part of my internship task at **SWYNEX Technologies**.

The main objective of this task is to clean and prepare a raw dataset so that it can be used for further data analysis.

---

## 📊 Dataset

For this task, I used a public **Employee Dataset** containing employee-related information such as:

* Employee ID
* First Name
* Last Name
* Age
* Department
* Region
* Status
* Joining Date
* Salary
* Email
* Phone
* Performance Score
* Remote Work

The original dataset contains **1,020 records and 12 columns**.

---

## 🛠️ Tools Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* GitHub

---

## 🔍 Data Issues I Found

While checking the dataset, I found the following data-quality issues:

### 1. Missing Values

There were missing values in:

* **Age – 211 values**
* **Salary – 24 values**
* **Join_Date – 2 values**

I handled these missing values using suitable methods.

### 2. Duplicate Records

I checked the dataset for duplicate records.

There were **no duplicate records** in the dataset.

### 3. Incorrect Data Types

Some columns required data type conversion.

I converted:

* Age → Numeric
* Salary → Numeric
* Join_Date → Date/Datetime
* Remote_Work → Boolean

### 4. Inconsistent Values

I cleaned text values by removing unnecessary spaces and standardizing categorical values such as Status and Performance Score.

### 5. Department and Region

The original `Department_Region` column contained both department and region information.

I separated it into two columns:

* Department
* Region

---

## 🧹 Data Cleaning Process

I performed the following steps using Python and Pandas:

1. Loaded the raw CSV dataset.
2. Checked the number of rows and columns.
3. Checked missing values.
4. Checked duplicate records.
5. Removed unnecessary spaces from text columns.
6. Standardized categorical values.
7. Converted columns to the correct data types.
8. Handled missing Age values using the median.
9. Handled missing Salary values using the median.
10. Converted and handled missing Join_Date values using the median date.
11. Converted Remote_Work into Boolean values.
12. Separated Department and Region.
13. Checked the dataset again after cleaning.
14. Exported the cleaned dataset as a CSV file.

---

## 📈 Before and After Cleaning

### Before Cleaning

* Rows: **1,020**
* Columns: **12**
* Missing Age values: **211**
* Missing Salary values: **24**
* Missing Join_Date values: **2**
* Duplicate records: **0**

### After Cleaning

* Rows: **1,020**
* Columns: **13**
* Missing values: **0**
* Duplicate records: **0**
* Data types corrected
* Department and Region separated

---

## 📁 Project Structure

```text
SWYNEX-Data-Cleaning-Preparation/
│
├── data/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── data_cleaning.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

First install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the Python file:

```bash
python data_cleaning.py
```

The cleaned dataset will be saved inside the `data` folder.

---

## ✅ Final Result

After completing the cleaning process, the dataset has no remaining missing values or duplicate records and is properly structured for further data analysis.

This task helped me improve my practical knowledge of **Python, Pandas, data cleaning, data preprocessing, and data quality checking**.

---

#SWYNEX #Internship #DataCleaning #Python #Pandas #DataAnalytics #DataAnalysis #GitHub
