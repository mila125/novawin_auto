import turtle


def dibujar_torre_o_arbol_fractal(tortuga, x, y, lado, nivel, minsize, lado_viejo):
    if nivel == 0 or lado < minsize:
        return  # Detener si el nivel es 0 o el lado es menor que el tamaño mínimo

    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.fillcolor("green")
    tortuga.begin_fill()

    # Dibujar el cuadrado actual
    for _ in range(4):
        tortuga.forward(lado)
        tortuga.right(90)
    tortuga.end_fill()

    # Reducir el tamaño del siguiente nivel
    nuevo_lado = lado / 2
    nuevo_nivel = nivel - 1

    # Posición del siguiente cuadrado (apilado directamente arriba del anterior)
    nuevo_x_centro = x
    nuevo_y_centro = y + lado  # El nuevo cuadrado se dibuja justo encima del actual

    # Dibujar el cuadrado en el centro
    dibujar_torre_o_arbol_fractal(tortuga, nuevo_x_centro, nuevo_y_centro, nuevo_lado, nuevo_nivel, minsize, lado_viejo)

    # Dibujar los cuadrados a los lados (como ramas), también apilados
    offsets = [
        (x - nuevo_lado / 2, y + lado),  # Rama izquierda
        (x + lado - nuevo_lado / 2, y + lado),  # Rama derecha
    ]
    
    for nuevo_x, nuevo_y in offsets:
        dibujar_torre_o_arbol_fractal(tortuga, nuevo_x, nuevo_y, nuevo_lado, nuevo_nivel, minsize, lado_viejo)


# Configuración inicial
def main():
    turtle.speed(0)
    turtle.bgcolor("black")

    tortuga = turtle.Turtle()
    tortuga.color("white")
    tortuga.speed(0)  # Velocidad rápida para fractales

    # Parámetros iniciales de la torre/árbol fractal
    x, y = -50, -200  # Posición inicial
    lado_inicial = 100
    niveles = 5  # Profundidad de la recursión
    minsize = 10

    # Dibujar la torre/árbol fractal
    dibujar_torre_o_arbol_fractal(tortuga, x, y, lado_inicial, niveles, minsize, lado_inicial)

    tortuga.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
