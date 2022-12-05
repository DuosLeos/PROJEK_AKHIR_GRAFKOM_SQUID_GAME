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
        if Pencet == False and (-640 <= PosisiX <= -460 and -140 <= PosisiY <= -40):
            Pencet = True
        if (-640 <= PosisiX <= -460 and -260 <= PosisiY <= -160):
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
    if (-640<= PosisiX <= -460 and -140 <= PosisiY <= -40):
        merah = 0
        hijau = 1
        biru = 0
    if (PosisiX <= -640 or -460  <= PosisiX or PosisiY <=-140 or -40 <= PosisiY):
        merah = 1
        hijau = 1
        biru = 1

    if (-640 <= PosisiX <= -460 and -260 <= PosisiY <= -160):
        merah2 = 0
        hijau2 = 1
        biru2 = 0
    if (PosisiX <= -640 or -460 <= PosisiX or PosisiY <= -260 or -160 <= PosisiY):
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

        glPopMatrix()

    def logo():
        glPushMatrix()
        #bintang besar
        #//1
   
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
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-400,200)#titik F
         glVertex2f (-280.3981451085366,202.1865402888576)#titik E
         glVertex2f (-281.4159084699256,168.9335130756445)#titik K
         glVertex2f (-357.9387663390008,167.6365154846433)#titik L
         glVertex2f (-357.9387663390008,130.0235853456063)#titik M
         glVertex2f (-400.2970829679632,106.2673900013163)#titik G
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-357.9387663390008,130.0235853456063)#titik M
         glVertex2f (-400.2970829679632,106.2673900013163)#titik G
         glVertex2f (-277.733724267216,103.6029691599957)#titik H
         glVertex2f (-229.5360048298746,137.8055708916139)#titik N
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)
         glVertex2f (-277.733724267216,103.6029691599957)#titik H
         glVertex2f (-229.5360048298746,137.8055708916139)#titik N
         glVertex2f (-224.3480144658695,-26.913123165548)#titik O
         glVertex2f (-280,0)#titik l
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)
         glVertex2f (-224.3480144658695,-26.913123165548)#titik O
         glVertex2f (-398.1456916600404,-33.3981111205544)#titik P
         glVertex2f (-400, 0 )#titik J
         glVertex2f (-280,0)#titik l
         glEnd()

         #garis huruf q
         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-200, 200)#titik Q
         glVertex2f (-169.9598498999853, 162.7128195360355)#titik Z
         glVertex2f (-86.6266898850762, 161.6711550358492)#titik C1
         glVertex2f (-51.2100968787398, 201.254406042931)#titik T
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-54.3350903792989, -8.1201584945281)#titik U
         glVertex2f (-82.4600318843308, 9.5881380086401)#titik B1
         glVertex2f (-86.6266898850762, 161.6711550358492)#titik C1
         glVertex2f (-51.2100968787398, 201.254406042931)#titik T
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-54.3350903792989, -8.1201584945281)#titik U
         glVertex2f (-82.4600318843308, 9.5881380086401)#titik B1
         glVertex2f (0, -100)#titik V
         glVertex2f (-36.6267938761307, -101.8699635113008)#titik W
         glVertex2f (-109.3894818824777, -22.4148438341348)#titik S
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-82.4600318843308, 9.5881380086401)#titik B1
         glVertex2f (-54.3350903792989, -8.1201584945281)#titik U
         glVertex2f (-109.3894818824777, -22.4148438341348)#titik S
         glVertex2f (-198.0847914050171, -23.7451259973236)#titik R
         glVertex2f (-165.7931918992399, 8.5464735084537)#titik A1
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-198.0847914050171, -23.7451259973236)#titik R
         glVertex2f (-165.7931918992399, 8.5464735084537)#titik A1
         glVertex2f (-169.9598498999853, 162.7128195360355)#titik Z
         glVertex2f (-200, 200)#titik Q
         glEnd()
         
         #huruf U
         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (0, 200)#titik D
         glVertex2f (33.0583310062419, 200.1748152770248)#titik H1
         glVertex2f (43.9389927138686, 47.8455513702514)#titik l1
         glVertex2f (0,0)#titik E1
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (43.9389927138686, 47.8455513702514)#titik l1
         glVertex2f (0,0)#titik E1
         glVertex2f (132, 0)#titik F1
         glVertex2f (95.2335407641087, 46.2911711263047)#titik J1
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (132, 0)#titik F1
         glVertex2f (95.2335407641087, 46.2911711263047)#titik J1
         glVertex2f (100, 200)#titik K1
         glVertex2f (137.2018073506687, 197.0660547891314)#titik G1
         glEnd()

         #huruf I
         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (179.9359349200683, 196.9614674998164)#titik L1
         glVertex2f (167.1437764555124, 1.8810509153372)#titik M1
         glVertex2f (211.1168211774235, 1.0815410113024)#titik O1
         glVertex2f (212.715840985493, 196.1619575957816)#titik N1
         glEnd()

         # huruf D
         # //1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (257.0461158103591, 198.4442701854224)#titik P1
         glVertex2f (289.1983479061838, 177.3443678725373)#titik T1
         glVertex2f (375.6074716637128, 153.2301938006687)#titik V1
         glVertex2f (350, 200)#titik S1
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (350, 200)#titik S1
         glVertex2f (375.6074716637128, 153.2301938006687)#titik V1
         glVertex2f (411.7787327715157, 174.3300961135538)#titik Z1
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (375.6074716637128, 153.2301938006687)#titik V1
         glVertex2f (411.7787327715157, 174.3300961135538)#titik Z1
         glVertex2f (402.735917494565, 20.6022364053912)#titik R1
         glVertex2f (374.6027144107183, 52.754468501216)#titik W1
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (402.735917494565, 20.6022364053912)#titik R1
         glVertex2f (374.6027144107183, 52.754468501216)#titik W1
         glVertex2f (289.1983479061838, 35.6735952003091)#titik U1
         glVertex2f (260,0)#titik Q1
         glEnd()
         
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (289.1983479061838, 35.6735952003091)#titik U1
         glVertex2f (260,0)#titik Q1
         glVertex2f (257.0461158103591, 198.4442701854224)#titik P1
         glVertex2f (289.1983479061838, 177.3443678725373)#titik T1
         glEnd()

         #=========GAME=========
         #Huruf G
         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-117.5434245291542, -94.1984729565961)#titik A2
         glVertex2f (-125.9999825457698, -133.0986398330282)#titik l2
         glVertex2f (-220.7134323318653, -133.0986398330282)#titik j2
         glVertex2f (-244.3917947783892, -95.8897845599192)#titik B2
         glEnd()
         
         #//2 
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-220.7134323318653, -133.0986398330282)#titik j2
         glVertex2f (-244.3917947783892, -95.8897845599192)#titik B2
         glVertex2f (-310.3529473079914, -155.085690676229)#titik C2
         glVertex2f (-257.9222876049742, -171.9988067094604)#titik K2
         glEnd()
         
         #//3
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-310.3529473079914, -155.085690676229)#titik C2
         glVertex2f (-257.9222876049742, -171.9988067094604)#titik K2
         glVertex2f (-269.7614688282362, -232.8860244290933)#titik L2
         glVertex2f (-322.1921285312533, -237.9599592390627)#titik D2
         glEnd()
         #//4
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-269.7614688282362, -232.8860244290933)#titik L2
         glVertex2f (-322.1921285312533, -237.9599592390627)#titik D2
         glVertex2f (-266.3788456215899, -295.4645537520494)#titik E2
         glVertex2f (-203.800316298634, -249.7991404623247)#titik M2
         glEnd()

         #//5
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-266.3788456215899, -295.4645537520494)#titik E2
         glVertex2f (-203.800316298634, -249.7991404623247)#titik M2
         glVertex2f (-177.8414922100025, -233.7896469555579)#titik N2
         glVertex2f (-200, -300)#titik F2
         glEnd()

         #//5
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-177.8414922100025, -233.7896469555579)#titik N2
         glVertex2f (-200, -300)#titik F2
         glVertex2f (-114.1608013225079, -215.9729083958619)#titik G2
         glEnd()

         #//6
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-177.8414922100025, -233.7896469555579)#titik N2
         glVertex2f (-114.1608013225079, -215.9729083958619)#titik G2
         glVertex2f (-220.7134323318653, -207.5163503792463)#titik H2
         glVertex2f (-233.4116799068374, -225.8510487131529)#titik O2
         glEnd()
         #Huruf A
         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-42.2136848484562, -122.028320342029)#titik P2
         glVertex2f (-35.8576017153063, -208.6299530311967)#titik S2
         glVertex2f (-100, -300)#titik R2
         glVertex2f (-150, -300)#titik Q2
         glEnd()

         #//2
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-42.2136848484562, -122.028320342029)#titik P2
         glVertex2f (-35.8576017153063, -208.6299530311967)#titik S2
         glVertex2f (12.7561457499604, -228.6204610355472)#titik W2
         glVertex2f (46.4742475029727, -119.9692962303112)#titik T2
         glEnd()
         #  //3
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (12.7561457499604, -228.6204610355472)#titik W2
         glVertex2f (46.4742475029727, -119.9692962303112)#titik T2
         glVertex2f (69.6192720958971, -301.4451667066592)#titik U2
         glVertex2f (33.7057186142529, -306.4331602457765)#titik V2
         glEnd()

         #  A dalem pink
         glColor3ub(255, 153, 204)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-29.3402700978092, -148.7247220804493)#titik v7
         glVertex2f (17.8917233402977, -147.7986045620551)#titik W7
         glVertex2f (18.8178408586919, -188.5477753714009)#titik Z7
         glVertex2f (-31.1925051345977, -181.1388352242471)#titik A8
         glEnd()

         #Huruf m
         #//1
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (100, -300)#titik A3
         glVertex2f (143.6478049625043, -288.2643877302697)#titik L3
         glVertex2f (129.5730295344887, -159.8320619496266)#titik K3
         glVertex2f (86.2618257771104, -99.9461979381938)#titik Z2
         glEnd()

         #//2
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (86.2618257771104, -99.9461979381938)#titik Z2
         glVertex2f (163.299003688429, -101.1499038430581)#titik B3
         glVertex2f (129.5730295344887, -159.8320619496266)#titik K3
         glEnd()

         #//3
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (129.5730295344887, -159.8320619496266)#titik K3
         glVertex2f (163.299003688429, -101.1499038430581)#titik B3
         glVertex2f (182.5582981662587, -181.7981994689702)#titik C3
         glVertex2f (166.5193150330297, -224.9278983041992)#titik J3
         glEnd()

         #//4
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (166.5193150330297, -224.9278983041992)#titik J3
         glVertex2f (182.5582981662587, -181.7981994689702)#titik C3
         glVertex2f (205.2249474600727, -223.1685513756972)#titik l3
         glEnd()

         #//5
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (205.2249474600727, -223.1685513756972)#titik l3
         glVertex2f (182.5582981662587, -181.7981994689702)#titik C3
         glVertex2f (212.6509457878676, -105.9647274625156)#titik D3
         glVertex2f (250.9679676011236, -168.6287965921364)#titik H3
         glEnd()
         
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (250.9679676011236, -168.6287965921364)#titik H3
         glVertex2f (212.6509457878676, -105.9647274625156)#titik D3
         glVertex2f (286.1549061711627, -100.0142663805599)#titik E3
         glEnd()
         
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (286.1549061711627, -100.0142663805599)#titik E3
         glVertex2f (290.6468730960428, -281.2996144999011)#titik F3
         glVertex2f (250.9679676011236, -284.7456938732658)#titik G3
         glVertex2f (250.9679676011236, -168.6287965921364)#titik H3
         glEnd()

         #Huruf E
         #//0
         glColor3f(1,1,1)
         glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (450.1034708039131, -51.6919288607136)#titik W3
         glVertex2f (457.7189589734655, -71.9998973128537)#titik Z3
         glVertex2f (400, -100)#titik V3
         glVertex2f (334.6019002323669, -99.9233539345462)#titik M3
         glEnd()


         #//1
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (334.6019002323669, -99.9233539345462)#titik M3
         glVertex2f (400, -100)#titik V3
         glVertex2f (385.3718213627169, -145.6162829518613)#titik U3
         glVertex2f (366.3331009388356, -196.3862040822114)#titik R3
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (385.3718213627169, -145.6162829518613)#titik U3
         glVertex2f (366.3331009388356, -196.3862040822114)#titik R3
         glVertex2f (453.9112148886893, -173.5397395735539)#titik S3
         glVertex2f (452.6419668604306, -132.9238026692738)#titik T3
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (385.3718213627169, -145.6162829518613)#titik U3
         glVertex2f (334.6019002323669, -99.9233539345462)#titik M3
         glVertex2f (330.7941561475907, -301.7337904276878)#titik N3
         glVertex2f (365.0638529105769, -244.617629156044)#titik Q3
         glVertex2f (366.3331009388356, -196.3862040822114)#titik R3
         glEnd()

         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (330.7941561475907, -301.7337904276878)#titik N3
         glVertex2f (365.0638529105769, -244.617629156044)#titik Q3
         glVertex2f (450.1034708039131, -223.0404126756452)#titik P3
         glVertex2f (452.6419668604306, -266.1948456364428)#titik O3
         glEnd()
         # Warna pink
         glColor3ub(255, 153, 204)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (457.7189589734655, -71.9998973128537)#titik Z3
         glVertex2f (400, -100)#titik V3
         glVertex2f (385.3718213627169, -145.6162829518613)#titik U3
         glVertex2f (452.6419668604306, -132.9238026692738)#titik T3
         glEnd()
         
         glColor3ub(255, 153, 204)# menetapkan warna menjadi kuning
         glBegin(GL_POLYGON) 
         glVertex2f (450.1034708039131, -223.0404126756452)#titik P3
         glVertex2f (453.9112148886893, -173.5397395735539)#titik S3
         glVertex2f (366.3331009388356, -196.3862040822114)#titik R3
         glVertex2f (365.0638529105769, -244.617629156044)#titik Q3
         glEnd()
         
         glPopMatrix()

    def Bingkai_menu():
         glPushMatrix()
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
         glVertex2f (-650, -30)#titik B8
         glVertex2f (-450, -30)#titik C8
         glVertex2f (-450, -150)#titik Z7
         glVertex2f (-650, -150)#titik W7
         
         glColor3f(0,0,0)# menetapkan warna menjadi kuning
         glVertex2f (-640, -40)#titik A4
         glVertex2f (-640, -140)#titik B4
         glVertex2f (-460, -140)#titik D4
         glVertex2f (-460, -40)#titik C4

         #kotak quit
         glColor3f(1,1,1)# menetapkan warna menjadi kuning
         glVertex2f (-650, -150)#titik W7
         glVertex2f (-650, -270)#titik V7
         glVertex2f (-450, -270)#titik A8
         glVertex2f (-450, -150)#titik Z7

         glColor3f(0,0,0)# menetapkan warna menjadi kuning
         glVertex2f (-640, -160)#titik E4
         glVertex2f (-640, -260)#titik F4
         glVertex2f (-460, -260)#titik G4
         glVertex2f (-460, -160)#titik H4

         glEnd() #Mengakhiri objek

         glPopMatrix()

    def tulisan_start():
      glPushMatrix()
      
      #============= START =============
      #huruf s
      #//1
      glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f(-602.7559159105535, -63.1996507473249) #titik l4
      glVertex2f(-603.5210359498011, -74.8127957958856) #titik O4
      glVertex2f(-623.6170378732514, -74.3741168768651) #titik P4
      glVertex2f(-629.9178685179241, -64.6292272003445) #titik J4
      glEnd()# Mengakhiri objek  

      #//2
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f(-629.9178685179241, -64.6292272003445) #titik J4
      glVertex2f(-623.6170378732514, -74.3741168768651)#titik P4
      glVertex2f(-620, -89.9) #titik Q4
      glVertex2f(-629.9178685179241, -97.5094856197931)#titik K4
      glEnd()# Mengakhiri objek  


      #//3
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f(-620, -89.9) #titik Q4
      glVertex2f(-629.9178685179241, -97.5094856197931)#titik K4
      glVertex2f(-607.0446452696121, -100.3686385258321)#titik L4
      glVertex2f(-600, -89.9) #titik R4
      glEnd()# Mengakhiri objek  

      # #//4
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f(-607.0446452696121, -100.3686385258321)#titik L4
      glVertex2f(-600, -89.9) #titik R4
      glVertex2f(-597.1197715816262, -120.3328979695743) #titik S4
      glVertex2f(-607.0446452696121, -117.5235559620662) #titik M4
      glEnd()# Mengakhiri objek  

      # #//5
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f(-597.1197715816262, -120.3328979695743) #titik S4
      glVertex2f(-607.0446452696121, -117.5235559620662) #titik M4
      glVertex2f(-630.6326567444339, -117.5235559620662) #titik N4
      glVertex2f(-626.9923386331094, -124.2447817501257)#titik T4
      glEnd()# Mengakhiri objek  


      #huruf T
      #//1
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-594.9860167922345, -63.4327702524633)#titik U4
      glVertex2f (-594.6303909940026, -73.3902926029578)#titik V4
      glVertex2f (-562.9325745170911, -72.4467451635837)#titik D5
      glVertex2f (-555.9562495476276, -63.8951210074671)#titik C5
      glEnd()# Mengakhiri objek  

      #//2
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-580.2608655702747, -72.8968306454846)#titik W4
      glVertex2f(-572.3843696370095, -74.0220443502368)#titik B5
      glVertex2f (-577.3353099379191, -117.0052078717704)#titik A5
      glVertex2f (-584.3116349073827, -117.2302506127209)#titik Z4
      glEnd()# Mengakhiri objek  

      #huruf A
      #//1
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-567.0763802783653, -113.3446618975105)#titik F5
      glVertex2f (-562.1782871113811, -113.3446618975105)#titik L5
      glVertex2f (-553.2726631714099, -92.1938050400789)#titik K5
      glVertex2f (-552.6047413759121, -64.1410896291695)#titik E5
      glEnd()# Mengakhiri objek  

      #//2
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-553.2726631714099, -92.1938050400789)#titik K5
      glVertex2f (-552.6047413759121, -64.1410896291695)#titik E5
      glVertex2f (-544.8123204284373, -63.6958084321709)#titik G5
      glVertex2f (-546.3708046179322, -91.9711644415796)#titik J5
      glEnd()# Mengakhiri objek  

      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-544.8123204284373, -63.6958084321709)#titik G5
      glVertex2f (-546.3708046179322, -91.9711644415796)#titik J5
      glVertex2f (-540.8047896554502, -119.8012392539897)#titik l5
      glVertex2f (-533.6802905034733, -118.6880362614932)#titik H5
      glEnd()# Mengakhiri objek  
   
      #huruf r
      #//1
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-504.7997426683807, -62.5675369658114)#titik O5
      glVertex2f (-504.7997426683807, -76.1343089570932)#titik P5
      glVertex2f (-520, -89.9)#titik Q5
      glVertex2f (-529.5851914986066, -64.1329337340363)#titik M5
      glEnd()# Mengakhiri objek 

      #//2
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-520, -89.9)#titik Q5
      glVertex2f (-529.5851914986066, -64.1329337340363)#titik M5
      glVertex2f (-526.9761968848986, -118.6609211605337)#titik N5
      glVertex2f (-521.2364087347411, -117.8782227764213)#titik U5
      glEnd()# Mengakhiri objek 

      #//3
      # glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-520, -89.9)#titik Q5
      glVertex2f (-521.2364087347411, -101.4415567100609)#titik T5
      glVertex2f (-514.4530227391002, -114.7474292399717)#titik S5
      glVertex2f(-506.6260388979762, -112.3993340876345)#titik R5
      glEnd()

      #//4 warna pink
      glColor3ub(255, 153, 204)
      glBegin(GL_QUADS)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-511.3222292026507, -66.2201294250027)#titik A6
      glVertex2f (-510.2786313571675, -71.9599175751604)#titik Z5
      glVertex2f (-522.2800065802243, -83.4394938754756)#titik W5
      glVertex2f (-522.8018055029659, -69.0900235000815)#titik V5
      glEnd()# Mengakhiri objek 
      
      #huruf T
      #//1
      glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-497.3344649795508, -61.8370671798031)#titik B6
      glVertex2f (-497.1163336021505, -72.7436360498188)#titik C6
      glVertex2f (-468.000157346757, -72.9530421721231)#titik H6
      glVertex2f (-468.000157346757, -61.3397276393303)#titik l6
      glEnd()# Mengakhiri objek  

      #//2
      glColor3f(merah,hijau,biru)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-489.69986677054, -72.7436360498188)#titik D6
      glVertex2f(-482.7807394794021, -72.9530421721231)#titik G6
      glVertex2f (-483.0446784460564, -113.8635820035515)#titik F6
      glVertex2f (-489.9070915790702, -113.8635820035515)#titik E6
      glEnd()# Mengakhiri objek  
      glPopMatrix()

    def tulisan_exit():
      glPushMatrix()
      #=============EXIT============= 
      #Huruf E
      #//1
      glColor3f(merah2,hijau2,biru2)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-590.3067342179772, -175.9178712212961)#titik t6
      glVertex2f (-591.023734365581, -183.326872746534)#titik U6
      glVertex2f (-606.7977376128661, -184.5218729925402)#titik S6
      glVertex2f (-618.3144006204549, -176.3506634987146)#titik J6
      glEnd()# Mengakhiri objek  

      # //2
      # glColor3f(merah2,hijau2,biru2)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-618.3144006204549, -176.3506634987146)#titik J6
      glVertex2f (-606.7977376128661, -184.5218729925402)#titik S6
      glVertex2f (-611.1646047827719, -218.8025762849464)#titik N6
      glVertex2f (-621.8892985392964, -230.4209945211783)#titik K6
      glEnd()# Mengakhiri objek 

      #//3
      # glColor3f(merah2,hijau2,biru2)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-607.5897068639304, -191.543979653787)#titik R6
      glVertex2f (-591.5026662291435, -188.4159439748015)#titik Q6
      glVertex2f (-591.5026662291435, -201.3749489305986)#titik P6
      glVertex2f (-607.5897068639304, -202.2686734103087)#titik O6
      glEnd()# Mengakhiri objek 

      #//4
      # glColor3f(merah2,hijau2,biru2)
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-611.1646047827719, -218.8025762849464)#titik N6
      glVertex2f (-621.8892985392964, -230.4209945211783)#titik K6
      glVertex2f (-594.1838396682747, -230.8678567610334)#titik L6
      glVertex2f (-594.1838396682747, -220.5900252443667)#titik M6
      glEnd()# Mengakhiri objek 

      #Huruf X
      # //1
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-583.6147328403412, -175.2008710736924)#titik V6
      glVertex2f (-575.0107310690947, -174.4838709260887)#titik W6
      glVertex2f (-566.599999999997, -198.2)#titik Z6
      glVertex2f (-573.8157308230883, -197.6668756986075)#titik l7
      glVertex2f (-565.9287291994458, -204.597877125443)#titik F7
      glEnd()# Mengakhiri objek 
      
      # //2
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-551.8277262965698, -229.6928822915716)#titik D7
      glVertex2f (-556.8467273297969, -230.8878825375778)#titik E7
      glVertex2f (-565.9287291994458, -204.597877125443)#titik F7
      glVertex2f (-566.599999999997, -198.2)#titik Z6
      glVertex2f (-560.6707281170175, -196.9498755510038)#titik C7
      glEnd()# Mengakhiri objek 
      
      # //3
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-562.5827285106278, -175.6788711720948)#titik A7
      glVertex2f (-554.9347269361866, -175.9178712212961)#titik B7
      glVertex2f (-560.6707281170175, -196.9498755510038)#titik C7
      glVertex2f (-566.599999999997, -198.2)#titik Z6
      glEnd()# Mengakhiri objek 
      
      # //4
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-584.8097330863476, -228.9758821439679)#titik H7
      glVertex2f (-579.7907320531206, -228.9758821439679)#titik G7
      glVertex2f (-565.9287291994458, -204.597877125443)#titik F7
      glVertex2f (-566.599999999997, -198.2)#titik Z6
      glVertex2f (-573.8157308230883, -197.6668756986075)#titik l7
      glEnd()# Mengakhiri objek 
      
      # Huruf I
      # //1
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-538.9594583397594, -176.9072808305017)#titik M7
      glVertex2f (-546.599999999997, -178.2)#titik J7
      glVertex2f (-546.6763652905702, -229.5638223771968)#titik K7
      glVertex2f (-539.1864261912538, -229.7907902286912)#titik L7
      glEnd()# Mengakhiri objek 

      # Huruf T
      # //1
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-531.5937527863596, -175.6432625233768)#titik N7
      glVertex2f (-532.6104566495143, -184.7935972917673)#titik U7
      glVertex2f (-482.7919673549309, -183.5227174628241)#titik P7
      glVertex2f (-481.7752634917761, -174.118206728645)#titik O7
      glEnd()# Mengakhiri objek 

      # //2
      glBegin(GL_POLYGON)  # memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
      glVertex2f (-503.3802205838149, -182.251837633881)#titik Q7
      glVertex2f (-512.2763793864191, -184.0310693944014)#titik T7
      glVertex2f (-510.4971476258983, -225.4617518179471)#titik S7
      glVertex2f(-504.3969244469696, -226.4784556811015)#titik R7
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
    tulisan_judul()


def Game_1():

    #=-=-=-=- Latar -=-=-=-=
    #--- LANGIT ---
    glBegin(GL_QUADS)
    glColor3ub(135 , 206 , 235)
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

    def tulisan_YouWin():

        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        # Huruf Y
        glVertex2f(-558.3482480887665, 290.4439587288034) #titik E
        glVertex2f(-519.2007882925448, 304.4882893627338) #titik G
        glVertex2f(-485.8933190281239, 228.203440402286) # titik H
        glVertex2f(-515.5603556138905, 201.3025160728115)#titik F

        glVertex2f(-455.8091532409052, 301.2649858855318) #titik I
        glVertex2f(-412.8317735448783, 294.8183789311278) #titik J
        glVertex2f(-520.2752227849454, 103.5690392838079) #titik K
        glVertex2f(-558.3482480887665, 117.5095599761792)#titik L
        
        # Huruf O
        glVertex2f(-381.6731732652589, 295.8928134235284)#titik M
        glVertex2f(-253.8154686695791, 299.1161169007305) #titik P
        glVertex2f(-254.8899031619797, 104.6434737762086) # titik O
        glVertex2f(-380.5987387728582, 104.6434737762086)#titik N
      

        # Huruf U
        glVertex2f(-227.7484851434938, 297.7940781343482) #titik U
        glVertex2f(-200, 300)#titik A1
        glVertex2f(-201.962388464912, 135.2295555954625) #titik B1
        glVertex2f(-229.9907544198922, 104.9589203640838) # titik V

        glVertex2f(-201.962388464912, 135.2295555954625) #titik B1
        glVertex2f(-229.9907544198922, 104.9589203640838) #titik V
        glVertex2f(-129.0886369819634, 102.7166510876854) #titik W
        glVertex2f(-155.9958682987444, 132.9872863190641) # titik C1

        glVertex2f(-155.9958682987444, 132.9872863190641) #titik C1
        glVertex2f(-129.0886369819634, 102.7166510876854) #titik W
        glVertex2f(-126.8463677055649, 298.9152127725474) # titik Z
        glVertex2f(-153.753599022346, 298.9152127725474) #titik D1


        # Huruf W
        glVertex2f(-66.3050972428076, 297.7940781343482) #titik E1
        glVertex2f(-31.5499234586322, 296.672943496149) #titik P1
        glVertex2f(9.9320581547386, 180.0749411234309) #titik O1
        glVertex2f(-38.2767312878274, 103.8377857258845) # titik F1

        glVertex2f(9.9320581547386, 180.0749411234309) #titik O1
        glVertex2f(-38.2767312878274, 103.8377857258845) # titik F1
        glVertex2f(18.9011352603323, 99.3532471730877)#titik G1
        glVertex2f(34.5970201951212, 143.0774980628569)# titik H1

        glVertex2f(9.9320581547386, 180.0749411234309) #titik O1
        glVertex2f(34.5970201951212, 143.0774980628569) #titik H1
        glVertex2f(65.988790064699, 182.3172103998294) #titik M1
        glVertex2f(39.081558747918, 215.9512495458057) # titik N1

        glVertex2f(65.988790064699, 182.3172103998294) #titik M1
        glVertex2f(34.5970201951212, 143.0774980628569) #titik H1
        glVertex2f(52.5351744063085, 108.3223242786814) #titik I1
        glVertex2f(100, 100) # titik J1

        glVertex2f(52.5351744063085, 108.3223242786814) #titik I1
        glVertex2f(100, 100) #titik J1
        glVertex2f(128.7723298038548, 302.278616687145) #titik K1
        glVertex2f(100, 300) # titik L1
       
        # Huruf I
        glVertex2f(150, 300) #titik Q1
        glVertex2f(200, 300) #titik T1
        glVertex2f(200, 100) #titik S1
        glVertex2f(150, 100) # titik R1

        # Huruf N
        glVertex2f(243.1280629001741, 298.9152127725474) #titik U1
        glVertex2f(276.2207946421577, 299.31898093948) #titik W1
        glVertex2f(277.8832366843496, 100.4743818112868) # titik E2
        glVertex2f(242.0069282619749, 101.5955164494861)#titik V1

        glVertex2f(276.2207946421577, 299.31898093948) #titik W1
        glVertex2f(274.5198327697519, 210.3455763548096)#titik F2
        glVertex2f(317.1229490213219, 104.9589203640837) # titik D2
        glVertex2f(328.2816457114811, 171.5963596494065) #titik Z1

        glVertex2f(317.1229490213219, 104.9589203640837) #titik D2
        glVertex2f(359.7260652728918, 104.9589203640837) #titik C2
        glVertex2f(365.3317384638879, 300.0363474107465) # titik B2
        glVertex2f(331.6976993179116, 300.0363474107465) #titik A2
        
        glEnd()
      #  dalem Huruf O
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(-359.1577473869547, 274.122549255441)#titik Q
        glVertex2f(-280.8135084471286, 277.0513058513224) #titik T
        glVertex2f(-277.8847518512472, 124.0237737165216) # titik S
        glVertex2f(-359.1577473869547, 122.5593954185809)#titik R
        glEnd()


    def emas():
        
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        #sisi depan
        glColor3ub(255,215,0) #warna emas
        glVertex2f(-272, -24) #titik H2
        glVertex2f(-272, -200) #titik l2
        glVertex2f(300, -200)#titik J2
        glVertex2f(300, -24) #titik K2
        glEnd()# Mengakhiri objek

    def dolar_emas():
        #huruf S
        glColor3ub(204, 172, 0) #kuning gelap
        glBegin(GL_QUADS)#memulai membuat sebuah objek, GL_POLIGON untuk mengambar poligon
        #//1
        glVertex2f(60.3226165473092, -60.1530838478018) #titik L2
        glVertex2f(60.8286947294992, -89.5056184148179)#titik M2
        glVertex2f(-50.508505352286, -88.999540232628)#titik O2
        glVertex2f(-81.3792744658719, -60.6591620299917) #titik N2

        glVertex2f(-81.3792744658719, -60.6591620299917) #titik N2
        glVertex2f(-50.508505352286, -88.999540232628) #titik O2
        glVertex2f(-48.9902708057162, -109.2426675202253) #titik P2
        glVertex2f(-81.3792744658719, -134.040498447532) #titik Q2
        
        glVertex2f(-48.9902708057162, -109.2426675202253) #titik P2
        glVertex2f(-81.3792744658719, -134.040498447532) #titik Q2
        glVertex2f(43.1159583528515, -132.5222639009621) #titik S2
        glVertex2f(59.8165383651193, -109.2426675202253) #titik R2
        
        glVertex2f(59.8165383651193, -109.2426675202253) #titik R2
        glVertex2f(43.1159583528515, -132.5222639009621)#titik S2
        glVertex2f(43.1159583528515, -155.8018602816991) #titik T2
        glVertex2f(61.840851093879, -173.0085184761568)#titik U2
        
        glVertex2f(43.1159583528515, -155.8018602816991) #titik T2
        glVertex2f(61.840851093879, -173.0085184761568)#titik U2
        glVertex2f(-85.4278999233913, -174.5267530227266) #titik W2
        glVertex2f(-81.8853526480618, -155.8018602816991)#titik V2
        
        glVertex2f(-23.6516884239555, -40.7265587305026) #titik Z2
        glVertex2f(-4.4101113946123, -40.039517237825) #titik C3
        glVertex2f(-4.5885344340126, -188.8046919446165) #titik B3
        glVertex2f(-25.8478457956111, -189.5377716467406) #titik A3
        
        
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
    tulisan_YouWin()
    emas()
    Circle()
    dolar_emas()
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
        #huruf L
        glBegin(GL_POLYGON)
        glVertex2f(-383,0) 
        glVertex2f(-384,199) 
        glVertex2f(-300,200) 
        glVertex2f(-305,58) 
        glVertex2f(-200,60) 
        glVertex2f(-200,0) 
        glVertex2f(-383,0) 
        glEnd()

        #huruf O
        glBegin(GL_QUADS)
        glVertex2f(-150,0) 
        glVertex2f(-146,183) 
        glVertex2f(-54,207) 
        glVertex2f(-50,0) 
        glVertex2f(-150,0)  
        glEnd()
        

        #huruf 0 dalam 
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(-127, 28) #titik d1
        glVertex2f(-120,161) # titik r4
        glVertex2f(-69, 176) #titik w4
        glVertex2f(-78, 26) #titik l1
        glEnd()

        #huruf S

        glColor3f(1,1,1)
        #huruf L
        glBegin(GL_POLYGON)
        glVertex2f(80,200) 
        glVertex2f(220,200) 
        glVertex2f(219,174) 
        glVertex2f(140,174) 
        glVertex2f(140,140) 
        glVertex2f(206,109) 
        glVertex2f(206,75) 
        glVertex2f(65,42) 
        glEnd()
    
        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(56, 147) 
        glVertex2f(133,108) 
        glVertex2f(133,87) 
        glVertex2f(67, 73) 
        glVertex2f(56, 147)  
        glEnd()



        #huruf E
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        glVertex2f(332,208) 
        glVertex2f(469,207) 
        glVertex2f(468,174) 
        glVertex2f(381,174) 
        glVertex2f(381,140) 
        glVertex2f(466,139) 
        glVertex2f(467,103) 
        glVertex2f(381,101) 
        glVertex2f(381,58) 
        glVertex2f(463,60) 
        glVertex2f(464,27) 
        glVertex2f(333,21) 
        glVertex2f(332,208) 
        glEnd()

        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(381, 174) 
        glVertex2f(468,174) 
        glVertex2f(466,139) 
        glVertex2f(381, 140) 
        glVertex2f(381, 174)  
        glEnd()

        glColor3f(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(467, 103) 
        glVertex2f(463,60) 
        glVertex2f(381,58) 
        glVertex2f(381, 101) 
        glVertex2f(467, 103)   
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
        # lingkaran_polygon(-360, 170, 70, 100) #Huruf o #1 sisi luar
        # lingkaran_polygon(100, 170, 70, 100) #Huruf o #2 sisi luar

        # glColor3ub(204, 14, 117) #warma pink squid game
        # lingkaran_polygon(-360, 170, 40, 100) #Huruf o #1 sisi dalam
        # lingkaran_polygon(100, 170, 40, 100) #Huruf o #2 sisi dalam

        glColor3f(0,1,0)
        lingkaran_polygon(-200, -100, 50, 100) #kepala player

        glColor3f(1,0,0)
        lingkaran_polygon(-200, -80, 5, 100) #kepala player

        glColor3f(1,0,0)
        lingkaran_polygon(40, -100, 50, 100) #kepala npc

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

