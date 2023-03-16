import streamlit as st
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
from pandas import datetime
import seaborn as sns

# Load the dataset from a CSV
def parser(x):
    return datetime.strptime(x,'%m%Y')
data = pd.read_csv('/Users/ACER/Desktop/ts_brutt.csv', sep=";",index_col=1,parse_dates=[1], squeeze=True, date_parser=parser)
data['valeur']=data.valeur.fillna(0)

# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard")
st.markdown("##")

# TOP KPI's

left_column,right_column = st.columns(2)
with left_column:
    st.subheader("Total Customers:")
    total_customers = data['client'].nunique()
    st.write("Total Customers:", total_customers)
    st.subheader(f"{total_customers:}")

with right_column:
    st.subheader("Total Consumption:")
    total_cust = data['valeur'].nunique()
    st.write("Total Consumption:", total_cust)
    st.subheader(f"{total_cust:}")

st.markdown("""---""")


# Sidebar for graph selection
st.sidebar.header("Select Graph Type")
graph_type = st.sidebar.selectbox("Choose Graph Type", ["Total Customers", "Line Graph", "Bar Graph"])

# Total Customers
total_customers = data['client'].nunique()

# Monthly Consumption
monthly_consumption = data.groupby('date')['valeur'].sum().reset_index()

# Annual Consumption
annual_consumption = data.groupby('date')['valeur'].sum().reset_index()

# Line graph
if graph_type == "Line Graph":
    st.write("Line Graph")
    fig1, ax1 = plt.subplots()
    sns.lineplot(x='date', y='valeur', data=monthly_consumption, ax=ax1)
    st.pyplot(fig1)

# Bar graph
elif graph_type == "Bar Graph":
    st.write("Bar Graph")
    fig2, ax2 = plt.subplots()
    sns.barplot(x='date', y='valeur', data=annual_consumption, ax=ax2)
    st.pyplot(fig2)

# Total Customers
else:
    st.write("Total Customers:", total_customers)




