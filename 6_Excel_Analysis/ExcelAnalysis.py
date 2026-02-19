import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as matplotlib
import os

plt.show()
output_dir = "analysis_plots"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "plot1.png"))
plt.close()
#matplotlib.use("Agg") 


file_path = "C:\\Users\\maulik.prajapati\\OneDrive - Icertis Solutions\\SNOW\\Learning\\Python\\6_Excel_Analysis\\AssignedCases.xlsx";


def analyze_excel(file_path, sheet_name="None"):
    """
    Perform full analysis of the uploaded Excel file.
    :param file_path: Path to the Excel file
    :param sheet_name: Optional, sheet name (default is first sheet)
    """
    # Load Excel file
    df = pd.read_excel(file_path, sheet_name="None")

    print("="*60)
    print("📊 DATA OVERVIEW")
    print("="*60)
    print(df.head(), "\n")

    print("="*60)
    print("📌 BASIC INFO")
    print("="*60)
    print(df.info(), "\n")

    print("="*60)
    print("🔢 STATISTICS")
    print("="*60)
    print(df.describe(include='all').transpose(), "\n")

    print("="*60)
    print("🚩 MISSING VALUES")
    print("="*60)
    print(df.isnull().sum(), "\n")

    # Correlation analysis (only numeric columns)
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        print("="*60)
        print("📈 CORRELATION MATRIX")
        print("="*60)
        print(numeric_df.corr(), "\n")

        # Plot correlation heatmap
        plt.figure(figsize=(10,6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()

    # Distribution plots
    for col in numeric_df.columns:
        plt.figure(figsize=(8,4))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.show()

    # Boxplots for outlier detection
    for col in numeric_df.columns:
        plt.figure(figsize=(8,4))
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.show()

    print("✅ Analysis completed successfully!")

# Example usage:
# analyze_excel("your_file.xlsx")
