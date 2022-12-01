import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import *

deltaX = 0
deltaY = 0

boolGerakX= False
Gerak = False
pos_x = 0
pos_x2 = 0

Merah = 0
Hijau = 0





def square():
    glPushMatrix()
    global pos_x
    glColor3ub(204, 172, 0) #kuning gelap
    glTranslated(pos_x, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-650, 0) #titik c
    glVertex2f(-550, 0) #titik e
    glVertex2f(-550, -150)#titik f
    glVertex2f(-650, -150) #titik d
    glEnd()
    glPopMatrix()


def square2():
    glPushMatrix()
    global pos_x2, pos_y2

    glColor3ub(204, 172, 0) #kuning gelap
    glTranslated(pos_x2, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-650, 0) #titik c
    glVertex2f(-550, 0) #titik e
    glVertex2f(-550, -150)#titik f
    glVertex2f(-650, -150) #titik d
    glEnd()
    glPopMatrix()

def line():
    glPushMatrix()
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(-700, -150) #titik a
    glVertex2f(750, -150) #titik b
    glEnd()
    glPopMatrix()

def lingkaran_polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def lampu():
    global Merah,Hijau

    glPushMatrix()
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(-140, 260) #titik e
    glVertex2f(-140, 140) #titik h
    glVertex2f(140, 140)#titik g
    glVertex2f(140, 260) #titik f
    glEnd()
    glColor3f(Merah,0,0)
    lingkaran_polygon(-55, 200,50,100) #titik A
    glColor3f(0,Hijau,0)
    lingkaran_polygon(55, 200,50,100) #titik C
    glPopMatrix()

def keyboard_coba(key,x,y):
    global Gerak
    global boolGerakX
    if key == GLUT_KEY_RIGHT:
        boolGerakX=True

    if key == GLUT_KEY_LEFT:
        boolGerakX=False

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
        print("Tombol Kanan ditekan ", "x : ", pos_x)
        if Gerak == False:
            print('Game Over')
    elif key == GLUT_KEY_LEFT :
        pos_x -= 5
        print("Tombol Kiri ditekan ", "x : ", pos_x)
    
    if pos_x == -1235:
        print('you Win')
def time():
    global Merah,Hijau,Gerak
    import time
    localtime = time.localtime(time.time())
    # print ("Local current time :", localtime)
    # print(localtime.tm_sec)
    #kelemahan: lampu hijau selalu hanya 1  detik
    if int(localtime.tm_sec) % 5 == 0:
        print('Lampu Hijau')
        Hijau = 1
        Merah = 0
        Gerak = True
    else: 
        Merah = 1
        Hijau = 0
        Gerak = False


    # if int(localtime.tm_sec) % 3 == 0:
    #     print("lampu Merah")
    #     Merah =1
    # else:
    #     Merah = 0
        
        


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
    lampu()
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
