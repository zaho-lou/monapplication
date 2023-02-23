# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd



st.write('''
# Bienvenue 
Hello word 
''')
st.sidebar.header("les parametres")

df = pd.read_excel("lydia18.xlsx")
st.line_chart(df)



