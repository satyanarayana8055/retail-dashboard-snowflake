import pandas as pd
import os

def clean_superstore_data():
    # File paths
    input_path = "data/raw/superstore.csv"
    output_path = "data/processed/superstore_cleaned.csv"

    # Load the data
    df = pd.read_csv(input_path)

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill or drop missing values (you can customize as needed)
    df.fillna("", inplace=True)

    # Create processed folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")

if __name__ == "__main__":
    clean_superstore_data()
