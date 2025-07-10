import pandas as pd
from pathlib import Path
from db_connect import get_snowflake_connection
import os

def load_csv_to_snowflake(csv_path, table_name):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    # Create table first (optional if already created)
    create_query = """
    CREATE OR REPLACE TABLE SUPERSTORE (
        "Row ID" INTEGER,
        "Order ID" STRING,
        "Order Date" DATE,
        "Ship Date" DATE,
        "Ship Mode" STRING,
        "Customer ID" STRING,
        "Customer Name" STRING,
        "Segment" STRING,
        "Country" STRING,
        "City" STRING,
        "State" STRING,
        "Postal Code" STRING,
        "Region" STRING,
        "Product ID" STRING,
        "Category" STRING,
        "Sub-Category" STRING,
        "Product Name" STRING,
        "Sales" FLOAT,
        "Quantity" INTEGER,
        "Discount" FLOAT,
        "Profit" FLOAT
    );
    """
    cursor.execute(create_query)

    # Create Stage
    stage_name = "SUPERSTORE_STAGE"
    cursor.execute(f"CREATE OR REPLACE STAGE {stage_name}")

    # PUT CSV to Stage
    cursor.execute(f"PUT file://{csv_path} @{stage_name}")

    # COPY INTO table
    copy_query = f"""
    COPY INTO {table_name}
    FROM @{stage_name}/{os.path.basename(csv_path)}
    FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '"')
    """
    cursor.execute(copy_query)

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data loaded into {table_name}")

if __name__ == "__main__":
    base_dir = Path().resolve().parent
    data_dir = base_dir / "data" / "raw"
    csv_file = "superstore.csv"
    table_name = "SUPERSTORE"
    csv_path = data_dir / csv_file

    load_csv_to_snowflake(csv_path, table_name)
