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
   
def draw_parsed_squares(t,coordinates,min_width,numeros, numeros_derecha,main_width, main_height,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde,old_width,old_heigth,h,lados_rectangulos,perimetro):
    numeros_cuadrado= np.array([])
    numeros_derecha_cuadrados= np.array([])

    lado_cuadrado=min_width
    area_total=abs(main_width*main_height)
    print(f"Area total: {area_total}")
    i=min_width
    while (i>min_width):
        if(i<distancia_hasta_el_borde):
            i=distancia_hasta_el_borde
            if(area_total%i**2==0):
                lado_cuadrado=i
        i+=1
    print(f"Lado cuadrado : {lado_cuadrado}")
    print(f"Area cuadrado : {lado_cuadrado**2}")
    cantidad= int(area_total/lado_cuadrado**2)
    print(f"Cantidad de cuadrados: {cantidad}")
    
    numeros_derecha=draw_squares_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados)

    return numeros_derecha
def draw_squares_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados):
    espacio_del_cuadrado=int(perimetro/cantidad)
    print(f"espacio_del_cuadrado: {espacio_del_cuadrado}")
    j=0
    i=0
    
    j=2

    espacio_del_cuadrado=espacio_del_cuadrado*lado_cuadrado*0.5
    while(j<600): #x
     print(f"j: {j}")  
     if((j%espacio_del_cuadrado == 0) and (j >= espacio_del_cuadrado)):
            coordinates[0] =-600+j+(lado_cuadrado/2)
            coordinates[1] =-(600/2)
            print(f"coordinates[0]: {coordinates[0]}")
            print(f"coordinates[1]: {coordinates[1]}")
            
            numeros_cuadrado= np.append(numeros_cuadrado, coordinates)
            numeros_derecha_cuadrados=draw_rectangle(t,coordinates, lado_cuadrado, lado_cuadrado,numeros_derecha_cuadrados)  
            numeros_derecha= np.append(numeros_derecha, [coordinates[0]+lado_cuadrado , coordinates[1]+lado_cuadrado])
            
     j+=1
          
    while(i<600):
        print(f"i: {i}")  
        if((i%espacio_del_cuadrado == 0) and (i >= espacio_del_cuadrado)):
            coordinates[0]=-600+j-espacio_del_cuadrado
            coordinates[1]=(-600/2)+i+(lado_cuadrado/2)
    
            print(f"coordinates[0]: {coordinates[0]}")
            print(f"coordinates[1]: {coordinates[1]}")
            
            numeros_cuadrado= np.append(numeros_cuadrado, coordinates)
            numeros_derecha_cuadrados=draw_rectangle(t,coordinates, lado_cuadrado, lado_cuadrado,numeros_derecha_cuadrados)  
            numeros_derecha= np.append(numeros_derecha, [coordinates[0]+lado_cuadrado , coordinates[1]+lado_cuadrado])
            
        i+=1
    j=0
    i=0
    h=0   
     
    while h < (lados_rectangulos.size - 2):
        print(f"h: {h}")
        print(f"lados_rectangulos[h]: {lados_rectangulos[h]}")
    
        while j < lados_rectangulos[h]:  # x
            print(f"j: {j}")  
            if (j % espacio_del_cuadrado == 0) and (j >= espacio_del_cuadrado):
                coordinates[0] = -lados_rectangulos[h] + j + (lado_cuadrado / 2)
                coordinates[1] = -(lados_rectangulos[h + 1] / 2)
                print(f"coordinates[0]: {coordinates[0]}")
                print(f"coordinates[1]: {coordinates[1]}")

                numeros_cuadrado = np.append(numeros_cuadrado, coordinates)
                numeros_derecha_cuadrados = draw_rectangle(t, coordinates, lado_cuadrado, lado_cuadrado, numeros_derecha_cuadrados)  
                numeros_derecha = np.append(numeros_derecha, [coordinates[0] + lado_cuadrado, coordinates[1] + lado_cuadrado])
        
            j += 1
    
        while i < lados_rectangulos[h + 1]:
            print(f"i: {i}")  
            if (i % espacio_del_cuadrado == 0) and (i >= espacio_del_cuadrado):
                coordinates[0] = -lados_rectangulos[h] + j - espacio_del_cuadrado
                coordinates[1] = (-lados_rectangulos[h + 1] / 2) + i + (lado_cuadrado / 2)
    
                print(f"coordinates[0]: {coordinates[0]}")
                print(f"coordinates[1]: {coordinates[1]}")
            
                numeros_cuadrado = np.append(numeros_cuadrado, coordinates)
                numeros_derecha_cuadrados = draw_rectangle(t, coordinates, lado_cuadrado, lado_cuadrado, numeros_derecha_cuadrados)  
                numeros_derecha = np.append(numeros_derecha, [coordinates[0] + lado_cuadrado, coordinates[1] + lado_cuadrado])
        
            i += 1
    
        j = 0
        i = 0  
        h += 2

    return numeros_derecha
def draw_nested_rectangles():
    perimetro = 0
    coordinates = np.zeros(2)
    modo_reducido = False
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
    perimetro+=(2*old_width)+(2*old_heigth)
    print(f"Perimetro ahora: {perimetro}")
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
         
     distancia_hasta_el_borde = lados_rectangulos [1]-numeros_derecha[h+1]
     print(f"distancia_hasta_el_borde:{distancia_hasta_el_borde}")   
     if(((distancia_hasta_el_borde-lados_rectangulos [h])<0) and(h>0)):

        numeros_derecha=draw_parsed_squares(t,coordinates,min_width,numeros,numeros_derecha,main_width, main_height,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde,old_width,old_heigth,h-2,lados_rectangulos,perimetro)     
        modo_reducido=True
     if(modo_reducido==False):
      numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)  
      print(f"lados_rectangulos[h]: {lados_rectangulos[h]}")
      print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}")
      perimetro+=lados_rectangulos[h]+(2*lados_rectangulos[h+1])
      print(f"Perimetro ahora: {perimetro}")
     modo_reducido=False
      
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