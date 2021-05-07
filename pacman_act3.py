#Tabatha Gaytan Lopez
#A00827656
#Reflexión: Tuve un mavore entendimiento del código y el propósito de cada línea de manera individual.
#Problemas: Tuve problemas para hacer los fantasmas más inteligentes, ya que realicé este ceodigo de manera individual.
#Resolución: utilizando los conceptos de trabajos anteriores, al igual que consultar la grabación de la clase.

#Jueves 6 de mayo 2021

#imports de la librerias
from random import choice
from turtle import * #el * significa importar todo, en este caso de la libreria de turtle
from freegames import floor, vector

#almacena el score del juego (cantidad de galletas consumidas)
state = {'score': 0}
#hace invisible la turtle, asimismo creando 2 objetos de la clase turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)
#dirección el pacman
aim = vector(5, 0)
#crea el pacman en esta posición
pacman = vector(-40, -80)
#lista de listas de los fantasmas
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
#arreglo del tablero (20 columnas con 20 reglones = 400 tiles)
tiles = [
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

#dibuja un square con su esquina inferior izquierda en (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

#retornar True si point es un tile válido (que no tenga pared)
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    #si la celda es cero = pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

#dibuja el tablero
def world():
    "Draw world using path."
    bgcolor('black')
    path.color('darkviolet')
    
    #recorre toda la lista de tiles
    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            #dibuja la galleta en el square
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(4, 'white')

def move():
    colores = ['blue','green','cyan','pink']
    "Move pacman and all ghosts."
    writer.undo()
    #writer.write(state['score'])
    valor = state['score']
    writer.write(f' Score: {valor}')

    clear()

    #si es una posición válida del pacman
    if valid(pacman + aim):
        pacman.move(aim)

    #retorna la posición del pacman
    index = offset(pacman)

    #1 - camino
    if tiles[index] == 1:
        #a esa posición le asigna 2 - comer la galleta
        tiles[index] = 2
        #se incremementa el score
        state['score'] += 1
        #calcula la posición (x,y) del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        #dibuja el square sin galleta
        square(x, y)

    up()
    #se va a la posición del pacman
    goto(pacman.x + 10, pacman.y + 10)
    #dibuja el pacman
    dot(20, 'yellow')
    
    k = 0
    
     for point, course in ghosts:
        #valida si el fantasma se puede mover
        #FANTASMA MÁS INTELIGENTE
        if pacman.x > point.x and valid(point + vector(5,0)):
            course = vector(5,0)
            point.move(course)

        elif pacman.x < point.x and valid(point + vector(-5,0)):
            course = vector(-5,0)
            point.move(course)
        
        elif pacman.y > point.y and valid(point + vector(0,5)):
            course = vector(0,5)
            point.move(course)
            
        elif pacman.y < point.y and valid(point + vector(0,-5)):
            course = vector(0,-5)
            point.move(course)
            
        #si el fantasma no se puede mover
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            #guarda la nueva posición del fantasma
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

    update()

    #recorre la lista de fantasmas para observar si colisionaron con el pacman
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-120,0)            
            writer.write('GAME OVER',font = ('Arial',30,'bold'))
            return
    #velocidad
    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

#tamaño de la ventana
setup(420, 420, 370, 0)
hideturtle()
#oculta forma de dibujar
tracer(False)
writer.goto(160, 160)
writer.color('white')
valor = state['score']
writer.write(f' Score: {valor}')
listen()
#teclado que determina la dirección del pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
