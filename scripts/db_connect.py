import snowflake.connector
import os
from dotenv import load_dotenv
from pathlib import Path

def get_snowflake_connection():
    # Load environment variables
    env_path = Path(__file__).resolve().parents[1] / '.env'
    load_dotenv(dotenv_path=env_path)

    # Fetch account and region
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    region = os.getenv("SNOWFLAKE_REGION")

    # Print for debug (optional)
    print("Connecting to Snowflake account:", f"{account}.{region}")

    # Create connection
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=f"{account}.{region}",  # Combine account and region properly
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    return conn
