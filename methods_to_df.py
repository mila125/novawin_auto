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

def hilo_exportar_HK(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_HK(main_window, path_csv, app)
def exportar_reporte_HK(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
       # main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
          #  graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")

        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        HK_method_menu_item = app.window(best_match="Tables").child_window(title="HK method", control_type="MenuItem")
        HK_method_menu_item.click_input()
        print("Submenú 'HK method' seleccionado.")

        HK_method_menu_item = app.window(best_match="HK method")
      #  HK_method_menu_item.print_control_identifiers(depth=2)
        Pore_Size_Distribution_menu_item = HK_method_menu_item.child_window(title=" Pore Size Distribution", control_type="MenuItem")
        Pore_Size_Distribution_menu_item.click_input()
        print("Se seleccionó ' Pore Size Distribution' exitosamente.")

        time.sleep(1)
        secondary_window2 = app.window(title_re=f".*tab:Pore Size Distribution: file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(1)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"hk.csv")

         # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(1)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)
       

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
            # Obtener ruta relativa
            ruta_relativa = os.path.relpath(ruta_exportacion, start=os.getcwd())
            print(f"Archivo exportado correctamente en: {ruta_relativa}")
            # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
              return ruta_relativa
        else:
            raise Exception("Botón 'Guardar' no encontrado.")

    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()
def hilo_exportar_DFT(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_DFT(main_window, path_csv, app)
def exportar_reporte_DFT(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
       # main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
           # graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")

        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        bet_menu_item = app.window(best_match="Tables").child_window(title="DFT method", control_type="MenuItem")
        bet_menu_item.click_input()
        print("Submenú 'DFT method' seleccionado.")

        bet_menu_item = app.window(best_match="DFT method")
     #   bet_menu_item.print_control_identifiers(depth=2)
        single_point_menu_item = bet_menu_item.child_window(title=" Pore Size Distribution", control_type="MenuItem")
        single_point_menu_item.click_input()
        print("Se seleccionó ' Pore Size Distribution' exitosamente.")

        time.sleep(1)
        secondary_window2 = app.window(title_re=f".*tab: Pore Size Distribution: file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(1)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"dft.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(1)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()
def hilo_exportar_BJHA(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_BJHA(main_window, path_csv, app)
def exportar_reporte_BJHA(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
       # main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
            #graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")
       
        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        BJHA_menu_item = app.window(best_match="Tables").child_window(title="BJH Pore Size Distribution", control_type="MenuItem")
        BJHA_menu_item.click_input()
        print("Submenú 'BJH Pore Size Distribution' seleccionado.")

        BJHA_menu_item = app.window(best_match="BJH Pore Size Distribution")
        BJHA_menu_item.print_control_identifiers(depth=2)
        Adsorption_menu_item = BJHA_menu_item.child_window(title=" Adsorption ", control_type="MenuItem")
        Adsorption_menu_item.click_input()
        print("Se seleccionó ' Adsorption ' exitosamente.")

        time.sleep(2)
        secondary_window2 = app.window(title_re=f".*tab: Adsorption: file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(2)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"bjha.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(2)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()

def hilo_exportar_BJHD(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_BJHD(main_window, path_csv, app)

def exportar_reporte_BJHD(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
     #   main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
           # graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")
       
        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        BJHD_menu_item = app.window(best_match="Tables").child_window(title="BJH Pore Size Distribution", control_type="MenuItem")
        BJHD_menu_item.click_input()
        print("Submenú 'BJH Pore Size Distribution' seleccionado.")

        BJHD_menu_item = app.window(best_match="BJH Pore Size Distribution")
        BJHD_menu_item.print_control_identifiers(depth=2)
        Desorption_menu_item = BJHD_menu_item.child_window(title=" Desorption ", control_type="MenuItem")
        Desorption_menu_item.click_input()
        print("Se seleccionó ' Desorption' exitosamente.")

        time.sleep(2)
        secondary_window2 = app.window(title_re=f".*tab: Desorption: file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(2)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"bjhd.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(2)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)


        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()

def hilo_exportar_FFHA(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_FFHA(main_window, path_csv, app)

def exportar_reporte_FFHA(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
      #  main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
           # graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")
       
        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        Fractal_Dimension_Methods_menu_item = app.window(best_match="Tables").child_window(title="Fractal Dimension Methods", control_type="MenuItem")
        Fractal_Dimension_Methods_menu_item.click_input()
        print("Submenú 'Fractal Dimension Methods' seleccionado.")

        BJHD_menu_item = app.window(best_match="Fractal Dimension Methods")
      #  BJHD_menu_item.print_control_identifiers(depth=2)
        Adsorption_menu_item = BJHD_menu_item.child_window(title="FHH Method Fractal Dimension(Adsorption )", control_type="MenuItem")
        Adsorption_menu_item.click_input()
        print("Se seleccionó FHH Method Fractal Dimension(Adsorption )' exitosamente.")

        time.sleep(2)
        secondary_window2 = app.window(title_re=f".*tab: FHH Method Fractal Dimension(Adsorption ): file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(2)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"ffha.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(2)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()

def hilo_exportar_NKA(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_NKA(main_window, path_csv, app)

def exportar_reporte_NKA(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
      #  main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
          #  graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")
       
        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        Fractal_Dimension_Methods_menu_item = app.window(best_match="Tables").child_window(title="Fractal Dimension Methods", control_type="MenuItem")
        Fractal_Dimension_Methods_menu_item.click_input()
        print("Submenú 'Fractal Dimension Methods' seleccionado.")

        BJHD_menu_item = app.window(best_match="Fractal Dimension Methods")
      #  BJHD_menu_item.print_control_identifiers(depth=2)
        Adsorption_menu_item = BJHD_menu_item.child_window(title="NK Method Fractal Dimension(Adsorption )", control_type="MenuItem")
        Adsorption_menu_item.click_input()
        print("Se seleccionó NK Method Fractal Dimension(Adsorption )' exitosamente.")

        time.sleep(2)
        secondary_window2 = app.window(title_re=f".*tab: NK Method Fractal Dimension(Adsorption ): file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(2)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"nka.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(2)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()
        
def hilo_exportar_BET(main_window, path_csv, app):
    # Aquí va la lógica para exportar el reporte
    exportar_reporte_BET(main_window, path_csv, app)        
def exportar_reporte_BET(main_window, ruta_exportacion, app):
    try:
        # Imprimir detalles de los controles y ventanas hijas de main_window
        all_controls = main_window.children()
      #  main_window.print_control_identifiers()

        # Buscar el control por su clase
        graph_view_window = main_window.child_window(class_name="TGraphViewWindow")

        if graph_view_window.exists():
            print("Componente 'TGraphViewWindow' encontrado.")
         #   graph_view_window.print_control_identifiers()
            graph_view_window.right_click_input()
            time.sleep(1)
        else:
            print("No se encontró el componente 'TGraphViewWindow'.")

        context_menu = app.window(title_re=".*Context.*")
        tables_menu_item = context_menu.child_window(title="Tables", control_type="MenuItem")
        tables_menu_item.click_input()
        print("Menú 'Tables' seleccionado.")

        bet_menu_item = app.window(best_match="Tables").child_window(title="BET", control_type="MenuItem")
        bet_menu_item.click_input()
        print("Submenú 'BET' seleccionado.")

        bet_menu_item = app.window(best_match="BET")
     #   bet_menu_item.print_control_identifiers(depth=2)
        single_point_menu_item = bet_menu_item.child_window(title="Single Point Surface Area", control_type="MenuItem")
        single_point_menu_item.click_input()
        print("Se seleccionó 'Single Point Surface Area' exitosamente.")

        time.sleep(2)
        secondary_window2 = app.window(title_re=f".*tab:Single Point Surface Area: file_to_open_nameonly.*")
        main_window.right_click_input()
        time.sleep(1)

        savecsv_menu_item = context_menu.child_window(title="Export to .CSV", control_type="MenuItem")
        savecsv_menu_item.click_input()
        print("Se seleccionó 'Export to .CSV' exitosamente.")

        time.sleep(2)
        csv_dialog = app.window(class_name="#32770")

        print("llegó hasta aquí")
        ruta_exportacion = generar_nombre_unico(ruta_exportacion,"bet.csv")
        # Enfocar el cuadro de texto con Alt + M
        send_keys('%m')  # % representa la tecla Alt en pywinauto
        time.sleep(2)
        send_keys(ruta_exportacion)  # % representa la tecla Alt en pywinauto
        # Esperar hasta que el cuadro de texto esté enfocado
        edit_box = csv_dialog.child_window(control_type="Edit", found_index=0)

        csv_button = csv_dialog.child_window(control_type="Button", title="Guardar") \
            if csv_dialog.child_window(control_type="Button", title="Guardar").exists() \
            else csv_dialog.child_window(control_type="Button", title="Save")
        
        if csv_button.exists():
            print("Existe el botón")
            csv_button.click_input()
            print("Archivo exportado exitosamente.")
                        # Conecta con el proceso de NovaWin
            try:
              app = Application(backend='uia').connect(title_re='.*NovaWin.*', process=2000)
              window = app.window(title_re='.*NovaWin.*')

              # Cerrar la ventana
              window.close()
              print("Ventana cerrada exitosamente.")
            except Exception as e:
              print(f"Error al cerrar la ventana: {e}")
            return ruta_exportacion
        else:
            raise Exception("Botón 'Guardar' no encontrado.")


    except Exception as e:
        print(f"Error durante la exportación: {e}")
        traceback.print_exc()        

def hilo_leer_csv_y_crear_dataframe(ruta_csv, resultado_dict):
    try:
        resultado_dict['dataframe'] = leer_csv_y_crear_dataframe(ruta_csv)
    except Exception as e:
        resultado_dict['error'] = f"Error al leer CSV: {e}"

# Función para agregar el CSV al Excel en un hilo
def hilo_agregar_csv_a_plantilla_excel(ruta_csv, ruta_excel, resultado_dict):
    try:
        agregar_csv_a_plantilla_excel(ruta_csv, ruta_excel)
        resultado_dict['agregado'] = True
    except Exception as e:
        resultado_dict['error'] = f"Error al agregar datos del CSV a Excel: {e}"

# Función para guardar el DataFrame en un archivo INI en un hilo
def hilo_guardar_dataframe_en_ini(df, archivo_ini, resultado_dict):
    try:
        guardar_dataframe_en_ini(df, archivo_ini)
        resultado_dict['guardado'] = True
    except Exception as e:
        resultado_dict['error'] = f"Error al guardar INI: {e}"
        
def df_main(path_qps, path_csv, path_novawin):
    
    resultado_dict = {}
    ruta_excel=path_csv
  
    print("Inicio de df_main")
    
    print(ruta_excel)
    
    # Construir la ruta del archivo correctamente
    archivo_planilla = os.path.join(ruta_excel, "Reporte.xlsx")

    # Imprimir la ruta completa
    print(archivo_planilla)
    # Si el archivo ya existe, eliminarlo
    if os.path.exists(archivo_planilla):
      os.remove(archivo_planilla)
      print(f"Archivo '{archivo_planilla}' eliminado.")

    # Crear un nuevo archivo Excel
    wb = Workbook()
    hoja = wb.active
    hoja.title = "Leeme"
    hoja["A1"] = "Datos de analisis hecho en NovaWin"  # Agregar un título en la celda A1

    # Guardar el archivo_planilla
    wb.save(archivo_planilla)
    print(f"Archivo '{archivo_planilla}' creado nuevamente.")
    try:
        # Inicializar y manejar NovaWin
        app, main_window = manejar_novawin(path_novawin, path_qps)

        # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_HK = exportar_reporte_HK(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_HK}")

        # Mostrar el archivo exportado
        if ruta_csv_HK:
            print(f"Archivo exportado exitosamente: {ruta_csv_HK}")
        else:
            print("No se exportó ningún archivo.")
        hilo_exportacion_HK = threading.Thread(target=hilo_exportar_HK, args=(main_window, path_csv, app))
        hilo_exportacion_HK.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_HK.join()
        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_HK)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_HK = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_HK, resultado_dict))
        hilo_leer_csv_HK.start()
        hilo_leer_csv_HK.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "HK", dataframe)
        
        # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_DFT = exportar_reporte_DFT(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_DFT}")


        # Mostrar el archivo exportado
        if ruta_csv_DFT:
            print(f"Archivo exportado exitosamente: {ruta_csv_DFT}")
        else:
            print("No se exportó ningún archivo.")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_DFT = threading.Thread(target=hilo_exportar_DFT, args=(main_window, path_csv, app))
        hilo_exportacion_DFT.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_DFT.join()
        # Crear DataFrame y guardar
        
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_DFT)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_DFT = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_DFT, resultado_dict))
        hilo_leer_csv_DFT.start()
        hilo_leer_csv_DFT.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "DFT", dataframe)
        
        # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_BJHD = exportar_reporte_BJHD(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_BJHD}")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_BJHD = threading.Thread(target=hilo_exportar_BJHD, args=(main_window, path_csv, app))
        hilo_exportacion_BJHD.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_BJHD.join()
        # Mostrar el archivo exportado
        if ruta_csv_BJHD:
            print(f"Archivo exportado exitosamente: {ruta_csv_BJHD}")
        else:
            print("No se exportó ningún archivo.")

        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_BJHD)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_BJHD = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_BJHD, resultado_dict))
        hilo_leer_csv_BJHD.start()
        hilo_leer_csv_BJHD.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "BJHD", dataframe)
        
        # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_BJHA = exportar_reporte_BJHA(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_BJHA}")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_BJHA = threading.Thread(target=hilo_exportar_BJHA, args=(main_window, path_csv, app))
        hilo_exportacion_BJHA.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_BJHA.join()
        # Mostrar el archivo exportado
        if ruta_csv_BJHA:
            print(f"Archivo exportado exitosamente: {ruta_csv_BJHA}")
        else:
            print("No se exportó ningún archivo.")

        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_BJHA)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_BJHA = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_BJHA, resultado_dict))
        hilo_leer_csv_BJHA.start()
        hilo_leer_csv_BJHA.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "BJHA", dataframe)
       
        #guardar_dataframe_en_ini(dataframe, path_csv+"dataframe.ini")
        
          # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_FFHA = exportar_reporte_FFHA(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_FFHA}")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_FFHA = threading.Thread(target=hilo_exportar_FFHA, args=(main_window, path_csv, app))
        hilo_exportacion_FFHA.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_FFHA.join()
        # Mostrar el archivo exportado
        if ruta_csv_FFHA:
            print(f"Archivo exportado exitosamente: {ruta_csv_FFHA}")
        else:
            print("No se exportó ningún archivo.")

        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_FFHA)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_FFHA = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_FFHA, resultado_dict))
        hilo_leer_csv_FFHA.start()
        hilo_leer_csv_FFHA.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "FFHA", dataframe)
        #guardar_dataframe_en_ini(dataframe, path_csv+"dataframe.ini")
        
        
        # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_NKA = exportar_reporte_NKA(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_NKA}")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_NKA = threading.Thread(target=hilo_exportar_NKA, args=(main_window, path_csv, app))
        hilo_exportacion_NKA.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_NKA.join()
        # Mostrar el archivo exportado
        if ruta_csv_NKA:
            print(f"Archivo exportado exitosamente: {ruta_csv_NKA}")
        else:
            print("No se exportó ningún archivo.")

        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_NKA)
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_NKA = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_NKA, resultado_dict))
        hilo_leer_csv_NKA.start()
        hilo_leer_csv_NKA.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "NKA", dataframe)
        
        
        # Inicializar y manejar NovaWin nuevamente
        app, main_window = manejar_novawin(path_novawin, path_qps)
         # Exportar reportes y guardar la ruta de los archivos exportados
        ruta_csv_BET = exportar_reporte_BET(main_window, path_csv, app)
        print(f"Archivo exportado a: {ruta_csv_BET}")

        # Crear un hilo para la exportación (ya no es necesario exportar de nuevo)
        hilo_exportacion_BET = threading.Thread(target=hilo_exportar_BET, args=(main_window, path_csv, app))
        hilo_exportacion_BET.start()

        # Esperar a que el hilo termine antes de proceder
        hilo_exportacion_BET.join()
        # Mostrar el archivo exportado
        if ruta_csv_BET:
            print(f"Archivo exportado exitosamente: {ruta_csv_BET}")
        else:
            print("No se exportó ningún archivo.")

        # Crear DataFrame y guardar
        dataframe = leer_csv_y_crear_dataframe(ruta_csv_BET)
        
        print(dataframe)
        # Crear hilos para cada tarea
        hilo_leer_csv_BET = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv_BET, resultado_dict))
        hilo_leer_csv_BET.start()
        hilo_leer_csv_BET.join()
        agregar_dataframe_a_nueva_hoja(archivo_planilla, "BET", dataframe)
        
        #guardar_dataframe_en_ini(dataframe, path_csv+"dataframe.ini")      

        print("Proceso completado exitosamente.")
        
        # Crear hilos para cada tarea
        #hilo_leer_csv = threading.Thread(target=hilo_leer_csv_y_crear_dataframe, args=(ruta_csv, resultado_dict))
        hilo_agregar_excel = threading.Thread(target=hilo_agregar_csv_a_plantilla_excel, args=(ruta_csv, path_csv, resultado_dict))
        hilo_guardar_ini = threading.Thread(target=hilo_guardar_dataframe_en_ini, args=(resultado_dict.get('dataframe', None), path_csv + "dataframe.ini", resultado_dict))

        # Iniciar hilos
        hilo_leer_csv.start()
        hilo_agregar_excel.start()
        hilo_guardar_ini.start()

        # Esperar a que todos los hilos terminen
        hilo_leer_csv.join()
        hilo_agregar_excel.join()
        hilo_guardar_ini.join()

        # Verificar errores o resultados en el diccionario
        if 'error' in resultado_dict:
            print(f"Error: {resultado_dict['error']}")
        else:
            print("Todas las tareas completadas exitosamente.")

        # Continuar con otras tareas si es necesario
        print("Proceso completado exitosamente.")

    except Exception as e:
        print(f"Error en hk_main: {e}")
        traceback.print_exc()