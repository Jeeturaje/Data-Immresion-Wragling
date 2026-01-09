import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv("raw_customer_data.csv")

print("Initial Shape:", df.shape)

# Missing values handling
df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean(), inplace=True)

# Convert dates
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Feature Engineering - Customer Age
current_year = datetime.now().year
df['Customer_Age'] = current_year - df['DOB'].dt.year

# Save cleaned data
df.to_csv("cleaned_customer_data.csv", index=False)

print("Final Shape:", df.shape)
print("Data Cleaning Completed Successfully")
