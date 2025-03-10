import pandas as pd

# Sample data
data = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "password": "pass123"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "password": "secure456"},
    {"id": 3, "name": "Alice Brown", "email": "alice.brown@example.com", "password": "alice789"},
    {"id": 4, "name": "Bob White", "email": "bob.white@example.com", "password": "bobpass321"}
]

# Create and save CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
