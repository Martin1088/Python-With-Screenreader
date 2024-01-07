import pandas as pd
from sklearn import tree

df = pd.read_csv("QM.csv", delimiter=";", decimal=",")
target = df["ergebnis"]
## drop noch hinzufügen
df = df.drop(columns=["ergebnis"])

print(df)
model = tree.DecisionTreeClassifier(random_state=0)
data = df.to_numpy()
model.fit(data, target)
print(tree.export_text(model, feature_names=list(df.columns)))
# print(tree.export_graphviz(model))
result = model.predict([[1, 0.8]])
print(result)
