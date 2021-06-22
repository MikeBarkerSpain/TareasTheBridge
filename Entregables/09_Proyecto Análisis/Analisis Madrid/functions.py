# Importamos librerías
import requests
from bs4 import BeautifulSoup
import pandas as pd
import html
import numpy as np
import lxml

def create_df():
    Locales_MAD = pd.read_csv('OPEN DATA Locales-Epigrafes202104.csv', sep=';')