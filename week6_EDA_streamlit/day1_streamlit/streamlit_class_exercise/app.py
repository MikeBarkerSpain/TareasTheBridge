# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os
from utils.stream_config import create_sliders, draw_map
from utils.dataframes import load_normal_csv, get_data_from_df, load_csv_df, load_csv_for_map

path = os.path.dirname(__file__)
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenida", 'Analizador', "Mapa con globos"])

if menu == 'Bienvenida':
    st.title('Welcome to the web app')
    st.write('It is a pleasure having you in the bridge\n\n')
    st.title('Wine Quality Classifier Web App')
    st.write('This is a web app to classify the quality of your wine based on\
            several features that you can see in the sidebar. Please adjust the\
            value of each feature. After that, click on the Predict button at the bottom to\
            see the prediction of the classifier.')

if menu == 'Analizador':
    slider_csv = st.sidebar.file_uploader("Select CSV", type=['csv'])
    # Cargar el dataframe
    if type(slider_csv) != type(None):
        #Añadir filtro por edades y cargar archivo
        filtro_edades = st.sidebar.checkbox('Filtrar edad <10')
        df_slider = load_normal_csv (slider_csv)

        # pintar gráfico en función de la opción seleccionada
        if filtro_edades:
            df_slider = df_slider[df_slider['age'] < 10]
            st.bar_chart(df_slider)
            st.table(df_slider)
        else:
            st.bar_chart(df_slider)
            st.table(df_slider)

if menu == 'Mapa con globos':
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)        # llama a la función que está en stream_config