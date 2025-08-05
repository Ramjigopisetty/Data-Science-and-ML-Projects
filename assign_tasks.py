import pandas as pd
from datetime import datetime

# Load CSV files
tasks = pd.read_csv("tasks_cleaned.csv")
users = pd.read_csv("users.csv")

# Strip column names to avoid spacing issues
tasks.columns = tasks.columns.str.strip()
users.columns = users.columns.str.strip()

# Convert Deadline to datetime
tasks["Deadline"] = pd.to_datetime(tasks["Deadline"])

# Fill empty assignments
tasks["AssignedTo"] = tasks["AssignedTo"].fillna("")

# Get only unassigned tasks sorted by deadline
unassigned_tasks = tasks[tasks["AssignedTo"] == ""]
unassigned_tasks = unassigned_tasks.sort_values("Deadline")

# Sort users by current task load (least loaded first)
users = users.sort_values("current_tasks")

# Assign each task
for i, task in unassigned_tasks.iterrows():
    if users.empty:
        break
    assignee = users.iloc[0]["username"]
    tasks.at[i, "AssignedTo"] = assignee
    users.at[users.index[0], "current_tasks"] += 1
    users = users.sort_values("current_tasks")

# Save updated tasks
tasks.to_csv("tasks_cleaned.csv", index=False)
print("✅ Tasks assigned successfully!")