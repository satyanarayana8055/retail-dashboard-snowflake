# retail-dashboard-snowflake
“Retail analytics project using Snowflake, Python EDA, and Power BI dashboard”

retail-dashboard-snowflake/
│
├── data/
│   ├── raw/                      # Original CSV files (before cleaning)
│   │   ├── sales.csv
│   │   ├── stores.csv
│   │   ├── products.csv
│   │   └── calendar.csv
│   ├── processed/               # Merged and cleaned data
│   │   └── final_cleaned_data.csv
│   └── exports/                 # Optional: CSVs exported from DB or for Power BI
│
├── notebooks/
│   └── eda.ipynb                # Jupyter Notebook for EDA using Pandas + SQL
│
├── snowflake_sql/
│   ├── create_tables.sql        # CREATE TABLE statements
│   ├── insert_data.sql          # COPY INTO or INSERT INTO statements
│   └── queries.sql              # Frequently used SQL queries for analysis
│
├── scripts/
│   ├── db_connect.py            # Snowflake connection code
│   ├── load_to_snowflake.py     # Upload local CSVs to Snowflake tables
│   ├── fetch_from_snowflake.py  # Run SQL & load data to Pandas
│   └── clean_and_merge.py       # Merge & clean raw data (optional CSV export)
│
├── dashboard/
│   └── powerbi.pbix             # Power BI file with dashboard visuals
│
├── .env                         # (Optional) For storing Snowflake credentials securely
├── requirements.txt             # Python dependencies
├── README.md                    # Project description, setup, screenshots
└── .gitignore                   # Ignore data/.env/.ipynb_checkpoints etc.
