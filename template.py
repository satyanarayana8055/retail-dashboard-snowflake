import os
from pathlib import Path

# Retail dashboard folder structure
project_structure = {
    "data/raw": ["sales.csv", "stores.csv", "products.csv", "calendar.csv"],
    "data/processed": ["final_cleaned_data.csv"],
    "data/exports": [],
    "notebooks": ["eda.ipynb"],
    "snowflake_sql": ["create_tables.sql", "insert_data.sql", "queries.sql"],
    "scripts": [
        "db_connect.py",
        "load_to_snowflake.py",
        "fetch_from_snowflake.py",
        "clean_and_merge.py"
    ],
    "dashboard": ["powerbi.pbix"],
    ".": [
        ".env",
        ".gitignore",
        "README.md",
        "requirements.txt"
    ],
}


def create_folders(base_path, structure):
    print("📁 Creating folders...")
    for folder in structure:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"✅ Folder created: {folder_path}")


def create_files(base_path, structure):
    print("\n📄 Creating files...")
    for folder, files in structure.items():
        for file in files:
            file_path = os.path.join(base_path, folder, file)
            file_dir = os.path.dirname(file_path)
            os.makedirs(file_dir, exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    if not file.endswith(".csv") and not file.endswith(".pbix"):
                        f.write(f"# {file}")
                print(f"✅ File created: {file_path}")


def create_project_structure():
    base_path = Path(__file__).resolve().parent
    create_folders(base_path, project_structure)
    create_files(base_path, project_structure)
    print(f"\n🚀 Retail Dashboard Project structure created at:\n   {base_path}")


if __name__ == "__main__":
    create_project_structure()
