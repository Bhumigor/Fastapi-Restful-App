import pandas as pd
from sqlalchemy import create_engine, MetaData, select
from config.db import conn  # Use existing database connection
from models.index import users  # Import the users table from user.py

# CSV File Path
CSV_FILE = "data.csv"

def import_csv_to_db():
    """Reads data from CSV file and inserts it into the MySQL database only if empty."""
    try:
        # Check if table is empty
        result = conn.execute(select(users)).fetchone()
        if result:
            print("Database already has data. Skipping CSV import.")
            return

        df = pd.read_csv(CSV_FILE)
        for _, row in df.iterrows():
            conn.execute(users.insert().values(
                id=row['id'],
                name=row['name'],
                email=row['email'],
                password=row['password']
            ))
        conn.commit()
        print("CSV data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Call function to import data
import_csv_to_db()
