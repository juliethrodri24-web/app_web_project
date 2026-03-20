import streamlit as st
import pandas as pd
import plotly.express as px

df_ventas_vehiculos = pd.read_csv('vehicles_us.csv')
hist_button = st.button('contruccion histograma')

if hist_button:  # al hacer clkic el boton
    # escribe un mensaje
    st.write('creacion histograma para la columna de odometro del DF ventas vehiculos')
    # crear un histogramna
    fig = px.histogram(df_ventas_vehiculos, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
# creo nuevo boton que al hacer clic crea un grafico de dispersion
scatter_button = st.button('construir grafico de dispersion ')

if scatter_button:
    st.write(
        'creacxion de grafico de dispersion:  Precio vs. Odometro')
    fig = px.scatter(df_ventas_vehiculos, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)


st.header('Analisis exploratorio de datos de vehiculos')
col1, col2 = st.columns(2)

with col1:
    build_histogram = st.checkbox('construir histograma')
with col2:
    build_scatter = st.checkbox('construir grafico de dispersion')

if build_histogram:
    st.subheader('Distribucion del kilometraje (odometer)')
    # agrego etiquetas mas claras
    fig_hist = px.histogram(df_ventas_vehiculos, x='odometer',
                            title="Frecuencia del kilometraje",
                            labels={'odometer': 'kilometraje'})
    st.plotly_chart(fig_hist, use_container_with=True)

if build_scatter:
    st.subheader('Relacion: Kilometraje vs. Precio')
    # agrego etiquetas mas claras
    fig_scatter = px.scatter(df_ventas_vehiculos, x='odometer', y='price',
                             title="kilometraje frente a precio de venta",
                             labels={'odometer': 'kilometraje', 'price': 'precio($)'})
    st.plotly_chart(fig_scatter, use_container_with=True)
    print(ig_scatter)
