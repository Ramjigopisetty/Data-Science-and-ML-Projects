import pandas as pd

# Load the tasks data
df = pd.read_csv("tasks_cleaned.csv")

# Check if 'Status' column exists
if 'Status' not in df.columns:
    print("❌ 'Status' column not found in the CSV.")
    exit()

# Group by AssignedTo and Status
performance = df.groupby(['AssignedTo', 'Status']).size().unstack(fill_value=0)

# Show report
print("📈 User Performance Report:\n")
print(performance)