import pandas as pd
import matplotlib.pyplot as plt


def load_sales_data(file_path):
    """Load sales data from a CSV file."""
    return pd.read_csv(file_path)


def analyze_sales(df):
    """Generate basic sales performance metrics."""
    analysis = {}

    if "Sales" in df.columns:
        analysis["Total Sales"] = df["Sales"].sum()
        analysis["Average Sales"] = df["Sales"].mean()

    if "Profit" in df.columns:
        analysis["Total Profit"] = df["Profit"].sum()

    return analysis


def display_summary(df):
    """Display a summary of the sales dataset."""
    print("\n===== SALES PERFORMANCE SUMMARY =====")

    print(f"Total Records: {len(df)}")

    if "Sales" in df.columns:
        print(f"Total Sales: {df['Sales'].sum():,.2f}")
        print(f"Average Sales: {df['Sales'].mean():,.2f}")

    if "Profit" in df.columns:
        print(f"Total Profit: {df['Profit'].sum():,.2f}")


def main():
    print("📊 Sales Performance Business Analytics")

    file_path = input("Enter the path to your sales CSV file: ")

    try:
        df = load_sales_data(file_path)

        print("\nDataset loaded successfully!")
        print("\nColumns:")
        print(list(df.columns))

        display_summary(df)

    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")

    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    main()
