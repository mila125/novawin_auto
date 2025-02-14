import turtle
import numpy as np
def draw_diagonal_squares_left(t, start_x, start_y, side_length, count):
    """Dibuja una serie de cuadrados en diagonal."""
    for i in range(count):
        x = start_x + (i * side_length / 2)
        y = start_y + (i * side_length / 2)
        draw_rectangle(t, [x, y], side_length, side_length, [])
def draw_diagonal_squares_rigth(t, start_x, start_y, side_length, count):
    """Dibuja una serie de cuadrados en diagonal."""
    for i in range(count):
        x = start_x + (-i * side_length / 2)
        y = start_y + (i * side_length / 2)
        draw_rectangle(t, [x, y], side_length, side_length, [])
def draw_straight_branches_left(t, start_x, start_y, side_length, count):
    """Dibuja una serie de cuadrados en diagonal."""
    for i in range(count):
        x = start_x
        y = start_y + (i * side_length / 2)
        draw_rectangle(t, [x, y], side_length, side_length, [])
def draw_straight_branches_rigth(t, start_x, start_y, side_length, count):
    """Dibuja una serie de cuadrados en diagonal."""
    for i in range(count):
        x = start_x
        y = start_y + (i * side_length / 2)
        draw_rectangle(t, [x, y], side_length, side_length, [])
def draw_square(h,i,j,i_x,i_y,j_x,j_y,lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag):
   #draw_square( h,i,j,numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3]-lados_rectangulos[h+1],numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag) 
    coordinates_i = np.zeros(2)
    coordinates_j = np.zeros(2)
    
    coordinates_i[0]=i_x
    coordinates_i[1]=i_y
    coordinates_j[0]=j_x
    coordinates_j[1]=j_y
    exit_flag=False
    while exit_flag==False: #y
     print(f"i: {i}")  
     if (i % espacio_del_cuadrado == 0) and (i >= espacio_del_cuadrado):
         
            numeros_cuadrado = np.append(numeros_cuadrado, coordinates_i)  #para no dejar espacios vacios
            numeros_derecha_cuadrados = draw_rectangle(t, coordinates_i, lado_cuadrado, lado_cuadrado, numeros_derecha_cuadrados)  
            if(direction_flag==True):               
             coordinates_i[1]+=lado_cuadrado
            if(direction_flag==False): 
              coordinates_i[1]-=lado_cuadrado

            
     if(direction_flag==True):   
      i+=lado_cuadrado
      if(i >= lados_rectangulos[h+1]):
       exit_flag=True
     if(direction_flag==False): 
      i-=lado_cuadrado
      if(i <= 2):
       j=numeros_derecha[h]-numeros_derecha[h-2]
       exit_flag=True
    coordinates_j[1] = coordinates_i[1]  
    exit_flag=False
    while exit_flag==False: #x
        print(f"j: {j}")  
        if((j%espacio_del_cuadrado == 0) and (j >= espacio_del_cuadrado)):
         
            coordinates_j[0]+=lado_cuadrado
             
            numeros_cuadrado= np.append(numeros_cuadrado, coordinates_j)
            numeros_derecha_cuadrados=draw_rectangle(t,coordinates_j, lado_cuadrado, lado_cuadrado,numeros_derecha_cuadrados)  
 
            
        if(direction_flag==True):   
          j+=lado_cuadrado
          if(j >= lados_rectangulos[h]):
           exit_flag=True
        if(direction_flag==False): 
          j-=lado_cuadrado
          if(j <= 2): 
           exit_flag=True
    #return numeros_derecha        
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
   
def work_with_squares(t,coordinates,min_width,numeros, numeros_derecha,rectangle_width, rectangle_height,lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde,old_width,old_heigth,h,lados_rectangulos,perimetro,distancia_hasta_el_borde_old):
     
    numeros_cuadrado= np.array([])
    numeros_derecha_cuadrados= np.array([])

    lado_cuadrado=min_width
       
    print(f"lado_cuadrado: {lado_cuadrado}") 
    print(f"rectangle_width: {rectangle_width}") 
    print(f"rectangle_height: {rectangle_height}") 
    
    area_total=abs(rectangle_width*rectangle_height)
    print(f"Area total: {area_total}")
    i=min_width
    while (i>min_width):
        if(i<distancia_hasta_el_borde):
            i=distancia_hasta_el_borde
            if(area_total%i**2==0):
                lado_cuadrado=i
        i+=1

    print(f"Area cuadrado : {lado_cuadrado**2}")
    cantidad= int(area_total/lado_cuadrado**2)
    print(f"Cantidad de cuadrados: {cantidad}")
    
    draw_squares_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old)

    draw_diagonal_branches_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old)
    
    draw_straight_branches_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old)
        
def draw_squares_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old):
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

    #numeros derecha incluyen el sado superior del cuadrado anfitrion

    h=2
    i=0   
    j=0 
    
    while h < (lados_rectangulos.size-2 ):
       if numeros_derecha[1]-numeros_derecha[h+1] <= lados_rectangulos[h+1]:

        break
       direction_flag=True
       draw_square(h,i,j,numeros_derecha[h+2]-lados_rectangulos[h],numeros_derecha[h+3]-lados_rectangulos[h+1],numeros_derecha[h+2]-lados_rectangulos[h],numeros_derecha[h+3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)
      
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
    
def draw_diagonal_branches_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old):
    espacio_del_cuadrado=int(perimetro/cantidad)
    direction_flag=True 
    coordinates_i=coordinates
    coordinates_j=coordinates

    h=0  
    j=0
    i=0   

    coordinates[0]=numeros_derecha[2]-lados_rectangulos[0]
    coordinates[1]=numeros_derecha[3]-100
     
    direction_flag=True 
    draw_square(h,i,j,numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3]-lados_rectangulos[1],numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)

    #numeros derecha incluyen el sado superior del cuadrado anfitrion

    h=2
    i=0   
    j=0 
    
    while h < (lados_rectangulos.size-2 ):
       if numeros_derecha[1]-numeros_derecha[h+1] <= lados_rectangulos[h+1]:

        break
       direction_flag=True
       
       if ((numeros_derecha[h+1] - numeros_derecha[h+3]) >= lado_cuadrado and distancia_hasta_el_borde_old == (old_heigth - numeros_derecha[h+1])):
         draw_diagonal_squares_rigth(t, numeros_derecha[h]-lados_rectangulos[h-2], numeros_derecha[h+1], lado_cuadrado, 10)
    
         draw_diagonal_squares_left(t, numeros_derecha[h], numeros_derecha[h+1], lado_cuadrado, 10)
       else:
         draw_diagonal_squares_rigth(t, numeros_derecha[h]-lados_rectangulos[h-2], numeros_derecha[h+1]-lado_cuadrado, lado_cuadrado, 10)
    
         draw_diagonal_squares_left(t, numeros_derecha[h], numeros_derecha[h+1]-lado_cuadrado, lado_cuadrado, 10)  
       h+=2
       i=0   
       j=0  
       coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-4]/2)-(lados_rectangulos[h]/2) 
       coordinates[1]=numeros_derecha[h+1] 

def draw_straight_branches_around_the_fig(perimetro,cantidad,lados_rectangulos,numeros_derecha,lado_cuadrado,coordinates,numeros_cuadrado,t,numeros_derecha_cuadrados,numeros,distancia_hasta_el_borde_old):
    espacio_del_cuadrado=int(perimetro/cantidad)
    direction_flag=True 
    coordinates_i=coordinates
    coordinates_j=coordinates

    h=0  
    j=0
    i=0   

    coordinates[0]=numeros_derecha[2]-lados_rectangulos[0]
    coordinates[1]=numeros_derecha[3]-100
     
    direction_flag=True 
    draw_square(h,i,j,numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3]-lados_rectangulos[1],numeros_derecha[2]-lados_rectangulos[0],numeros_derecha[3],lado_cuadrado,numeros_derecha,lados_rectangulos,espacio_del_cuadrado,numeros_derecha_cuadrados,numeros_cuadrado,t,direction_flag)

    #numeros derecha incluyen el sado superior del cuadrado anfitrion

    h=2
    i=0   
    j=0 
    
    while h < (lados_rectangulos.size-2 ):
       if numeros_derecha[1]-numeros_derecha[h+1] <= lados_rectangulos[h+1]:

        break
       direction_flag=True
       
       if ((numeros_derecha[h+1] - numeros_derecha[h+3]) >= lado_cuadrado and distancia_hasta_el_borde_old == (old_heigth - numeros_derecha[h+1])):
         draw_straight_branches_rigth(t, numeros_derecha[h]-lados_rectangulos[h-2], numeros_derecha[h+1], lado_cuadrado, 10)
    
         draw_straight_branches_left(t, numeros_derecha[h], numeros_derecha[h+1], lado_cuadrado, 10)
       else:
         draw_straight_branches_rigth(t, numeros_derecha[h]-lados_rectangulos[h-2], numeros_derecha[h+1]-lado_cuadrado, lado_cuadrado, 10)
    
         draw_straight_branches_left(t, numeros_derecha[h], numeros_derecha[h+1]-lado_cuadrado, lado_cuadrado, 10)  
       h+=2
       i=0   
       j=0  
       coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-4]/2)-(lados_rectangulos[h]/2) 
       coordinates[1]=numeros_derecha[h+1] 
       
def draw_nested_rectangles():
    distancia_hasta_el_borde=0
    distancia_hasta_el_borde_old=0
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
    print(f"coordinates: {coordinates}")  
     #cuadrado anfitrion

    numeros=np.append(numeros,coordinates) 
    numeros_derecha=draw_rectangle(t,coordinates, main_width, main_height,numeros_derecha)
    


    perimetro+=(2*main_width)+(2*main_height)


    
    coordinates[0]=coordinates[0]+(main_width/2)-(lados_rectangulos[0]/2)

    
    print(f"coordinates: {coordinates}")  
    h=0
    while(h<(lados_rectangulos.size-2)):
     # Dibujar segundo rectángulo sobre el primero


     if(lados_rectangulos[h-2]>lados_rectangulos[h]):
         min_width=lados_rectangulos[h]
     if(lados_rectangulos[h-1]>lados_rectangulos[h+1]):
         min_height=lados_rectangulos[h+1]
         
     distancia_hasta_el_borde = lados_rectangulos [1]-numeros_derecha[h+1]

     if(((distancia_hasta_el_borde-lados_rectangulos [h])<0) and(h>0)):
        print(f"lados_rectangulos[h]: {lados_rectangulos[h]}") 
        print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}") 
       
        work_with_squares(t,coordinates,min_width,numeros,numeros_derecha,lados_rectangulos[h],lados_rectangulos[h+1],lados_cuadrado,numeros_cuadrado,numeros_cuadrado_derecha,distancia_hasta_el_borde,main_width,main_height,h-2,lados_rectangulos,perimetro,distancia_hasta_el_borde_old)     
        modo_reducido=True
     if(modo_reducido==False):
      distancia_hasta_el_borde_old = distancia_hasta_el_borde
      numeros_derecha=draw_rectangle(t,coordinates, lados_rectangulos[h], lados_rectangulos[h+1],numeros_derecha)  
      #print(f"lados_rectangulos[h]: {lados_rectangulos[h]}")
      #print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}")
      perimetro+=lados_rectangulos[h]+(2*lados_rectangulos[h+1])
      #print(f"Perimetro ahora: {perimetro}")
     modo_reducido=False
      
     h+=2

     

     coordinates[0]=coordinates[0]+lados_rectangulos[h-2]-(lados_rectangulos[h-2]/2)-(lados_rectangulos[h]/2) #coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-2]/2)-(main_width/2)
     coordinates[1]=coordinates[1]+lados_rectangulos[h-1] #coordinates[1]=numeros_derecha[h+1]

     numeros=np.append(numeros,coordinates)

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo

draw_nested_rectangles()