# LOOPALYTICS 

Loopalytics is a lightweight Python-based data analysis tool that automates basic statistical workflows and generates a structured PDF report from a dataset.

Date: February 20, 2026  

## Purpose

LOOPALYTICS is designed to:

- Clean datasets
- Compute descriptive statistics
- Analyze correlations
- Generate regression plots
- Export results into a single PDF report

It is intended for internal research, survey analysis, and experimental data review.


## Features

### Data Input
- Supports CSV files

### Data Cleaning
- Removes rows with missing values
- Exports cleaned dataset as `clean.xlsx`

### Statistical Analysis
- Mean
- Variance
- 95% Confidence Intervals (t-distribution)
- Pearson Correlation Matrix

### Visualizations
- Histogram for each numeric variable
- Scatter plots
- Linear regression lines

### Output
- `LOOPALYTICS_Report.pdf` containing:
  - Descriptive statistics
  - Confidence intervals
  - Correlation matrix
  - All generated plots

## Installation

Install required dependencies:
```bash
pip install pandas numpy matplotlib scipy openpyxl
```

## Usage

Run the program:
```bash
python main.py
```
When prompted:
```bash
Enter file path (CSV/XLSX):
```
Type:
```bash
dataset.csv
```
After execution, the following files will be generated:
clean.xlsx
LOOPALYTICS_Report.pdf

<img width="486" height="441" alt="image" src="https://github.com/user-attachments/assets/30f5e357-0ba4-4904-b514-3246e1611cab" />
<img width="421" height="313" alt="image" src="https://github.com/user-attachments/assets/bdfc9435-0be8-4a70-bbce-74ecd6636d14" />
<img width="421" height="313" alt="image" src="https://github.com/user-attachments/assets/e2beb304-4b1d-4c87-8b51-21982666114e" />
<img width="403" height="309" alt="image" src="https://github.com/user-attachments/assets/209e8e0a-1a4d-4c0e-90a0-0a1ac0305a0a" />

## Limitations
- No categorical variable analysis
- No hypothesis testing (t-test, ANOVA)
- No multiple regression
- No graphical user interface
- Designed for structured numeric datasets
