import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


deltaX = 0
deltaY = 0

boolGerakX= False

pos_x = 0
pos_y = 0

pos_x2 = 0
pos_y2 = 0

collisionp1 = -250
collisionp2 = -250


def square():
    glPushMatrix()
    global pos_x, pos_y
    glColor3ub(204, 172, 0) #kuning gelap
    glTranslated(pos_x, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-250, -50) #titik c
    glVertex2f(-150, -50) #titik e
    glVertex2f(-150, -200)#titik f
    glVertex2f(-250, -200) #titik d
    glEnd()


def square2():
 

    glColor3ub(204, 172, 0) #kuning gelap
    glBegin(GL_QUADS)
    glVertex2f(150, -50) #titik c
    glVertex2f(250, -50) #titik e
    glVertex2f(250, -200)#titik f
    glVertex2f(150, -200) #titik d
    glEnd()


def line():

    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(-1500, -150) #titik a
    glVertex2f(1650, -150) #titik b
    glEnd()
    glPopMatrix()

def keyboard_coba(key,x,y):
    global boolGerakX
    if key == GLUT_KEY_RIGHT:
        boolGerakX=True
    if key == GLUT_KEY_LEFT:
        boolGerakX=False
def time():
    global pos_x
    import time
    localtime = time.localtime(time.time())
    # print ("Local current time :", localtime)
    # print(localtime.tm_sec)
    if localtime.tm_sec %2 == 1:
        pos_x += 0.02

def input_keyboard(key,x,y):
    global pos_x, pos_y
    # Untuk mengubah posisi kotak
    # if key == GLUT_KEY_UP :
    #     pos_y += 5
        # print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    # elif key == GLUT_KEY_DOWN :
    #     pos_y -= 5
        # print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    if key == GLUT_KEY_RIGHT :
        pos_x += 5
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT :
        pos_x -= 5
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)
    
    if pos_x == -435:
        print('P2 Win')
        pass
    elif pos_y == 435:
        print('P1 Win')
        pass


def iterate():
    glViewport(0, 0, 1364, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-682.,682.,-350.,350.)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #letak background



    iterate()
    #letak objek
    square()
    square2()
    line()
    time()
    glutSwapBuffers()
def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1364, 700)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Layer Menang")
    # timer(0) #fungsi timer dipanggil disini
    glutDisplayFunc(ShowScreen)
    glutSpecialFunc(input_keyboard)
    # glutMouseFunc(iniHandleMouse)
    glutIdleFunc(ShowScreen)
    glutMainLoop()

Main()
