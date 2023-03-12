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


# importer le fichier csv
def parser(x):
    return datetime.strptime(x,'%m%Y')
data = pd.read_csv('ts_brutt.csv', sep=";",index_col=1,parse_dates=[1], squeeze=True, date_parser=parser)
data['valeur']=data.valeur.fillna(0)

# afficher le tableau de chaque client
for client in data.client.unique():
    client_data = data[data.client == client]
    st.subheader(f"Client {client}")
    st.dataframe(client_data)
