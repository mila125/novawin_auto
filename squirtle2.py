import turtle
import math

def es_cuadrado_perfecto(n):
    raiz = math.sqrt(n)
    return raiz == int(raiz)
	
def dibujar(maxsize, minsize, angle, x, y, color):
    tortuga = turtle.Turtle()
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.setheading(angle)
    tortuga.pendown()
    tortuga.fillcolor(color)
    tortuga.begin_fill()
    
    while (maxsize >= minsize ** 2):
        # Encuentra el mayor cuadrado perfecto menor o igual a maxsize
        lado = int(math.sqrt(maxsize))
        area = lado ** 2
        
        # Dibuja un cuadrado
        for _ in range(4):
            tortuga.forward(lado)
            tortuga.right(90)
        
        # Ajusta `maxsize` para el siguiente cuadrado
        maxsize -= area
        tortuga.penup()
        tortuga.goto(tortuga.xcor(), tortuga.ycor() + lado)  # Sube para el siguiente
        tortuga.pendown()
    
    tortuga.end_fill()
    return tortuga.xcor(), tortuga.ycor(), tortuga.heading()

# Datos iniciales
px2 = [9033, 6178, 24758, 77066, 55300]
px2 = sorted(px2)
minsize = 2
angle = 90
x, y = 0, 0

# Iterar sobre los colores y tamaños
colores = ["red", "orange", "yellow", "green", "blue"]
for i, maxsize in enumerate(px2):
    # Seleccionar un vértice aleatorio del cuadrado más grande
    x, y, angle = dibujar(maxsize, minsize, angle, x, y, colores[i])

# Finalizar el dibujo
turtle.done()