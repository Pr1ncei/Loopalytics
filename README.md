# LOOPALYTICS

LOOPALYTICS is a lightweight Python-based data analysis tool that automates basic statistical workflows and generates a structured PDF report from a dataset.

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

## Limitations
- No categorical variable analysis
- No hypothesis testing (t-test, ANOVA)
- No multiple regression
- No graphical user interface
- Designed for structured numeric datasets
