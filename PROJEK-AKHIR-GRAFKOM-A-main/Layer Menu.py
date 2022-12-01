import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

# w, h = 1364, 700
x_time = 0 #utk gerak horizontal
y_time = 0 #utk gerak vertikal
# Warna
hijau = 1
biru = 1
merah = 1

hijau2 = 1
biru2 = 1
merah2 = 1

Pencet = False

PosisiX = 0
PosisiY = 0

mouseX=int
mouseY=int

# deltaX=0
# deltaY=0
# #membuat gerak bintang
# gerak_bintang_x =1
# gerak_bintang_y =2
# #colision bintang
# collision_bintang_x_1 = -508
# collision_bintang_y_1 = 394

# boolGerakX= False
# boolGerakY= False

gerakX=2
gerakY=4

# represent variabel perubahan yang dipakai di gltranslated
deltaX=0
deltaY=0

# represent arah gerak
boolGerakX= False
boolGerakY= False
# boolGerakY= False


mouseX=int
mouseY=int

collisionX1=-246
# collisionX[0]=manggil x1

# ===== SQUID GAME =====

def bg():
    glPushMatrix()
    # -=-=-=-=- Latar -=-=-=-=-
    glBegin(GL_QUADS)
    # BG layer 1
    glColor3ub(23, 21, 19)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    # Tanah
    glColor3ub(46, 46, 41)
    glVertex2f(-682, -350)
    glVertex2f(-682, -300)
    glVertex2f(682, -300)
    glVertex2f(682,-350)
    # BG layer 2
    glColor3ub(36, 36, 33)
    glVertex2f(-482, -250)
    glVertex2f(-482, 250)
    glVertex2f(482, 250)
    glVertex2f(482, -250)
    # BG layer 3
    glColor3ub(74, 74, 54)
    glVertex2f(-282, -150)
    glVertex2f(-282, 150)
    glVertex2f(282, 150)
    glVertex2f(282, -150)
    glEnd()

def frame():
    glBegin(GL_QUADS)
    # Frame atas
    glColor3ub(38, 38, 30)
    glVertex2f(-682, 350)
    glVertex2f(-642, 330)
    glVertex2f(642, 330)
    glVertex2f(682, 350)
    # Frame bawah
    glVertex2f(-682, -350)
    glVertex2f(-642, -330)
    glVertex2f(642, -330)
    glVertex2f(682, -350)
    # Frame kiri
    glVertex2f(-682, 350)
    glVertex2f(-662, 310)
    glVertex2f(-662, -310)
    glVertex2f(-682, -350)
    # Frame kanan
    glVertex2f(682, 350)
    glVertex2f(662, 310)
    glVertex2f(662, -310)
    glVertex2f(682, -350)
    glEnd()
    # Lampu Frame atas & lampu bawah
    def Lampu1(x):
        # Lampu frame atas
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(-601 + x, 340)
        glVertex2f(-597 + x, 335)
        glVertex2f(-593 + x, 340)
        glVertex2f(-597 + x, 345)

        # lampu frame bawah
        glVertex2f(-601 + x, -340)
        glVertex2f(-597 + x, -335)
        glVertex2f(-593 + x, -340)
        glVertex2f(-597 + x, -345)
        glEnd()

     # Lampu Frame kanan & lampu kiri
    def Lampu2(y):
        # Lampu frame kanan
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(676, 245 - y)
        glVertex2f(672, 240 - y)
        glVertex2f(668, 245 - y)
        glVertex2f(672, 250 - y)
        # lampu frame kiri
        glVertex2f(-676, 245 - y)
        glVertex2f(-672, 240 - y)
        glVertex2f(-668, 245 - y)
        glVertex2f(-672, 250 - y)
        glEnd()
    
    kor_x = (0,100,200,300,400,500,600,700,800,900,1000,1100,1200)
    kor_y = (0,100,200,300,400,500)
    for i in kor_x:
        Lampu1(i)
    for i in kor_y:
        Lampu2(i)

    # Kerangka Jembatan Kiri
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(-662, 0)
    glVertex2f(-662, -10)
    glVertex2f(-182, -10)
    glVertex2f(-182, 0)
    # Penopang miring
    glVertex2f(-542, -10)
    glVertex2f(-662, -80)
    glVertex2f(-662, -90)
    glVertex2f(-522, -10)
    # Besi Bawah
    glVertex2f(-572, -30)
    glVertex2f(-572, -35)
    glVertex2f(-282, -35)
    glVertex2f(-282, -30)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glVertex2f(-287, -10)
    glVertex2f(-287, -30)
    glVertex2f(-347, -10)
    glVertex2f(-347, -30)
    glVertex2f(-407, -10)
    glVertex2f(-407, -30)
    glVertex2f(-467, -10)
    glVertex2f(-467, -30)
    glVertex2f(-527, -10)
    glVertex2f(-527, -30)
    # Pegangan
    glVertex2f(-212, 0)
    glVertex2f(-212, 7.5)
    glVertex2f(-252, 0)
    glVertex2f(-252, 7.5)
    glVertex2f(-207, 7.5)
    glVertex2f(-257, 7.5)
    # --
    glVertex2f(-322, 0)
    glVertex2f(-322, 7.5)
    glVertex2f(-362, 0)
    glVertex2f(-362, 7.5)
    glVertex2f(-317, 7.5)
    glVertex2f(-367, 7.5)
    # --
    glVertex2f(-432, 0)
    glVertex2f(-432, 7.5)
    glVertex2f(-472, 0)
    glVertex2f(-472, 7.5)
    glVertex2f(-427, 7.5)
    glVertex2f(-477, 7.5)
    # --
    glVertex2f(-542, 0)
    glVertex2f(-542, 7.5)
    glVertex2f(-582, 0)
    glVertex2f(-582, 7.5)
    glVertex2f(-537, 7.5)
    glVertex2f(-587, 7.5)
    glEnd()

    # Kerangka Jembatan Kanan
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(662, 0)
    glVertex2f(662, -10)
    glVertex2f(182, -10)
    glVertex2f(182, 0)
    # Penopang miring
    glVertex2f(542, -10)
    glVertex2f(662, -80)
    glVertex2f(662, -90)
    glVertex2f(522, -10)
    # Besi Bawah
    glVertex2f(572, -30)
    glVertex2f(572, -35)
    glVertex2f(282, -35)
    glVertex2f(282, -30)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glVertex2f(287, -10)
    glVertex2f(287, -30)
    glVertex2f(347, -10)
    glVertex2f(347, -30)
    glVertex2f(407, -10)
    glVertex2f(407, -30)
    glVertex2f(467, -10)
    glVertex2f(467, -30)
    glVertex2f(527, -10)
    glVertex2f(527, -30)
    # Pegangan
    glVertex2f(212, 0)
    glVertex2f(212, 7.5)
    glVertex2f(252, 0)
    glVertex2f(252, 7.5)
    glVertex2f(207, 7.5)
    glVertex2f(257, 7.5)
    # --
    glVertex2f(322, 0)
    glVertex2f(322, 7.5)
    glVertex2f(362, 0)
    glVertex2f(362, 7.5)
    glVertex2f(317, 7.5)
    glVertex2f(367, 7.5)
    # --
    glVertex2f(432, 0)
    glVertex2f(432, 7.5)
    glVertex2f(472, 0)
    glVertex2f(472, 7.5)
    glVertex2f(427, 7.5)
    glVertex2f(477, 7.5)
    # --
    glVertex2f(542, 0)
    glVertex2f(542, 7.5)
    glVertex2f(582, 0)
    glVertex2f(582, 7.5)
    glVertex2f(537, 7.5)
    glVertex2f(587, 7.5)
    glEnd()
    glPopMatrix()
def logo():
    glPushMatrix()
    #bintang besar
    #//1
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-380,170) #titik t2
    glVertex2f(-460,170) #titik v2
    glVertex2f(-390,140) #titik w2
    glVertex2f(-420,70) #titik b3
    glVertex2f(-360,120) #titik c3
    glVertex2f(-300,70) #titik d3
    glVertex2f(-330,140) #titik a3
    glVertex2f(-260,170) #titik z2
    glVertex2f(-340,170) #titik u2
    glEnd()# Mengakhiri objek   

    #//2
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-361,232) #titik s2
    glVertex2f(-380,170) #titik t2
    glVertex2f(-340, 170) #titik u2
    glEnd()# Mengakhiri objek

    #segitiga besar
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-450,-230) #titik o
    glVertex2f(-370,-100) #titik N
    glVertex2f(-290,-230) #titik P
    glEnd()# Mengakhiri objek

    # daun payung 
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glVertex2f(460,140) #titik m
    glVertex2f(459,150) #titik p2
    glVertex2f(457,160) #titik n3
    glVertex2f(454,170) #titik o3
    glVertex2f(450,178) #titik r3
    glVertex2f(442,190) #titik s3
    glVertex2f(435,198) #titik a4
    glVertex2f(426,205) #titik c4
    glVertex2f(415,212) #titik i4
    glVertex2f(405,216) #titik m4
    glVertex2f(395,218) #titik o4
    glVertex2f(385,219) #titik p4
    glVertex2f(375,219) #titik b5
    glVertex2f(365,218) #titik q4
    glVertex2f(355,216) #titik r4
    glVertex2f(345,211) #titik w4
    glVertex2f(335,206) #titik e5
    glVertex2f(327,200) #titik g4
    glVertex2f(322,195) #titik j4
    glVertex2f(314,186) #titik n4
    glVertex2f(310,178) #titik d4
    glVertex2f(305,167) #titik s4
    glVertex2f(301,154) #titik t4
    glVertex2f(300,140) #titik l
    glEnd()

def pengangan_payung():
    #pengangan atas
    glBegin(GL_QUADS)
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glVertex2f(378, 166) #titik l3
    glVertex2f(382, 166) #titik m3
    glVertex2f(382, 60) #titik f5
    glVertex2f(378, 60) #titik d5
    glEnd()

    #Pengangan Bawah
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glVertex2f(378, 166) #titik l3
    glVertex2f(382, 166) #titik m3
    glVertex2f(382, 60) #titik f5
    glVertex2f(378, 60) #titik d5
    glEnd()


    #titik
    glPointSize(2) #menentukan besarnya titik
    glBegin(GL_POINTS)# memulai membuat sebuah objek, GL_POINTS untuk mengambar titik
    glColor3f(1.0, 1.0, 1.0) #menetapkan warna menjadi putih
    glVertex2f(-532,-280) # titik i
    glVertex2f(-627,-218) # titik j
    glVertex2f(-544,-112) # titik k
    glVertex2f(-625,-15) # titik t
    glVertex2f(-540,45) # titik u
    glVertex2f(-600,44) # titik v
    glVertex2f(-628,245) # titik w
    glVertex2f(-521,281) # titik z
    glVertex2f(-356,260) # titik a1
    glVertex2f(-94,277) # titik b1
    glVertex2f(165,264) # titik c1
    glVertex2f(376,284) # titik d1
    glVertex2f(626,202) # titik f1
    glVertex2f(503,41) # titik e1
    glVertex2f(631,-144) # titik j1
    glVertex2f(526,-268) # titik g1
    glVertex2f(272,-277) # titik h1
    glVertex2f(22,-264) # titik i1
    glVertex2f(-255,-286) # titik k1
    glEnd()# Mengakhiri objek

    glPopMatrix()

def lingkaran_polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def Circle():
    glColor3ub(36, 36, 33)
    lingkaran_polygon(440, 140, 20, 60)
    lingkaran_polygon(400, 140, 20, 60)
    lingkaran_polygon(360, 140, 20, 60)
    lingkaran_polygon(320, 140, 20, 60)
    glColor3f(1, 1, 1) #menetapkan warna menjadi putih
    lingkaran_polygon(380, -160, 74, 100) #logo lingkaran luar
    glColor3ub(36, 36, 33)
    lingkaran_polygon(380, -160, 63, 100) #logo lingkaran dalam
    glColor3f(1, 1, 1) #menetapkan warna menjadi putih
    lingkaran_polygon(-72, 180, 52, 100) #huruf q luar
    glColor3ub(255, 20, 147) 
    lingkaran_polygon(-72, 180, 35, 100) #huruf q dalam





def logo_dalam():
    glPushMatrix()
    #bintang besar
    #//1
    glColor3ub(36, 36, 33)
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-374, 164) #titik i17
    glVertex2f(-430, 164) #titik n17
    glVertex2f(-384, 144) #titik h17
    glVertex2f(-405,90) #titik s16
    glVertex2f(-360, 128) #titik u14
    glVertex2f(-315, 90) #titik l17
    glVertex2f(-336, 144) #titik k17
    glVertex2f(-290, 164) #titik m17
    glVertex2f(-346, 164) #titik j17
    glEnd()# Mengakhiri objek  

    #//2
    glColor3ub(36, 36, 33)
    glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-361,218) #titik o17
    glVertex2f(-374, 164) #titik i17
    glVertex2f(-346, 164) #titik j17
    glEnd()# Mengakhiri objek

    #segitiga besar
    glColor3ub(36, 36, 33)
    glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-430, -220) #titik z14
    glVertex2f(-370, -120) #titik v14
    glVertex2f(-310, -220) #titik w14
    glEnd()# Mengakhiri objek

    glPopMatrix()


def bintang_jatuh():
    glPushMatrix() 
    glColor3f(1,1,1)#menetapkan warna menjadi merah
    glTranslated(deltaX, deltaY, 0) #kalo mau mindah objek
    
    
    # glScaled(0.1,0.1,0)
    # glRotated(x_time,0,0,1)
    glBegin(GL_LINE_LOOP)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-520, 435) #titik k14
    glVertex2f(-516, 420) #titik m14
    glVertex2f(-498, 420) #titik t14
    glVertex2f(-514, 412) #titik s14
    glVertex2f(-508, 394) #titik r14
    glVertex2f(-520, 405) #titik q14
    glVertex2f(-532, 394) #titik p14
    glVertex2f(-526, 412) #titik o14
    glVertex2f(-542, 420) #titik n14
    glVertex2f(-524, 420) #titik l14
    glEnd()# Mengakhiri objek  


 
    glBegin(GL_LINE_LOOP)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-440, 980) #titik k15
    glVertex2f(-436, 965) #titik m15
    glVertex2f(-418, 965) #titik t15
    glVertex2f(-434, 957) #titik s15
    glVertex2f(-428, 939) #titik r15
    glVertex2f(-440, 950) #titik q15
    glVertex2f(-452, 939) #titik p15
    glVertex2f(-446, 957) #titik o15
    glVertex2f(-462, 965) #titik n15
    glVertex2f(-444, 965) #titik l15
    glEnd()# Mengakhiri objek  


    glBegin(GL_LINE_LOOP)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-240, 1380) #titik k15
    glVertex2f(-236, 1365) #titik m15
    glVertex2f(-218, 1365) #titik t15
    glVertex2f(-234, 1357) #titik s15
    glVertex2f(-228, 1339) #titik r15
    glVertex2f(-240, 1350) #titik q15
    glVertex2f(-252, 1339) #titik p15
    glVertex2f(-246, 1357) #titik o15
    glVertex2f(-262, 1365) #titik n15
    glVertex2f(-244, 1365) #titik l15
    glEnd()# Mengakhiri objek  
 



    glBegin(GL_LINE_LOOP)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-320, 235) #titik k14
    glVertex2f(-316, 220) #titik m14
    glVertex2f(-298, 220) #titik t14
    glVertex2f(-314, 212) #titik s14
    glVertex2f(-308, 194) #titik r14
    glVertex2f(-320, 205) #titik q14
    glVertex2f(-332, 194) #titik p14
    glVertex2f(-326, 212) #titik o14
    glVertex2f(-342, 220) #titik n14
    glVertex2f(-324, 220) #titik l14
    glEnd()# Mengakhiri objek  
    glPopMatrix()

def timer(value): #fungsi timer
    global collisionX1
    global gerakX
    global gerakY
    global boolGerakX
    glutTimerFunc(1000//30, timer, 0)  # callback function timer dg parameter miliseconds, fungsi yang dipanggil, dan value
    global deltaX #panggil variabel global kedalam fungsi timer
    global deltaY


    if boolGerakX==True:
        deltaX -= gerakX
        deltaY += gerakY
        collisionX1 -=gerakX
    else :
        collisionX1 +=gerakX
        deltaX += gerakX
        deltaY -= gerakY

    if collisionX1 == 400 :
        deltaX=0
        deltaY=0
# def update(value):
#     glutPostRedisplay()
#     glutTimerFunc(10,update,0)

def iniHandleMouse(button,state,x,y):
    global Pencet
    global hijau, biru, merah
    global hijau2, biru2, merah2
    global boolGerakX
    global PosisiX,PosisiY
    
    # Saat mengklik kanan warna kotak akan berubah menjadi warna biru dan merah
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        boolGerakX=True
        # if biru< 1:
        #     hijau = 0
        #     biru = 1
        #     merah = 0
        # elif merah < 1:
        #     hijau = 0
        #     biru = 0
        #     merah = 1
    # Saat mengklik kiri warna kotak akan berubah menjadi warna hijau dan hitam
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        Pencet = True
        
        if (261<PosisiX<420 and 255<PosisiY<310): #posisi quit
            if merah2 == 1 :
                hijau2 = 1
                biru2 = 0
                merah2 = 0
            else:
                hijau2 = 1
                biru2 = 1
                merah2 = 1
        elif (261<PosisiX<421 and 191<PosisiY<245): #posisi Start
            if merah == 1 :
                hijau = 1
                biru = 0
                merah = 0
            else:
                hijau = 1
                biru = 1
                merah = 1



    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        # Pencet = False
        hijau = 1
        biru = 1
        merah = 1

    print("Klik Kiri ditekan ", "(", x, ",", y, ")")
def mouseFunc(mouseX,mouseY):
    x=mouseX
    y=mouseY
    global PosisiX,PosisiY
    PosisiX = mouseX//2
    PosisiY = mouseY//2
    global Start
    global boolGerakX

    # print(Pencet)
    # if (523<mouseX<840 and 381<mouseY<489) and Pencet == True: #berdasarkan koordinat window
    #     print('perintah start ditekan jalan')
    # elif (524<mouseX<840 and 511<mouseY<619) and Pencet == True: #berdasarkan koordinat window
    #     print('perintah exit ditekan jalan')
    #     # boolgerakX= not boolGerakX
    print("posisi mouse x :", PosisiX)
    print("posisi mouse y :", PosisiY)
def segitiga_kecil():
    #segitiga kecil
    glColor3ub(255, 255, 255)#menetapkan warna menjadi merah
    glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-600,-200) #titik a1
    glVertex2f(-600,-210) #titik p2
    glVertex2f(-590,-200) #titik q2


    glVertex2f(-520,-30) #titik u1
    glVertex2f(-520,-40) #titik v1
    glVertex2f(-530,-30) #titik t1

    # glVertex2f(-640,60) #titik w1
    # glVertex2f(-640,50) #titik c2
    # glVertex2f(-630,60) #titik d2

    # glVertex2f(-540,150) #titik e2
    # glVertex2f(-530,150) #titik f2
    # glVertex2f(-530,140) #titik g2

    glVertex2f(-610,220) #titik l2
    glVertex2f(-620,220) #titik q2
    glVertex2f(-620,210) #titik k2

    # glVertex2f(-560,260) #titik i2 (Rusak)
    # glVertex2f(-570,270) #titik h2 (Rusak)
    # glVertex2f(-550,-270) #titik j2 (Rusak)

    # glVertex2f(-450,260) #titik e4
    # glVertex2f(-450,270) #titik f4
    # glVertex2f(-460,270) #titik r2

    glVertex2f(-350,290) #titik l4
    glVertex2f(-350,280) #titik h4
    glVertex2f(-340,290) #titik k4

    # glVertex2f(-140,270) #titik u4 (Rusak)
    # glVertex2f(-140,260) #titik v4 (Rusak)
    # glVertex2f(-150,-260) #titik b1 (Rusak)

    # glVertex2f(34,290) #titik z4
    # glVertex2f(30,280) #titik a5
    # glVertex2f(40,280) #titik c5

    glVertex2f(240,280) #titik g5
    glVertex2f(250,280) #titik k5
    glVertex2f(250,270) #titik j5

    # glVertex2f(410,280) #titik m5
    # glVertex2f(410,270) #titik n5
    # glVertex2f(420,270) #titik p5

    # glVertex2f(600,260) #titik s5
    # glVertex2f(610,260) #titik v5
    # glVertex2f(610,250) #titik z5

    glVertex2f(500,190) #titik a6
    glVertex2f(500,180) #titik c6
    glVertex2f(510,190) #titik d6

    # glVertex2f(600,110) #titik f6
    # glVertex2f(610,110) #titik g6
    # glVertex2f(610,100) #titik i6

    # glVertex2f(500,-10) #titik j6
    # glVertex2f(510,-10) #titik l6
    # glVertex2f(505,0) #titik n6

    glVertex2f(610,-100) #titik p6
    glVertex2f(620,-100) #titik q6
    glVertex2f(620,-110) #titik r6

    # glVertex2f(520,-190) #titik w6
    # glVertex2f(520,-200) #titik v6
    # glVertex2f(510,-200) #titik s6

    # glVertex2f(610,-260) #titik z6
    # glVertex2f(620,-260) #titik b7
    # glVertex2f(620,-270) #titik a7

    glVertex2f(450,-280) #titik c7 
    glVertex2f(460,-290) #titik d7
    glVertex2f(460,-280) #titik e7

    # glVertex2f(310,-260) #titik f7
    # glVertex2f(320,-270) #titik g7
    # glVertex2f(310,-270) #titik h7

    # glVertex2f(90,-270) #titik j7
    # glVertex2f(80,-280) #titik i7
    # glVertex2f(90,-280) #titik k7

    # glVertex2f(-124,-270) #titik n7 (Rusak)
    # glVertex2f(-120,-280) #titik m7 (Rusak)
    # glVertex2f(-130,-280) #titik l7 (Rusak)

    glVertex2f(-350,-280) #titik q7
    glVertex2f(-350,-290) #titik p7
    glVertex2f(-360,-280) #titik O7

    # glVertex2f(-510,-260) #titik r7
    # glVertex2f(-510,-270) #titik s7
    # glVertex2f(-500,-270) #titik t7

    glEnd()# Mengakhiri objek


def tulisan_judul():
    glPushMatrix()
    #=========SQUID=========
    #huruf s
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-250, 132)#titik n18
    glVertex2f (-250, 152)#titik i18
    glVertex2f (-162, 152)#titik a19
    glVertex2f (-162, 132)#titik u17
    glEnd()

    #//2
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon

    glVertex2f (-162, 194)#titik d18
    glVertex2f (-154, 193)#titik c24
    glVertex2f (-146, 189)#titik a24
    glVertex2f (-137, 182)#titik w23
    glVertex2f (-133, 174)#titik u23
    glVertex2f (-131, 166)#titik s23
    glVertex2f (-131, 158)#titik q23
    glVertex2f (-134, 150)#titik o23      
    glVertex2f (-139, 142)#titik m23
    glVertex2f (-146, 136)#titik k23
    glVertex2f (-154, 133)#titik i23
    glVertex2f (-162, 132)#titik u17
    glEnd()


    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-162, 194)#titik d18
    glVertex2f(-162, 174) #titik b18
    glVertex2f (-200, 174)#titik c18
    glVertex2f (-200, 194)#titik w17
    glEnd()

    
    #//4
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon

    glVertex2f (-200, 174)#titik c18
    glVertex2f (-206, 174)#titik i24
    glVertex2f (-212, 176)#titik j24
    glVertex2f (-218, 180)#titik k24
    glVertex2f (-224, 185)#titik l24
    glVertex2f (-228, 192)#titik m24
    glVertex2f (-230, 199)#titik n24
    glVertex2f (-228, 218)#titik q24
    glVertex2f (-222, 226)#titik r24      
    glVertex2f (-218, 230)#titik s24
    glVertex2f (-212, 233)#titik t24
    glVertex2f (-206, 235)#titik u24
    glVertex2f (-200, 236)#titik g18
    glVertex2f (-200, 216)#titik z17
    glEnd()
 
    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-200, 236)#titik g18
    glVertex2f (-200, 216)#titik z17
    glVertex2f (-130, 216)#titik a18
    glVertex2f (-130, 236)#titik e18
    glEnd()

    #garis huruf q
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-77, 165)#titik k20
    glVertex2f (-62, 170)#titik j20
    glVertex2f (-17, 100)#titik l20
    glVertex2f (-32, 100)#titik m20
    glEnd()

    #huruf U
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-12, 210)#titik f19
    glVertex2f (-12, 150)#titik j19
    glVertex2f (8, 150)#titik l19
    glVertex2f (8, 210)#titik h19
    glEnd()

    #//2
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (8, 150)#titik l19
    glVertex2f (-12, 150)#titik j19
    glVertex2f (-9, 140)#titik s25
    glVertex2f (-5, 130)#titik t25
    glVertex2f (2, 121)#titik u25
    glVertex2f (10, 115)#titik v25
    glVertex2f (20, 111)#titik w25
    glVertex2f (30, 110)#titik z25
    glVertex2f (40, 111)#titik a26
    glVertex2f (50, 113)#titik b26
    glVertex2f (60, 118)#titik c26
    glVertex2f (70, 130)#titik d26
    glVertex2f (78, 140)#titik e26
    glVertex2f (78, 150)#titik f26
    glVertex2f (78, 160)#titik v19
    glVertex2f (58, 160)#titik t19
    glEnd()

    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (58, 230)#titik m19
    glVertex2f (78, 230)#titik s19
    glVertex2f (78, 160)#titik v19
    glVertex2f (58, 160)#titik t19
    glEnd()

    # sisi dalam U
    glColor3ub(74, 74, 54)
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (8, 150)#titik l19
    glVertex2f (12, 140)#titik g26
    glVertex2f (20, 133)#titik h26
    glVertex2f (30, 130)#titik i26
    glVertex2f (40, 130)#titik j26
    glVertex2f (48, 134)#titik m26
    glVertex2f (54, 141)#titik l26
    glVertex2f (58, 150)#titik k26
    glEnd()

    # sisi dalam U
    glColor3ub(36, 36, 33)
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (8, 150)#titik l19
    glVertex2f (58, 150)#titik k26
    glVertex2f (58, 160)#titik t19
    glVertex2f (8, 170)#titik c27
    glEnd()

    #Huruf I
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (98, 230)#titik w19
    glVertex2f (118, 230)#titik z19
    glVertex2f (118, 130)#titik b20
    glVertex2f (98, 130)#titik c20
    glEnd()

    #Huruf D
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (128, 230)#titik w20
    glVertex2f (148, 230)#titik z20
    glVertex2f (148, 130)#titik b21
    glVertex2f (128, 130)#titik c21
    glEnd()

    #//2
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (148, 230)#titik z20
    glVertex2f (148, 210)#titik d20
    glVertex2f (188, 210)#titik g20
    glVertex2f (188, 230)#titik f20
    glEnd()
    #huruf U
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-12, 210)#titik f19
    glVertex2f (-12, 150)#titik j19
    glVertex2f (8, 150)#titik l19
    glVertex2f (8, 210)#titik h19
    glEnd()

    #//2
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-12, 210)#titik f19
    glVertex2f (-12, 150)#titik j19
    glVertex2f (8, 150)#titik l19
    glVertex2f (8, 210)#titik h19
    glEnd()

    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (58, 230)#titik m19
    glVertex2f (78, 230)#titik s19
    glVertex2f (78, 160)#titik v19
    glVertex2f (58, 160)#titik t19
    glEnd()

    #Huruf I
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (98, 230)#titik w19
    glVertex2f (118, 230)#titik z19
    glVertex2f (118, 130)#titik b20
    glVertex2f (98, 130)#titik c20
    glEnd()

    #Huruf D
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (128, 230)#titik w20
    glVertex2f (148, 230)#titik z20
    glVertex2f (148, 130)#titik b21
    glVertex2f (128, 130)#titik c21
    glEnd()

    #//2
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (148, 230)#titik z20
    glVertex2f (148, 210)#titik d20
    glVertex2f (188, 210)#titik g20
    glVertex2f (188, 230)#titik f20
    glEnd()

    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (188, 230)#titik f20
    glVertex2f (200, 228)#titik w24
    glVertex2f (209, 225)#titik z24
    glVertex2f (219, 219)#titik a25
    glVertex2f (228, 209)#titik b25
    glVertex2f (233, 200)#titik c25
    glVertex2f (237, 190)#titik d25
    glVertex2f (238, 180)#titik e25
    glVertex2f (237, 170)#titik f25
    glVertex2f (234, 160)#titik g25
    glVertex2f (228, 150)#titik h25
    glVertex2f (220, 141)#titik i25
    glVertex2f (210, 135)#titik j25
    glVertex2f (200, 131)#titik k25
    glVertex2f (188, 130)#titik i20
    glEnd()

    #//4
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (148, 150)#titik e20
    glVertex2f (148, 130)#titik b21
    glVertex2f (188, 130)#titik i20
    glVertex2f (188, 150)#titik h20
    glEnd()

    #sisi dalam D
    glColor3ub(36, 36, 33) #bg layer 2
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (188, 210)#titik g20
    glVertex2f (148, 210)#titik d20
    glVertex2f (148, 150)#titik e20
    glVertex2f (188, 150)#titik h20
    glVertex2f (200, 152)#titik r25
    glVertex2f (210, 160)#titik q25
    glVertex2f (216, 170)#titik p25
    glVertex2f (218, 180)#titik o25
    glVertex2f (216, 190)#titik n25
    glVertex2f (210, 200)#titik m25
    glVertex2f (199, 208)#titik l25
    glEnd()

    #=========GAME=========
    #Huruf G
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-17, 100)#titik l20
    glVertex2f (-37, 80)#titik o20
    glVertex2f (-107, 80)#titik q20
    glVertex2f (-107, 100)#titik p20
    glEnd()
    
    #//2 lengkungan
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-107, 100)#titik p20
    glVertex2f (-129, 94)#titik r26
    glVertex2f (-144, 80)#titik s26
    glVertex2f (-151, 59)#titik t26
    glVertex2f (-150, 40)#titik u26
    glVertex2f (-140, 24)#titik v26
    glVertex2f (-125, 13)#titik w26
    glVertex2f (-107, 10)#titik s20
    glEnd()
    
    #//2 hitam lengkungan
    glColor3ub(74, 74, 54)# menetapkan warna menjadi kuning
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-107, 80)#titik q20
    glVertex2f (-126, 70)#titik z26
    glVertex2f (-131, 50)#titik a27
    glVertex2f (-120, 34)#titik b27
    glVertex2f (-107, 30)#titik r20
    glEnd()
    #//3
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-107, 30)#titik r20
    glVertex2f (-107, 10)#titik s20
    glVertex2f (-33, 10)#titik q20 (di kanan in)
    glVertex2f (-47, 30)#titik u20 (di kanan in)
    glEnd()

    #//4
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-18, -21)#titik g21
    glVertex2f (-4, -15)#titik a21
    glVertex2f (-67, 65)#titik f21
    glVertex2f (-72, 50)#titik v20
    glEnd()

    #//5
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-67, 65)#titik f21
    glVertex2f (-72, 50)#titik v20
    glVertex2f (-112, 50)#titik d21
    glVertex2f (-112, 65)#titik e21
    glEnd()

    #Huruf A
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_TRIANGLES)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-12, 10)#titik i21
    glVertex2f (88, 10)#titik k21
    glVertex2f (38, 100)#titik h21

    glColor3ub(255,20,147) #warma pink squid game
    glVertex2f (38, 70)#titik k21
    glVertex2f (17, 10)#titik j21
    glVertex2f (58, 10)#titik l21
    glEnd()


    #Huruf m
    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (107, 10)#titik n21
    glVertex2f (127, 10)#titik r21
    glVertex2f (127, 100)#titik p21
    glVertex2f (107, 100)#titik h21
    glEnd()

    #//2
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (127, 100)#titik p21
    glVertex2f (127, 70)#titik s21
    glVertex2f (158, 10)#titik t21
    glVertex2f (168, 25)#titik q21
    glEnd()

    #//3
    glBegin(GL_TRIANGLES)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (158, 10)#titik t21
    glVertex2f (168, 25)#titik q21
    glVertex2f (177, 10)#titik u21
    glEnd()

    #//4
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (168, 25)#titik q21
    glVertex2f (177, 10)#titik u21
    glVertex2f (207, 70)#titik b22
    glVertex2f (208, 100)#titik v21
    glEnd()

    #//5
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (208, 100)#titik v21
    glVertex2f (207, 10)#titik a22
    glVertex2f (227, 10)#titik z21
    glVertex2f (227, 100)#titik w21
    glEnd()

    #Huruf E
    #//0
    glColor3ub(255,20,147)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (260, 90)#titik i22
    glVertex2f (260, 30)#titik j22
    glVertex2f (330, 30)#titik f22
    glVertex2f (330, 90)#titik h22


    #//1
    glColor3f(1,1,1)# menetapkan warna menjadi kuning

    glVertex2f (240, 110)#titik c22
    glVertex2f (330, 110)#titik g22
    glVertex2f (330, 90)#titik h22
    glVertex2f (240, 90)#titik n26

    #//2
    glVertex2f (240, 110)#titik c22
    glVertex2f (260, 110)#titik 026
    glVertex2f (260, 10)#titik p26
    glVertex2f (240, 10)#titik d22

    #//3
    glVertex2f (240, 10)#titik d22
    glVertex2f (240, 30)#titik q26
    glVertex2f (330, 30)#titik f22
    glVertex2f (330, 10)#titik e22

    #//4
    glVertex2f (280, 70)#titik l22
    glVertex2f (280, 50)#titik k22
    glVertex2f (370, 50)#titik n22
    glVertex2f (370, 70)#titik m22
    glEnd()
    glPopMatrix()
    




def Bingkai_menu():
    glPushMatrix()
    #kotak start
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-160, -30)#titik u7
    glVertex2f (-160, -140)#titik v7
    glVertex2f (160, -140)#titik w7
    glVertex2f (160, -30)#titik z7

    glColor3f(0,0,0)# menetapkan warna menjadi kuning
    glVertex2f (-145, -45)#titik h6
    glVertex2f (-145, -125)#titik o6
    glVertex2f (145, -125)#titik t6
    glVertex2f (145, -45)#titik u6

    #kotak quit
    glColor3f(1,1,1)# menetapkan warna menjadi kuning
    glVertex2f (-160, -160)#titik j8
    glVertex2f (-160, -270)#titik m8
    glVertex2f (160, -270)#titik d8
    glVertex2f (160, -160)#titik z7

    glColor3f(0,0,0)# menetapkan warna menjadi kuning
    glVertex2f (-145, -175)#titik u7
    glVertex2f (-145, -255)#titik v7
    glVertex2f (145, -255)#titik w7
    glVertex2f (145, -175)#titik z7

    glEnd() #Mengakhiri objek

    glPopMatrix()


def tulisan_start():
    glPushMatrix()
    
    #============= START =============
    #huruf s
    #//1
    glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-140, -110) #titik i1
    glVertex2f(-140, -120) #titik n8
    glVertex2f(-90, -120) #titik u8
    glVertex2f(-90, -110) #titik a8
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-90, -120) #titik u8
    glVertex2f(-90, -110) #titik a8
    glVertex2f(-83, -105) #titik n10
    glVertex2f(-83, -101) #titik o10
    glVertex2f(-85, -97) #titik p10
    glVertex2f(-90, -95) #titik b8
    glVertex2f(-90, -85) #titik v8
    glVertex2f(-86, -85) #titik d11
    glVertex2f(-82, -87) #titik c11
    glVertex2f(-78, -90) #titik b11
    glVertex2f(-75, -94) #titik a11
    glVertex2f(-73, -98) #titik z10
    glVertex2f(-72, -102) #titik w10
    glVertex2f(-73, -106) #titik v10
    glVertex2f(-74, -110) #titik u10
    glVertex2f(-76, -113) #titik t10
    glVertex2f(-78, -116) #titik s10
    glVertex2f(-82, -118) #titik r10
    glVertex2f(-86, -119) #titik q10
    
    glEnd()# Mengakhiri objek  


    #//3
    # glColor3f(merah,hijau,biru)
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-90, -95) #titik b8
    glVertex2f(-90, -85) #titik v8
    glVertex2f(-110, -85) #titik w8
    glVertex2f(-110, -95) #titik c8
    glEnd()# Mengakhiri objek  

    # #//4
    # glColor3f(merah,hijau,biru)
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-110, -85) #titik w8
    glVertex2f(-110, -95) #titik c8
    glVertex2f(-114, -94) #titik j11
    glVertex2f(-118, -93) #titik k11
    glVertex2f(-122, -90) #titik l11
    glVertex2f(-125, -86) #titik m11
    glVertex2f(-127, -82) #titik n11
    glVertex2f(-127, -78) #titik o11
    glVertex2f(-127, -74) #titik p11
    glVertex2f(-126, -70) #titik q11
    glVertex2f(-123, -66) #titik r11
    glVertex2f(-120, -63) #titik s11
    glVertex2f(-116, -61) #titik t11
    glVertex2f(-113, -60) #titik u11
    glVertex2f(-110, -60) #titik g8
    glVertex2f(-110, -70) #titik z8
    glVertex2f(-112, -70) #titik i11
    glVertex2f(-115, -72) #titik h11
    glVertex2f(-117, -76) #titik g11
    glVertex2f(-117, -80) #titik f11
    glVertex2f(-114, -84) #titik e11
    glEnd()# Mengakhiri objek  

    # #//5
    # glColor3f(merah,hijau,biru)
    glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f(-110, -60) #titik g8
    glVertex2f(-110, -70) #titik z8
    glVertex2f(-72, -70) #titik a9
    glVertex2f(-72, -60) #titike8
    glEnd()# Mengakhiri objek  


    #huruf T
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-65, -60)#titik v9
    glVertex2f (-65, -70)#titik w9
    glVertex2f (-15, -70)#titik b10
    glVertex2f (-15, -60)#titik c10
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-45, -70)#titik z9
    glVertex2f (-35, -70)#titik a10
    glVertex2f (-35, -120)#titik u9
    glVertex2f (-45, -120)#titik r9
    glEnd()# Mengakhiri objek  

    #huruf A
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-25, -120)#titik n9
    glVertex2f (-10, -120)#titik o9
    glVertex2f (5, -82)#titik s9
    glVertex2f (5, -60)#titik t9
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (5, -82)#titik s9
    glVertex2f (5, -60)#titik t9
    glVertex2f (35, -120)#titik p9
    glVertex2f (20, -120)#titik q9
    glEnd()# Mengakhiri objek  

    #huruf r
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (40, -120)#titik b9
    glVertex2f (50, -120)#titik c9
    glVertex2f (50, -60)#titik a12
    glVertex2f (40, -60)#titik d9
    glEnd()# Mengakhiri objek 

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (50, -60)#titik a12
    glVertex2f (50, -70)#titik e9
    glVertex2f (70, -70)#titik w11
    glVertex2f (70, -60)#titik v11
    glEnd()# Mengakhiri objek 

    #//3
    # glColor3f(merah,hijau,biru)
    glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (70, -70)#titik w11
    glVertex2f (70, -60)#titik v11
    glVertex2f (74, -60)#titik g12
    glVertex2f (78, -61)#titik h12
    glVertex2f (82, -63)#titik i12
    glVertex2f (85, -66)#titik j12
    glVertex2f (87, -70)#titik k12
    glVertex2f (89, -74)#titik l12
    glVertex2f (89, -78)#titik m12
    glVertex2f (88, -82)#titik n12
    glVertex2f (87, -86)#titik 012
    glVertex2f (84, -89)#titik p12
    glVertex2f (82, -91)#titik q12
    glVertex2f (78, -93)#titik r12
    glVertex2f (74, -94)#titik f9
    glVertex2f (70, -85)#titik z11
    glEnd()# Mengakhiri objek 

    #//4
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (60, -85)#titik i8
    glVertex2f (70, -120)#titik h8
    glVertex2f (80, -120)#titik f8
    glVertex2f (70, -85)#titik z11
    glVertex2f (74, -84)#titik f12
    glVertex2f (76, -82)#titik e12
    glVertex2f (77, -78)#titik d12
    glVertex2f (76, -74)#titik c12
    glVertex2f (74, -71)#titik b12
    glVertex2f (70, -70)#titik w11
    glEnd()# Mengakhiri objek 
    
    #huruf T
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (90, -60)#titik k10
    glVertex2f (90, -70)#titik h10
    glVertex2f (140, -70)#titik i10
    glVertex2f (140, -60)#titik j10
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (110, -70)#titik f10
    glVertex2f (120, -70)#titik g10
    glVertex2f (120, -120)#titik e10
    glVertex2f (110, -120)#titik d10
    glEnd()# Mengakhiri objek 
    glPopMatrix()
def tulisan_exit():
    glPushMatrix()
    #=============EXIT============= 
    #Huruf E
    #//1
    glColor3f(merah2,hijau2,biru2)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-120, -190)#titik t12
    glVertex2f (-75, -190)#titik a13
    glVertex2f (-75, -200)#titik b13
    glVertex2f (-120, -200)#titik c14
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah2,hijau2,biru2)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-120, -190)#titik t12
    glVertex2f (-110, -190)#titik d14
    glVertex2f (-110, -245)#titik e14
    glVertex2f (-120, -245)#titik s12
    glEnd()# Mengakhiri objek 

    #//3
    # glColor3f(merah2,hijau2,biru2)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-120, -190)#titik t12
    glVertex2f (-120, -200)#titik c14
    glVertex2f (-75, -200)#titik b13
    glVertex2f (-75, -190)#titik a13
    glEnd()# Mengakhiri objek 

    #//4
    # glColor3f(merah2,hijau2,biru2)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-120, -235)#titik f14
    glVertex2f (-120, -245)#titik s12
    glVertex2f (-80, -245)#titik u12
    glVertex2f (-80, -235)#titik v12
    glEnd()# Mengakhiri objek 

    #//5
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-100, -210)#titik d13
    glVertex2f (-100, -220)#titik c13
    glVertex2f (-55, -220)#titik f13
    glVertex2f (-55, -210)#titik e13
    glEnd()# Mengakhiri objek 

    #Huruf X
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (-40, -190)#titik i13
    glVertex2f (-20, -190)#titik j13
    glVertex2f (30, -245)#titik n13
    glVertex2f (10, -245)#titik m13
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (10, -190)#titik k13
    glVertex2f (30, -190)#titik l13
    glVertex2f (-20, -245)#titik h13
    glVertex2f (-40, -245)#titik g13
    glEnd()# Mengakhiri objek  

    #Huruf I
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (45, -190)#titik q13
    glVertex2f (60, -190)#titik r13
    glVertex2f (60, -245)#titik p13
    glVertex2f (45, -245)#titik o13
    glEnd()# Mengakhiri objek 

    #huruf T
    #//1
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (70, -190)#titik s13
    glVertex2f (70, -200)#titik t13
    glVertex2f (120, -200)#titik w13
    glVertex2f (120, -190)#titik z13
    glEnd()# Mengakhiri objek  

    #//2
    # glColor3f(merah,hijau,biru)
    glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
    glVertex2f (90, -200)#titik u13
    glVertex2f (100, -200)#titik v13
    glVertex2f (100, -245)#titik b14
    glVertex2f (90, -245)#titik a14
    glEnd()# Mengakhiri objek 
    glPopMatrix()

def main_menu():
    
    bg()
    bintang_jatuh()
    logo() 
    logo_dalam()
    Bingkai_menu()
    segitiga_kecil()
    tulisan_start()
    tulisan_exit()
    

    Circle()
    pengangan_payung()
    tulisan_judul()
    frame()

    

def iterate():
    glViewport(0, 0, 1364, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluOrtho2D(-1364,1364,-700,700)
    gluOrtho2D(-682,682,-350,350)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    main_menu()
    # if play == True:
    #     layer_kalah()
    glFlush()


    glutSwapBuffers()
def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1364,700)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Test")
    glutDisplayFunc(ShowScreen)
    glutMouseFunc(iniHandleMouse)
    glutPassiveMotionFunc(mouseFunc)
    # glutTimerFunc(50, update, 0)
    timer(0)
    glutIdleFunc(ShowScreen)
    glutMainLoop()

Main()

