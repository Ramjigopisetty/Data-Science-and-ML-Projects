import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import date
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="AI Task Management", layout="wide", page_icon="📘")

# Custom CSS for animations and styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .animated-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(90deg, #ff512f, #dd2476, #ff512f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 4s infinite linear;
    }
    @keyframes glow {
        0% { background-position: -400px; }
        100% { background-position: 400px; }
    }
    .stButton > button {
        background-color: #0072ff;
        color: white;
        border-radius: 12px;
        padding: 0.5em 1em;
        font-weight: bold;
        box-shadow: 0 4px 14px rgba(0, 114, 255, 0.4);
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #0052cc;
        transform: scale(1.05);
    }
    .block-style {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Animated title
st.markdown("<div class='animated-title'>🧠 AI-Powered Task Management Dashboard</div><br>", unsafe_allow_html=True)



# Load data files
task_file = "tasks_cleaned.csv"
user_file = "user_data.csv"
prediction_file = "model_predictions.csv"

# 🔽 COMBINED CRUD SECTION: ADD / UPDATE / DELETE TASKS

# 🔽 CSS Styling
st.markdown("""
<style>
.expander-header {
    font-weight: bold;
    font-size: 18px;
    color: #0072ff;
}
.stTextInput > div > input,
.stDateInput > div > input,
.stSelectbox > div > div,
.stButton > button {
    border-radius: 10px;
}
.stButton > button {
    background-color: #0072ff;
    color: white;
    font-weight: bold;
    transition: 0.2s ease-in-out;
}
.stButton > button:hover {
    background-color: #0052cc;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# 🔽 Functions
def load_tasks():
    if os.path.exists(task_file):
        return pd.read_csv(task_file)
    return pd.DataFrame(columns=["TaskID", "Description", "Deadline", "AssignedTo", "Priority", "Status"])

def save_tasks(df):
    df.to_csv(task_file, index=False)

# 🔽 EXPANDER 1: ADD NEW TASK
with st.expander("➕ Add New Task", expanded=False):
    st.markdown("<div class='expander-header'>Enter new task details:</div>", unsafe_allow_html=True)
    with st.form("add_task_form"):
        col1, col2 = st.columns(2)

        with col1:
            description = st.text_input("📝 Task Description")
            deadline = st.date_input("📅 Deadline")

        with col2:
            assigned_to = st.text_input("👤 Assigned To")
            priority = st.selectbox("🔥 Priority", ["High", "Medium", "Low"])

        status = st.selectbox("📌 Status", ["Pending", "In Progress", "Completed"])
        submit_add = st.form_submit_button("Add Task")

        if submit_add:
            if description.strip() == "":
                st.warning("⚠️ Description is required.")
            elif deadline < date.today():
                st.warning("⚠️ Deadline cannot be in the past.")
            else:
                tasks = load_tasks()
                next_id = int(tasks["TaskID"].max()) + 1 if not tasks.empty else 1
                new_row = pd.DataFrame([{
                    "TaskID": next_id,
                    "Description": description,
                    "Deadline": str(deadline),
                    "AssignedTo": assigned_to,
                    "Priority": priority,
                    "Status": status
                }])
                tasks = pd.concat([tasks, new_row], ignore_index=True)
                save_tasks(tasks)
                st.success("✅ Task added successfully!")
                st.rerun()

# 🔽 EXPANDER 2: UPDATE TASK STATUS
with st.expander("🔄 Update Task Status", expanded=False):
    st.markdown("<div class='expander-header'>Select a task to update:</div>", unsafe_allow_html=True)
    tasks = load_tasks()
    if not tasks.empty:
        task_options = [f"{row['Description']} (ID: {int(row['TaskID'])})" for _, row in tasks.iterrows()]
        selected = st.selectbox("📋 Select Task", task_options)
        new_status = st.selectbox("🔁 New Status", ["Pending", "In Progress", "Completed"])
        update_btn = st.button("Update Status")

        if update_btn:
            task_id = int(selected.split("(ID:")[1].replace(")", "").strip())
            tasks.loc[tasks["TaskID"] == task_id, "Status"] = new_status
            save_tasks(tasks)
            st.success("✅ Status updated!")
            st.rerun()
    else:
        st.info("ℹ️ No tasks available.")

# 🔽 EXPANDER 3: DELETE TASK
with st.expander("🗑️ Delete Task", expanded=False):
    st.markdown("<div class='expander-header'>Select a task to delete:</div>", unsafe_allow_html=True)
    tasks = load_tasks()
    if not tasks.empty:
        delete_options = [f"{row['Description']} (ID: {int(row['TaskID'])})" for _, row in tasks.iterrows()]
        selected = st.selectbox("🗂️ Choose Task", delete_options, key="delete")
        delete_btn = st.button("Delete Task")

        if delete_btn:
            task_id = int(selected.split("(ID:")[1].replace(")", "").strip())
            tasks = tasks[tasks["TaskID"] != task_id]
            save_tasks(tasks)
            st.success("✅ Task deleted!")
            st.rerun()
    else:
        st.info("ℹ️ No tasks to delete.")



if not os.path.exists(task_file):
    st.error("❌ File 'tasks_cleaned.csv' not found.")
elif not os.path.exists(user_file):
    st.error("❌ File 'user_data.csv' not found.")
elif not os.path.exists(prediction_file):
    st.error("❌ File 'model_predictions.csv' not found.")
else:
    tasks = pd.read_csv(task_file)
    user_data = pd.read_csv(user_file)
    predictions = pd.read_csv(prediction_file)

    # Task Table
    # Task Table (Updated with Priority Sorting)
with st.container():
    st.markdown("<div class='block-style'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Task Assignment Table")

    # 👉 Define desired priority order
    priority_order = pd.CategoricalDtype(['High', 'Medium', 'Low'], ordered=True)

    # 👉 Convert Priority column to categorical with defined order
    tasks['Priority'] = tasks['Priority'].astype(priority_order)

    # 👉 Sort by Priority first, then Deadline
    tasks_sorted = tasks.sort_values(by=['Priority', 'Deadline'])

    # 👉 Display the sorted table
    st.dataframe(tasks_sorted)

    st.markdown("</div>", unsafe_allow_html=True)

    # Priority Pie Chart

    # Prediction Accuracy
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.subheader("Prediction Accuracy")
        if {'Priority', 'PredictedPriority'}.issubset(predictions.columns):
            correct = (predictions['Priority'] == predictions['PredictedPriority']).sum()
            total = len(predictions)
            accuracy = correct / total * 100
            st.success(f"✅ Model Prediction Accuracy: {accuracy:.2f}%")
        else:
            st.warning("⚠️ Required columns 'Priority' and 'PredictedPriority' not found.")
        st.markdown("</div>", unsafe_allow_html=True)
