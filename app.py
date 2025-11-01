# LLamar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

#Leer data
df_cars = pd.read_csv('vehicles_us.csv')

#Título de la aplicación
st.header("Anuncios de vehículos en US")

#Crear boton para histograma

hist_button = st.button('Construir Histograma')

if hist_button:
    #Mostrar mensaje
    st.write('Creacion de histograma para el conjunto de datos de anuncios de vehículos en US')
    #Crear histograma
    fig = px.histogram(df_cars, x='price', title='Distribución de Precios de Vehículos en US', labels={'price':'Precio de Vehículos (USD)'})
    #Mostrar histograma
    st.plotly_chart(fig, use_container_width=True)

#Crear boton para gráfico de dispersión

scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    #Mostrar mensaje
    st.write('Creacion de gráfico de dispersión para el conjunto de datos de anuncios de vehículos en US')
    #Crear gráfico de dispersión
    fig2 = px.scatter(df_cars, x='model_year', y='price', labels={'model_year':'Año del Modelo', 'price':'Precio de Vehículos (USD)'}, title='Relación entre Año del Modelo y Precio de Vehículos en US')
    #Mostrar gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)


#Crear casilla de verificación
build_bars = st.checkbox('Mostrar Gráfico de Barras')  
if build_bars:
    #Mostrar mensaje
    st.write('Creacion de gráfico de barras  para el conjunto de datos de anuncios de vehículos en US')
    #Crear grafico de barras
    fig = px.bar(df_cars, x='model', y='price', title='Distribución de Precios de Vehículos en US por modelo', labels={'price':'Precio de Vehículos (USD)', 'model':'Modelo del Vehículo'}, color='model', height=700, width=1500)
    fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_tickangle=-45)
    #Mostrar grafico de barras
    st.plotly_chart(fig, use_container_width=True)




