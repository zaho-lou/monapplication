import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("ts_brutt.csv")

# Convertir la colonne "date" en format "mmyyyy" en format "mm-yyyy"
df["date"] = pd.to_datetime(df["date"], format="%m%Y").dt.strftime("%m-%Y")

# Enregistrer le fichier CSV modifié
df.to_csv("votre_fichier_modifie.csv", index=False)
