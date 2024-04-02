import streamlit as st
import pandas as pd
import plotly_express as px

car_data= pd.read_csv('C:\Users\lilia\Desktop\Data scientist\Proyecto-5-1\vehicles_us.cvs')
st.header('Exploración de datos de vehículos')
hist_button= st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig= px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button= st.button('Construir grafico de dispersion')
if scatter_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig= px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)





