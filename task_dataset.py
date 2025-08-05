import pandas as pd  

# Sample task data
data = {
    'TaskID': [1, 2, 3, 4, 5],
    'Description': [
        'Fix login bug in website',
        'Write daily sales report',
        'Implement search filter',
        'Design new user interface',
        'Deploy backend API'
    ],
    'Deadline': ['2025-07-20', '2025-07-18', '2025-07-25', '2025-07-22', '2025-07-21'],
    'AssignedTo': ['Ravi', 'Komal', 'Amit', 'Ravi', 'Neha'],
    'Priority': ['High', 'Medium', 'High', 'Low', 'High']
}

# DataFrame bana rahe hain
df = pd.DataFrame(data)

# Save as CSV file
df.to_csv('tasks.csv', index=False)

# Print result
print("✅ Task dataset CSV file ban gayi!")
print(df)