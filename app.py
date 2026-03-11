import streamlit as st
import pandas as pd
import plotly.express as px

df_ventas_vehiculos = pd.read_csv('vehicles_us.csv')
hist_button = st.button('contruccion histograma')

if hist_button:  # al hacer clkic el boton
    # escribe un mensaje
    st.write('creacion histograma para df ventas vehiculos')
    # crear un histogramna
    fig = px.histoframa(df_ventas_vehiculos, x="odometer")
    # mostrar grafico en plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# creo nuevo boton que al hacer clic crea un grafico de dispersion
# scatter_button = st_button('construir grafico de dispersion')

# if scatter_button:
 #   st.write(
  #      'creacxion de grafico de dispersion para el DF de anuncios de ventas de coches')
   # fig = px.scatter(df_ventas_vehiculos, x='odometer', y='price')
    # st.plotly_chart(fig, use_container_width=True)
