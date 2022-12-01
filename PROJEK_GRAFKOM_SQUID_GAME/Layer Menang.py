import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


def background():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    glBegin(GL_QUADS)
    # //red color
    glColor3ub(0,0,0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0,-1.0)
    # //blue color
    glColor3ub(204, 172, 0)
    glVertex2f(1.0,-1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def tulisan_winner():

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    # Huruf w
    glVertex2f(-560, 260) #titik b1
    glVertex2f(-520, 260) #titik n1
    glVertex2f(-490, 140) # titik o1
    glVertex2f(-520, 100) #titik c1

    glVertex2f(-520, 100) #titik c1
    glVertex2f(-440, 260) #titik q1
    glVertex2f(-440, 180) #titik i1
    glVertex2f(-460, 100) #titik d1

    glVertex2f(-440, 260) #titik q1
    glVertex2f(-440, 180) #titik i1
    glVertex2f(-420, 100) #titik j1
    glVertex2f(-390, 140) #titik s1

    glVertex2f(-420, 100) #titik j1
    glVertex2f(-360, 260) #titik m1
    glVertex2f(-320, 260) #titik l1
    glVertex2f(-360, 100) #titik k1
    
    # Huruf n
    glVertex2f(-300, 260) #titik p1
    glVertex2f(-260, 260) #titik t1
    glVertex2f(-260, 100) # titik u1
    glVertex2f(-300, 100) #titik r1

    # Huruf n
    glVertex2f(-240, 260) #titik a2
    glVertex2f(-200, 260) #titik g2
    glVertex2f(-199, 60) #titik w1
    glVertex2f(-240, 60) # titik v1

    glVertex2f(-200, 200) #titik z1
    glVertex2f(-200, 260) #titik g2
    glVertex2f(-120, 160) #titik f2
    glVertex2f(-120, 100) # titik b2

    glVertex2f(-120, 260) #titik e2
    glVertex2f(-120, 100) #titik b2
    glVertex2f(-80, 100) # titik c2
    glVertex2f(-80, 260) #titik d2


    # Huruf n #2
    glVertex2f(-60, 260) #titik a3
    glVertex2f(-20, 260) #titik g3
    glVertex2f(-20, 60) #titik w2
    glVertex2f(-60, 60) # titik v2

    glVertex2f(-20, 200) #titik z2
    glVertex2f(-20, 260) #titik g3
    glVertex2f(60, 160) #titik f3
    glVertex2f(60, 100) # titik b3

    glVertex2f(60, 260) #titik e3
    glVertex2f(60, 100) #titik b3
    glVertex2f(100, 100) # titik c3
    glVertex2f(100, 260) #titik d3

    # Huruf e
    glVertex2f(140, 260) #titik h2
    glVertex2f(280, 260) #titik k2
    glVertex2f(280, 220) #titik l2
    glVertex2f(140, 220) # titik j6

    glVertex2f(140, 260) #titik h2
    glVertex2f(180, 260) #titik k6
    glVertex2f(180, 100) #titik m6
    glVertex2f(140, 100) # titik i2

    glVertex2f(140, 140) #titik l6
    glVertex2f(140, 100) # titik i2
    glVertex2f(280, 100) # titik j2
    glVertex2f(280, 140) #titik o2
    
    glVertex2f(220, 200) #titik p2
    glVertex2f(220, 160) # titik q2
    glVertex2f(360, 160) # titik r2
    glVertex2f(360, 200) #titik s2

    # Huruf R
    glVertex2f(400, 260) #titik t2
    glVertex2f(440, 260) #titik i3
    glVertex2f(440, 100) #titik h3
    glVertex2f(400, 100) # titik u2

    glVertex2f(440, 260) #titik i3
    glVertex2f(500, 260) #titik j3
    glVertex2f(500, 230) # titik r3
    glVertex2f(440, 230) #titik q3

    glEnd()

    #//3
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(500, 260) #titik j3
    glVertex2f(520,256) #titik o6
    glVertex2f(540,240) #titik p6
    glVertex2f(550,210) #titik q6
    glVertex2f(540,180) #titik r6
    glVertex2f(520,164) #titik s6
    glVertex2f(500, 160) #titik l3
    glEnd()# Mengakhiri objek   

    #//3 dalam r
    glColor3f(0,0,0) #warma pink squid game
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(500, 230) #titik r3
    glVertex2f(517,220) #titik t6
    glVertex2f(518,201) #titik u6
    glVertex2f(500, 190) #titik p3
    glEnd()# Mengakhiri objek  ]

    #//4
    glColor3f(1,1,1)
    glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(500, 160) #titik l3
    glVertex2f(480,190) #titik n6
    glVertex2f(500, 190) #titik p3
    glVertex2f(520,164) #titik s6
    glEnd()# Mengakhiri objek

    #//5
    glColor3f(1,1,1)
    glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(450, 190) #titik 06
    glVertex2f(480,190) #titik n6
    glVertex2f(560, 80) #titik m3
    glVertex2f(530, 80) #titik n3
    glEnd()# Mengakhiri objek   
 

def emas():
    
    glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    #sisi depan
    glColor3ub(255,215,0) #warna emas
    glVertex2f(100, -140) #titik e
    glVertex2f(100, -300) #titik l
    glVertex2f(540, -300) #titik q
    glVertex2f(540, -140) #titik p

    #sisi atas
    glColor3ub(230, 198, 25)
    glVertex2f(100, -140) #titik e
    glVertex2f(540, -140) #titik p
    glVertex2f(600, -80) #titik s
    glVertex2f(160, -80) #titik r

    #sisi kanan
    glColor3ub(204, 172, 0)
    glVertex2f(540, -140) #titik p
    glVertex2f(540, -300) #titik q
    glVertex2f(600, -240) #titik t
    glVertex2f(600, -80) #titik s
    glEnd()# Mengakhiri objek

def Nominal_emas():
    #huruf S
    glColor3ub(204, 172, 0) #kuning gelap
    glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    #//1
    glVertex2f(130, -250) #titik i5
    glVertex2f(130, -260) #titik n5
    glVertex2f(180, -260) #titik u5
    glVertex2f(180, -250) #titik a6
    glEnd()

    #//2
    glBegin(GL_POLYGON)
    glVertex2f(180, -225) #titik v6
    glVertex2f(188, -227) #titik j7
    glVertex2f(194, -233) #titik i7
    glVertex2f(197, -243) #titik h7
    glVertex2f(194, -253) #titik g7
    glVertex2f(188, -258) #titik e7
    glVertex2f(180, -260) #titik u5
    glEnd()

    #//3
    glBegin(GL_QUADS)
    glVertex2f(180, -225) #titik v6
    glVertex2f(180, -235) #titik b7
    glVertex2f(160, -235) #titik c7
    glVertex2f(160, -225) #titik w6
    glEnd()

    #//4
    glBegin(GL_POLYGON)
    glVertex2f(160, -235) #titik c7
    glVertex2f(150, -232) #titik d7
    glVertex2f(144, -224) #titik f7
    glVertex2f(143, -214) #titik k7
    glVertex2f(147, -206) #titik l7
    glVertex2f(155, -201) #titik n7
    glVertex2f(160, -200) #titik g6
    glEnd()


    #//4
    glBegin(GL_QUADS)
    glVertex2f(160, -200) #titik g6
    glVertex2f(160, -210) #titik z6
    glVertex2f(198, -210) #titik a8
    glVertex2f(198, -200) #titik e6
    glEnd()

    #garis
    glBegin(GL_QUADS)
    glVertex2f(166, -184) #titik p7
    glVertex2f(174, -184) #titik q7
    glVertex2f(174, -276) #titik s7
    glVertex2f(166, -276) #titik r7
    glEnd()

    #angka 4
    #//1
    glBegin(GL_QUADS)
    glVertex2f(250, -200) #titik h5
    glVertex2f(245, -206) #titik t7
    glVertex2f(245, -270) #titik d5
    glVertex2f(250, -270) #titik g5

    #//2
    glVertex2f(210, -245) #titik j5
    glVertex2f(214, -240) #titik u7
    glVertex2f(245, -240) #titik c5
    glVertex2f(245, -245) #titik m5

    #//3
    glVertex2f(210, -245) #titik j5
    glVertex2f(214, -245) #titik v7
    glVertex2f(250, -210) #titik w7
    glVertex2f(250, -200) #titik h5

    glEnd()   

def logo_bitcoin():
    glColor3ub(204, 172, 0) #kuning gelap
    #garis 
    glBegin(GL_QUADS)
    glVertex2f(-500, -90) #titik k4
    glVertex2f(-480, -90) #titik l4
    glVertex2f(-480, -330)#titik q4
    glVertex2f(-500, -330) #titik p4

    #garis #2
    glVertex2f(-460, -90) #titik t4
    glVertex2f(-440, -90) #titik u4
    glVertex2f(-440, -330) #titik z4
    glVertex2f(-460, -330) #titik w4

    #Huruf B
    #//1
    glVertex2f(-520, -120) #titik z
    glVertex2f(-500, -120) #titik m4
    glVertex2f(-500, -300) #titik 04
    glVertex2f(-520, -300) #titik a1

    #//2
    glVertex2f(-520, -120) #titik z
    glVertex2f(-520, -140) #titik z7
    glVertex2f(-440, -140) #titik c4
    glVertex2f(-440, -120) #titik k3
    glEnd()

    #//3
    glBegin(GL_POLYGON)
    glVertex2f(-440, -120) #titik k3
    glVertex2f(-420, -123) #titik d8
    glVertex2f(-400, -144) #titik e8
    glVertex2f(-395, -160) #titik f8
    glVertex2f(-400, -180) #titik g8
    glVertex2f(-413, -194) #titik h8
    glVertex2f(-440, -200) #titik c8
    glEnd()

    #//4
    glColor3ub(255, 217, 0) #kuning emas
    glBegin(GL_POLYGON)
    glVertex2f(-440, -140) #titik c4
    glVertex2f(-427, -144) #titik r8
    glVertex2f(-417, -161) #titik q8
    glVertex2f(-425, -179) #titik p8
    glVertex2f(-440, -185) #titik z3
    glEnd()

    #//4
    glColor3ub(204, 172, 0) #kuning gelap
    glBegin(GL_QUADS)
    glVertex2f(-440, -185) #titik z3
    glVertex2f(-440, -200) #titik c8
    glVertex2f(-520, -199)#titik s3
    glVertex2f(-500, -185) #titik i8

    #//5
    glVertex2f(-440, -200) #titik c8
    glVertex2f(-520, -199)#titik s3
    glVertex2f(-520, -215)#titik j8
    glVertex2f(-440, -215) #titik j4
    glEnd()

    #//6
    glBegin(GL_POLYGON)
    glVertex2f(-440, -200) #titik c8
    glVertex2f(-430, -200) #titik t3
    glVertex2f(-403, -211) #titik k8
    glVertex2f(-389, -230) #titik l8
    glVertex2f(-385, -251) #titik m8
    glVertex2f(-392, -276) #titik o8
    glVertex2f(-408, -293) #titik n8
    glVertex2f(-440, -300) #titik u3
    glEnd()

    #//7
    glColor3ub(255, 217, 0) #kuning emas
    glBegin(GL_POLYGON)
    glVertex2f(-440, -215) #titik j4
    glVertex2f(-421, -221) #titik u8
    glVertex2f(-409, -237) #titik v8
    glVertex2f(-409, -259) #titik w8
    glVertex2f(-421, -274) #titik z8
    glVertex2f(-440, -280) #titik i4
    glEnd()

    # //8
    glColor3ub(204, 172, 0) #kuning gelap
    glBegin(GL_QUADS)
    glVertex2f(-440, -280) #titik i4
    glVertex2f(-440, -300) #titik u3
    glVertex2f(-520, -300)#titik a1
    glVertex2f(-520, -280) #titik b8
    glEnd()


def player():
    glColor3f(0,1,0) #kuning gelap
    glBegin(GL_LINES)
    glVertex2f(-270, -100) #titik h
    glVertex2f(-270, -280) #titik i

    glVertex2f(-270, -280) #titik i
    glVertex2f(-300, -340) #titik j

    glVertex2f(-270, -280) #titik i
    glVertex2f(-200, -340) #titik k

    glVertex2f(-270, -160)#titik o
    glVertex2f(-370, -80) #titik n

    glVertex2f(-270, -160)#titik o
    glVertex2f(-160, -120) #titik u

    glEnd()





def lingkaran_polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def Circle():
    glColor3ub(255, 217, 0)
    lingkaran_polygon(-450, -200, 140, 100) #keping bitcoin
    
    glColor3ub(204, 172, 0) #kuning gelap
    lingkaran_polygon(265, -245, 15, 60) #titik e5
    lingkaran_polygon(295, -245, 15, 60) #titik k5
    lingkaran_polygon(325, -245, 15, 60) #titik o5
    lingkaran_polygon(355, -245, 15, 60) #titik q5
    lingkaran_polygon(385, -245, 15, 60) #titik v5
    lingkaran_polygon(415, -245, 15, 60) #titik z5
    lingkaran_polygon(445, -245, 15, 60) #titik c6
    lingkaran_polygon(475, -245, 15, 60) #titik s5
    lingkaran_polygon(505, -245, 15, 60) #titik f6

    glColor3ub(255,215,0) #warna emas

    lingkaran_polygon(265, -245, 10, 60) #titik e5
    lingkaran_polygon(295, -245, 10, 60) #titik k5
    lingkaran_polygon(325, -245, 10, 60) #titik o5
    lingkaran_polygon(355, -245, 10, 60) #titik q5
    lingkaran_polygon(385, -245, 10, 60) #titik v5
    lingkaran_polygon(415, -245, 10, 60) #titik z5
    lingkaran_polygon(445, -245, 10, 60) #titik c6
    lingkaran_polygon(475, -245, 10, 60) #titik s5
    lingkaran_polygon(505, -245, 10, 60) #titik f6 

    glColor3f(0,1,0)
    lingkaran_polygon(-270, -80, 40, 60) #titik e5



def layer_kalah():
    tulisan_winner()
    emas()
    Circle()
    Nominal_emas()
    logo_bitcoin()
    player()


def iterate():
    glViewport(0, 0, 1364, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-682,682,-350,350)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #letak background
    background() 
    iterate()
    #letak objek   
    layer_kalah()

  


    glutSwapBuffers()
def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1364, 700)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Layer Menang")
    # timer(0) #fungsi timer dipanggil disini
    glutDisplayFunc(ShowScreen)
    # glutMouseFunc(iniHandleMouse)
    glutIdleFunc(ShowScreen)
    glutMainLoop()

Main()

