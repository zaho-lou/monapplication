import pandas as pd
import folium
import streamlit as st

# Charger les données à partir du fichier CSV
df = pd.read_csv('ts_brutt.csv')

# Convertir la colonne "date" en format date
df['date'] = pd.to_datetime(df['date'], format='%m%Y')

# Créer une carte centrée
m = folium.Map(location=[46.7111, 1.7191], zoom_start=5)

# Ajouter des marqueurs pour chaque client
for index, row in df.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    nom = row['id_client']
    folium.Marker(location=[lat , lon], popup=nom).add_to(m)

# Afficher la carte
st.markdown('<h1>Situation géographique des clients</h1>', unsafe_allow_html=True)
st.write(m)
