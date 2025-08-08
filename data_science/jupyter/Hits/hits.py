import pandas as pd

df = pd.read_csv("500hits.csv", encoding="latin-1")
df = df.drop(columns=["PLAYER", "CS"])
print(df.head())
