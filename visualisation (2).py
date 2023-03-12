import streamlit as st
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
from pandas import datetime

from pylab import rcParams


# Load the dataset from a CSV
def parser(x):
    return datetime.strptime(x,'%m%Y')
data = pd.read_csv('ts_brutt.csv', sep=";",index_col=1,parse_dates=[1], squeeze=True, date_parser=parser)
data['valeur']=data.valeur.fillna(0)


# Créer une liste de clients uniques
clients = data['client'].unique()

# Créer une application Streamlit
st.title('Visualiser les données  ')
client = st.selectbox('Sélectionnez un client', clients)

# Filtrer les données pour le client sélectionné
data_client = data[data['client'] == client]

# Afficher le graphique
st.subheader('Graphique')
fig, ax =plt.subplots()
plt.plot(data_client.index, data_client['valeur'])
plt.title(client)
plt.xlabel('Date')
plt.ylabel('Valeur')
st.pyplot(fig)

# Afficher la table de données
st.subheader('Tableau de données')
st.write(data_client)
