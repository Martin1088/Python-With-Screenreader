import pandas as pd
from sklearn import tree

pd.set_option("display.max_rows", 200)

df = pd.read_csv("bewerber.csv", delimiter=";", decimal=",")
target = df["Performance"]
## drop noch hinzufügen
df = df.drop(columns=["Performance"])
df = df.drop(columns=["Geschlecht", "PersonalNr", "Alter", "Ehestand", "Attrition"])
# Anpassen der Werte
df.Reisetaetigkeit = df.Reisetaetigkeit.map({"Nie": 0, "Selten": 50, "Haeufig": 100})
df.Abteilung = df.Abteilung.map({"Entwicklung": 1, "Vertrieb": 2, "Personal": 3})
df.Position = df.Position.map(
    {
        "Vertreib": 1,
        "Wissenschaftler": 2,
        "Abteilungsleiter": 3,
        "Labortechniker": 4,
        "Manager": 5,
        "Produktmanager": 6,
        "AbteilungsleiterForschung": 7,
    }
)
df.ueberstunden = df.ueberstunden.map({"No": 0, "Yes": 1})

# print(df["Position"])
model = tree.DecisionTreeClassifier(random_state=0)
data = df.to_numpy()
model.fit(data, target)
print(tree.export_text(model))
