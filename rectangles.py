import turtle
import numpy as np

# Crear un arreglo vacío

numeros = np.array([])
numeros_2 = np.array([])
def draw_parsed_rectangles(t, reduced_width, reduced_height,cantidad):
    global numeros, numeros_2  # Acceso a variables globales
    
    i, j = 0, 0  # Contadores

    while j < cantidad:  # -1 para evitar index error
        t.penup()
        
        if j % 2 == 0:  # Cada 2 vueltas, tomar la esquina superior izquierda
            referencia_x = numeros[j]
            referencia_y = numeros[j + 1]  # Directamente el valor correcto     
        
        if i % 2 == 1:  # Dibujar cuadrados en los vértices izquierdos
            t.goto(referencia_x - reduced_width, referencia_y)
            t.pendown()
            
            for _ in range(2):
                t.forward(reduced_width)
                numeros_2 = np.append(numeros_2, [referencia_x, referencia_y])
                t.left(90)
                t.forward(reduced_height)
                t.left(90)

        i += 1   
        j += 2  # Saltar de 2 en 2 porque las coordenadas son pares (x, y)

    #print("Coordenadas almacenadas en numeros_2:", numeros_2.reshape(-1, 2))
def draw_rectangle(t,coordinates, width, height):
    global numeros  # Referencia a la variable global
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
    #numeros = np.append(numeros, [x - width, y- height])
   
    return coordinates  # Devolver la coordenada relevante
def draw_nested_rectangles(main_width, main_height):

    coordinates = np.zeros(2)
    global numeros  # Referencia a la variable global
    window = turtle.Screen()
    window.title("División de Rectángulos")
    window.setup(width=600, height=600)  
    window.tracer(0)  

    t = turtle.Turtle()
    t.speed(0)  

    # Dibujar el rectángulo principal y actualizar coordenadas

    main_x = -(main_width / 2)
   
    main_y = -90
    coordinates[0]=main_x
    coordinates[1]=main_y
    print(coordinates)
    numeros=np.append(numeros,coordinates) 
    draw_rectangle(t,coordinates, main_width, -main_height)
    old_heigth=main_height
    old_width=main_width
     
    # Dibujar segundo rectángulo sobre el primero
    main_width, main_height = 42, 80

    coordinates[0]=coordinates[0]+(old_width / 2) - (main_width / 2)
    numeros=np.append(numeros,coordinates) 
    coordinates = draw_rectangle(t,coordinates, main_width, main_height)
    old_heigth=main_height
    old_width=main_width
    

    # Dibujar segundo rectángulo sobre el primero
    main_width, main_height = 10, 50
   
    coordinates[0]=coordinates[0]+(old_width / 2) - (main_width / 2)
    coordinates[1]=coordinates[1]+old_heigth
    
    numeros=np.append(numeros,coordinates) 
    coordinates = draw_rectangle(t,coordinates, main_width, main_height)
    old_heigth=main_height
    old_width=main_width
   
    main_width, main_height = 90, 10
  
    total_area=main_height*main_width

    i=int(total_area)
    parsed_area=0
    cantidad=0
    print(numeros)
    while(i>=100):
     if(total_area%i==0 and i<total_area and i>1):
        cantidad=int(total_area/i)
     i-=1
    if(cantidad==0):
        cantidad=int(total_area/10)
    # Dibujar cuadrados en los vértices
    parsed_area=int(total_area/cantidad)

    parsed_width=int(parsed_area/4)
   # print(parsed_width)
    parsed_height=int(parsed_area/4)+(parsed_area%4)
    
    coordinates[0]=coordinates[0]+(old_width / 2) - (parsed_width / 2)
     #if(i%2==0):
    coordinates[1]=coordinates[1]+old_heigth
    #draw_parsed_rectangles(t, parsed_width, parsed_height,cantidad)  
   
    #print(cantidad)
    cantidad_restante=cantidad
    #while(cantidad_restante>0):

    # coordinates[0]=coordinates[0]-parsed_width
    # coordinates = draw_rectangle(t,coordinates, parsed_width, parsed_height)    
    # cantidad_restante-=1
    j=1
    signo=1
    print(numeros.size)
    print(cantidad_restante)
    print(parsed_width)
    
    coordinates[0]=int(numeros[j-1])
     
    coordinates[0]-=parsed_width#lado izquierdo
     
    coordinates[1]=int(numeros[j])
    signo=1
    print(j-1)
    print((j-1)%4)
    if((j-1)%4==0 or (j-1)==0):
       signo=-1
    if(signo==-1):
     coordinates[1]-=(parsed_height*2)
    print(coordinates[1]) 
    print(coordinates[0])  

    if(cantidad_restante>0):
     coordinates = draw_rectangle(t,coordinates, parsed_width, signo*parsed_height)
     cantidad_restante-=1
    j=j+2
    
    coordinates[0]=int(numeros[j-1])
     
    coordinates[0]-=parsed_width#lado izquierdo
     
    coordinates[1]=int(numeros[j])
    signo=1
    if((j-1)%4==0 or (j-1)==0):
      signo=-1
    coordinates[1]+=(parsed_height*2)*signo
    print(coordinates[1]) 
    print(coordinates[0])  

    if(cantidad_restante>0):
     coordinates = draw_rectangle(t,coordinates, parsed_width, signo*parsed_height)
     cantidad_restante-=1
    j=j+2
    
       
    coordinates[0]=int(numeros[j-1])
     
    coordinates[0]-=parsed_width#lado izquierdo
     
    coordinates[1]=int(numeros[j])
    signo=1
    if((j-1)%4==0 or (j-1)==0):
      signo=-1
    coordinates[1]+=(parsed_height*2)*signo
    print(coordinates[1]) 
    print(coordinates[0])  

    if(cantidad_restante>0):
     coordinates = draw_rectangle(t,coordinates, parsed_width, signo*parsed_height)
     cantidad_restante-=1
    j=j+2
   
    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo
main_width = 300
main_height = 200
sub_width = 120
sub_height = 100
coordinates=draw_nested_rectangles(main_width, main_height)