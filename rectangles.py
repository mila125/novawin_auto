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
    numeros_derecha = np.append(numeros_derecha, [coordinates[0]+width , coordinates[1]+height])
    return(numeros_derecha)
   
def draw_parsed_squares(t,coordinates,min_width,numeros, numeros_derecha,main_width, main_height,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde):
   

    print("hola")
    area_total=abs(main_width*main_height)
    print(f"Area total: {area_total}")
    i=min_width
    while (i>min_width):
        if()
    cantidad= int(area_total*0.5/min_width)
    cantidad_recalculada= cantidad
    print(cantidad)
    
    cantidad=int(main_width*main_height)/(min_width*min_width)
    print(f"Cantidad: {cantidad}")
    modulo=int(main_width*main_height)%(min_width*min_width)
    print(f"Modulo: {modulo}")
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
    coordinates[0]=numeros[0]
    coordinates[1]=numeros[1]
    print(coordinates)
    print(cantidad_recalculada)
    print((cantidad_recalculada*2)-2)
   
    print(numeros_cuadrado) 
def draw_nested_rectangles():

    coordinates = np.zeros(2)

    min_width = 0
    min_heigth = 0
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
    lados_rectangulos = np.append(lados_rectangulos, [400, 400])
    lados_rectangulos = np.append(lados_rectangulos, [0, 0]) #finaliza la sequencia
    window = turtle.Screen()
    window.title("División de Rectángulos")
    window.setup(width=600, height=600)  
    window.tracer(0)  

    t = turtle.Turtle()
    t.speed(0)  

    # Dibujar el rectángulo principal y actualizar coordenadas
    main_width = window.window_width()
    main_height = window.window_height()
    coordinates[0] -=main_width
   
    coordinates[1] -=(main_height/2)
    
     #cuadrado anfitrion
 
    print(f"coordenadas iniciales: {coordinates}")
    numeros=np.append(numeros,coordinates) 
    numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)

    print(f"numeros_derecha: {numeros_derecha}")
    old_heigth=main_height
    old_width=main_width
    print(f"old_width: {old_width}")
    print(f"old_width: {old_width}")   

    main_width = lados_rectangulos[0]
    main_height = lados_rectangulos[1]
    
    coordinates[0]=numeros_derecha[0]-(old_width/2)-(main_width/2)
    coordinates[1]=numeros_derecha[1]-old_heigth
    
    print(f"coordinates[0]: {coordinates[0]}")
    print(f"coordinates[1]: {coordinates[1]}")
    
    h=0
    while(h<(lados_rectangulos.size-2)):
     # Dibujar segundo rectángulo sobre el primero

     print(f"main_width:{main_width} main_height:{main_height}")

     if(lados_rectangulos[h-2]>main_width):
         min_width=main_width
     if(lados_rectangulos[h-1]>main_height):
         min_heigth=main_height
         
 
        
     numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)  
     distancia_hasta_el_borde = lados_rectangulos [1]-numeros_derecha[h+1]
     print(f"distancia_hasta_el_borde:{distancia_hasta_el_borde}")   
     if(((distancia_hasta_el_borde-main_height)<0) and(h>0)):

        draw_parsed_squares(t,coordinates,min_width,numeros,numeros_derecha,main_width, main_height,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde)      
     h+=2
     
     print(f"numeros_derecha[h]:{numeros_derecha[h]}")    
     print(f"numeros_derecha[h+1]:{numeros_derecha[h+1]}")  
     
     main_width = lados_rectangulos[h]
     main_height = lados_rectangulos[h+1]
     print(f"main_width:{main_width}")    
     print(f"main_height:{main_height}")     
     coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-2]/2)-(main_width/2)
     coordinates[1]=numeros_derecha[h+1]
     print(f"coordinates[0]: {coordinates[0]}")
     print(f"coordinates[1]: {coordinates[1]}")
     numeros=np.append(numeros,coordinates)

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo

draw_nested_rectangles()