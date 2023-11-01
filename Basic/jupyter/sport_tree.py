import pandas as pd
from sklearn import tree

df = pd.read_csv('Sport.csv', delimiter=',')
target = df['Entscheidung']
df = df.drop(columns='Entscheidung')
df = df.drop(columns='Tag')
df = df.drop(columns='Aussicht')
df.Wind = df.Wind.map({'schwach': 1, 'stark': 2})
df.Luftfeuchte = df.Luftfeuchte.map({'normal': 1, 'hoch': 2 })

model = tree.DecisionTreeClassifier( random_state=0)
data = df.to_numpy()
model.fit(data, target)
print(tree.export_text(model))

result = model.predict([[20, 1, 1]])
print(df)
print(result)


