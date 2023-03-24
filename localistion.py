import streamlit as st
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
from pandas import datetime
import folium
from streamlit_folium import folium_static

# Chargement des données des clients
def parser(x):
    return datetime.strptime(x,'%m%Y')
data = pd.read_csv('/Users/ACER/Desktop/ts_bruttt22.csv', sep=";",index_col=1,parse_dates=[1], squeeze=True, date_parser=parser, encoding='ISO-8859-1')
data['valeur']=data.valeur.fillna(0)


# Création de la carte centrée sur l'Algérie
m = folium.Map(location=[36.7602, 5.0554], zoom_start=10)


# Demander à l'utilisateur d'entrer l'ID du client
client_id = st.number_input('Entrez l\'ID du client :', min_value=1, max_value=data['client_id'].max(), step=1)

# Obtenir les informations du client correspondant à l'ID entré
client_info = data.loc[data['client_id'] == client_id]

# Vérifier si le client a été trouvé
if len(client_info) == 0:
    st.write('Client introuvable.')
else:
    # Afficher les informations du client
    st.write('Nom du client :', client_info['name'].values[0])
    st.write('Adresse :', client_info['City'].values[0])

    # Obtenir la latitude et la longitude de l'adresse du client
    latitude = client_info['Latitude'].values[0]
    longitude = client_info['Longitude'].values[0]

    # Afficher la carte avec la position du client
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker(location=[latitude, longitude], popup=client_info['name'].values[0]).add_to(m)
    folium_static(m)




