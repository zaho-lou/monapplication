import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pyarrow.lib as _lib
import pyarrow as pa


# Importer les données à partir du fichier CSV
data = pd.read_csv("ts_brutt.csv")

# Convertir la date en format de date
data['date'] = pd.to_datetime(data['date'], format='%m%Y')

# Créer une figure avec plusieurs sous-graphes pour chaque ID client
fig, ax = plt.subplots(nrows=len(data['id_client'].unique()), figsize=(10, 8), sharex=True)

# Parcourir chaque sous-ensemble de données pour chaque ID client
for i, (id_client, subset) in enumerate(data.groupby('id_client')):
    # Tracer la consommation en fonction de la date pour chaque ID client
    ax[i].plot(subset['date'], subset['consommation'])
    ax[i].set_title(f"ID client {id_client}")
    ax[i].set_xlabel("Date")
    ax[i].set_ylabel("Consommation")

# Ajuster les espacements entre les sous-graphes
fig.tight_layout()

# Afficher la figure dans Streamlit
st.pyplot(fig)
