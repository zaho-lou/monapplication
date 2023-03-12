import streamlit as st
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
from pandas import datetime


# Load the dataset from a CSV
def parser(x):
    return datetime.strptime(x,'%m%Y')
data = pd.read_csv('ts_brutt.csv', sep=";",index_col=1,parse_dates=[1], squeeze=True, date_parser=parser)
data['valeur']=data.valeur.fillna(0)

# afficher le graphe de chaque client
for client in data.client.unique():
    client_data = data[data.client == client]
    st.subheader(f"Client {client}")
    st.line_chart(client_data['valeur'])
