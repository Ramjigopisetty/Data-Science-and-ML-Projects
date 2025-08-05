import pandas as pd

# Load the raw task dataset
df = pd.read_csv("tasks.csv")

# Drop empty rows and duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("tasks_cleaned.csv", index=False)

print("✅ Cleaned data saved as tasks_cleaned.csv")