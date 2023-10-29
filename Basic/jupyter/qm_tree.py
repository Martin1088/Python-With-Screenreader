import pandas as pd
from sklearn import tree

df = pd.read_csv('QM.csv', delimiter=';', decimal=",")
target = df['ergebnis']
## drop noch hinzufügen
df = df.drop(columns=['ergebnis'])

model = tree.DecisionTreeClassifier( random_state=0)
data = df.to_numpy()
model.fit(data, target)
tree.plot_tree(model)
result = model.predict([[ 1, 0.8 ]])
print(result)
