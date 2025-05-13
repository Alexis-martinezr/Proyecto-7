import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Analisis Exploratorio de Datos de Vehiculos')

car_data = pd.read_csv('C:/Users\HP/Desktop/Proyecto-7/notebooks/vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creacion de histograma de precios')
    fig = px.histogram(car_data, x='price', nbins=50, title='Distribución de precios')
    st.plotly_chart(fig, use_container_width=True)

graf_button = st.button('Construir grafico de barras')
if graf_button:
    st.write('Creacion de grafico de barras')
    mean_prices = car_data.groupby('model')['price'].mean().reset_index().sort_values('price', ascending=False).head(10)
    figb= px.bar(mean_prices, x='model', y='price', title='Top 10 modelos con mayor precio promedio')
    st.plotly_chart(figb, use_contaider_width=True)

disp_button = st.button('Construir grafico de dispersion')
if disp_button:
    st.write('Creacion de graficos de dispersion')
    figd = px.scatter(car_data, x='odometer', y='price', color='condition', title='Precio vs Odómetro')
    st.plotly_chart(figd, use_container_width_=True)