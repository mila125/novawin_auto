import turtle

def draw_rectangle(t, x, y, width, height):
    """
    Dibuja un rectángulo dado su posición inicial y dimensiones.
    Devuelve las nuevas coordenadas (X, Y) de la esquina superior derecha en un arreglo.
    """
    # Guardar la posición inicial del rectángulo
    start_x = x
    start_y = y

    # Dibujar el rectángulo
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    # Calcular las nuevas coordenadas de la esquina superior derecha
    new_x = x + width
    new_y = y + height

    # Devolver las coordenadas actualizadas en un array
    return [new_x, new_y]

def draw_nested_rectangles(main_width, main_height):
    """Dibuja un rectángulo principal y subrectángulos uniformemente dentro de él."""
    # Configuración de la ventana
    window = turtle.Screen()
    window.title("División de Rectángulos")
    window.setup(width=600, height=600)  # Tamaño de la ventana en píxeles
    window.tracer(0)  # Deshabilitar animación para dibujo más rápido

    t = turtle.Turtle()
    t.speed(0)  # Máxima velocidad

    # Dibujar el rectángulo principal
    main_x = -main_width / 2
    main_y = -90 #abajoo
    coordinates=draw_rectangle(t, main_x, main_y, main_width, -main_height)
    main_height_old=main_height
    main_width_old=main_width

    main_width=42
    main_height=80
    
    main_y = coordinates[1] #arriba del hermano mayor
    print(main_y)
    main_y=main_y+main_height_old
    
    main_x = coordinates[0]
    main_x=main_x-main_width_old/2-main_width/2
    
    coordinates=draw_rectangle(t, main_x, main_y, main_width, main_height)
 
    main_height_old=main_height
    main_width_old=main_width

    main_width=10
    main_height=50
    
    main_y = -coordinates[1] #arriba del hermano mayor
    print(main_y)
    main_y=main_y+main_height_old-main_height

    main_x = coordinates[0]
    main_x=main_x-main_width_old/2-main_width/2
    coordinates=draw_rectangle(t, main_x, main_y, main_width, -main_height)
    
    main_height_old=main_height
    main_width_old=main_width

    main_width=10
    main_height=70
    
    main_y = coordinates[1] #arriba del hermano mayor
    print(main_y)
    main_y=main_y+main_height_old
    
    main_x = coordinates[0]
    main_x=main_x-main_width_old/2-main_width/2
    
    coordinates=draw_rectangle(t, main_x, main_y, main_width, main_height)
    # Finalizar
    window.update()
    window.mainloop()

# Parámetros: rectángulo principal y subrectángulo
main_width = 300
main_height = 200
sub_width = 120
sub_height = 100
coordinates=draw_nested_rectangles(main_width, main_height)