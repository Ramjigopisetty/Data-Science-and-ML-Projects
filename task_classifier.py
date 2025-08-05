import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Step 1: Load the cleaned task data
df = pd.read_csv("tasks_cleaned.csv")

# Step 2: Prepare features and labels
X = df["Description"]
y = df["Priority"]

# Step 3: Text Vectorization using TF-IDF
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Step 5: Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Predict Priority for all tasks
X_all = vectorizer.transform(df["Description"])
df["PredictedPriority"] = model.predict(X_all)

# Step 7: Save predictions
df[["TaskID", "Description", "Priority", "PredictedPriority"]].to_csv("model_predictions.csv", index=False)

print("✅ Model predictions saved to model_predictions.csv")