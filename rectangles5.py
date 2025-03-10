import turtle
import numpy as np

#numeros_derecha_struct = np.array([[]] * 5, dtype=object)
lados_rectangulos = np.array([])
numeros_derecha = np.array([])
numeros = np.array([])
coordinates = np.zeros(2)
lados_cuadrado = np.array([])
numeros_cuadrado = np.array([])
numeros_cuadrado_derecha = np.array([])
numeros_cuadrado= np.array([])
numeros_derecha_cuadrados= np.array([])

diagonal_flag=False
perimetro=0
rigth_j_max=0
numeros_ramas_derecha=  np.array([])
def draw_same_squares_rectangle(cantidad,lado_cuadrado,t,h,main_width,main_height): 
   global numeros_ramas_derecha
   global perimetro
   global numeros_derecha   
   global coordinates
   global lados_rectangulos 
   espacio_del_cuadrado=int(perimetro/cantidad)
   print(f"espacio_del_cuadrado: {espacio_del_cuadrado}") 
   print(f"Perimetro ahora: {perimetro}") 
   #direction_flag=True 
   print(f"H: {h}")
   print(f"lados_rectangulos: {lados_rectangulos}")
   print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}")
   print(f"lados_rectangulos[h]: {lados_rectangulos[h]}")
   j=0
   i=0   
  
   coordinates[0]=numeros_derecha[0]-(main_width/2)-(lados_rectangulos[h]/2)
   
   print(f"lados_rectangulos[h]: {lados_rectangulos[h]}") 
   print(f"coordinates[0]: {coordinates[0]}") 
   print("dibuja") 
   while i<lados_rectangulos[h+1]: #y
     
    print(f"i: {i}")  
    j=0            
    while j<lados_rectangulos[h]: #x 
        print(f"j: {j}") 

        draw_rectangle(t, lado_cuadrado, lado_cuadrado)
        coordinates[0]+=1
        coordinates[1]-=lado_cuadrado #draw rectangle agrega el alto del cuadrado a la coordenada por defecto ajusto esto
        j+=lado_cuadrado
    coordinates[1]+=lado_cuadrado 
    i+=lado_cuadrado    
    coordinates[0]=numeros_derecha[0]-(main_width/2)-(lados_rectangulos[h]/2)
   print(f"coordinates[1] en draw_same_squares_rectangle: {coordinates[1]}") 
   numeros_derecha = np.append(numeros_derecha, coordinates)  
   
def draw_straight_branches_left(t, start_x, start_y, side_length, count):
    global numeros_ramas_derecha
    global rigth_j_max
    global perimetro
    lado_cuadrado = 10
    """Dibuja una serie de cuadrados en diagonal hacia la izquierda."""
    width = int(side_length / lado_cuadrado)
    heigth = int((count - (2 * width)) / 2)
    print(f"width : {width}") 
    print(f"heigth: {heigth}") 
    print(f"numeros_derecha[0]: {numeros_derecha[0]}") 
    x = start_x
    y = start_y

    for i in range(int(heigth)):

        for j in range(int(width), 0, -1):  # Ahora j se mueve en orden inverso
            print(f"int(x): {int(x)}") 
            print(f"int(numeros_derecha[0])-int(main_width): {int(numeros_derecha[0])-int(main_width)}")              
    
            if(int(x) <= int(numeros_derecha[0]-main_width)):
             print("salgo") 
             lados_x_ramas = np.append(lados_x_ramas, side_length)
             numeros_ramas_derecha = np.append(numeros_ramas_derecha, [coordinates[0], coordinates[1])
             diagonal_flag=False
             return count
            #if(int(x*lado_cuadrado) <= -int(main_width*lado_cuadrado)):
             #print("salgo") 
             #return count
            x -= 1  # Se invierte la dirección de x
            coordinates[0] = x
            coordinates[1] = y

            draw_rectangle(t, lado_cuadrado, lado_cuadrado)
            count -= 1
            x = coordinates[0]
            y = coordinates[1]

            y -= lado_cuadrado  # Mantiene la dirección de y

        j = 0
        x = start_x - (i * lado_cuadrado)  # Cambio en la dirección de x
        x -= 1  # Se invierte el ajuste de x

        i += lado_cuadrado  
        y += lado_cuadrado  # Ajuste normal de y

        perimetro += lado_cuadrado * 2
        
        print(f"left j: {j}") 
        print(f"left x: {x}") 
        print(f"left i: {i}") 
        print(f"left y: {y}")      

    perimetro += side_length  
    print("Rama izquierda finalizada") 
    return count
def draw_straight_branches_rigth(t, start_x, start_y, side_length, count,main_width,main_height):
  global rigth_j_max
    global perimetro
    lado_cuadrado=10
    """Dibuja una serie de cuadrados en diagonal."""
    width=int(side_length/lado_cuadrado)

    heigth=int(count-(2*width))/2
    

    print(f"width : {width}") 
    print(f"heigth: {heigth}") 
    print(f"numeros_derecha[0]: {numeros_derecha[0]}") 
    x = start_x
    y = start_y
    for i in range(int(heigth)):

        for j in range(int(width)):
            
         print(f"main_width*lado_cuadrado: {main_width*lado_cuadrado}") 
         if(int(numeros_derecha[0])+int(x*lado_cuadrado) >= int(numeros_derecha[0])-int(main_width)):
             print("salgo") 
             lados_x_ramas = np.append(lados_x_ramas, side_length)
             numeros_ramas_derecha = np.append(numeros_ramas_derecha, [coordinates[0], coordinates[1])
             diagonal_flag=False
             return count
         x+=1
         coordinates[0]=x
        
         coordinates[1]=y
         
         draw_rectangle(t,lado_cuadrado, lado_cuadrado)#, []
         count-=1
         x = coordinates[0]
         y = coordinates[1]
         
         y -= lado_cuadrado

         j += 1
         rigth_j_max=j
        j=0
        x=start_x+(i*lado_cuadrado)
        
        x+=1
        
        i+=lado_cuadrado  
        y+=lado_cuadrado
        
        perimetro+=lado_cuadrado*2
        
        print(f"j: {j}") 
        print(f"x: {x}") 
        print(f"i: {i}") 
        print(f"y: {y}")      
   
    perimetro+=side_length #mejor
    print("Rama derecha finalizada") 
    return count
def draw_diagonal_branches_left(t, start_x, start_y, side_length, count, main_width, main_height):
    global diagonal_flag
    global rigth_j_max
    global perimetro
    lado_cuadrado = 10
    """Dibuja una serie de cuadrados en diagonal hacia la izquierda."""
    width = int(side_length / lado_cuadrado)
    heigth = int((count - (2 * width)) / 2)
    print(f"width : {width}") 
    print(f"heigth: {heigth}") 
    print(f"numeros_derecha[0]: {numeros_derecha[0]}") 
    x = start_x
    y = start_y

    for i in range(int(heigth)):

        for j in range(int(width), 0, -1):  # Ahora j se mueve en orden inverso
            print(f"int(x): {int(x)}") 
            print(f"int(numeros_derecha[0])-int(main_width): {int(numeros_derecha[0])-int(main_width)}")              
    
            if(int(x) <= int(numeros_derecha[0]-main_width)):
             print("salgo") 
             lados_x_ramas = np.append(lados_x_ramas, side_length)
             numeros_ramas_derecha = np.append(numeros_ramas_derecha, [coordinates[0], coordinates[1])
             diagonal_flag=True
             return count
            #if(int(x*lado_cuadrado) <= -int(main_width*lado_cuadrado)):
             #print("salgo") 
             #return count
            x -= 1  # Se invierte la dirección de x
            coordinates[0] = x
            coordinates[1] = y

            draw_rectangle(t, lado_cuadrado, lado_cuadrado)
            count -= 1
            x = coordinates[0]
            y = coordinates[1]

            y -= lado_cuadrado  # Mantiene la dirección de y

        j = 0
        x = start_x - (i * lado_cuadrado)  # Cambio en la dirección de x
        x -= 1  # Se invierte el ajuste de x

        i += lado_cuadrado  
        y += lado_cuadrado  # Ajuste normal de y

        perimetro += lado_cuadrado * 2
        
        print(f"left j: {j}") 
        print(f"left x: {x}") 
        print(f"left i: {i}") 
        print(f"left y: {y}")      

    perimetro += side_length  
    print("Rama izquierda finalizada") 
    return count
def draw_diagonal_branches_rigth(t, start_x, start_y, side_length, count,main_width,main_height):
    global rigth_j_max
    global perimetro
    global diagonal_flag
    lado_cuadrado=10
    """Dibuja una serie de cuadrados en diagonal."""
    width=int(side_length/lado_cuadrado)

    heigth=int(count-(2*width))/2
    

    print(f"width : {width}") 
    print(f"heigth: {heigth}") 
    print(f"numeros_derecha[0]: {numeros_derecha[0]}") 
    x = start_x
    y = start_y
    for i in range(int(heigth)):

        for j in range(int(width)):
            
         print(f"main_width*lado_cuadrado: {main_width*lado_cuadrado}") 
         if(int(numeros_derecha[0])+int(x*lado_cuadrado) >= int(numeros_derecha[0])-int(main_width)):
             print("salgo") 
             lados_x_ramas = np.append(lados_x_ramas, side_length)
             numeros_ramas_derecha = np.append(numeros_ramas_derecha, [coordinates[0], coordinates[1])
             diagonal_flag=True
             return count
         x+=1
         coordinates[0]=x
        
         coordinates[1]=y
         
         draw_rectangle(t,lado_cuadrado, lado_cuadrado)#, []
         count-=1
         x = coordinates[0]
         y = coordinates[1]
         
         y -= lado_cuadrado

         j += 1
         rigth_j_max=j
        j=0
        x=start_x+(i*lado_cuadrado)
        
        x+=1
        
        i+=lado_cuadrado  
        y+=lado_cuadrado
        
        perimetro+=lado_cuadrado*2
        
        print(f"j: {j}") 
        print(f"x: {x}") 
        print(f"i: {i}") 
        print(f"y: {y}")      
   
    perimetro+=side_length #mejor
    print("Rama derecha finalizada") 
    return count
def draw_rectangle(t, width, height):
    
    global numeros_derecha
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
    coordinates[0]+=width
    coordinates[1]+=height
    #numeros_derecha = np.append(numeros_derecha, [coordinates[0]+width , coordinates[1]+height])
def work_with_squares(t,rectangle_width,rectangle_height,distancia_hasta_el_borde_x,distancia_hasta_el_borde_y,old_width,old_heigth,h,distancia_hasta_el_borde_oldl):
    global perimetro
    global numeros_ramas_derecha
    global numeros_derecha
    global numeros_cuadrado
    global numeros_derecha_cuadrados
    lado_cuadrado = 10    
    print(f"lado_cuadrado: {lado_cuadrado}") 
    print(f"rectangle_width: {rectangle_width}") 
    print(f"rectangle_height: {rectangle_height}") 

    area_total=abs(rectangle_width*rectangle_height)
   
         
    if(rectangle_height > distancia_hasta_el_borde_y or rectangle_width > 600) :
      # print("El rectangulo no cabe en el espacio restante") 
  
      # cantidad= int(area_total/lado_cuadrado**2)
      # print(f"cantidad: {cantidad}")
      # print(f"Perimetro ahora: {perimetro}")
      # rama_derecha=draw_diagonal_branches_rigth(t, numeros_derecha[h]+lados_rectangulos[h-2]+lado_cuadrado, numeros_derecha[h+1], lados_rectangulos[h-2]/2, cantidad/2,old_width,old_heigth)
      # print(f"Perimetro ahora: {perimetro}") 
      # rama_izquierda=draw_diagonal_branches_left(t, numeros_derecha[h], numeros_derecha[h+1],lados_rectangulos[h-2]/2, cantidad/2,old_width,old_heigth)
       
      # ramas_diagonales = np.append(rama_izquierda, rama_derecha)
       numeros_ramas_derecha  =  np.append(numeros_ramas_derecha , numeros_derecha[h-2], numeros_derecha[h-1], numeros_derecha[h], numeros_derecha[h+1])   
       h = 0
       while(count>= 0):

            rama_derecha=draw_diagonal_branches_rigth(t, numeros_ramas_derecha[h]-lados_ramas[h-2], numeros_ramas_derecha[h+1], (lados_ramas[h-2]/2)-(lados_ramas[h]/2), cantidad/2,old_width,old_heigth)
            rama_izquierda=draw_diagonal_branches_left(t, numeros_ramas_derecha[h]+lados_ramas[h-2], numeros_ramas_derecha[h+1],(lados_ramas[h-2]/2)-(lados_ramas[h]/2), cantidad/2,old_width,old_heigth)
           
            rama_derecha=draw_straight_branches_rigth(t, numeros_ramas_derecha[h]-lados_ramas[h-2], numeros_ramas_derecha[h+1], (lados_ramas[h-2]/2)-(lados_ramas[h]/2), cantidad/2,old_width,old_heigth)
            rama_izquierda=draw_straight_branches_left(t, numeros_ramas_derecha[h]+lados_ramas[h-2], numeros_ramas_derecha[h+1],(lados_ramas[h-2]/2)-(lados_ramas[h]/2), cantidad/2,old_width,old_heigth)
            count = rama_derecha + rama_izquierda
            print(f"Perimetro ahora1: {perimetro}") 
    else:
        print("El rectangulo cabe en el espacio restante") 
        new_heigth=rectangle_height
        new_width=rectangle_width
        perimetro+=(new_width*2)+(new_heigth*2)
        print(f"Perimetro ahora: {perimetro}") 
         
        print(f"lado_cuadrado: {lado_cuadrado}") 
        print(f"coordinates: {coordinates}") 
        print(f"t: {t}") 
        print(f"h: {h}") 
        cantidad= int(area_total/lado_cuadrado**2)
        print(f"cantidad: {cantidad}")
        print(f"coordinates[1] en work_with_squares: {coordinates[1]}") 
        draw_same_squares_rectangle(cantidad,lado_cuadrado,t,h,old_width,old_heigth)

        
def draw_squares_around_the_fig(cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old):
    espacio_del_cuadrado=int(perimetro/cantidad)
    direction_flag=True 
    coordinates_i=coordinates
    coordinates_j=coordinates
    i=0
    j=0
    
    old_width=600
    old_heigth=600
    
    espacio_del_cuadrado=espacio_del_cuadrado*lado_cuadrado*0.5
    while(j<old_width): #x
     
     if((j%espacio_del_cuadrado == 0) and (j >= espacio_del_cuadrado)):
            coordinates[0] =-old_width+j+(lado_cuadrado/2)
            coordinates[1] =-(old_width/2)

            
            numeros_cuadrado= np.append(numeros_cuadrado, coordinates)
            numeros_derecha_cuadrados=draw_rectangle(t,coordinates, lado_cuadrado, lado_cuadrado,numeros_derecha_cuadrados)  
            
            
     j+=1
          
    while(i<old_width):
        
        if((i%espacio_del_cuadrado == 0) and (i >= espacio_del_cuadrado)):
            coordinates[0]=-old_width+j-espacio_del_cuadrado
            coordinates[1]=(-old_heigth/2)+i+(lado_cuadrado/2)
    
            
            numeros_cuadrado= np.append(numeros_cuadrado, coordinates)
            numeros_derecha_cuadrados=draw_rectangle(t,coordinates, lado_cuadrado, lado_cuadrado,numeros_derecha_cuadrados)  

            
        i+=lado_cuadrado

    h=0  
    j=0
    i=0   

    coordinates[0]=numeros_derecha[2]-lados_rectangulos[0]
    coordinates[1]=numeros_derecha[3]-100
     
    direction_flag=True 
    draw_square(h,i,j,numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3]-lados_rectangulos[1],numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)
    # Guardar la coordenada superior izquierda
    numeros_derecha = np.append(numeros_derecha, [coordinates[0]+lados_rectangulos[h] , coordinates[1]+lados_rectangulos[h+1]])
   
    #numeros derecha incluyen el sado superior del cuadrado anfitrion

    h=2
    i=0   
    j=0 
    
    while h < (lados_rectangulos.size-2 ):
       if numeros_derecha[1]-numeros_derecha[h+1] <= lados_rectangulos[h+1]:

        break
       direction_flag=True
       draw_square(h,i,j,numeros_derecha[h+2]-lados_rectangulos[h],numeros_derecha[h+3]-lados_rectangulos[h+1],numeros_derecha[h+2]-lados_rectangulos[h],numeros_derecha[h+3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)
       numeros_derecha = np.append(numeros_derecha, [coordinates[0]+lados_rectangulos[h] , coordinates[1]+lados_rectangulos[h+1]])
       h+=2
       i=0   
       j=0  
       coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-4]/2)-(lados_rectangulos[h]/2) 
       coordinates[1]=numeros_derecha[h+1] 
       
    print(f"Lado top: {lados_rectangulos[h-2]}")   
    h-=2
    
    j=lados_rectangulos[h]
    i=lados_rectangulos[h+1]
    coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-4]/2)-(lados_rectangulos[h]/2) 
    coordinates[1]=numeros_derecha[h+1] 
    direction_flag=False

    draw_square(h,i,j,numeros_derecha[h+2],numeros_derecha[h+3],numeros_derecha[h+2],numeros_derecha[h+3]-lados_rectangulos[h],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)
      
    h-=2
    
    coordinates[0]=numeros_derecha[h+2] 
    coordinates[1]=numeros_derecha[h+3] 

    
    while(h>=0): 
      direction_flag=False
      j=lados_rectangulos[h]
      i=lados_rectangulos[h+1]
      draw_square(h,i,j,numeros_derecha[h+2],numeros_derecha[h+3],numeros_derecha[h+2],numeros_derecha[h+3]-lados_rectangulos[h],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag) 
   
      h-=2
    i=0
    j=0  
     
    coordinates[0]=numeros_derecha[0]-old_width
    coordinates[1]=numeros_derecha[1] 
       
def draw_nested_rectangles():
    global numeros
    global numeros_derecha
    global perimetro
    distancia_hasta_el_borde=0
    distancia_hasta_el_borde_old=0
    perimetro = 0
    global coordinates
    modo_reducido = False
    numeros = np.array([])
    
    global lados_rectangulos
    
    lados_rectangulos = np.append(lados_rectangulos, [210,330])
    lados_rectangulos = np.append(lados_rectangulos, [150, 180])
    lados_rectangulos = np.append(lados_rectangulos, [40, 500])
    lados_rectangulos = np.append(lados_rectangulos, [50, 10])
    lados_rectangulos = np.append(lados_rectangulos, [0, 0]) #finaliza la sequencia   

    print(f"lados_rectangulos: {lados_rectangulos}") 
    global lados_cuadrado
    global numeros_cuadrado
    global numeros_cuadrado_derecha
    lado_cuadrado = 10
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
    print(f"coordinates: {coordinates}")  
    #cuadrado anfitrion

    numeros=np.append(numeros,coordinates)
    print(f"numeros_derecha: {numeros_derecha}")    
    draw_rectangle(t, main_width, main_height)
    numeros_derecha = np.append(numeros_derecha, [coordinates[0] , coordinates[1]])

    print(f"numeros_derecha: {numeros_derecha}") 

    perimetro+=(2*main_width)+(2*main_height)


    
    coordinates[0]=coordinates[0]+(main_width/2)-(lados_rectangulos[0]/2)
    coordinates[1]=coordinates[1]-main_height
    numeros_derecha = np.append(numeros_derecha, coordinates) 
    print(f"coordinates: {coordinates}")  
    
    h=0
    
    while(h<(lados_rectangulos.size-2)):
     # Dibujar segundo rectángulo sobre el primero
    ## numeros_derecha = np.append(numeros_derecha, [coordinates[0]+lados_rectangulos[h] , coordinates[1]+lados_rectangulos[h+1]])
     print(f"h: {h}")      
     print(f"lados_rectangulos[h]: {lados_rectangulos[h]}") 
     print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}") 
     
     print(f"numeros_derecha[h+2]: {numeros_derecha[h+2]}") 
     print(f"numeros_derecha[h+3]: {numeros_derecha[h+3]}") 
     #numeros_derecha = np.append(numeros_derecha, [coordinates[0]+lados_rectangulos[h] , coordinates[1]+lados_rectangulos[h+1]]) 
     distancia_hasta_el_borde_y = (numeros_derecha[1])-numeros_derecha[h+3]
     distancia_hasta_el_borde_x = (main_width/2) #lados_rectangulos [0]
    
     print(f"distancia_hasta_el_borde_y : {distancia_hasta_el_borde_y }") 
     print(f"distancia_hasta_el_borde_x: {distancia_hasta_el_borde_x}")
   

     work_with_squares(t,lados_rectangulos[h],lados_rectangulos[h+1],distancia_hasta_el_borde_x,distancia_hasta_el_borde_y,main_width,main_height,h,distancia_hasta_el_borde_old)     
                  
   
     #distancia_hasta_el_borde_old = distancia_hasta_el_borde
  
     h+=2
     coordinates[0]=lados_rectangulos[h-2]-(lados_rectangulos[h-2]/2)-(lados_rectangulos[h]/2) #coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-2]/2)-(main_width/2)
     
     print(f"coordinates[1] en nested rectangles: {coordinates[1]}")
     print(f"coordinates[1]: {coordinates[1]}")
     numeros_derecha = np.append(numeros_derecha, coordinates) 
    #numeros=np.append(numeros,coordinates)

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo

draw_nested_rectangles()