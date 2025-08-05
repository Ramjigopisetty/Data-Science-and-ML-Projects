import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 🔁 Step 1: Load Cleaned Data
df = pd.read_csv("tasks_cleaned.csv")
df.columns = df.columns.str.strip().str.lower()

X = df['description']
y = df['priority']

# 🔠 Step 2: TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 🤖 Step 3: Train Model Again
model = LogisticRegression(class_weight='balanced')
model.fit(X_vectorized, y)

# 📝 Step 4: User Input
new_task = input("📝 Enter a task description: ")

# ✨ Step 5: Transform & Predict
new_vector = vectorizer.transform([new_task])
predicted_priority = model.predict(new_vector)

# 📢 Step 6: Show Output
print(f"\n🚀 Predicted Priority: {predicted_priority[0]}")