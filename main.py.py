##########################
import sys
from random import choice, randrange
from time import sleep

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''
ERROR: PyOpenGL not installed properly.
        ''')
  sys.exit()
###########################

###  32 Column 40 rows ###

# variabel global # 
(keylocx,keylocy) = (400,430)
ambil_kunci = False
levels = [""]
ani = 0

### Variabel untuk player ###
koorx = 0
koory = 0
left = 0
right = 0
up = 0
down = 0

### Variabel untuk ghost ###
leftg = 0
rightg = 0
upg = 0
downg = 0
koorxg = 0
kooryg = 0
change_dir = False
dirg = choice(['up','down','left','right'])

### Variabel untuk ghost1 ###
leftg1 = 0
rightg1 = 0
upg1 = 0
downg1 = 0
koorxg1 = 0
kooryg1 = 0
change_dir1 = False
dirg1 = choice(['up','down','left','right'])
Ghost_alpha = 0

### Variabel untuk ghost2 ###
leftg2 = 0
rightg2 = 0
upg2 = 0
downg2 = 0
koorxg2 = 0
kooryg2 = 0
change_dir2 = False
dirg2 = choice(['up','down','left','right'])

### Baterai ###
nyala_baterai = False
baterai = 90
baterai_habis = False

### MAZE ###
screen_x = 0
screen_y = 0

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                    XXXXXXXXXXXX                      X",
"X  XXXXX  XXXXXXXXX     XXXXXXXXX XXXXXXXXX    XXXXXXXXX",
"XX XXXX  XXXXXXXX            XXX               XXXXXXXXX",
"XX XXXX XXXXXX    XXX  XXXXX   X  XXXXX             XXXX",
"XX       XXX   XXXXX   XXXXXXX      XXXX  XXXXXXXX  XXXX",
"XX  XXX  XXXX   XXXXXX   XXXXXXXXX     XX           XXXX",
"XX  XXX XXXX  XXXXX       XXXXXXX       XXXXXXXX   XXXXX",
"XXX  XXX XXX  XXXXXX   XXXXXXXX   XXX    XXXXXXXXX  XXXX",
"XX  XX         XXXX   XXXXXXXXX   XXXXX      XXXX  XXXXX",
"XXX   X   XXXXXXX   XXXXXX    XXXXXXXXX      XX    XXXXX",
"XXX  X   XXXXXXXXXX        XXXXXXXXXXXXXXXX    X   XXXXX",
"XXX     XXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXX XXXX   XXXXX",
"XXX  XXXXXXXXXXXXXXX               XXXXXXXX XXX    XXXXX",
"X     XX              X    XXXXXX   XXXXXXX XX  XXXXXXXX",
"XX X     XXX   XXX  XXX  XXXXXX     XXXXXXX XXX      XXX",
"XX    XX   XXXXXXXXXX   XXXXXXXXX      XXX  XXXXX    XXX",
"XX   XXX    XXX XXXX   XXXX       XXXXXX   XX          X",
"X    XXX              XXXXX      XXXXXXX XX            X",
"X XX    XXXXX    XXXXXX              XXX XXX  XXXXXXXXXX",
"X XX  XXXXXX      XXX    XXXXX     XXXXX XXXX  XXXXXXXXX",
"X     XXXXX    XXXXXX       XXXXX  XXXXX XX        XXXXX",
"XX  XXXXXXX    XXXX      XXXXXXXXX  XXXXXX     XXXXXXXXX",
"XX  XXXXX    XXXXXXXX   XXXXXXXXX  XXXXXXXX    XXXXX XXX",
"XX  XX    XXXXXXXXX    XXXXXXXXX  XXXXXXXXXX         XXX",
"XX   XX   XXXXX          XXXXXXXXX  XXXXXXX    XXXXXX XX",
"XX  XX   XXXXX    XX    XXXXXX           XXX   XXXX   XX",
"XX  XXX   XXX   XXX    XXXXXX    XXXXX   XX  XXXXXX   XX",
"XX   XXX  XXXX   XXX        XX  XXXXXX      XXXXXXXXX  X",
"X   XXXX   XXX  XXXXX    XXXX   XXXXXX    XXXXXXXXXX  XX",
"X    X XXXXX   XXXX   XXXX          XXXX    XXXXXXX  XXX",
"X              XXX             XXXXXXXXXXX            XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1) #menambah level ke list levels
walls = [] #koordinat dinding

def animation(value): #animasi karakter yang dapat bergerak
    global ani
    if ani == 0:
        ani += 2
        glutTimerFunc(150,animation,0)

    elif ani== 2:
        ani -= 2
        glutTimerFunc(150,animation,0)

class Draw(): #membuat class draw untuk menggambar
    def dot(self,size,red,green,blue,x,y): #point
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        glPointSize(size)
        glBegin(GL_POINTS)
        glColor3f(red,green,blue)
        glVertex2f(x,y)
        glEnd()

    def draw_ghost(self,size,red,green,blue,alpha,x,y): #point dengan alpha
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        self.x = x
        self.y = y
        glPushMatrix()
        glPointSize(size)
        glTranslatef(0,ani,0)
        glColor4f(red,green,blue,alpha)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        glPopMatrix()

    def draw_ghostline(self,size,red,green,blue,alpha,x1,y1,x2,y2): #line dengan alpha
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        glPushMatrix()
        glLineWidth(size)
        glTranslatef(0,ani,0)
        glColor4f(red,green,blue,alpha)
        glBegin(GL_LINES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()
        glPopMatrix()

    def draw_walls(self,size,red,green,blue): #point untuk dinding
        global screen_x,screen_y
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        glPointSize(size)
        glBegin(GL_POINTS)
        glColor3f(red,green,blue)
        for i in walls:
            glVertex2f(i[0],i[1])
        glEnd()

def setup_maze(level): #setup maze dengan parameter level
    global walls
    for y in range(len(level)): # untuk setiap baris
        for x in range(len(level[y])): #setiap koordinat pada baris
            character = level[y][x] #variabel karakter dengan isi setiap pasang koordinat
            screen_x = 10 + (x*15) #mengasign koordinat x pada setup maze
            screen_y = 10 + (y*15) #mengasign koordinat y pada setup maze
            if character == "X": #jika karakter adalah X
                walls.append((screen_x,screen_y)) #menambah koordinat screen_x dan screen_y pada walls

setup_maze(levels[1]) #memanggil setup maze

class Player(): #membuat kelas player
    def playerk(self,x,y): #menggambar player
        global koorx,koory
        self.koorx = koorx = x
        self.koory = koory = y
        draw.draw_ghostline(4,0.9,0.8,0.8,1,(koorx-4)+left+right,(koory+2)+up+down,(koorx+4)+left+right,(koory+2)+up+down)
        draw.draw_ghostline(5,0.6,0.6,0.6,1,(koorx-4)+left+right,(koory+6)+up+down,(koorx+4)+left+right,(koory+6)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx-4)+left+right,(koory-3)+up+down,(koorx-4)+left+right,(koory+3)+up+down)
        draw.draw_ghostline(2,0.9,0.8,0.8,1,(koorx-2)+left+right,(koory-7)+up+down,(koorx-2)+left+right,(koory-4)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx-5)+left+right,(koory+2)+up+down,(koorx-5)+left+right,(koory+8)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx-5)+left+right,(koory+8)+up+down,(koorx-3)+left+right,(koory+10)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx-3)+left+right,(koory+10)+up+down,(koorx+3)+left+right,(koory+10)+up+down)
        draw.draw_ghostline(3,0.9,0.8,0.9,1,(koorx+4)+left+right,(koory-1)+up+down,(koorx-4)+left+right,(koory-1)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx-5)+left+right,(koory)+up+down,(koorx+4)+left+right,(koory)+up+down)
        draw.draw_ghostline(2,0.8,0.1,0.9,1,(koorx+2)+left+right,(koory)+up+down,(koorx-2)+left+right,(koory)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx+4)+left+right,(koory-3)+up+down,(koorx-4)+left+right,(koory-3)+up+down)
        draw.draw_ghostline(2,0.6,0.1,0.8,1,(koorx+3)+left+right,(koory-3)+up+down,(koorx-3)+left+right,(koory-3)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx+5)+left+right,(koory+2)+up+down,(koorx+5)+left+right,(koory+8)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx+4)+left+right,(koory-3)+up+down,(koorx+4)+left+right,(koory+3)+up+down)
        draw.draw_ghostline(2,0.9,0.8,0.8,1,(koorx+2)+left+right,(koory-7)+up+down,(koorx+2)+left+right,(koory-4)+up+down)
        draw.draw_ghostline(1,0.3,0.3,0.3,1,(koorx+5)+left+right,(koory+8)+up+down,(koorx+3)+left+right,(koory+10)+up+down)

        draw.draw_ghost(2,0.9,0.8,0.8,1,(koorx+1)+left+right,(koory+5)+up+down)
        draw.draw_ghost(2,0.9,0.8,0.8,1,(koorx-1.5)+left+right,(koory+5)+up+down)
        draw.draw_ghostline(1,0,0.7,0.9,1,(koorx+1.5)+left+right,(koory+3)+up+down,(koorx+1.5)+left+right,(koory+6)+up+down)
        draw.draw_ghostline(1,0,0.7,0.9,1,(koorx-1.5)+left+right,(koory+3)+up+down,(koorx-1.5)+left+right,(koory+6)+up+down)

    def player_movement(key,x,y): #membuat perilaku dan colision player 
        global up, down, left, right, koorxg, kooryg, ambil_kunci, Ghost_alpha,nyala_baterai,baterai_habis
        ### collision dengan ghost ###
        #jika player berada tepat pada ghost atau diatasnya satu kotak
        if (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg)) or (koorx+left+right, koory+up+down) == ((koorxg1+leftg1+rightg1, kooryg1+upg1+downg1)):
            draw.dot(15,0.9,0.9,0.9,koorx+left+right,koory+up+down) #membuat player berwarna putih untuk animasi mati
            print("Player tertangkap oleh hantu!!\nGame Over") #pemberitahuan di terminal
            left -= 1000 #player dipindah keluar dari map

        ### Player Movement ###
        if (koorx+left+right, koory+up+down+15) not in walls: #jika koordinat diatas player tidak ada pada walls
            if key == GLUT_KEY_UP: #jika menekan tombol up
                up += 15
        if (koorx+left+right, koory+up+down-15) not in walls:
            if key == GLUT_KEY_DOWN:
                down -= 15
        if (koorx+left+right+15, koory+up+down) not in walls:
            if key == GLUT_KEY_RIGHT:
                right += 15
        if (koorx+left+right-15, koory+up+down) not in walls:
            if key == GLUT_KEY_LEFT:
                left -= 15
        if ambil_kunci == True: #jika mengambil kunci
            if (koorx+left+(right), koory+up+down) == (820,25): #jikakoordinat player = pintu keluar
                print("SELAMAT\nANDA BERHASIL KELUAR DARI LABIRIN!!") 
                right += 45 #mengeluarkan player melalui pintu keluar

        ### Jika baterai > 0###
        if baterai >= 0:
            baterai_habis = False
            ### Kalau hantunya tidak kelihatan ###
            if Ghost_alpha == 0:
                ### Kalau player menekan tombol END ###
                if key == GLUT_KEY_END:
                    if baterai >= 0:
                        ### nyala baterai jadi True
                        nyala_baterai = True
                        ### Transparasi hantu jadi 1 ###
                        Ghost_alpha += 1

            #jika hantu kelilhatan
            elif Ghost_alpha == 1:
                if key == GLUT_KEY_END:
                    nyala_baterai = False
                    Ghost_alpha -= 1
                    baterai == 0

        #jika baterai habis
        elif baterai == 0 or baterai <= 0:
            Ghost_alpha = 0 #hantu akan tidak terlihat
            baterai_habis = True
        else:
            Ghost_alpha = 0

    def minbaterai(value): #logika pengurangan baterai
        global baterai, nyala_baterai
        if baterai_habis == False: #jika baterai belum habis
            if nyala_baterai == True: #jika ghost detector dinyalakan
                baterai -= 5 #baterai berkurang
            elif nyala_baterai == False: #jika ghost detector tidak dinyalakan
                baterai -= 0 #baterai tidak berkurang
        elif baterai_habis == True: #jika baterai habis
            baterai = 0 #baterai tetap pada angka 0
        else:
            baterai = 0
        glutTimerFunc(500,Player.minbaterai,0) #mengulangi fungsi setiap 0.5 detik

    def gbr_baterai(): #gambar baterai
    ### BATERAI ###
        glBegin(GL_QUADS)
        glColor3f(1,1,0)
        glVertex2f(860,460)
        glVertex2f(860,480)
        glVertex2f(860+baterai,480)
        glVertex2f(860+baterai,460)
        glVertex2f(848,465)
        glVertex2f(848,475)
        glVertex2f(856,475)
        glVertex2f(856,465)
        glEnd()

        glLineWidth(1)
        glBegin(GL_LINES)
        glColor3f(1,1,0)
        glVertex2f(858,482)
        glVertex2f(858,458)
        glVertex2f(857,482)
        glVertex2f(952,482)
        glVertex2f(952,482)
        glVertex2f(952,458)
        glVertex2f(952,458)
        glVertex2f(858,458)
        glEnd()

class Ghost(): #kelas ghost
### Ghost 0 ###
    def slender(self,gx,gy,atas,bawah,kanan,kiri): #method untuk menggambar ghost
        self.x = x = gx
        self.y = y = gy
        self.at = at = atas
        self.ba = ba = bawah
        self.ka = ka = kanan
        self.ki = ki = kiri
        ### Kepala ###
        draw.draw_ghostline(12,0.9,0.9,0.9,Ghost_alpha,(x-4)+ki+ka,(y+20)+at+ba, (x+4)+ki+ka,(y+20)+at+ba)
        draw.draw_ghostline(2.5,0,0,0,Ghost_alpha, (x-4)+ki+ka,(y+28)+at+ba, (x+4)+ki+ka,(y+28)+at+ba)
        draw.draw_ghost(2,0,0,0,Ghost_alpha, (x-5)+ki+ka, (y+27)+at+ba)
        draw.draw_ghost(2,0,0,0,Ghost_alpha, (x+5)+ki+ka, (y+27)+at+ba)
        draw.draw_ghostline(2.5,0,0,0,Ghost_alpha, (x-6)+ki+ka,(y+26)+at+ba, (x-6)+ki+ka,(y+14)+at+ba)
        draw.draw_ghostline(2.5,0,0,0,Ghost_alpha, (x+6)+ki+ka,(y+26)+at+ba, (x+6)+ki+ka,(y+14)+at+ba)
        draw.draw_ghost(2,0,0,0,Ghost_alpha, (x-5)+ki+ka, (y+13)+at+ba)
        draw.draw_ghost(2,0,0,0,Ghost_alpha, (x+5)+ki+ka, (y+13)+at+ba)
        draw.draw_ghostline(2.5,0,0,0,Ghost_alpha, (x-4)+ki+ka,(y+12)+at+ba, (x+4)+ki+ka,(y+12)+at+ba)
        ### Wajah ###
        draw.draw_ghostline(3,0,0,0,Ghost_alpha, (x)+ki+ka,(y+20)+at+ba, (x)+ki+ka,(y+15)+at+ba)
        draw.draw_ghost(3,0.7,0,0,Ghost_alpha, (x-3)+ki+ka,(y+23)+at+ba)
        draw.draw_ghost(3,0.7,0,0,Ghost_alpha, (x+2)+ki+ka,(y+23)+at+ba)
        ### Badan ###
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-4)+ki+ka,(y+10)+at+ba, (x+4)+ki+ka,(y+10)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-6)+ki+ka,(y+8)+at+ba, (x+6)+ki+ka,(y+8)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-8)+ki+ka,(y+6)+at+ba, (x+8)+ki+ka,(y+6)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-8)+ki+ka,(y+4)+at+ba, (x+8)+ki+ka,(y+4)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-8)+ki+ka,(y+2)+at+ba, (x+8)+ki+ka,(y+2)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-8)+ki+ka,(y)+at+ba, (x+8)+ki+ka,(y)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-6)+ki+ka,(y-2)+at+ba, (x+6)+ki+ka,(y-2)+at+ba)
        draw.draw_ghost(3.5,0.9,0.9,0.9,Ghost_alpha, (x)+ki+ka, (y+6)+at+ba)
        draw.draw_ghostline(2,0,0,0,Ghost_alpha, (x-4)+ki+ka,(y-4)+at+ba, (x+4)+ki+ka,(y-4)+at+ba)
        draw.draw_ghost(2,0.9,0.9,0.9,Ghost_alpha, (x-5)+ki+ka, (y)+at+ba)
        draw.draw_ghost(2,0.9,0.9,0.9,Ghost_alpha, (x+5)+ki+ka, (y)+at+ba)
        ### Dasi ###
        draw.draw_ghostline(2,0.8,0,0,Ghost_alpha, (x)+ki+ka,(y+8)+at+ba, (x)+ki+ka,(y)+at+ba)
        ### Kaki ###
        draw.draw_ghostline(5,0,0,0,Ghost_alpha, (x-3)+ki+ka,(y-2)+at+ba, (x-3)+ki+ka,(y-8)+at+ba)
        draw.draw_ghostline(5,0,0,0,Ghost_alpha, (x+3)+ki+ka,(y-2)+at+ba, (x+3)+ki+ka,(y-8)+at+ba)

    def ghost(self): #ghost pertama
        global upg,downg,leftg,rightg, koorxg, kooryg,left, Ghost_alpha
        self.koorxg = koorxg = 370 #koordinat pertama
        self.kooryg = kooryg = 340
        self.Ghost_alpha = Ghost_alpha
        self.slender(koorxg,kooryg,upg,downg,rightg,leftg) #memanggil fungsi menggambar
        if (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg)) or (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg+15)):
            #collision dengan player
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(15,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 1000

    def g_dir(self): #movement ai dari ghost
        global change_dir,dirg
        self.change_dir = True #pengubah arah
        self.dirg = dirg = choice(["up","down","right","left"]) #pemilih aras
        if (koorx+left+(right), koory+up+down) != (880,25): #jika player belum keluar dari pintu exit
            if self.change_dir == True: #pengubah arah = True
                upg == 0
                downg == 0
                leftg == 0
                rightg == 0

                if dirg == "up": #jika ke atas
                    self.go_up(0) #memanggil fungsi keatas
                elif dirg == "down": #dan seterusnya
                    self.go_down(0)
                elif dirg == "left":
                    self.go_left(0)
                elif dirg == "right":
                    self.go_right(0)

    def go_up(self,value): #fungsi ke atas
        global upg
        self.upg = upg 
        self.g_dir == True #pengubah arah = True
        if (koorxg+leftg+rightg, kooryg+upg+downg+15) not in walls: #jika hantu tidak menabrak dinding
            upg += 15 #berjalan ke atas
            glutTimerFunc(randrange(200,300,100),self.go_up,0) #mengulangi sampai menabrak dinding
        else:
            self.g_dir() #jika menabrak dinding, maka mencari arah baru

    #fungsi sama dengan go_up
    def go_down(self,value):
        global downg
        self.downg = downg
        self.g_dir == True
        if (koorxg+leftg+rightg, kooryg+upg+downg-15) not in walls:
            downg -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down,0)
        else:
            self.g_dir()

    def go_left(self,value):
        global leftg
        self.leftg = leftg
        self.g_dir == True
        if (koorxg+leftg+rightg-15, kooryg+upg+downg) not in walls:
            leftg -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left,0)
        else:
            self.g_dir()
            # print("change")

    def go_right(self,value):
        global rightg
        self.rightg = rightg
        self.g_dir == True
        if (koorxg+leftg+rightg+15, kooryg+upg+downg) not in walls:
            rightg += 15
            draw.draw_ghost(8,0,0,0,Ghost_alpha, (koorxg+7)+leftg+rightg, (kooryg+7)+upg+downg)
            glutTimerFunc(randrange(200,300,100),self.go_right,0)
        else:
            self.g_dir()

### Ghost 1 ###
### Slenderman ###
    def ghost1(self):
        global upg1,downg1,leftg1,rightg1, koorxg1, kooryg1,left, Ghost_alpha
        self.koorxg1 = koorxg1 = 610
        self.kooryg1 = kooryg1 = 55
        self.Ghost_alpha = Ghost_alpha
        self.slender(koorxg1,kooryg1,upg1,downg1,rightg1,leftg1)
        if (koorx+left+right, koory+up+down) == ((koorxg1+leftg1+rightg1, kooryg1+upg1+downg1)) or (koorx+left+right, koory+up+down) == ((koorxg1+leftg1+rightg1, kooryg1+upg1+downg1+15)):
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(35,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 990

    def g_dir1(self):
        global change_dir1, dirg1
        self.change_dir1 = True
        self.dirg1 = dirg1 = choice(["up","down","right","left"])
        if (koorx+left+(right), koory+up+down) != (880,25):
            if self.change_dir1 == True:
                upg1 == 0
                downg1 == 0
                leftg1 == 0
                rightg1 == 0
                if dirg1 == "up":
                    self.go_up1(0)
                elif dirg1 == "down":
                    self.go_down1(0)
                elif dirg1 == "left":
                    self.go_left1(0)
                elif dirg1 == "right":
                    self.go_right1(0)

    def go_up1(self,value):
        global upg1
        self.upg1 = upg1
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1, kooryg1+upg1+downg1+15) not in walls:
            upg1 += 15
            glutTimerFunc(randrange(200,300,100),self.go_up1,0)
        else:
            self.g_dir1()

    def go_down1(self,value):
        global downg1
        self.downg1 = downg1
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1, kooryg1+upg1+downg1-15) not in walls:
            downg1 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down1,0)
        else:
            self.g_dir1()

    def go_left1(self,value):
        global leftg1
        self.leftg1 = leftg1
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1-15, kooryg1+upg1+downg1) not in walls:
            leftg1 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left1,0)
        else:
            self.g_dir1()

    def go_right1(self,value):
        global rightg1
        self.rightg1 = rightg1
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1+15, kooryg1+upg1+downg1) not in walls:
            rightg1 += 15
            glutTimerFunc(randrange(200,300,100),self.go_right1,0)
        else:
            self.g_dir1()

### Ghost 2 ###
    def ghost2(self):
        global upg2,downg2,leftg2,rightg2, koorxg2, kooryg2,left, Ghost_alpha
        self.koorxg2 = koorxg2 = 115
        self.kooryg2 = kooryg2 = 55
        self.Ghost_alpha = Ghost_alpha
        self.slender(koorxg2,kooryg2, upg2,downg2,rightg2,leftg2)
        if (koorx+left+right, koory+up+down) == ((koorxg2+leftg2+rightg2, kooryg2+upg2+downg2)) or (koorx+left+right, koory+up+down) == ((koorxg2+leftg2+rightg2, kooryg2+upg2+downg2+15)):
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(35,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 990

    def g_dir2(self):
        global change_dir2, dirg2
        self.change_dir2 = True
        self.dirg2 = dirg2 = choice(["up","down","right","left"])
        if (koorx+left+(right), koory+up+down) != (880,25):
            if self.change_dir2 == True:
                upg2 == 0
                downg2 == 0
                leftg2 == 0
                rightg2 == 0
                if dirg2 == "up":
                    self.go_up2(0)
                elif dirg2 == "down":
                    self.go_down2(0)
                elif dirg2 == "left":
                    self.go_left2(0)
                elif dirg2 == "right":
                    self.go_right2(0)

    def go_up2(self,value):
        global upg2
        self.upg2 = upg2
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2, kooryg2+upg2+downg2+15) not in walls:
            upg2 += 15
            glutTimerFunc(randrange(200,300,100),self.go_up2,0)
        else:
            self.g_dir2()

    def go_down2(self,value):
        global downg2
        self.downg2 = downg2
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2, kooryg2+upg2+downg2-15) not in walls:
            downg2 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down2,0)
        else:
            self.g_dir2()

    def go_left2(self,value):
        global leftg2
        self.leftg2 = leftg2
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2-15, kooryg2+upg2+downg2) not in walls:
            leftg2 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left2,0)
        else:
            self.g_dir2()

    def go_right2(self,value):
        global rightg2
        self.rightg2 = rightg2
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2+15, kooryg2+upg2+downg2) not in walls:
            rightg2 += 15
            glutTimerFunc(randrange(200,300,100),self.go_right2,0)
        else:
            self.g_dir2()

class ExitKey(): #kelas kunci keluar
    def exitkey(self,x,y): #method untuk menggambar kunci
        global keylocx,keylocy,ambil_kunci,koorx,left,right, koory,up,down
        self.keylocx = keylocx = x
        self.keylocy = keylocy = y
        draw.dot(10,255,0,255,keylocx,keylocy)
        draw.dot(4,0,0,0,keylocx,keylocy)
        draw.dot(6,255,0,255,keylocx+8,keylocy)
        draw.dot(6,255,0,255,keylocx+14,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy-3)

        if ambil_kunci == True: #jika player telah mengambil kunci
            draw.dot(15,0.45,0.65,0.4,835,25) #membuka pintu keluar
            glColor3f(0.7,0.4,0)
            ExitKey.text_exit(850,20,"Exit") #memberitahu letak pintu keluar

        if (keylocx,keylocy) == (koorx+(left-15)+(right+15), koory+(up+15)+(down-15)): #jika player berada pada letak kunci
            ambil_kunci = True #ambil kunci = True
            keylocx += 470 #mengubah lokasi kunci ke interface
            keylocy -= 90
            print("Kunci keluar telah diambil\nCepat! Cari jalan keluar!")

    def text_kunci(xpos, ypos,text): #teks kunci
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))

    def text_exit(xpos, ypos,text): #teks exit
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(text[i]))

    def petunjuk(xpos, ypos,text): #teks petunjuk
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(text[i]))

### class instance ###
draw = Draw()
player = Player()
exitkey = ExitKey()
ghosts = Ghost()

def iterate(): #iterasi
    glViewport(0, 0, 1000, 500) #ukuran viewport
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glEnable(GL_BLEND) 
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) #untuk menyalakan alpha
    glLoadIdentity()


def showScreen(): #apa yang ditampilkan di viewport
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #jenis color dan depth buffer
    glClearColor(0.1,0.2,0.3,0.4) #warna latar belakang
    glLoadIdentity()
    iterate() #memanggil iterasi
    draw.draw_walls(15,0.1,0.7,1.9) #menggambar dinding
    player.playerk(25,25) #menggambar player
    sleep(0.15) # membuat player berjalan lebih lambat dari hantu
    glColor3f(0, 0.5, 0.9) #warna teks kunci
    ExitKey.text_kunci(850,350,"kunci") #teks kunci
    glColor3f(0.9,0.9,0)
    ExitKey.petunjuk(850,440,"Baterai Ghost Detector")
    glColor3f(0.9,0,0)
    ExitKey.petunjuk(850,100,"Tekan tombol END")
    ExitKey.petunjuk(850,80,"untuk aktifkan ghost detector")
    ghosts.ghost() #menggambar ghost 1
    ghosts.ghost1() #ghost2
    ghosts.ghost2() #ghost3
    Player.gbr_baterai() #gambar baterai
    exitkey.exitkey(keylocx,keylocy) #kunci exit
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100,0)
wind = glutCreateWindow("Ghost.gl")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(Player.player_movement) #fungsi special untuk player
ghosts.g_dir() #memanggil ai dari ghost
ghosts.g_dir1() #ghost 2
ghosts.g_dir2() #ghost3
player.minbaterai() #pengurangan baterai saat dinyalakan
animation(0) #animasi dari player dan hantu
glutMainLoop()