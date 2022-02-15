#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from OpenGL.GL import *
from glew_wish import *
import glfw
import math

#unidades por segundo
velocidad = 0.5
posicion_triangulo = [0.2,0.0,0.0]
posicion_cuadrado = [-0.2, 0.0, 0.0]
window = None

tiempo_anterior = 0.0

def actualizar():
    global tiempo_anterior
    global window
    global posicion_triangulo
    global posicion_cuadrado

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    colision_triangulo_cuadrado = colisionando(
        posicion_triangulo[0],posicion_triangulo[1],
        0.05,0.05,0.05,0.05,
        posicion_cuadrado[0], posicion_cuadrado[1],
        0.05,0.05,0.2,0.2)

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta
    if estado_tecla_arriba == glfw.PRESS:
        if not colisionando(
            posicion_triangulo[0],posicion_triangulo[1] + cantidad_movimiento,
            0.05,0.05,0.05,0.05,
            posicion_cuadrado[0], posicion_cuadrado[1],
            0.05,0.05,0.2,0.2):
            posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
    
    if estado_tecla_derecha == glfw.PRESS:
        if not colisionando(
            posicion_triangulo[0] + cantidad_movimiento,posicion_triangulo[1],
            0.05,0.05,0.05,0.05,
            posicion_cuadrado[0], posicion_cuadrado[1],
            0.05,0.05,0.2,0.2):
            posicion_triangulo[0] = posicion_triangulo[0] + cantidad_movimiento
    if estado_tecla_abajo == glfw.PRESS:
        if not colisionando(
            posicion_triangulo[0],posicion_triangulo[1] - cantidad_movimiento,
            0.05,0.05,0.05,0.05,
            posicion_cuadrado[0], posicion_cuadrado[1],
            0.05,0.05,0.2,0.2):
            posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
    if estado_tecla_izquierda == glfw.PRESS:
        if not colisionando(
            posicion_triangulo[0] - cantidad_movimiento,posicion_triangulo[1],
            0.05,0.05,0.05,0.05,
            posicion_cuadrado[0], posicion_cuadrado[1],
            0.05,0.05,0.2,0.2):
            posicion_triangulo[0] = posicion_triangulo[0] - cantidad_movimiento

    if estado_tecla_w == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] + cantidad_movimiento
    if estado_tecla_d == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
    if estado_tecla_s == glfw.PRESS:
        posicion_cuadrado[1] = posicion_cuadrado[1] - cantidad_movimiento
    if estado_tecla_a == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento

    tiempo_anterior = tiempo_actual
    
def colisionando(x1,y1,wl1,wr1,hu1,hd1,x2,y2,wl2,wr2,hu2,hd2):
    colisionando = False
    #Método de bounding box:
    #Extrema derecha del primero >= Extrema izquierda segundo
    #Extrema izquierda del primero <= Extrema derecha segundo
    #Extremo superior del primero >= Extremo inferior del segundo
    #Extremo inferior del primero <= Extremo superior del segundo
    if (x1 + wr1 >= x2 - wl2 
        and x1 - wl1 <= x2 + wr2 
        and y1 + hu1 >= y2 - hd2 
        and y1 - hd1 <= y2 + hu2):
        
        colisionando = True 
    return colisionando

def draw_triangulo():
    global posicion_triangulo
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1],0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    if colisionando(posicion_triangulo[0],posicion_triangulo[1],
        0.05,0.05,0.05,0.05,
        posicion_cuadrado[0], posicion_cuadrado[1],
        0.05,0.05,0.2,0.2):
        glColor3f(0,0,1)
    else:
        glColor3f(1,0,0)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.05, -0.05, 0)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05, 0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glEnd()

    glPopMatrix()

def draw_cuadrado():
    global posicion_cuadrado
    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.9, 0.21)
    glVertex3f(-0.05,0.2,0.0)
    glVertex3f(0.05,0.2,0.0)
    glVertex3f(0.05,-0.2,0.0)
    glVertex3f(-0.05,-0.2,0.0)
    glEnd()
    
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.05,0.2,0.0)
    glVertex3f(0.05,0.2,0.0)
    glVertex3f(0.05,-0.2,0.0)
    glVertex3f(-0.05,-0.2,0.0)
    glEnd()

    glPopMatrix()

def draw():
    draw_triangulo()
    draw_cuadrado()


def main():
    global window

    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        actualizar()
        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()



    
    