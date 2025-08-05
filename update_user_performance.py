import pandas as pd
from collections import defaultdict

# Step 1: Read predictions
predictions = pd.read_csv('model_predictions.csv')

# Step 2: Group by AssignedTo and Priority
performance = defaultdict(lambda: {'High': 0, 'Medium': 0, 'Low': 0})

for _, row in predictions.iterrows():
    user = row['AssignedTo']
    priority = row['Priority']
    if pd.notna(user) and priority in performance[user]:
        performance[user][priority] += 1

# Step 3: Convert to DataFrame
performance_data = []

for user, counts in performance.items():
    total = sum(counts.values())
    high_ratio = counts['High'] / total if total else 0
    performance_data.append({
        'Username': user,
        'TotalTasks': total,
        'HighPriorityRatio': round(high_ratio, 2)
    })

df_perf = pd.DataFrame(performance_data)
df_perf.to_csv('user_data.csv', index=False)

print("✅ user_data.csv created successfully!")