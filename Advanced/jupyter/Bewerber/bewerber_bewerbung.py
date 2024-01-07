import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

pd.set_option("display.max_rows", 2000)

df = pd.read_csv("bewerber.csv", delimiter=";", decimal=",")
target = df["Performance"]
## drop noch hinzufügen
df = df.drop(columns=["Performance"])
df = df.drop(columns=["Geschlecht", "PersonalNr", "Alter", "Ehestand", "Attrition"])
# Anpassen der Werte

# print(df["Position"].unique())
df.Reisetaetigkeit = df.Reisetaetigkeit.map({"Nie": 0, "Selten": 50, "Haeufig": 100})
df.Abteilung = df.Abteilung.map({"Entwicklung": 1, "Vertrieb": 2, "Personal": 3})
df.Position = df.Position.map(
    {
        "Vertrieb": 1,
        "Wissenschaftler": 2,
        "Abteilungsleiter": 3,
        "Labortechniker": 4,
        "Manager": 5,
        "Produktmanager": 6,
        "AbteilungsleiterForschung": 7,
        "Vertriebsmitarbeiter": 8,
        "Personal": 9,
    }
)
df.ueberstunden = df.ueberstunden.map({"No": 0, "Yes": 1})

# print(df["Position"])
# print(df)
# df.to_csv("out.csv", sep=";", encoding="utf-8", na_rep="None")
model = tree.DecisionTreeClassifier(random_state=0)
data = df.to_numpy()
model.fit(data, target)
# print(tree.export_text(model))
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.1)
# Genauigkeit bestimmen
print("score", model.score(x_test, y_test))
# accuracy
y_pred = model.predict(x_test)
print("accurcy :", accuracy_score(y_test, y_pred))
print()
print(confusion_matrix(y_test, y_pred))
