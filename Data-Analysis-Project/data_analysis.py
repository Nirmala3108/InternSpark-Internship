import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================

file_path = "dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!\n")

except FileNotFoundError:
    print("CSV file not found!")
    exit()

# ==========================
# Basic Information
# ==========================

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# ==========================
# Data Cleaning
# ==========================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill numeric missing values with mean
numeric_columns = df.select_dtypes(include=['number']).columns

for col in numeric_columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Remove rows still containing null values
df.dropna(inplace=True)

print("\nData cleaned successfully!")

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

# ==========================
# Filtering Example
# ==========================

if "Sales" in df.columns:
    high_sales = df[df["Sales"] > df["Sales"].mean()]

    print("\nHigh Sales Records:")
    print(high_sales.head())

# ==========================
# Grouping Example
# ==========================

if "Category" in df.columns and "Sales" in df.columns:

    category_sales = df.groupby("Category")["Sales"].sum()

    print("\nTotal Sales by Category:")
    print(category_sales)

# ==========================
# Insights
# ==========================

print("\nKey Insights")

rows = len(df)
columns = len(df.columns)

print(f"Total Records: {rows}")
print(f"Total Columns: {columns}")

if len(numeric_columns) > 0:
    print("\nAverage Values:")
    print(df[numeric_columns].mean())

# ==========================
# Visualization
# ==========================

if "Category" in df.columns and "Sales" in df.columns:

    category_sales.plot(
        kind="bar",
        figsize=(8,5),
        title="Sales by Category"
    )

    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    plt.savefig("analysis_graph.png")
    plt.show()

    print("\nGraph saved as analysis_graph.png")

print("\nAnalysis Completed Successfully!")