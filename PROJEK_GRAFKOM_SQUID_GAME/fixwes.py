from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

# w, h = 1364, 700
x_time = 0 #utk gerak horizontal
y_time = 0 #utk gerak vertikal

# Warna
merah, hijau, biru = 1, 1, 1
merah2, hijau2, biru2  = 1,1,1
merah3, hijau3, biru3 = 1,1,1

# ===== KLIK MOUSE =====
Pencet = False
Lanjut = False

# ===== KOORDINAT MOUSE =====
PosisiX = 0
PosisiY = 0

# Game 1
pos_x = 0
Nyawa =  5
max_lose = 0
Merah_lampu = 0
Hijau_lampu = 0
Gerak = False
jarak_hati, index = [0,40,80,120,160], 4

# ----------
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

def Lingkaran_Polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def iniHandleMouse(button,state,x,y):
    global Pencet,Lanjut
    global hijau, biru, merah
    global boolGerakX
    global PosisiX,PosisiY
    global pos_x

    # Saat mengklik tombol kanan mouse
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        boolGerakX=True

    # Saat mengklik tombol kiri mouse
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if Pencet == False and (-145 <= PosisiX <= 145 and -125 <= PosisiY <= -45):
            Pencet = True
        if (-145 <= PosisiX <= 145 and -255 <= PosisiY <= -175):
            Lanjut = True
        if Pencet == True and (585 <= PosisiX <= 665 and -330 <= PosisiY <= -260):
            Pencet = False
            global jarak_hati, index, Nyawa, max_lose
            tampung = [0,40,80,120,160]
            for i in tampung:
                jarak_hati.append(i)
            pos_x = 0
            index += 5
            Nyawa += 5
            max_lose -= 5
        
def KoorMouse(mouseX,mouseY):
    global PosisiX,PosisiY,pos_x
    global merah, hijau, biru, merah2, hijau2, biru2, merah3, hijau3, biru3
    PosisiX = mouseX - 682
    PosisiY = (mouseY - 350) * -1
    # print('posisi x',PosisiX)
    if (-145 <= PosisiX <= 145 and -125 <= PosisiY <= -45):
        merah = 0
        hijau = 1
        biru = 0
    if (PosisiX <= -145 or 145 <= PosisiX or PosisiY <= -125 or -45 <= PosisiY):
        merah = 1
        hijau = 1
        biru = 1

    if (-145 <= PosisiX <= 145 and -255 <= PosisiY <= -175):
        merah2 = 0
        hijau2 = 1
        biru2 = 0
    if (PosisiX <= -145 or 145 <= PosisiX or PosisiY <= -255 or -175 <= PosisiY):
        merah2 = 1
        hijau2 = 1
        biru2 = 1

    if (585 <= PosisiX <= 665 and -330 <= PosisiY <= -260):
        merah3 = 0
        hijau3 = 1
        biru3 = 0
    if (PosisiX <= 585 or 665 <= PosisiX or PosisiY <= -330 or -260 <= PosisiY):
        merah3 = 1
        hijau3 = 1
        biru3 = 1

def input_keyboard(key,x,y): 

    global pos_x,max_lose,Gerak,Nyawa, jarak_hati, index
    if key == GLUT_KEY_LEFT :
        if max_lose >= 5:
            pass
        else:
            pos_x -= 2.5
    if Nyawa > 0 and Gerak == False and key == GLUT_KEY_LEFT:
        if max_lose < 5:
            max_lose += 1
            Nyawa -= 1
            jarak_hati.pop(index)
            index -= 1
        if Nyawa == 0:
            pass

    # CHEAT
    if key == GLUT_KEY_UP :
        if max_lose >= 5:
            pass
        else:
            pos_x -= 250
    if Nyawa > 0 and Gerak == False and key == GLUT_KEY_UP:
        if max_lose < 5:
            max_lose += 1
            Nyawa -= 1
            jarak_hati.pop(index)
            index -= 1
        if Nyawa == 0:
            pass
    
    # WINING
    if pos_x == -1000:
        print('You Win')
    
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

def main_menu():

    def Lingkaran_Polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
        glBegin(GL_POLYGON)    
        for i in range(360):    
            sudut = i * (2*pi/Jumlah_titik)
            x = Posisi_x + Radius * cos(sudut)
            y = Posisi_y + Radius * sin(sudut)
            glVertex2f(x, y)
        glEnd()
    
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

        # Lampu Frame atas & lampu bawah
        def Lampu1(x):
            # Lampu frame atas
            glBegin(GL_QUADS)
            glColor3ub(255, 218, 30)
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
            glColor3ub(255, 218, 30)
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
        #segitiga besar
        glColor3f(1,1,1)#menetapkan warna menjadi merah
        glBegin(GL_TRIANGLES)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f(-450,-230) #titik o
        glVertex2f(-370,-100) #titik N
        glVertex2f(-290,-230) #titik P
        glEnd()# Mengakhiri objek
   
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

    def Circle():
        glColor3ub(36, 36, 33)
        Lingkaran_Polygon(440, 140, 20, 60)
        Lingkaran_Polygon(400, 140, 20, 60)
        Lingkaran_Polygon(360, 140, 20, 60)
        Lingkaran_Polygon(320, 140, 20, 60)
        glColor3f(1, 1, 1) #menetapkan warna menjadi putih
        Lingkaran_Polygon(380, -160, 74, 100) #logo lingkaran luar
        glColor3ub(36, 36, 33)
        Lingkaran_Polygon(380, -160, 63, 100) #logo lingkaran dalam
        # glColor3f(1, 1, 1) #menetapkan warna menjadi putih
        # Lingkaran_Polygon(-72, 180, 52, 100) #huruf q luar
        # glColor3ub(255, 20, 147) 
        # Lingkaran_Polygon(-72, 180, 35, 100) #huruf q dalam

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

        glVertex2f(-610,220) #titik l2
        glVertex2f(-620,220) #titik q2
        glVertex2f(-620,210) #titik k2

        glVertex2f(-350,290) #titik l4
        glVertex2f(-350,280) #titik h4
        glVertex2f(-340,290) #titik k4

        glVertex2f(240,280) #titik g5
        glVertex2f(250,280) #titik k5
        glVertex2f(250,270) #titik j5

        glVertex2f(500,190) #titik a6
        glVertex2f(500,180) #titik c6
        glVertex2f(510,190) #titik d6


        glVertex2f(610,-100) #titik p6
        glVertex2f(620,-100) #titik q6
        glVertex2f(620,-110) #titik r6

        glVertex2f(450,-280) #titik c7 
        glVertex2f(460,-290) #titik d7
        glVertex2f(460,-280) #titik e7

        glVertex2f(-350,-280) #titik q7
        glVertex2f(-350,-290) #titik p7
        glVertex2f(-360,-280) #titik O7

        glEnd()# Mengakhiri objek

    def tulisan_judul():
        glPushMatrix()
        #=========SQUID=========
        #huruf s
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-250, 132)#titik n18
        glVertex2f (-250, 152)#titik i18
        glVertex2f (-162, 152)#titik a19
        glVertex2f (-162, 132)#titik u17
        glEnd()

        #//2
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon

        glVertex2f (-162, 194)#titik d18
        glVertex2f (-142, 194)#titik c24
        glVertex2f (-142, 132)#titik a24
        glVertex2f (-162, 132)#titik w23
        glVertex2f (-162, 194)#titik u23  
        glEnd()


        #//3
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-162, 194)#titik d18
        glVertex2f(-162, 174) #titik b18
        glVertex2f (-200, 174)#titik c18
        glVertex2f (-200, 194)#titik w17
        glEnd()

        
        #//4
        glSecondaryColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon

        glVertex2f (-220, 236)#titik c18
        glVertex2f (-220, 174)#titik i24
        glVertex2f (-200, 174)#titik j24
        glVertex2f (-200, 236)#titik k24
        glEnd()
    
        #//5
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-200, 236)#titik g18
        glVertex2f (-200, 216)#titik z17
        glVertex2f (-130, 216)#titik a18
        glVertex2f (-130, 236)#titik e18
        glEnd()

        #garis huruf q
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-77, 165)#titik k20
        glVertex2f (-62, 170)#titik j20
        glVertex2f (-17, 100)#titik l20
        glVertex2f (-32, 100)#titik m20
        glEnd()
       
        #//2
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-120, 148)
        glVertex2f (-100, 148)
        glVertex2f (-100, 235)
        glVertex2f (-120, 235)
        glEnd()
       
        #//3
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-20, 132)#titik m20
        glVertex2f (-20, 148)#titik l20
        glVertex2f (-120, 148)#titik k20
        glVertex2f (-120, 132)#titik j20
        glEnd()
       
        #//4
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-20, 148)#titik j20
        glVertex2f (-40, 148)#titik k20
        glVertex2f (-40, 235)#titik l20
        glVertex2f (-20, 235)#titik m20
        glEnd()
       
        #//5
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-40, 235)#titik k20
        glVertex2f (-40, 220)#titik j20
        glVertex2f (-120, 220)#titik l20
        glVertex2f (-120, 235)#titik m20
        glEnd()


        #huruf U
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-12, 235)#titik f19
        glVertex2f (-12, 150)#titik j19
        glVertex2f (8, 150)#titik l19
        glVertex2f (8, 235)#titik h19
        glEnd()

        # //2
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (58, 235)#titik m19
        glVertex2f (78, 235)#titik s19
        glVertex2f (78, 160)#titik v19
        glVertex2f (58, 160)#titik t19
        glEnd()

        # sisi dalam U
        glColor3ub(205,229,50)
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (8, 150)#titik l19
        glVertex2f (12, 140)#titik g26
        glVertex2f (20, 133)#titik h26
        glVertex2f (30, 140)#titik i26
        glVertex2f (40, 130)#titik j26
        glVertex2f (48, 134)#titik m26
        glVertex2f (54, 141)#titik l26
        glVertex2f (58, 150)#titik k26
        glEnd()

        # sisi dalam U
        glColor3ub(205,229,50)
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (8, 150)#titik l19
        glVertex2f (58, 150)#titik k26
        glVertex2f (58, 160)#titik t19
        glVertex2f (8, 170)#titik c27
        glEnd()

        #Huruf I
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (98, 235)#titik w19
        glVertex2f (118, 235)#titik z19
        glVertex2f (118, 130)#titik b20
        glVertex2f (98, 130)#titik c20
        glEnd()

        #Huruf D
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (128, 235)#titik w20
        glVertex2f (148, 235)#titik z20
        glVertex2f (148, 135)#titik b21
        glVertex2f (128, 135)#titik c21
        glEnd()

        #//2
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (148, 230)#titik z20
        glVertex2f (148, 210)#titik d20
        glVertex2f (188, 210)#titik g20
        glVertex2f (188, 230)#titik f20
        glEnd()
        

        #Huruf I
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (98, 230)#titik w19
        glVertex2f (118, 230)#titik z19
        glVertex2f (118, 130)#titik b20
        glVertex2f (98, 130)#titik c20
        glEnd()

        #Huruf D
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (128, 230)#titik w20
        glVertex2f (148, 230)#titik z20
        glVertex2f (148, 130)#titik b21
        glVertex2f (128, 130)#titik c21
        glEnd()

        #//2
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (140, 230)#titik z20
        glVertex2f (140, 235)#titik d20
        glVertex2f (180, 235)#titik g20
        glVertex2f (180, 230)#titik f20
        glEnd()

        #//3
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (180, 235)#titik f20
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (148, 150)#titik e20
        glVertex2f (148, 130)#titik b21
        glVertex2f (188, 130)#titik i20
        glVertex2f (188, 150)#titik h20
        glEnd()

        #sisi dalam D
        glColor3ub(205,229,50) #bg layer 2
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-17, 100)#titik l20
        glVertex2f (-37, 80)#titik o20
        glVertex2f (-107, 80)#titik q20
        glVertex2f (-107, 100)#titik p20
        glEnd()
        
        #//2 lengkungan
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-107, 80)#titik q20
        glVertex2f (-126, 70)#titik z26
        glVertex2f (-131, 50)#titik a27
        glVertex2f (-120, 34)#titik b27
        glVertex2f (-107, 30)#titik r20
        glEnd()
        #//3
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-107, 30)#titik r20
        glVertex2f (-107, 10)#titik s20
        glVertex2f (-33, 10)#titik q20 (di kanan in)
        glVertex2f (-47, 30)#titik u20 (di kanan in)
        glEnd()

        #//4
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
        glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f (-18, -21)#titik g21
        glVertex2f (-4, -15)#titik a21
        glVertex2f (-67, 65)#titik f21
        glVertex2f (-72, 50)#titik v20
        glEnd()

        #Huruf A
        #//1
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning
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
        glColor3ub(205,229,50)# menetapkan warna menjadi kuning

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

    bg()
    bintang_jatuh()
    logo() 
    logo_dalam()
    Bingkai_menu()
    segitiga_kecil()
    tulisan_start()
    tulisan_exit()
    Circle()
    tulisan_judul()


def Game_1():

    #=-=-=-=- Latar -=-=-=-=
    #--- LANGIT ---
    glBegin(GL_QUADS)
    glColor3ub(201, 208, 255)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    glEnd()

    def gunung(x):
        glBegin(GL_TRIANGLES)
        glColor3ub(178, 191, 207)
        glVertex2f(-682+x, 30)
        glVertex2f(-511.5+x, 180)
        glVertex2f(-341+x, 30)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(-682+x, -50)
        glVertex2f(-341+x, -50)
        glVertex2f(-341+x, 30)
        glVertex2f(-682+x, 30)
        glEnd()

    def rumput(y):
        glBegin(GL_TRIANGLES)
        glColor3ub(54, 102, 24)
        glVertex2f(-690+y, -50)
        glVertex2f(-677.5+y, -25)
        glVertex2f(-665+y, -50)
        glEnd()

    titik_gunung = (0,341,682,1023)
    titik_rumput = (0,15,30,45,60,75,90,105,120,135,150,
                    165,180,195,210,225,240,255,270,285,
                    300,315,330,345,360,375,390,405,420,
                    435,450,465,480,495,510,525,540,555,
                    570,585,600,615,630,645,660,675,690,
                    705,720,735,750,765,780,795,810,825,
                    840,855,870,885,900,915,930,945,960,
                    975,990,1005,1020,1035,1050,1065,1080,
                    1095,1110,1125,1140,1155,1170,1185,1200,
                    1215,1230,1245,1260,1275,1290,1305,1320,
                    1335,1350,1365,1380,1395,1410,1425,1440,
                    1455,1470,1485,)
    for i in titik_gunung:
        gunung(i)
    for i in titik_rumput:
        rumput(i)

    #--- LAND ---
    glBegin(GL_QUADS)
    glColor3ub(0, 255, 140)
    glVertex2f(-682, -350)
    glVertex2f(-682, -50)
    glVertex2f(682, -50)
    glVertex2f(682, -350)

    #--- RUMAH ---
    glColor3ub(173, 255, 196)
    glVertex2f(682, -50)
    glVertex2f(602, -50)
    glVertex2f(602, 30)
    glVertex2f(682, 30)
    # Atap
    glColor3ub(212, 72, 72)
    glVertex2f(682, 30)
    glVertex2f(582, 30)
    glVertex2f(612, 80)
    glVertex2f(682, 80)
    # Pintu
    glColor3ub(54, 38, 21)
    glVertex2f(602, -50)
    glVertex2f(567, -50)
    glVertex2f(567, 10)
    glVertex2f(602, 10)
    glEnd()
    # Jendela
    Lingkaran_Polygon(640,-4,20,60)
    glBegin(GL_QUADS)
    glVertex2f(620, -4)
    glVertex2f(660, -4)
    glVertex2f(660, -34)
    glVertex2f(620, -34)
    glEnd()
    # Kaca Jendela
    glColor3ub(213, 222, 220)
    Lingkaran_Polygon(640,-4,16,60)
    glBegin(GL_QUADS)
    glVertex2f(624, -4)
    glVertex2f(656, -4)
    glVertex2f(656, -30)
    glVertex2f(624, -30)
    # Bingkai
    glColor3ub(54, 38, 21)
    glVertex2f(638, 12)
    glVertex2f(642, 12)
    glVertex2f(642, -30)
    glVertex2f(638, -30)
    glVertex2f(624, -11)
    glVertex2f(656, -11)
    glVertex2f(656, -15)
    glVertex2f(624, -15)
    glEnd()

    #--- POHON ---
    glBegin(GL_QUADS)
    glColor3ub(10, 59, 22)
    glVertex2f(-638, -50)
    glVertex2f(-629, -30)
    glVertex2f(-585, -30)
    glVertex2f(-576, -50)
    glVertex2f(-629, -30)
    glVertex2f(-626, -10)
    glVertex2f(-588, -10)
    glVertex2f(-585, -30)
    glVertex2f(-626, -10)
    glVertex2f(-616, 40)
    glVertex2f(-598, 40)
    glVertex2f(-588, -10)
    # Dahan 1
    glVertex2f(-609, 40)
    glVertex2f(-596, 36)
    glVertex2f(-584, 53)
    glVertex2f(-586, 62)
    glVertex2f(-587, 53)
    glVertex2f(-586, 62)
    glVertex2f(-547, 72)
    glVertex2f(-556, 63)
    # Ranting Dahan 1
    glVertex2f(-595, 52)
    glVertex2f(-585, 54)
    glVertex2f(-596, 80)
    glVertex2f(-602, 80)
    # Dahan 2
    glVertex2f(-609, 40)
    glVertex2f(-617, 32)
    glVertex2f(-634, 53)
    glVertex2f(-632, 62)
    glVertex2f(-632, 62)
    glVertex2f(-634, 53)
    glVertex2f(-655, 66)
    glVertex2f(-662, 75)
    # Ranting Dahan 2
    glVertex2f(-622, 42)
    glVertex2f(-634, 53)
    glVertex2f(-645, 98)
    glVertex2f(-640, 90)
    glEnd()
    # Pucuk Ranting Dahan 1
    glBegin(GL_TRIANGLES)
    glVertex2f(-547, 72)
    glVertex2f(-556, 64)
    glVertex2f(-522, 68)
    glVertex2f(-550, 67)
    glVertex2f(-560, 64)
    glVertex2f(-535, 90)
    glVertex2f(-562, 67)
    glVertex2f(-567, 63)
    glVertex2f(-535, 45)
    glVertex2f(-572, 60)
    glVertex2f(-580, 60)
    glVertex2f(-556, 108)
    glVertex2f(-596, 80)
    glVertex2f(-602, 80)
    glVertex2f(-595, 113)
    glVertex2f(-595, 80)
    glVertex2f(-603, 80)
    glVertex2f(-620, 110)
    glEnd()

    # Garis Finish
    glBegin(GL_QUADS)
    glColor3ub(200, 0, 0)
    glVertex2f(-517, -49.5)
    glVertex2f(-527, -49.5)
    glVertex2f(-527, -52)
    glVertex2f(-517, -52)
    glEnd()

    def lampu():
        global Merah_lampu,Hijau_lampu

        glPushMatrix()
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex2f(-140, 260) #titik e
        glVertex2f(-140, 140) #titik h
        glVertex2f(140, 140)#titik g
        glVertex2f(140, 260) #titik f
        glEnd()
        glColor3f(Merah_lampu,0,0)
        Lingkaran_Polygon(-55, 200,50,100) #titik A
        glColor3f(0,Hijau_lampu,0)
        Lingkaran_Polygon(55, 200,50,100) #titik C
        glPopMatrix()

    def Game1_Peserta():
        glPushMatrix()
        glTranslated(pos_x,0,0)
        # Sepatu
        glColor3ub(255, 255, 255)
        glBegin(GL_POLYGON)
        glVertex2f(495, -50)
        glVertex2f(495, -45)
        glVertex2f(483, -50)
        glVertex2f(491, -45)
        glVertex2f(491, -50)
        glEnd()

        # Celana
        glColor3ub(0, 255, 51)
        glBegin(GL_QUADS)
        glVertex2f(495, -45)
        glVertex2f(491, -45)
        glVertex2f(489, -26)
        glVertex2f(497, -26)
        glColor3ub(255, 255, 255)
        glVertex2f(494, -45)
        glVertex2f(492, -45)
        glVertex2f(492, -26)
        glVertex2f(494, -26)

        # Baju
        glColor3ub(0, 255, 51)
        glVertex2f(488, -26)
        glVertex2f(498, -26)
        glVertex2f(498, -6)
        glVertex2f(488, -6)
        glEnd()
        Lingkaran_Polygon(493, -4, 5, 30)

        # Kepala
        glColor3ub(255, 204, 0)
        Lingkaran_Polygon(493, 9, 7, 30)   
        glPopMatrix()
    def Game1_Boneka():

        # Sepatu
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        glVertex2f(-560, -50)
        glVertex2f(-545, -50)
        glVertex2f(-545, -48)
        glVertex2f(-555, -45)
        glVertex2f(-560, -45)
        glEnd()
        Lingkaran_Polygon(-545.5, -48.25, 2, 30)
        Lingkaran_Polygon(-560, -47.5, 3, 30)

        # Kaki
        glBegin(GL_QUADS)
        glColor3ub(194, 242, 220)
        glVertex2f(-555, -45)
        glVertex2f(-561.5, -45)
        glVertex2f(-561.5, -30)
        glVertex2f(-555, -30)
        glColor3ub(3, 255, 139)
        glVertex2f(-561.5, -30)
        glVertex2f(-555, -30)
        glVertex2f(-555, -25)
        glVertex2f(-561.5, -25)
        glEnd()

        # Baju
        glBegin(GL_QUADS)
        glColor3ub(201, 93, 10)
        glVertex2f(-546, -25)
        glVertex2f(-570.5, -25)
        glVertex2f(-562.5, 15)
        glVertex2f(-554, 15)
        glEnd()
        Lingkaran_Polygon(-558.25, 14, 5, 30)
        glColor3ub(225, 255, 0)
        Lingkaran_Polygon(-558.25, 14, 3.5, 30)
        glBegin(GL_QUADS)
        glVertex2f(-561.5, 12)
        glVertex2f(-555, 12)
        glVertex2f(-555, 0)
        glVertex2f(-561.5, 0)
        glEnd()

        # Lengan
        glColor3ub(3, 255, 139)
        glBegin(GL_QUADS)
        glVertex2f(-555.5, 0)
        glVertex2f(-561, 0)
        glVertex2f(-561, -10)
        glVertex2f(-555.5, -10 )
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(-555.5, -10)
        glVertex2f(-551, -11.5)
        glVertex2f(-551, -13)
        glVertex2f(-561, -13)
        glVertex2f(- 561, -10)
        glEnd()

        # Kepala
        glBegin(GL_QUADS)
        glVertex2f(-560, 20)
        glVertex2f(-560, 30)
        glVertex2f(-556, 30)
        glVertex2f(-556, 20)
        glEnd()
        Lingkaran_Polygon(-556, 25, 5, 30)
        Lingkaran_Polygon(-559, 25, 5, 30)
        glColor3ub(0,0,0)
        glBegin(GL_LINES)
        glVertex2f(-566, 28)
        glVertex2f(-550, 28)
        glVertex2f(-566, 29)
        glVertex2f(-550.5, 29)
        glVertex2f(-566, 30)
        glVertex2f(-551.5, 30)
        glVertex2f(-564, 31)
        glVertex2f(-552.5, 31)
        glVertex2f(-562, 32)
        glVertex2f(-555, 32)
        glEnd()
        Lingkaran_Polygon(-568.5, 29, 3, 30)
        glBegin(GL_TRIANGLES)
        glVertex2f(-564, 29)
        glVertex2f(-572, 29)
        glVertex2f(-569, 19)
        glEnd()
    def Game1_Penjaga():

        # Sepatu
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        glVertex2f(-672, -50)
        glVertex2f(-668, -50)
        glVertex2f(-660, -50)
        glVertex2f(-668, -45)
        glVertex2f(-672, -45)
        glEnd()

        # Celana
        glBegin(GL_QUADS)
        glColor3ub(255,0,0)
        glVertex2f(-668, -45)
        glVertex2f(-672, -45)
        glVertex2f(-675, -26)
        glVertex2f(-666, -26)

        # Baju
        glVertex2f(-666, -26)
        glVertex2f(-675, -26)
        glVertex2f(-673.5, 0)
        glVertex2f(-667, 0)

        # Sabuk
        glColor3ub(0,0,0)
        glVertex2f(-675.5, -26)
        glVertex2f(-665.5, -26)
        glVertex2f(-666.5, -24)
        glVertex2f(-675.5, -24)
        glEnd()

        # Kepala
        glColor3ub(255,0,0)
        Lingkaran_Polygon(-670.5, 6, 7, 60)
        glColor3ub(0,0,0)
        glBegin(GL_LINES)
        glVertex2f(-667.5, 2)
        glVertex2f(-667.5, 10)
        glVertex2f(-666.5, -1)
        glVertex2f(-666.5, 13)
        glVertex2f(-665.5, 0)
        glVertex2f(-665.5, 12)
        glVertex2f(-664.5, 2)
        glVertex2f(-664.5, 10)
        glColor3ub(255,255,255)
        glVertex2f(-665.5, 3)
        glVertex2f(-665.5, 9)
        glVertex2f(-665.5, 9)
        glVertex2f(-664, 10)
        glVertex2f(-665.5, 3)
        glVertex2f(-664, 2)
        glEnd()

        # Lengan
        glBegin(GL_LINES)
        # SENAPAN
        glColor3ub(0,0,0)
        glVertex2f(-664, -13)
        glVertex2f(-664, -2)
        glVertex2f(-663, -13)
        glVertex2f(-663, 0)
        glEnd()
        # LENGAN
        glBegin(GL_QUADS)
        glColor3ub(255,0,0)
        glVertex2f(-675,0)
        glVertex2f(-665,-15)
        glVertex2f(-661,-10)
        glVertex2f(-668,0)
        glEnd()
        Lingkaran_Polygon(-663, -12, 3.5, 20)
    
    def time_lampu():
        global Merah_lampu,Hijau_lampu,Gerak
        import time, random
        localtime = time.localtime(time.time())
        if Nyawa > 0 :
            if int(localtime.tm_sec) % random.randrange(5,6)  == 0 :
                # print('Lampu Hijau')
                Hijau_lampu = 1
                Merah_lampu = 0
                Gerak = True
            elif int(localtime.tm_sec) % random.randrange(3,4) == 0 : 
                # print("Lampu merah")
                Merah_lampu  = 1
                Hijau_lampu  = 0
                Gerak = False
        else:
            pass

    def hati(x):
        glColor3ub(200,0,0)
        Lingkaran_Polygon(643-x, 320, 7, 20)
        Lingkaran_Polygon(630-x, 320, 7, 20)
        glBegin(GL_TRIANGLES)
        glVertex2f(650.5-x, 320)
        glVertex2f(622.5-x, 320)
        glVertex2f(637-x, 300)
        glEnd()
            
  
    lampu()
    time_lampu()
    Game1_Peserta()
    Game1_Boneka()
    Game1_Penjaga()

    global jarak_hati
    
    for i in jarak_hati:
        hati(i)

def Layer_menang() :
    def background():
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(-682, -350)
        glVertex2f(682,-350)   
        glVertex2f(682,350)
        glVertex2f(-682, 350)
        glEnd()

    def tulisan_winner():

        glColor3f(0.0, 1.0, 0.0)
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
        glVertex2f(-200, 100) #titik w1
        glVertex2f(-240, 100) # titik v1

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
        glVertex2f(-20, 100) #titik w2
        glVertex2f(-60, 100) # titik v2

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
        
        glVertex2f(140, 200) #titik p2
        glVertex2f(140, 160) # titik q2
        glVertex2f(280, 160) # titik r2
        glVertex2f(280, 200) #titik s2

        # Huruf R
        glVertex2f(320, 260) #titik t2
        glVertex2f(360, 260) #titik i3
        glVertex2f(360, 100) #titik h3
        glVertex2f(320, 100) # titik u2

        glVertex2f(360, 260) #titik i3
        glVertex2f(400, 260) #titik j3
        glVertex2f(400, 230) # titik r3
        glVertex2f(360, 230) #titik q3

        glEnd()

        #//3
        glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f(400, 260) #titik j3
        glVertex2f(420,256) #titik o6
        glVertex2f(440,240) #titik p6
        glVertex2f(450,210) #titik q6
        glVertex2f(440,180) #titik r6
        glVertex2f(420,164) #titik s6
        glVertex2f(400, 160) #titik l3
        glEnd()# Mengakhiri objek   

        #//3 dalam r
        # glColor3f(1.0, 0.43, 0.78) #warma pink squid game
        # glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        # glVertex2f(400, 230) #titik r3
        # glVertex2f(417,220) #titik t6
        # glVertex2f(418,201) #titik u6
        # glVertex2f(400, 190) #titik p3
        # glEnd()# Mengakhiri objek  ]

        #//4
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f(400, 160) #titik l3
        glVertex2f(380,190) #titik n6
        glVertex2f(400, 190) #titik p3
        glVertex2f(420,164) #titik s6
        glEnd()# Mengakhiri objek

        #//5
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        glVertex2f(350, 190) #titik 06
        glVertex2f(380,190) #titik n6
        glVertex2f(460, 100) #titik m3
        glVertex2f(430, 100) #titik n3
        glEnd()# Mengakhiri objek   

    def emas():
        
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        #sisi depan
        glColor3ub(255,215,0) #warna emas
        glVertex2f(100, -140) #titik e
        glVertex2f(-100, -300) #titik l
        glVertex2f(-540, -300) #titik q
        glVertex2f(-540, -140) #titik p
        glEnd()# Mengakhiri objek

    def Nominal_emas():
        #huruf S
        glColor3ub(204, 172, 0) #kuning gelap
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        #//1
        glVertex2f(-130, -250) #titik i5
        glVertex2f(-130, -260) #titik n5
        glVertex2f(-180, -260) #titik u5
        glVertex2f(-180, -250) #titik a6
        glEnd()

        #//2
        glBegin(GL_POLYGON)
        glVertex2f(-180, -225) #titik v6
        glVertex2f(-188, -227) #titik j7
        glVertex2f(-194, -233) #titik i7
        glVertex2f(-197, -243) #titik h7
        glVertex2f(-194, -253) #titik g7
        glVertex2f(-188, -258) #titik e7
        glVertex2f(-180, -260) #titik u5
        glEnd()

        #//3
        glBegin(GL_QUADS)
        glVertex2f(-180, -225) #titik v6
        glVertex2f(-180, -235) #titik b7
        glVertex2f(-160, -235) #titik c7
        glVertex2f(-160, -225) #titik w6
        glEnd()

        #//4
        glBegin(GL_POLYGON)
        glVertex2f(-160, -235) #titik c7
        glVertex2f(-150, -232) #titik d7
        glVertex2f(-144, -224) #titik f7
        glVertex2f(-143, -214) #titik k7
        glVertex2f(-147, -206) #titik l7
        glVertex2f(-155, -201) #titik n7
        glVertex2f(-160, -200) #titik g6
        glEnd()


        #//4
        glBegin(GL_QUADS)
        glVertex2f(-160, -200) #titik g6
        glVertex2f(-160, -210) #titik z6
        glVertex2f(-198, -210) #titik a8
        glVertex2f(-198, -200) #titik e6
        glEnd()

        #garis
        glBegin(GL_QUADS)
        glVertex2f(-166, -184) #titik p7
        glVertex2f(-174, -184) #titik q7
        glVertex2f(-174, -276) #titik s7
        glVertex2f(-166, -276) #titik r7
        glEnd()

        #angka 4
        #//1
        glBegin(GL_QUADS)
        glVertex2f(-250, -200) #titik h5
        glVertex2f(-245, -206) #titik t7
        glVertex2f(-245, -270) #titik d5
        glVertex2f(-250, -270) #titik g5

        #//2
        glVertex2f(-210, -245) #titik j5
        glVertex2f(-214, -240) #titik u7
        glVertex2f(-245, -240) #titik c5
        glVertex2f(-245, -245) #titik m5

        #//3
        glVertex2f(-210, -245) #titik j5
        glVertex2f(-214, -245) #titik v7
        glVertex2f(-250, -210) #titik w7
        glVertex2f(-250, -200) #titik h5
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

    def Tombol_lanjut():
        global merah3,hijau3,biru3
        glColor3f(merah3,hijau3,biru3) # Putih
        glBegin(GL_QUADS)  
        glVertex2f(585, -260) #titik S9
        glVertex2f(585, -330)#titik v9
        glVertex2f(665, -330) #titik w9
        glVertex2f(665, -260) #titik S9
        glEnd()

    background()
    tulisan_winner()
    emas()
    Circle()
    Nominal_emas()
    logo_bitcoin()
    player() 
    Tombol_lanjut()    

def Layer_kalah():
    def background():
        glBegin(GL_QUADS)
        glColor3ub(0,0, 50)
        glVertex2f(-682, -350)
        glVertex2f(682,-350)
        
        glVertex2f(682,350)
        glVertex2f(-682, 350)
        glEnd()

    def tulisan():
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        #Huruf Y
        #//1
        glVertex2f(-560, 260) #titik s
        glVertex2f(-520, 260) #titik t
        glVertex2f(-460, 200) # titik r
        glVertex2f(-500, 200) #titik q

        #//2
        glVertex2f(-440, 260) #titik u
        glVertex2f(-400, 260) #titik v
        glVertex2f(-460, 200) # titik r
        glVertex2f(-500, 200) #titik q

        #//3
        glVertex2f(-460, 200) # titik r
        glVertex2f(-500, 200) #titik q
        glVertex2f(-500, 102) #titik o
        glVertex2f(-460, 102) #titik p

        # Huruf U
        #//1
        glVertex2f(-280, 240) # titik b1
        glVertex2f(-240, 240) #titik c1
        glVertex2f(-240, 160) #titik d1
        glVertex2f(-280, 160) #titik m1
        glEnd()

        #//2
        glBegin(GL_POLYGON)
        glVertex2f(-280, 160) #titik m1
        glVertex2f(-276, 139) # titik s4
        glVertex2f(-249, 108) #titik t4
        glVertex2f(-200, 103) #titik u4
        glVertex2f(-174, 121) #titik v4
        glVertex2f(-160, 160) #titik k1
        glEnd()
        

        #//2 sisi dalam
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(-240, 160) #titik d1
        glVertex2f(-230,143) # titik r4
        glVertex2f(-207, 145) #titik w4
        glVertex2f(-200, 160) #titik l1
        glEnd()

        #//3
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex2f(-200, 160) #titik l1
        glVertex2f(-160, 160) #titik k1
        glVertex2f(-160, 280) #titik j1
        glVertex2f(-200, 280) #titik i1

        #huruf L
        #//1
        glVertex2f(-120, 260) #titik a
        glVertex2f(-80, 260) #titik e
        glVertex2f(-80, 100) #titik z4
        glVertex2f(-120, 100) #titik b

        #//2
        glVertex2f(-120, 140) #titik a5
        glVertex2f(20, 140) #titik d
        glVertex2f(20, 100) #titik c
        glVertex2f(-120, 100) #titik b



        #Huruf S
        #//1
        glVertex2f(170, 130) #titik i
        glVertex2f(170, 100) #titik j
        glVertex2f(320, 100) #titik k
        glVertex2f(320, 130) #titik l

        #//2
        glVertex2f(320, 160) #titik m
        glVertex2f(320, 190) #titik n1
        glVertex2f(270, 190) #titik o1
        glVertex2f(270, 160) #titik n

        #//3
        glVertex2f(270, 250) #titik p1
        glVertex2f(270, 220) #titik s1
        glVertex2f(350, 220) #titik r1
        glVertex2f(350, 250) #titik q1
        glEnd()

        #//4 Lengkungan dalam
        glBegin(GL_POLYGON)
        glVertex2f(320, 100) #titik k
        glVertex2f(340, 105) #titik b5
        glVertex2f(358, 121) #titik c5
        glVertex2f(365, 143) #titik d5
        glVertex2f(362, 159) #titik e5
        glVertex2f(343, 183) #titik f5
        glVertex2f(320, 190) #titik n1
        glEnd()

        #//5 Lengkungan luar
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(320, 130) #titik l
        glVertex2f(330, 134) #titik i5
        glVertex2f(335, 144) #titik g5
        glVertex2f(331, 155) #titik h5
        glVertex2f(320, 160) #titik m
        glEnd()

        #//6 lengkungan #2 luar
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        glVertex2f(270, 160) #titik n
        glVertex2f(250, 165) #titik j5
        glVertex2f(232, 180) #titik k5
        glVertex2f(225, 200) #titik l5
        glVertex2f(228, 222) #titik m5
        glVertex2f(240, 239) #titik n5
        glVertex2f(253, 247) #titik o5
        glVertex2f(270, 250) #titik p1
        glEnd()

        #//6 lengkungan #2 dalam
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(270, 190) #titik o1
        glVertex2f(260, 194) #titik r5
        glVertex2f(255, 206) #titik p5
        glVertex2f(260, 216) #titik q5
        glVertex2f(270, 220) #titik s1
        glEnd()

        #Huruf E
        #//1
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex2f(380, 250) #titik t1
        glVertex2f(380, 100) #titik u1
        glVertex2f(410, 100) #titik v1
        glVertex2f(410, 250) #titik w1

        #//2
        glVertex2f(380, 250) #titik t1
        glVertex2f(380, 220) #titik c2
        glVertex2f(500, 220) #titik d2
        glVertex2f(500, 250) #titik e2

        #//3
        glVertex2f(380, 130) #titik z1
        glVertex2f(380, 100) #titik u1
        glVertex2f(500, 100) #titik b2
        glVertex2f(500, 130) #titik a2

        #//4
        glVertex2f(440, 190) #titik f2
        glVertex2f(440, 160) #titik g2
        glVertex2f(560, 160) #titik h2
        glVertex2f(560, 190) #titik i2
        glEnd()

    def player_killed_action():
        glColor3f(0,1,0)
        glBegin(GL_LINES)
        glVertex2f(-200, -150) #titik k2
        glVertex2f(-200, -300) #titik n2

        glVertex2f(-200, -200) #titik o2
        glVertex2f(-240, -240) #titik q2

        glVertex2f(-200, -200) #titik o2
        glVertex2f(-160, -240) #titik p2

        glVertex2f(-200, -300) #titik n2
        glVertex2f(-240, -340) #titik r2

        glVertex2f(-200, -300) #titik n2
        glVertex2f(-160, -340) #titik s2
        glEnd()

    def npc_kill_action():
        glColor3f(1,0,0)
        glBegin(GL_LINES)
        glVertex2f(40, -150) #titik m2
        glVertex2f(40, -300) #titik w2

        glVertex2f(40, -200) #titik b3
        glVertex2f(-20, -160) #titik c3

        glVertex2f(40, -200) #titik b3
        glVertex2f(120, -180) #titik d3

        glVertex2f(40, -300) #titik w2
        glVertex2f(80, -340) #titik a3

        glVertex2f(40, -300) #titik w2
        glVertex2f(5, -340) #titik z2
        glEnd()

        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glVertex2f(-30, -170) #titik f3
        glVertex2f(-20, -170) #titik g3
        glVertex2f(-20, -150) #titik h3
        glVertex2f(-30, -150) #titik s5

        glVertex2f(-20, -150) #titik h3
        glVertex2f(-20, -160) #titik c3
        glVertex2f(-50, -160) #titik j3
        glVertex2f(-50, -150) #titik i3
        glEnd()

        glColor3f(0,0,0)
        glBegin(GL_TRIANGLES)
        glVertex2f(40, -62) #titik t2
        glVertex2f(20, -102) #titik u2
        glVertex2f(60, -102) #titik v2
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
        glColor3f(1,1,1)
        lingkaran_polygon(-360, 170, 70, 100) #Huruf o #1 sisi luar
        lingkaran_polygon(100, 170, 70, 100) #Huruf o #2 sisi luar

        glColor3ub(204, 14, 117) #warma pink squid game
        lingkaran_polygon(-360, 170, 40, 100) #Huruf o #1 sisi dalam
        lingkaran_polygon(100, 170, 40, 100) #Huruf o #2 sisi dalam

        glColor3f(0,1,0)
        lingkaran_polygon(-200, -100, 50, 100) #kepala player

        glColor3f(1,0,0)
        lingkaran_polygon(-200, -80, 5, 100) #kepala player

        glColor3f(1,0,0)
        lingkaran_polygon(40, -100, 50, 100) #kepala npc

    def logo():
        glColor3ub(204, 14, 117) #warma pink squid game
        glBegin(GL_QUADS)
        glVertex2f(-500, -50) #titik d9
        glVertex2f(-200, -50) #titik e9
        glVertex2f(-200, 250)#titik f9
        glVertex2f(-500, 250) #titik c9

        glColor3f(0,0,0)
        glVertex2f(-470, 220) #titik g9
        glVertex2f(-230, 220) #titik h9
        glVertex2f(-230, -20)#titik i9
        glVertex2f(-470, -20) #titik j9
        glEnd()

        glColor3ub(204, 14, 117) #warma pink squid game
        glBegin(GL_TRIANGLES)
        glVertex2f(-100, -50) #titik k9
        glVertex2f(200, -50) #titik m9
        glVertex2f(50, 250)#titik l9

        glColor3f(0,0,0)
        glVertex2f(-50, -20) #titik n9
        glVertex2f(150, -20) #titik p9
        glVertex2f(50, 190)#titik 09
        glEnd()
        glColor3ub(204, 14, 117) #warma pink squid game
        lingkaran_polygon(400, 100,160,100)

        glColor3f(0,0,0)
        lingkaran_polygon(400, 100,120,100)

    def Tombol_lanjut():
        global merah3,hijau3,biru3
        glColor3f(merah3,hijau3,biru3) # Putih
        glBegin(GL_QUADS)  
        glVertex2f(585, -260) #titik S9
        glVertex2f(585, -330)#titik v9
        glVertex2f(665, -330) #titik w9
        glVertex2f(665, -260) #titik S9
        glEnd()

    background()
    logo()
    tulisan()
    player_killed_action()
    npc_kill_action()
    Circle()
    Tombol_lanjut()

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
    iterate()
    
    def menu():
        main_menu()
        if Pencet == True:
            permainan_1()
        if Lanjut == True:
            print("exit")
            glutLeaveMainLoop()

    def permainan_1():
        Game_1()
        if max_lose >= 5:
            Layer_kalah()
            if Pencet == False:
                main_menu()
        if pos_x <= -1000:
            Layer_menang()

    menu()
     

    glFlush()
    glutSwapBuffers()

def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1364,700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("2D SHAPE OF SQUID GAME")
    glutDisplayFunc(ShowScreen)
    glutMouseFunc(iniHandleMouse)
    glutPassiveMotionFunc(KoorMouse)
    glutSpecialFunc(input_keyboard)

    timer(0)
    glutIdleFunc(ShowScreen)
    glutMainLoop()

Main()

