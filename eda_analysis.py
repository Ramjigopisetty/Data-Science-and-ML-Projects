import pandas as pd

# Step 1: Load cleaned data
df = pd.read_csv('tasks_cleaned.csv')

# Step 2: Priority count
priority_count = df['Priority'].value_counts()
print("\n📊 Priority Counts:")
print(priority_count)

# Step 3: Task count per person
task_per_person = df['AssignedTo'].value_counts()
print("\n👥 Tasks Assigned To:")
print(task_per_person)

# Step 4: Deadline distribution
deadline_count = df['Deadline'].value_counts().sort_index()
print("\n📅 Deadlines Distribution:")
print(deadline_count)