# 🛍️ Retail Dashboard with Snowflake, Python EDA, and Power BI

This project showcases a complete **Retail Analytics Pipeline** using:

- 📦 **Sample Superstore dataset**
- 🐍 **Python** for data cleaning and exploratory data analysis (EDA)
- ❄️ **Snowflake** as the cloud data warehouse
- 📊 **Power BI** for interactive business dashboards

---

## 📁 Project Structure

retail-dashboard-snowflake/
│
├── data/
│ ├── raw/ # Original CSV files
│ │ └── sample-super-store.csv
│ ├── processed/ # Cleaned + merged data
│ └── final_cleaned_data.csv
│
├── notebooks/
│ └── eda.ipynb # EDA in Pandas + SQL
│
├── snowflake_sql/
│ ├── create_tables.sql # CREATE TABLE scripts
│ ├── insert_data.sql # Data loading scripts (COPY INTO or INSERT INTO)
│ └── queries.sql # Common SQL queries for analytics
│
├── scripts/
│ ├── db_connect.py # Snowflake DB connection logic
│ ├── load_to_snowflake.py # Load processed data to Snowflake tables
│ └── clean_data.py # Data cleaning + transformation pipeline
│
├── dashboard/
│ └── powerbi.pbix # Power BI dashboard file
│
├── .env # (Optional) Store Snowflake credentials securely
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ✅ Project Pipeline Overview

### 1. 📂 Data Ingestion
- **Source:** `sample-super-store.csv` (stored in `data/raw/`)
- Loaded using Pandas for inspection and basic formatting

### 2. 🧹 Data Cleaning & Processing
- Script: `scripts/clean_data.py`
- Tasks:
  - Removed duplicates and nulls
  - Converted date columns to datetime
  - Exported cleaned data to `data/processed/final_cleaned_data.csv`

### 3. 📈 Exploratory Data Analysis (EDA)
- Notebook: `notebooks/eda.ipynb`
- Performed:
  - Sales trends and seasonal analysis
  - Profitability by category and region
  - Impact of discount on profit
  - Visualized outliers and trends

### 4. ❄️ Load Data into Snowflake
- Tables created via `snowflake_sql/create_tables.sql`
- Data uploaded using:
  - `scripts/load_to_snowflake.py`
  - `snowflake_sql/insert_data.sql`
- Common query patterns are stored in `queries.sql`

### 5. 📊 Power BI Dashboard
- File: `dashboard/powerbi.pbix`
- Connected to Snowflake (DirectQuery or Import)
- Includes visuals:
  - KPIs: Total Sales, Profit, Orders
  - Time-series trends
  - Sales by Category, Sub-Category, Region
  - Geographic view of State-wise performance
  - Interactive filters and slicers

---

## 🛠️ Tech Stack

| Component    | Tool/Library       |
|--------------|--------------------|
| Data Source  | Superstore CSV     |
| Language     | Python 3.x         |
| Libraries    | Pandas, Snowflake Connector, SQLAlchemy |
| Warehouse    | Snowflake Cloud DW |
| BI Tool      | Power BI Desktop   |

---

## ⚙️ Setup Instructions

### 🔧 Environment Setup

```bash
# Clone the r epository
git clone https://github.com/yourusername/retail-dashboard-snowflake.git
cd retail-dashboard-snowflake

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt 
