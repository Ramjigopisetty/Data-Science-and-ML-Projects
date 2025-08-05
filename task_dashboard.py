import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and prepare data
df = pd.read_csv("tasks_cleaned.csv")
df.columns = df.columns.str.strip().str.lower()

X = df['description']
y = df['priority']

# Vectorizer and model
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_vectorized, y)

# Streamlit UI
st.title("🧠 AI Task Priority Predictor")

task_input = st.text_area("✍️ Enter Task Description:")

if st.button("Predict Priority"):
    if task_input.strip() == "":
        st.warning("Please enter a task description.")
    else:
        input_vector = vectorizer.transform([task_input])
        prediction = model.predict(input_vector)
        st.success(f"📌 Predicted Priority: *{prediction[0]}**")