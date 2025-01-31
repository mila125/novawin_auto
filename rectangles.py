import turtle
import numpy as np

def draw_rectangle(t,coordinates, width, height,numeros_derecha):

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
    return(numeros_derecha)
   
def draw_parsed_squares(coordinates,min_width,numeros, numeros_derecha,lados_rectangulos,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha):
    
    t = turtle.Turtle()
    t.speed(0)  

    print("hola")
    area_total=abs(numeros_derecha[0]*numeros_derecha[0])
    print(int(area_total))
    cantidad= int(area_total*0.5/min_width)
    cantidad_recalculada= cantidad
    print(cantidad)
    modulo=0
    while(modulo>0):
     
     modulo=int(area_total%min_width)
     cantidad_recalculada+= int(modulo/cantidad)
     
    parsed_width=int(min_width)
    parsed_height=int(area_total*0.25/cantidad)
    print(cantidad_recalculada)
    print(f"Dimensiones de nuevo cuadrado: {parsed_width} x {parsed_height}")
    i=0
    j=0 #iterador para lados de rectangulo
    print(numeros)
    print(coordinates)
    print(cantidad_recalculada*2)-2)
    while(i<(cantidad_recalculada*2)-2): #x e y

     coordinates[0]=numeros[j] #x
     coordinates[1]=numeros[j+1]+parsed_height #y

     print(coordinates[0]) 
     print(coordinates[1])  
     numeros_cuadrado=np.append(numeros_cuadrado,coordinates) 
     print(numeros_cuadrado) 
     numeros_cuadrado_derecha=draw_rectangle(t,coordinates, parsed_width, parsed_height,numeros_cuadrado_derecha)
     if numeros_cuadrado[j]+parsed_height>numeros_derecha[j]:
         j=j+2
     i=i+2
    print(numeros_cuadrado) 
def draw_nested_rectangles():

    coordinates = np.zeros(2)
    min_width = 0
    
    numeros = np.array([])
    numeros_derecha = np.array([])
    lados_rectangulos = np.array([])
    lados_cuadrado = np.array([])
    numeros_cuadrado = np.array([])
    numeros_cuadrado_derecha = np.array([])
    
    lados_rectangulos = np.append(lados_rectangulos, [300,200])
    lados_rectangulos = np.append(lados_rectangulos, [120, 100])
    lados_rectangulos = np.append(lados_rectangulos, [100, 90])
    lados_rectangulos = np.append(lados_rectangulos, [42, 80])
    lados_rectangulos = np.append(lados_rectangulos, [10, 50])
    lados_rectangulos = np.append(lados_rectangulos, [4000, 4000])
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
    numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)
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
     if(old_width>main_width):
         min_width=main_width
     coordinates[0]=coordinates[0]+(old_width / 2) - (main_width / 2)
     coordinates[1]=coordinates[1]+old_heigth
    
     numeros=np.append(numeros,coordinates) 
     numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)
     old_heigth=main_height
     old_width=main_width

     print(numeros_derecha[h+1])
     if(numeros_derecha[h+1]-(coordinates[1]+main_height)<0):
         print(numeros_derecha[1])
         draw_parsed_squares(coordinates,min_width,numeros,numeros_derecha,lados_rectangulos,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha) 
     h+=2

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo

draw_nested_rectangles()