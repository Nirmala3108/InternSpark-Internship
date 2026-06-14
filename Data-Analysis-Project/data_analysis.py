import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Load dataset
try:
    df = pd.read_csv("dataset.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: dataset.csv not found.")
    exit()

# ----------------------------
# Display Dataset Information
# ----------------------------
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

# ----------------------------
# Data Cleaning
# ----------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing numeric values with mean
numeric_columns = df.select_dtypes(include="number").columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Remove remaining null rows
df.dropna(inplace=True)

print("\nData cleaned successfully!")

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

# ----------------------------
# Filtering
# ----------------------------

high_sales = df[df["Sales"] > df["Sales"].mean()]

print("\nRecords with Sales Above Average:")
print(high_sales)

# ----------------------------
# Grouping & Aggregation
# ----------------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(category_sales)

# ----------------------------
# Insights
# ----------------------------

print("\n----- INSIGHTS -----")

print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

highest_category = category_sales.idxmax()
highest_sales = category_sales.max()

print(
    f"Highest Performing Category: "
    f"{highest_category} ({highest_sales})"
)

print("\nAverage Values:")
print(df[numeric_columns].mean())

# ----------------------------
# Visualization
# ----------------------------

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("output/analysis_graph.png")
plt.show()

print("\nGraph saved successfully!")

print("\nAnalysis Completed Successfully!")