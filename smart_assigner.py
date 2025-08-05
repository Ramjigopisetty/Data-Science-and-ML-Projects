import pandas as pd
import random

def assign_task_smartly():
    task_file = "tasks_cleaned.csv"
    user_file = "user_data.csv"

    # Load the data
    try:
        tasks = pd.read_csv(task_file)
        users = pd.read_csv(user_file)
    except FileNotFoundError:
        print("❌ One or more input files not found.")
        return

    # Filter unassigned tasks
    unassigned_tasks = tasks[tasks['AssignedTo'].isnull() | (tasks['AssignedTo'] == '')]

    # If no unassigned tasks
    if unassigned_tasks.empty:
        print("✅ All tasks are already assigned.")
        return

    # Sort users by BehaviorScore and PendingTasks
    users = users.sort_values(by=['BehaviourScore', 'PendingTasks'], ascending=[False, True])

    user_cycle = users['Username'].tolist()
    user_index = 0

    for idx, row in unassigned_tasks.iterrows():
        assigned_user = user_cycle[user_index % len(user_cycle)]
        tasks.at[idx, 'AssignedTo'] = assigned_user
        users.loc[users['Username'] == assigned_user, 'PendingTasks'] += 1
        user_index += 1

    # Save updated files
    tasks.to_csv(task_file, index=False)
    users.to_csv(user_file, index=False)

    print("✅ Tasks successfully assigned.")