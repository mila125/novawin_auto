import turtle
import array
def dibujar(maxsize,minsize,angle,x,y):
    tortuga = turtle.Turtle()
    tortuga.set_agle=angle
    tortuga.set_x=x
    tortuga.set_y=y
    saved_x=tortuga(x) #guardo x inicial
    saved_y=tortuga(y) #guardo x inicial
    while(squirtle>minsize):

      
      squirtle=maxsize #empezamos con el maximo
      while(sqrt(squirtle)%int(sqrt(squirtle))>0):
        squirtle=quirtle-minsize
        
      while(maxsize > = squirtle): #Aun quedan ?
        saved_x_prima=tortuga(x) #guardo x inicial
        maxsize=maxsize-squirtle #quito bloque
        for _ in range(4):
         tortuga.forward(sqrt(squirtle))
         tortuga.right(sqrt(squirtle))
        max_distance=max_distance+squirtle
        min_width=squirtle
        tortuga.set(x)=saved_x_prima
        tortuga.forward(sqrt(squirtle))
    tortuga.set(x)=saved_x
    tortuga.set(y)=saved_y
    
    saved_x_prima=saved_x
    
    while(maxsize>0):
      for _ in range(4):
        tortuga.forward(sqrt(squirtle))
        tortuga.right(sqrt(squirtle))
        tortuga.set(x)=saved_x_prima
        maxsize=maxsize-squirtle
        tortuga.forward(sqrt(squirtle))
        if(max_distance==recorred_distance):
         tortuga.rigth(1)
         max_distance=min_width
        if(tortuga.color.is_white): 
         tortuga.rigth(1)
         while(tortuga.color.is_white):
           tortuga.forward(1)
         tortuga.left(1)
    coordinates = [] 
    coordinates.append(saved_x_prima)
    coordinates.append(saved_y_prima)
    coordinates.append(turtle(get_angle))
    return(coordinates)
px2 = []
px2.append(9033)
px2.append(6178)
px2.append(24758)
px2.append(77066)
px2.append(55300)

print(px2)
minsize=2
maxsize=px2[0]
x=0
y=0

angle=90


color=red
coordinates = dibujar(maxsize,minsize,angle,x,y,color)

maxsize=px2[1]

x=coordinates[0]
y=coordinates[1]
angle=coordinates[2]


color=orange
coordinates = dibujar(maxsize,minsize,angle,x,y,color)

maxsize=px2[2]

x=coordinates[0]
y=coordinates[1]
angle=coordinates[2]


color=yellow
coordinates = dibujar(maxsize,minsize,angle,x,y,color)

maxsize=px2[3]

x=coordinates[0]
y=coordinates[1]
angle=coordinates[2]


color=green
coordinates = dibujar(maxsize,minsize,angle,x,y,color)

maxsize=px2[4]

x=coordinates[0]
y=coordinates[1]
angle=coordinates[2]



color=blue
coordinates = dibujar(maxsize,minsize,angle,x,y,color)