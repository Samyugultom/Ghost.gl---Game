##########################
# import math
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

(keylocx,keylocy) = (400,430)
ambil_kunci = False
levels = [""]

### Variabel untuk player ###
koorx = 0
koory = 0
left = 0
right = 0
up = 0
down = 0
#############################

### Variabel untuk ghost ###
leftg = 0
rightg = 0
upg = 0
downg = 0

koorxg = 0
kooryg = 0

change_dir = False
dirg = choice(['up','down','left','right'])

Ghost_alpha = 0
baterai = 0

### Variabel untuk ghost1 ###
leftg1 = 0
rightg1 = 0
upg1 = 0
downg1 = 0

koorxg1 = 0
kooryg1 = 0
change_dir1 = False
dirg1 = choice(['up','down','left','right'])

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
nyala = False
umur_baterai = 100

### MAZE ###
screen_x = 0
screen_y = 0

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                    XXXXXXXXXXXX                      X",
"X  XXXXX  XXXXXXXXX     XXXXXXXXXXXXXXXXXXX    XXXXXXXXX",
"XX XXXX  XXXXXXXXX                             XXXXXXXXX",
"XX XXXX XXXXXX    XXX  XXXXX      XXXXX             XXXX",
"XX       XXX   XXXXX   XXXXXXX      XXXX  XXXXXXXX  XXXX",
"XX  XXX  XXXXX  XXXXXX   XXXXXXXXX     XX           XXXX",
"XX  XXX XXXX  XXXXX       XXXXXXX       XXXXXXXX   XXXXX",
"XXX  XXX XXX  XXXXXX   XXXXXXXX   XXX    XXXXXXXXX  XXXX",
"XX  XX         XXXX   XXXXXXXXX   XXXXX      XXXX  XXXXX",
"XXX   X   XXXXXXX   XXXXXXX    XXXXXXXX      X     XXXXX",
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
"XX    X   XXXXX          XXXXXXXXX  XXXXXXX    XXXXXX XX",
"XX  XX   XXXXX    XX    XXXXXX           XXX   XXXX   XX",
"XX  XXX   XXX   XXX    XXXXXX    XXXXX   XX  XXXXXX   XX",
"XX   XXX  XXXX   XXX        XX  XXXXXX      XXXXXXXXX  X",
"X   XXXX   XXX  XXXXX    XXXX   XXXXXX    XXXXXXXXXX  XX",
"X    X XXXXX   XXXX   XXXX          XXXX    XXXXXXX  XXX",
"X              XXX             XXXXXXXXXXX            XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1)

walls = []

class Draw():
    def dot(self,size,red,green,blue,x,y):
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

    def draw_ghost(self,size,red,green,blue,alpha,x,y):
        self.size = size
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        self.x = x
        self.y = y
        glPointSize(size)
        glColor4f(red,green,blue,alpha)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()

    def draw_walls(self,size,red,green,blue):
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

def setup_maze(level):
    global walls
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = 10 + (x*15)
            screen_y = 10 + (y*15)
            if character == "X":
                walls.append((screen_x,screen_y))

setup_maze(levels[1])

class Player():
    def playerk(self,x,y):
        global koorx,koory
        self.koorx = koorx = x
        self.koory = koory = y
        draw.dot(14,0,0.6,0.3,koorx+left+right,koory+up+down)

    def player_movement(key,x,y):
        global up, down, left, right, koorxg, kooryg, ambil_kunci, Ghost_alpha

        ### collision with ghost ###
        if (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg)) or (koorx+left+right, koory+up+down) == ((koorxg1+leftg1+rightg1, kooryg1+upg1+downg1)):
            draw.dot(15,0.9,0.9,0.9,koorx+left+right,koory+up+down)
            print("Player tertangkap oleh hantu!!\nGame Over")
            left -= 1000

        ### Player Movement ###
        if (koorx+left+right, koory+up+down+15) not in walls:
            if key == GLUT_KEY_UP:
                up += 15
                print(koorx+left+right, koory+up+down)
        if (koorx+left+right, koory+up+down-15) not in walls:
            if key == GLUT_KEY_DOWN:
                down -= 15
                print(koorx+left+right, koory+up+down)
        if (koorx+left+right+15, koory+up+down) not in walls:
            if key == GLUT_KEY_RIGHT:
                right += 15
                print(koorx+left+right, koory+up+down)
        if (koorx+left+right-15, koory+up+down) not in walls:
            if key == GLUT_KEY_LEFT:
                left -= 15
                print(koorx+left+right, koory+up+down)
        if ambil_kunci == True:
            if (koorx+left+(right), koory+up+down) == (820,25):
                print("SELAMAT\nANDA BERHASIL KELUAR DARI LABIRIN!!")
                right += 45
        ### Tekan tombol End untuk aktifkan ghost detector ###
        if Ghost_alpha == 0:
            if key == GLUT_KEY_END:
                Ghost_alpha += 1
                # print("hidup")
        elif Ghost_alpha == 1:
            if key == GLUT_KEY_END:
                Ghost_alpha -= 1
                # print("mati")

class Ghost():
### Ghost 0 ###
    def ghost(self):
        global upg,downg,leftg,rightg, koorxg, kooryg,left, Ghost_alpha
        self.koorxg = koorxg = 370
        self.kooryg = kooryg = 340
        self.Ghost_alpha = Ghost_alpha
        draw.draw_ghost(14,0,0,0.6,Ghost_alpha, koorxg+leftg+rightg, kooryg+upg+downg)

        if (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg)):
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(15,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 1000

    def g_dir(self):
        global change_dir,dirg
        self.change_dir = True
        self.dirg = dirg = choice(["up","down","right","left"])
        if (koorx+left+(right), koory+up+down) != (880,25):
            if self.change_dir == True:
                upg == 0
                downg == 0
                leftg == 0
                rightg == 0

                if dirg == "up":
                    self.go_up(0)
                elif dirg == "down":
                    self.go_down(0)
                elif dirg == "left":
                    self.go_left(0)
                elif dirg == "right":
                    self.go_right(0)

    def go_up(self,value):
        global upg
        self.upg = upg
        # print(koorxg+leftg+rightg, kooryg+upg+downg+15)
        self.g_dir == True
        if (koorxg+leftg+rightg, kooryg+upg+downg+15) not in walls:
            upg += 15
            glutTimerFunc(randrange(200,300,100),self.go_up,0)
        else:
            self.g_dir == True
            self.g_dir()
            # print("change")

    def go_down(self,value):
        global downg
        self.downg = downg
        # print(koorxg+leftg+rightg, kooryg+upg+downg-15)
        self.g_dir == True
        if (koorxg+leftg+rightg, kooryg+upg+downg-15) not in walls:
            downg -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down,0)
        else:
            self.g_dir == True
            self.g_dir()
            # print("change")

    def go_left(self,value):
        global leftg
        self.leftg = leftg
        # print(koorxg+leftg+rightg-15, kooryg+upg+downg)
        self.g_dir == True
        if (koorxg+leftg+rightg-15, kooryg+upg+downg) not in walls:
            leftg -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left,0)
        else:
            self.g_dir == True
            self.g_dir()
            # print("change")

    def go_right(self,value):
        global rightg
        self.rightg = rightg
        # print(koorxg+leftg+rightg+15, kooryg+upg+downg)
        self.g_dir == True
        if (koorxg+leftg+rightg+15, kooryg+upg+downg) not in walls:
            rightg += 15
            glutTimerFunc(randrange(200,300,100),self.go_right,0)
        else:
            self.g_dir == True
            self.g_dir()
            # print("change")

### Ghost 1 ###
    def ghost1(self):
        global upg1,downg1,leftg1,rightg1, koorxg1, kooryg1,left, Ghost_alpha
        self.koorxg1 = koorxg1 = 610
        self.kooryg1 = kooryg1 = 55
        self.Ghost_alpha = Ghost_alpha
        draw.draw_ghost(14,0,0.2,0.6,Ghost_alpha, koorxg1+leftg1+rightg1, kooryg1+upg1+downg1)
        if (koorx+left+right, koory+up+down) == ((koorxg1+leftg1+rightg1, kooryg1+upg1+downg1)):
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(35,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 990

    def g_dir1(self):
        global change_dir1, dirg1
        self.change_dir1 = True
        self.dirg1 = dirg1 = choice(["up","down","right","left"])
        # print(dirg1)
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
        # print(koorxg1+leftg1+rightg1, kooryg1+upg1+downg1+15)
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1, kooryg1+upg1+downg1+15) not in walls:
            upg1 += 15
            glutTimerFunc(randrange(200,300,100),self.go_up1,0)
        else:
            self.g_dir1 == True
            self.g_dir1()
            # print("change")

    def go_down1(self,value):
        global downg1
        self.downg1 = downg1
        # print(koorxg1+leftg1+rightg1, kooryg1+upg1+downg1-15)
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1, kooryg1+upg1+downg1-15) not in walls:
            downg1 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down1,0)
        else:
            self.g_dir1 == True
            self.g_dir1()
            # print("change")

    def go_left1(self,value):
        global leftg1
        self.leftg1 = leftg1
        # print(koorxg1+leftg1+rightg1-15, kooryg1+upg1+downg1)
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1-15, kooryg1+upg1+downg1) not in walls:
            leftg1 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left1,0)
        else:
            self.g_dir1 == True
            self.g_dir1()
            # print("change")

    def go_right1(self,value):
        global rightg1
        self.rightg1 = rightg1
        # print(koorxg1+leftg1+rightg1+15, kooryg1+upg1+downg1)
        self.g_dir1 == True
        if (koorxg1+leftg1+rightg1+15, kooryg1+upg1+downg1) not in walls:
            rightg1 += 15
            glutTimerFunc(randrange(200,300,100),self.go_right1,0)
        else:
            self.g_dir1 == True
            self.g_dir1()
            # print("change")

### Ghost 2 ###
    def ghost2(self):
        global upg2,downg2,leftg2,rightg2, koorxg2, kooryg2,left, Ghost_alpha
        self.koorxg2 = koorxg2 = 115
        self.kooryg2 = kooryg2 = 55
        self.Ghost_alpha = Ghost_alpha
        draw.draw_ghost(14,0.7,0.0,0.0,Ghost_alpha, koorxg2+leftg2+rightg2, kooryg2+upg2+downg2)
        if (koorx+left+right, koory+up+down) == ((koorxg2+leftg2+rightg2, kooryg2+upg2+downg2)):
            print("Player tertangkap oleh hantu!!\nGame Over")
            draw.draw_ghost(35,0.9,0.9,0.9,Ghost_alpha,koorx+left+right,koory+up+down)
            left -= 990

    def g_dir2(self):
        global change_dir2, dirg2
        self.change_dir2 = True
        self.dirg2 = dirg2 = choice(["up","down","right","left"])
        # print(dirg1)
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
        # print(koorxg1+leftg1+rightg1, kooryg1+upg1+downg1+15)
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2, kooryg2+upg2+downg2+15) not in walls:
            upg2 += 15
            glutTimerFunc(randrange(200,300,100),self.go_up2,0)
        else:
            self.g_dir2 == True
            self.g_dir2()
            # print("change")

    def go_down2(self,value):
        global downg2
        self.downg2 = downg2
        # print(koorxg1+leftg1+rightg1, kooryg1+upg1+downg1-15)
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2, kooryg2+upg2+downg2-15) not in walls:
            downg2 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_down2,0)
        else:
            self.g_dir2 == True
            self.g_dir2()
            # print("change")

    def go_left2(self,value):
        global leftg2
        self.leftg2 = leftg2
        # print(koorxg1+leftg1+rightg1-15, kooryg1+upg1+downg1)
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2-15, kooryg2+upg2+downg2) not in walls:
            leftg2 -= 15
            glutTimerFunc(randrange(200,300,100),self.go_left2,0)
        else:
            self.g_dir2 == True
            self.g_dir2()
            # print("change")

    def go_right2(self,value):
        global rightg2
        self.rightg2 = rightg2
        # print(koorxg1+leftg1+rightg1+15, kooryg1+upg1+downg1)
        self.g_dir2 == True
        if (koorxg2+leftg2+rightg2+15, kooryg2+upg2+downg2) not in walls:
            rightg2 += 15
            glutTimerFunc(randrange(200,300,100),self.go_right2,0)
        else:
            self.g_dir2 == True
            self.g_dir2()
            # print("change")

class ExitKey():
    def exitkey(self,x,y):
        global keylocx,keylocy,ambil_kunci,koorx,left,right, koory,up,down
        self.keylocx = keylocx = x
        self.keylocy = keylocy = y
        draw.dot(10,255,0,255,keylocx,keylocy)
        draw.dot(4,0,0,0,keylocx,keylocy)
        draw.dot(6,255,0,255,keylocx+8,keylocy)
        draw.dot(6,255,0,255,keylocx+14,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy-3)

        if ambil_kunci == True:
            draw.dot(14,0.2,0.3,0.1,835,25)
            glColor3f(0.9,0.9,0.9)
            ExitKey.text_exit(850,20,"Exit")

        if (keylocx,keylocy) == (koorx+(left-15)+(right+15), koory+(up+15)+(down-15)):
            ambil_kunci = True
            keylocx += 470
            keylocy -= 90
            print("Kunci keluar telah diambil\nCepat! Cari jalan keluar!")

    def text_kunci(xpos, ypos,text):
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))

    def text_exit(xpos, ypos,text):
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(text[i]))

### class instance ###
draw = Draw()
player = Player()
exitkey = ExitKey()
ghosts = Ghost()

def iterate():
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.2,0.3,0.1,1)
    glLoadIdentity()
    iterate()
    player.playerk(25,25)
    draw.draw_walls(14,0.5,0.2,0.1)
    # sleep(0.1)
    glColor3f(0, 0.5, 0.9)
    ExitKey.text_kunci(850,350,"kunci")
    ghosts.ghost()
    ghosts.ghost1()
    ghosts.ghost2()
    exitkey.exitkey(keylocx,keylocy)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("ini maze")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(Player.player_movement)
ghosts.g_dir()
ghosts.g_dir1()
ghosts.g_dir2()
glutMainLoop()