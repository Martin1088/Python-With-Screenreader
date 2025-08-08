import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

pd.set_option("display.max_rows", 2000)

df = pd.read_csv("bewerber_next.csv", delimiter=";", decimal=",")
target = df["Performance"]
## drop noch hinzufügen
df = df.drop(columns=["Performance"])
df = df.drop(columns=["Geschlecht", "PersonalNr", "Alter", "Ehestand", "Attrition"])
df = df.drop(columns=["ProzentGehaltserhoehung", "AktienOptionen"])
# Anpassen der Werte

# print(df["Position"].unique())
df.Reisetaetigkeit = df.Reisetaetigkeit.map({"Nie": 0, "Selten": 50, "Haeufig": 100})

df["ist_Vertrieb"] = (df["Abteilung"] == "Vertrieb").astype(int)
df["ist_Entwicklung"] = (df["Abteilung"] == "Entwicklung").astype(int)
df["ist_Personal"] = (df["Abteilung"] == "Personal").astype(int)
"""
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
"""
df["ist_Personal"] = (df["Position"] == "Personal").astype(int)
df["ist_Vertriebsmitarbeiter"] = (df["Position"] == "Vertriebsmitarbeiter").astype(int)
df["ist_AbteilungsleiterForschung"] = (
    df["Position"] == "AbteilungsleiterForschung"
).astype(int)
df["ist_Produktmanager"] = (df["Position"] == "Produktmanager").astype(int)

df["ist_Manager"] = (df["Position"] == "Manager").astype(int)
df["ist_Labortechniker"] = (df["Position"] == "Labortechniker").astype(int)
df["ist_Abteilungsleiter"] = (df["Position"] == "Abteilungsleiter").astype(int)
df["ist_Wissenschaftler"] = (df["Position"] == "Wissenschaftler").astype(int)
df["ist_Vertrieb"] = (df["Position"] == "Vertrieb").astype(int)

df.ueberstunden = df.ueberstunden.map({"No": 0, "Yes": 1})
##
df = df.drop(columns=["Position", "Abteilung"])
# print(df["Position"])
print(df)
df.to_csv("out_next.csv", sep=";", encoding="utf-8", na_rep="None")
model = tree.DecisionTreeClassifier(random_state=0)
data = df.to_numpy()
model.fit(data, target)
print(tree.export_text(model, feature_names=list(df.columns)))
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.1)
# Genauigkeit bestimmen
model.fit(x_train, y_train)
print("score", model.score(x_test, y_test))
# accuracy
y_pred = model.predict(x_test)
print("accurcy :", accuracy_score(y_test, y_pred))
print()
print(confusion_matrix(y_test, y_pred))
