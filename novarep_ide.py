from tkinter import Tk, Label, Button, Entry, filedialog
import configparser
import threading
from methods_to_df import df_main
from graphs import graphs_main
from datetime import datetime
from tests import tests_main
from tkinter import ttk
import pandas as pd
from tkinter import *
import os

# Archivo de configuración
config_file = "config.ini"

# Función para cargar la hoja BET del archivo Excel
def cargar_informe_BET(tests_main):
    ruta_csv = filedialog.askopenfilename(
        filetypes=[("Archivos de Excel", "*.xlsx"), ("Todos los archivos", "*.*")]
    )
    if ruta_csv:
        entry_csv.delete(0, END)
        entry_csv.insert(0, ruta_csv)
        try:
            # Leer únicamente la hoja BET
            df = pd.read_excel(ruta_csv, sheet_name="BET")
            
            # Verificar si la columna "Relative Pressure" existe
            if "Relative Pressure" in df.columns:
                relative_pressure_values = df["Relative Pressure"].dropna().tolist()
                
                # Ajustar las ComboBox con la cantidad máxima de valores disponibles
                combo_absorcion["values"] = list(range(1, len(relative_pressure_values) + 1))
                combo_desorcion["values"] = list(range(1, len(relative_pressure_values) + 1))
                
                label_estado.config(text=f"Datos cargados correctamente. {len(relative_pressure_values)} valores disponibles.")
            else:
                label_estado.config(text="Error: La columna 'Relative Pressure' no existe en la hoja BET.")
        except Exception as e:
            label_estado.config(text=f"Error al cargar el archivo: {str(e)}")

# Función para ejecutar el módulo de tests
def ejecutar_modulo_tests(funcion):
    # Obtener los valores seleccionados en las ComboBox
    try:
        rango_absorcion = int(combo_absorcion.get())  # Convertir a entero
        rango_desorcion = int(combo_desorcion.get())  # Convertir a entero

        # Obtener la ruta del archivo
        ruta_csv = entry_csv.get()
        # Corregir las barras
        ruta_csv = ruta_csv.replace("/", "\\")  # Reemplazar barras normales por barras invertidas
        # Normalizar la ruta del archivo
        ruta_excel = os.path.normpath(ruta_csv)
        ruta_excel = os.path.join(ruta_excel, "Reporte.xlsx")
        # Validar los valores y ejecutar la función
        if ruta_csv:
            print(f"Ejecutando {funcion.__name__} con rutas:")
            print(f"CSV: {ruta_csv}")
            print(f"Rango de Absorción: {rango_absorcion}")
            print(f"Rango de Desorción: {rango_desorcion}")

            ventana.quit()
            ventana.destroy()
            funcion(ruta_csv, rango_absorcion, rango_desorcion,ruta_excel)
        else:
            label_estado.config(text="Error: No se ha cargado ningún archivo.")
    except ValueError:
        label_estado.config(text="Error: Seleccione valores válidos en las ComboBox.")

# Función para cargar el archivo de Excel y crear el DataFrame
def cargar_archivo():

    ruta_csv = entry_csv.get()
    # Construir la ruta del archivo correctamente
    ruta_excel = os.path.join(ruta_csv, "Reporte.xlsx")
    if ruta_csv:
        entry_csv.delete(0, END)
        entry_csv.insert(0, ruta_csv)
        # Leer el archivo de Excel
        df = pd.read_excel(ruta_excel)
        # Llenar las ComboBox con los valores de la columna "Relative Pressure"
        relative_pressure_values = df["Relative Pressure"].tolist()
        combo_absorcion["values"] = relative_pressure_values
        combo_desorcion["values"] = relative_pressure_values
        label_estado.config(text="Archivo cargado correctamente")

def ejecutar_modulo_grafico(funcion):
    """Ejecutar una función pasando las rutas como argumentos."""

    ruta_csv = entry_csv.get()
    # Corregir las barras
    ruta_excel = ruta_csv.replace("/", "\\")  # Reemplazar barras normales por barras invertidas
    # Normalizar la ruta del archivo
    ruta_excel = os.path.normpath(ruta_excel)
    ruta_excel = os.path.join(ruta_excel, "Reporte.xlsx")
    print(f"Ejecutando {funcion.__name__} con rutas:")
    print(f"CSV: {ruta_csv}")
    ventana.quit()
    ventana.destroy()
    funcion(ruta_csv,ruta_excel)

# Función genérica para ejecutar módulos con rutas
def ejecutar_modulo(funcion):
    """Ejecutar una función pasando las rutas como argumentos."""

    ruta_csv = entry_csv.get()
    # Corregir las barras
    ruta_excel = ruta_csv.replace("/", "\\")  # Reemplazar barras normales por barras invertidas
    # Normalizar la ruta del archivo
    ruta_excel = os.path.normpath(ruta_excel)
    ruta_excel = os.path.join(ruta_excel, "Reporte.xlsx")
    ruta_qps = entry_qps.get()
    ruta_csv = entry_csv.get()
    ruta_novawin = entry_novawin.get()
    ruta_pdf = entry_pdf.get()
    print(f"Ejecutando {funcion.__name__} con rutas:")
    print(f"QPS: {ruta_qps}, CSV: {ruta_csv}, NovaWin: {ruta_novawin}, PDF: {ruta_pdf} , EXCELL: {ruta_excel}")
    ventana.quit()
    ventana.destroy()
    funcion(ruta_qps, ruta_csv, ruta_novawin,ruta_excel)

# Función genérica para seleccionar rutas
def seleccionar_ruta(entry, is_file=True):
    """Seleccionar archivo o carpeta y actualizar el Entry correspondiente."""
    try:
        ruta = (
            filedialog.askopenfilename(title="Seleccionar archivo") if is_file
            else filedialog.askdirectory(title="Seleccionar directorio")
        )
        if ruta:
            entry.delete(0, "end")
            entry.insert(0, ruta)
    except Exception as e:
        print(f"Error al seleccionar la ruta: {e}")

def seleccionar_ruta_async(entry, is_file=True):
    """Abrir el diálogo de selección en un hilo separado."""
    threading.Thread(target=seleccionar_ruta, args=(entry, is_file), daemon=True).start()

# Funciones para cargar y guardar configuración
def cargar_configuracion():
    config = configparser.ConfigParser()
    config.read(config_file)
    if "Rutas" in config:
        entry_qps.insert(0, config["Rutas"].get("ruta_qps", ""))
        entry_csv.insert(0, config["Rutas"].get("ruta_csv", ""))
        entry_novawin.insert(0, config["Rutas"].get("ruta_novawin", ""))
        entry_pdf.insert(0, config["Rutas"].get("ruta_pdf", ""))

def guardar_configuracion():
    config = configparser.ConfigParser()
    config["Rutas"] = {
        "ruta_qps": entry_qps.get(),
        "ruta_csv": entry_csv.get(),
        "ruta_novawin": entry_novawin.get(),
        "ruta_pdf": entry_pdf.get()
    }
    with open(config_file, "w") as configfile:
        config.write(configfile)
    print("Rutas guardadas en config.ini")

# Crear ventana principal
ventana = Tk()
ventana.title("Selector de Rutas")
ventana.geometry("1000x700")
ventana.resizable(False, False)

# Etiquetas y campos de entrada
Label(ventana, text="Ruta de archivos .qps:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_qps = Entry(ventana, width=50)
entry_qps.grid(row=0, column=1, padx=10, pady=10)
Button(ventana, text="Seleccionar Archivo", command=lambda: seleccionar_ruta(entry_qps)).grid(row=0, column=2, padx=10, pady=10)

Label(ventana, text="Ruta de directorio CSV:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_csv = Entry(ventana, width=50)
entry_csv.grid(row=1, column=1, padx=10, pady=10)
Button(ventana, text="Seleccionar Carpeta", command=lambda: seleccionar_ruta_async(entry_csv, False)).grid(row=1, column=2, padx=10, pady=10)

Label(ventana, text="Ruta de NovaWin:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_novawin = Entry(ventana, width=50)
entry_novawin.grid(row=2, column=1, padx=10, pady=10)
Button(ventana, text="Seleccionar Archivo", command=lambda: seleccionar_ruta(entry_novawin)).grid(row=2, column=2, padx=10, pady=10)

Label(ventana, text="Ruta para guardar PDFs:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_pdf = Entry(ventana, width=50)
entry_pdf.grid(row=3, column=1, padx=10, pady=10)
Button(ventana, text="Seleccionar Carpeta", command=lambda: seleccionar_ruta_async(entry_pdf, False)).grid(row=3, column=2, padx=10, pady=10)

# Botones para guardar configuración y ejecutar funciones
Button(ventana, text="Guardar Configuración", command=guardar_configuracion).grid(row=4, column=1, pady=10)

Button(ventana, text="Ejecutar Metodos", command=lambda: ejecutar_modulo(df_main)).grid(row=6, column=1, pady=10)

Button(ventana, text="Dibujar", command=lambda: ejecutar_modulo_grafico(graphs_main)(grphs_main)).grid(row=8, column=1, pady=10)

Button(ventana, text="Cargar informe BET", command=lambda: cargar_informe_BET(tests_main)).grid(row=10, column=1, pady=10)

Button(ventana, text="Hacer los tests", command=lambda: ejecutar_modulo_tests(tests_main)).grid(row=12, column=1, pady=10)

# Etiqueta y ComboBox para el Rango de Absorción
Label(ventana, text="Rango de Absorción:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
combo_absorcion = ttk.Combobox(ventana, width=5)
combo_absorcion.grid(row=6, column=0, padx=5, pady=5)

# Etiqueta y ComboBox para el Rango de Desorción
Label(ventana, text="Rango de Desorción:").grid(row=8, column=0, padx=5, pady=5, sticky="w")
combo_desorcion = ttk.Combobox(ventana, width=5)
combo_desorcion.grid(row=10, column=0, padx=5, pady=5)

# Etiqueta de estado
label_estado = Label(ventana, text="", fg="green")
label_estado.grid(row=14, column=0, columnspan=3, pady=5)

# Cargar configuración inicial
cargar_configuracion()

# Iniciar ventana
ventana.mainloop()