import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicle_sales = pd.read_csv('vehicles_us.csv')
hist_button = st.button('histogram construction')

if hist_button:  # al hacer clkic el boton
    # escribe un mensaje
    st.write(
        'Creating a histogram for the odometer column of vehicle sales in Mexico City')
    # crear un histogramna
    fig = px.histogram(df_vehicle_sales, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
# creo nuevo boton que al hacer clic crea un grafico de dispersion
scatter_button = st.button('construct a scatter plot')


if scatter_button:
    st.write(
        'creating a scatter plot:  Price vs. Odometer')
    fig = px.scatter(df_vehicle_sales, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True, theme="streamlit")


st.header('Exploratory analysis of vehicle data')
col1, col2 = st.columns(2)

with col1:
    build_histogram = st.checkbox('construct histogram')
with col2:
    build_scatter = st.checkbox('construct scatter plot')

if build_histogram:
    st.subheader('Mileage distribution (odometer)')
    # agrego etiquetas mas claras
    fig_hist = px.histogram(df_vehicle_sales, x='odometer',
                            title="Mileage frequency",
                            labels={'odometer': 'mileage (km)'})
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.subheader('Relationship: Mileage vs. Price')
    # agrego etiquetas mas claras
    fig_scatter = px.scatter(df_vehicle_sales, x='odometer', y='price',
                             title="mileage versus sale price",
                             labels={'odometer': 'mileage (km)', 'price': 'sale price ($)'})
    st.plotly_chart(fig_scatter, use_container_width=True, theme="streamlit")
