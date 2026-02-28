# LOOPALYTICS: Data Analysis Tool 
""" 
Features: 
    1. Loads CSV / Experimental Logs (Input)
    2. Cleans missing values
    3. Computes: 
        a. Mean/Variance
        b. Confidence Intervals
        c. Correlation Matrices
    4. Auto-Generates: 
        a. Scatter plots
        b. Histogram
        c. Regression-lines
    5. PDF File (Output)

    Created by: Prince Pamintuan
    Date: February 20, 2026 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy import stats

def load_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or XLSX.")

def clean_data(df):
    df_clean = df.dropna()
    df_clean.to_excel("clean.xlsx", index=False)
    return df_clean

def descriptive_stats(df):
    means = df.mean()
    variances = df.var()
    return means, variances

def confidence_intervals(df, confidence=0.95):
    ci_results = {}
    for col in df.columns:
        data = df[col]
        n = len(data)
        mean = np.mean(data)
        sem = stats.sem(data)
        margin = sem * stats.t.ppf((1 + confidence) / 2., n-1)
        ci_results[col] = (mean - margin, mean + margin)
    return ci_results

def generate_plots(df, pdf):
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    dependent = "Exam_Score"
    independents = [col for col in numeric_cols if col != dependent]
    
    for col in numeric_cols:
        plt.figure()
        df[col].hist()
        plt.title(f"Histogram - {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        pdf.savefig()
        plt.close()
    
    for col in independents:
        plt.figure()
        plt.scatter(df[col], df[dependent])
        
        m, b = np.polyfit(df[col], df[dependent], 1)
        plt.plot(df[col], m*df[col] + b)
        
        plt.title(f"{col} vs {dependent}")
        plt.xlabel(col)
        plt.ylabel(dependent)
        pdf.savefig()
        plt.close()
        
def main():
    file_path = input("Enter file path (CSV/XLSX): ")
    
    df = load_file(file_path)
    df = clean_data(df)
    
    means, variances = descriptive_stats(df)
    ci = confidence_intervals(df)
    correlation_matrix = df.corr()
    
    with PdfPages("LOOPALYTICS_Report.pdf") as pdf:
        
        # Add text summary page
        plt.figure(figsize=(8, 10))
        plt.axis("off")
        
        text = "LOOPALYTICS DATA REPORT\n\n"
        text += "MEANS:\n" + str(means) + "\n\n"
        text += "VARIANCES:\n" + str(variances) + "\n\n"
        text += "CONFIDENCE INTERVALS (95%):\n" + str(ci) + "\n\n"
        text += "CORRELATION MATRIX:\n" + str(correlation_matrix)
        
        plt.text(0.01, 0.99, text, va='top')
        pdf.savefig()
        plt.close()
        
        generate_plots(df, pdf)
    
    print("Report generated: LOOPALYTICS_Report.pdf")

if __name__ == "__main__":
    main()