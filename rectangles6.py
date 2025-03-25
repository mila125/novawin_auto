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
lados_ramas = np.array([])

diagonal_flag=False
perimetro=0
rigth_j_max=0
numeros_ramas_derecha=  np.array([])
MAX_DEPTH=0
def draw_same_squares_rectangle(cantidad,lado_cuadrado,t,h,main_width,main_height,pose): 
   global numeros_ramas_derecha
   global perimetro
   global numeros_derecha   
   global coordinates
   global lados_rectangulos 
   global lados_ramas
   espacio_del_cuadrado=int(perimetro/cantidad)
   print(f"espacio_del_cuadrado: {espacio_del_cuadrado}") 
   print(f"Perimetro ahora: {perimetro}") 

   print(f"H: {h}")
   print(f"lados_rectangulos: {lados_rectangulos}")
   print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}")
   print(f"lados_rectangulos[h]: {lados_rectangulos[h]}")
   j=0
   i=0   
  
   coordinates[0]=pose-(lados_rectangulos[h]/2)
   
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
    coordinates[0]=pose-(lados_rectangulos[h]/2)
   print(f"coordinates[1] en draw_same_squares_rectangle: {coordinates[1]}") 
   numeros_derecha = np.append(numeros_derecha, coordinates)  


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
def hoja(t, profundidad, rama_height,rama_width, count,rama_count,h):
    global lados_rectangulos

    #t.penup()
    print(f"count1: {count}")
    if(count==0):
        return
    else:
     
    
     
     lados_rectangulos = np.append(lados_rectangulos, 20) 
     lados_rectangulos = np.append(lados_rectangulos, 50)
     coordinates[0]=numeros_derecha[0]
     
     
     print(f"sigue: {count}")
     draw_same_squares_rectangle(rama_count,10,t,h,600,600,-(600/2)-lados_rectangulos[h-2]/2)

     coordinates[0]=numeros_derecha[0]
     coordinates[1]=numeros_derecha[1]
     count -= rama_count

    
     draw_same_squares_rectangle(rama_count,10,t,h,600,600,(-600/2)+(lados_rectangulos[h-2]/2)+20)
     count -= rama_count

     coordinates[0]=numeros_derecha[0]-(600/2)
     coordinates[1]=numeros_derecha[1]-lados_rectangulos[h+1]
     return 


def work_with_squares(t,rectangle_width,rectangle_height,distancia_hasta_el_borde_x,distancia_hasta_el_borde_y,old_width,old_heigth,h,distancia_hasta_el_borde_oldl):
    global perimetro
    global numeros_ramas_derecha
    global numeros_derecha
    global numeros_cuadrado
    global numeros_derecha_cuadrados
    global lados_ramas 
    global lados_rectangulos
    lado_cuadrado = 10    
    print(f"lado_cuadrado: {lado_cuadrado}") 
    print(f"rectangle_width: {rectangle_width}") 
    print(f"rectangle_height: {rectangle_height}") 

    area_total=abs(rectangle_width*rectangle_height)
    count= int(area_total/lado_cuadrado**2)
    
    if(rectangle_height > distancia_hasta_el_borde_y or rectangle_width > 600) :
       print("h:", h)
       print("lados_rectangulos[h]:", lados_rectangulos[h])
       if(lados_rectangulos[h]>0):
        print("El rectangulo no cabe en el espacio restante")  
       
        print("count:", count)
       
        rama_height=int(lados_rectangulos[-1]/3)#int(((distancia_hasta_el_borde_x**2)+(distancia_hasta_el_borde_y**2))**0.5)
        
      
        rama_width=int(lados_rectangulos[-2]/3)
        print(f"lados_ramas: {lados_ramas}") 
       
        nivel_ramas = 0
        global MAX_DEPTH
        MAX_DEPTH = 1
        coordinates[0]=numeros_derecha[-2]-lados_rectangulos[h]#/2
        coordinates[1]=numeros_derecha[-1]
        numeros_derecha = np.append(numeros_ramas_derecha,coordinates)
        
        rama_count=int(count/2)
        print("rama_count:", rama_count)
        hoja(t,0,rama_height,rama_width,count,rama_count,h)
        print(f"Perimetro ahora1: {perimetro}")
          
    if(rectangle_height <= distancia_hasta_el_borde_y and rectangle_width < 600) :
       if(lados_rectangulos[h]>0):  
         print("El rectangulo cabe en el espacio restante") 
         new_heigth=rectangle_height
         new_width=rectangle_width
         perimetro+=(new_width*2)+(new_heigth*2)
         print(f"Perimetro ahora: {perimetro}") 
         
         print(f"lado_cuadrado: {lado_cuadrado}") 
         print(f"coordinates: {coordinates}") 
         print(f"t: {t}") 
         print(f"h: {h}") 
         count= int(area_total/lado_cuadrado**2)
         print(f"count: {count}")
         print(f"coordinates[1] en work_with_squares: {coordinates[1]}") 
         if(count>0):
          draw_same_squares_rectangle(count,lado_cuadrado,t,h,old_width,old_heigth,numeros_derecha[0]-(600/2))

        
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

     print(f"h: {h}")      
     print(f"lados_rectangulos[h]: {lados_rectangulos[h]}") 
     print(f"lados_rectangulos[h+1]: {lados_rectangulos[h+1]}") 
      
     distancia_hasta_el_borde_y = abs(numeros_derecha[1]-coordinates[1])
     distancia_hasta_el_borde_x = (main_width/2) 
    
     print(f"distancia_hasta_el_borde_y : {distancia_hasta_el_borde_y }") 
     print(f"distancia_hasta_el_borde_x: {distancia_hasta_el_borde_x}")
   

     work_with_squares(t,lados_rectangulos[h],lados_rectangulos[h+1],distancia_hasta_el_borde_x,distancia_hasta_el_borde_y,main_width,main_height,h,distancia_hasta_el_borde_old)     
                  
  
     h+=2
     coordinates[0]=lados_rectangulos[h-2]-(lados_rectangulos[h-2]/2)-(lados_rectangulos[h]/2) #coordinates[0]=numeros_derecha[h]-(lados_rectangulos[h-2]/2)-(main_width/2)
     
     print(f"coordinates[1] en nested rectangles: {coordinates[1]}")
     print(f"coordinates[1]: {coordinates[1]}")
     numeros_derecha = np.append(numeros_derecha, coordinates) 

    # Finalizar
    window.update()
    window.mainloop()   
# Parámetros: rectángulo principal y subrectángulo

draw_nested_rectangles()