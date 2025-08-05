import pandas as pd

df = pd.read_csv('model_predictions.csv')
print("👉 Available columns:")
print(df.columns)