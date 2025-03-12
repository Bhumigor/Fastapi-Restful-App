import pandas as pd
from sqlalchemy.orm import Session
from config.db import SessionLocal  # Use existing database connection
from models.user import User  # Import the users table from user.py
from passlib.context import CryptContext
from utils.security import encode_password, hash_password  # Import encoding function

# Initialize password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# CSV File Path
CSV_FILE = "data.csv"

def import_csv_to_db():
    """Reads data from CSV file and inserts it into the MySQL database only if empty."""
    db: Session = SessionLocal()
    
    try:
        # Check if table is empty
        existing_data = db.query(User).first()
        if existing_data:
            print("Database already has data. Skipping CSV import.")
            return

        df = pd.read_csv(CSV_FILE)
        user_to_insert = []
        for _, row in df.iterrows():
            hashed_password = hash_password(row['password'])  # Hash password
            print(f"Hashed password: {hashed_password}")
            # encoded_password = encode_password(hashed_password)  # Apply encoding

            user_to_insert.append(User(
                id=int(row['id']), 
                name=row['name'], 
                email=row['email'], 
                password=hashed_password  # Store encoded password
            ))
        
        # Bulk insert all users
        db.add_all(user_to_insert)
        db.commit()
        print("CSV data inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error inserting data: {e}")
    
    finally:
        db.close()

# Call function to import data
import_csv_to_db()
