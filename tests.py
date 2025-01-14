#Graficos a partir de los dataframes

import openpyxl
import os
import csv
import traceback
from datetime import datetime
from pywinauto import Application, findwindows
import time
import threading
from novawinmng import manejar_novawin, leer_csv_y_crear_dataframe,agregar_csv_a_plantilla_excel, guardar_dataframe_en_ini,generar_nombre_unico,agregar_dataframe_a_excel_sin_borrar,agregar_dataframe_a_nueva_hoja
from pywinauto.keyboard import send_keys
from openpyxl import Workbook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def BET_BI(df, ruta_excel, Rango_de_Absorpcion, Rango_de_Desorpcion):
    # Normalizar la ruta del archivo
    ruta_excel = os.path.normpath(ruta_excel)
    ruta_excel = os.path.join(ruta_excel, "Report.xlsx")

    # Verificar si las columnas necesarias existen en el DataFrame
    if 'Volume @ STP' not in df.columns or '1 / [ W((P/Po) - 1) ]' not in df.columns:
        print("Las columnas necesarias no están en el DataFrame.")
        return
    try:
        # Convertir Rango_de_Desorpcion a entero y filtrar
        num_filas = int(Rango_de_Desorpcion)
        ultimo_rango_df = df.tail(num_filas)
        print("Últimos elementos filtrados según Rango de Desorción:")
        print(ultimo_rango_df)
    except ValueError:
        print("El valor de Rango_de_Desorpcion no es válido para realizar el filtrado.")
    
    # Filtrar los rangos y mostrar los datos
    filtered_df_a = ultimo_rango_df[
        (ultimo_rango_df['Relative Pressure'] >= 0.45) & (ultimo_rango_df['Relative Pressure'] <= 0.55)
    ]
    print("Filtrado en rango 0.45-0.55:")
    print(filtered_df_a)

    # Calcular el promedio de la columna 'Volume @ STP'
    if not ultimo_rango_df['Volume @ STP'].isnull().all():  # Verificar si la columna no está vacía
        promedio_volume_stp_a = filtered_df_a['Volume @ STP'].mean()
        print(f"Promedio de 'Volume @ STP': {promedio_volume_stp_a}")
    else:
        print("La columna 'Volume @ STP' está vacía o contiene solo valores nulos.")

    filtered_df_b = ultimo_rango_df[
        (ultimo_rango_df['Relative Pressure'] >= 0.6) & (ultimo_rango_df['Relative Pressure'] <= 0.75)
    ]
    print("Filtrado en rango 0.6-0.75:")
    print(filtered_df_b)

    # Calcular el promedio de la columna 'Volume @ STP'
    if not filtered_df_b['Volume @ STP'].isnull().all():  # Verificar si la columna no está vacía
        promedio_volume_stp_b = filtered_df_b['Volume @ STP'].mean()
        print(f"Promedio de 'Volume @ STP': {promedio_volume_stp_b}")
    else:
        print("La columna 'Volume @ STP' está vacía o contiene solo valores nulos.")

    # Dividir los promedios
    div = promedio_volume_stp_a / promedio_volume_stp_b
    print("La división es: " + str(round(div, 2)))  # Convierte el número a cadena y lo redondea

    # Filtrar los últimos N elementos según el valor de Rango_de_Desorpcion
   
        
def BET_P(df):
    # Filtrar las columnas necesarias
    columna_Volume_STP = df['Volume @ STP']
    columna_W_PIPo = df['1 / [ W((P/Po) - 1) ]']
    

def BET_C(df):
    # Filtrar las columnas necesarias
    columna_Volume_STP = df['Volume @ STP']
    columna_W_PIPo = df['1 / [ W((P/Po) - 1) ]']
 #   rango_0_45_0_55 =
  #  rango_0_6_0_75 =

def tests_main(archivo_ruta_completa,Rango_de_Absorpcion,Rango_de_Desorpcion):

    print("Inicio de graphs_main")
    print(archivo_ruta_completa)
        
    # Imprimir o procesar los valores obtenidos
    print(f"Rango de Absorción: {Rango_de_Absorpcion}")
    print(f"Rango de Desorción: {Rango_de_Desorpcion}")
    # Construir la ruta del archivo correctamente
    archivo_planilla = os.path.join(archivo_ruta_completa, "Reporte.xlsx")
       
    # Leer los datos de la hoja 'BET'
    df_bet = pd.read_excel(archivo_planilla, sheet_name='BET')
   
    BET_BI(df_bet,archivo_planilla,Rango_de_Absorpcion,Rango_de_Desorpcion)
    print(df_bet.head())

