import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("tasks_cleaned.csv")

# Title
st.title("📊 User Performance Dashboard")

# Task count per user
st.subheader("👤 Total Tasks Assigned to Each User")
user_counts = df['AssignedTo'].value_counts()
st.bar_chart(user_counts)

# Priority distribution per user
st.subheader("🔺 Task Priority Distribution per User")
users = df['AssignedTo'].unique()
for user in users:
    user_data = df[df['AssignedTo'] == user]
    priority_counts = user_data['Priority'].value_counts()
    st.write(f"*{user}*")
    st.bar_chart(priority_counts)

# Deadline tracking
st.subheader("⏳ Upcoming Deadlines")
df['Deadline'] = pd.to_datetime(df['Deadline'])
upcoming = df[df['Deadline'] >= pd.Timestamp.now()]
st.dataframe(upcoming.sort_values(by='Deadline'))

# Pie chart of overall priorities
st.subheader("📈 Overall Task Priority Breakdown")
priority_counts = df['Priority'].value_counts()
fig, ax = plt.subplots()
ax.pie(priority_counts, labels=priority_counts.index, autopct='%1.1f%%')
ax.axis("equal")
st.pyplot(fig)