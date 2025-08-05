import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and prepare data
df = pd.read_csv("tasks_cleaned.csv")
df.columns = df.columns.str.strip().str.lower()

X = df['description']
y = df['priority']

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_vectorized, y)

# 🔮 Predict priority for a new task
while True:
    new_task = input("\n📝 Enter a task description (or 'exit' to quit): ")

    if new_task.lower() == 'exit':
        break

    new_vector = vectorizer.transform([new_task])
    prediction = model.predict(new_vector)
    print(f"📌 Predicted Priority: {prediction[0]}")