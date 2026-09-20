# SWYNEX – Data Cleaning & Preparation

## Task 1
**Objective:** Clean and prepare a raw dataset for analysis.

## Dataset
This project uses the **Messy Employee Dataset**, a public employee dataset intentionally designed to contain common data-quality problems such as missing values, inconsistent formatting, duplicate records and invalid entries.

**Public source:** https://github.com/RobStilson/Employee-Datasets

The repository description identifies the Messy Employee Dataset as a 1,020-row dataset intended for data-cleaning practice and lists fields including Employee_ID, Age, Department_Region, Status, Join_Date, Salary, Email, Phone, Performance_Score and Remote_Work.

## Tools
- Python
- Pandas
- NumPy
- Jupyter Notebook
- GitHub

## Data Quality Issues Checked
- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent categorical values
- Inconsistent date formats
- Invalid/non-numeric salary values
- Compound Department_Region field

## Cleaning Performed
1. Removed leading/trailing whitespace from text columns.
2. Standardized Status and Performance_Score capitalization.
3. Converted Age and Salary to numeric values.
4. Converted Join_Date to datetime.
5. Normalized Remote_Work into Boolean values.
6. Split Department_Region into Department and Region.
7. Filled missing Age with the median age.
8. Filled invalid/missing Salary values with the median salary.
9. Filled missing Email values with `unknown@example.com`.
10. Removed exact duplicate rows.
11. Validated the final dataset for remaining duplicates and missing values.

## Repository Structure
```text
SWYNEX-Data-Cleaning-Preparation/
├── data/
│   ├── raw_dataset_working_copy.csv
│   ├── cleaned_dataset.csv
│   └── data_quality_report.csv
├── notebooks/
│   └── data_cleaning.ipynb
├── data_cleaning.py
├── requirements.txt
└── README.md
```

## Reproducibility
Run:

```bash
pip install -r requirements.txt
python data_cleaning.py
```

The script downloads the public source CSV, cleans it and writes `data/cleaned_dataset.csv`.

## Important Note About the Included Working Copy
The included `raw_dataset_working_copy.csv` and `cleaned_dataset.csv` are a small reproducible demonstration artifact created to show the cleaning workflow in this package. **For the final internship submission, run `data_cleaning.py` once with internet access and commit the resulting full `data/cleaned_dataset.csv` generated from the public source dataset.** This keeps the submission faithful to the stated public source.

## Result
The final dataset is structured, typed consistently and ready for downstream analysis or visualization.

## Author
SWYNEX Internship – Task 1
