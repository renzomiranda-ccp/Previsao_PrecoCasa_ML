import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:/Users/renzo/OneDrive/Documentos/Dados-Python/PrevisaoPrecoCasa/casas.csv')

x = df[["area", "quartos", "banheiros"]]
y = df[["preco"]]

modelo = LinearRegression()
modelo.fit(x,y)

st.markdown("<h1 style='text-align: center; color: black;'>Projeto ML </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Prevendo valor de casas </h2>", unsafe_allow_html=True)
st.divider()

area = st.number_input("Digite a área da casa: ", min_value=0)
quartos = st.number_input("Digite o número de quartos: ", min_value=0)
banheiros = st.number_input("Digite o número de banheiros: ", min_value=0)

if area and quartos and banheiros:
    preco_previsto = modelo.predict([[area, quartos, banheiros]])[0][0]
    st.write(f"O valor da casa com área de {area:.0f}m², {quartos:.0f} quartos e {banheiros:.0f} banheiros é de R${preco_previsto:.0f}.")
    st.balloons()