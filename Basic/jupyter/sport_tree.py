import pandas as pd
from sklearn import tree

df = pd.read_csv("Sport.csv", delimiter=",")
target = df["Entscheidung"]
df = df.drop(columns="Entscheidung")
df = df.drop(columns="Tag")
print(df)
df.Wind = df.Wind.map({"schwach": 0, "stark": 1})
df.Luftfeuchte = df.Luftfeuchte.map({"normal": 0, "hoch": 1})
df.Aussicht = df.Aussicht.map({"sonnig": 1, "bedeckt": 2, "regen": 3})

model = tree.DecisionTreeClassifier(random_state=0)
data = df.to_numpy()
model.fit(data, target)
print(tree.export_text(model))

result = model.predict([[1, 20, 1, 1]])
print(df)
print(result)
