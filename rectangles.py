import turtle
import numpy as np

# Crear un arreglo vacío

numeros = np.array([])
numeros_derecha = np.array([])
lados_rectangulos = np.array([])
lados_cuadrado = np.array([])
def draw_rectangle(t,coordinates, width, height):
    global numeros_derecha  # Referencia a la variable global
    x=coordinates[0]
    y=coordinates[1]
    
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Guardar la coordenada de inicio (esquina inferior izquierda)
  
    for _ in range(2):
        t.forward(width)
        x += width  # Actualizar coordenada X
        
        t.left(90)

        t.forward(height)
        y += height  # Actualizar coordenada Y
        t.left(90)

    # Guardar la coordenada superior izquierda
    numeros_derecha = np.append(numeros_derecha, [x , y])
   
    return coordinates  # Devolver la coordenada relevante
def draw_nested_rectangles():

    coordinates = np.zeros(2)
    global numeros  # Referencia a la variable global
    global numeros_derecha  # Referencia a la variable global
    global lados_rectangulos

    lados_rectangulos = np.append(lados_rectangulos, [300,200])
    lados_rectangulos = np.append(lados_rectangulos, [120, 100])
    lados_rectangulos = np.append(lados_rectangulos, [100, 90])
    lados_rectangulos = np.append(lados_rectangulos, [42, 80])
    lados_rectangulos = np.append(lados_rectangulos, [10, 50])
    window = turtle.Screen()
    window.title("División de Rectángulos")
    window.setup(width=600, height=600)  
    window.tracer(0)  

    t = turtle.Turtle()
    t.speed(0)  

    # Dibujar el rectángulo principal y actualizar coordenadas
    main_width = window.window_width()
    main_height = window.window_height()
    coordinates[0] = -main_width
   
    coordinates[1] = -main_height/2
    
     #cuadrado anfitrion
    print(coordinates)
    numeros=np.append(numeros,coordinates) 
    coordinates=draw_rectangle(t,coordinates, main_width, main_height)
    old_heigth=main_height
    old_width=main_width
     
    coordinates[0]=coordinates[0]+(old_width / 2) - (main_width / 2)
    coordinates[1]=coordinates[1]-old_heigth
    print(coordinates[0])
    
    print(lados_rectangulos.size)
    h=0
    while(h<(lados_rectangulos.size-2)):
     # Dibujar segundo rectángulo sobre el primero
     main_width, main_height = lados_rectangulos[h],lados_rectangulos[h+2]
   
     coordinates[0]=coordinates[0]+(old_width / 2) - (main_width / 2)
     coordinates[1]=coordinates[1]+old_heigth
    
     numeros=np.append(numeros,coordinates) 
     coordinates = draw_rectangle(t,coordinates, main_width, main_height)
     old_heigth=main_height
     old_width=main_width

     h+=2

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo
main_width = 500
main_height = 500

coordinates=draw_nested_rectangles()