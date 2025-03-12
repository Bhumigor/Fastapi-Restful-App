import pandas as pd

# Sample data
data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "password": "Password@123"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "password": "Password@123"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "password": "Password@123"},
    {"id": 4, "name": "David", "email": "david@example.com", "password": "Password@123"},
    {"id": 5, "name": "Eve", "email": "eve@gmail.com", "password": "Password@123"},
]

# Create and save CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
