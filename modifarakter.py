##########################
# import math
import sys
from random import choice, randrange

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

(keylocx,keylocy) = (505,250)
ambil_kunci = False
levels = [""]

### Variabel untuk player ###
koorx = 0
koory = 0
left = 0
right = 0
up = 0
down = 0
p_mati = False
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

### Baterai ###
nyala = False
umur_baterai = 100

### Jumpscare ###


### MAZE ###
screen_x = 0
screen_y = 0

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                    XXXXXXXXXXXX                XXXXXXX",
"X  XXXXXX XXXXXXXXX     XXXXXXXXXXXXXXXXXXX    XXXXXXXXX",
"XX XXX   XXXXXXXXX                         G   XXXXXXXXX",
"XX XXXX XXXXXX    XXX  XXXXX      XXXXX             XXXX",
"XX       XXX   XXXXX   XXXXXXX G    XXXX  XXXXXXXX  XXXX",
"XX  XXX  XXXXX  XXXXXX   XXXXXXXXX     XX           XXXX",
"XX  XXX XXXX  XXXXX       XXXXXXX       XXXXXXXX   XXXXX",
"XXX  XXX XXX  XXXXXX   XXXXXXXX   XXX    XXXXXXXXX  XXXX",
"XX  XX   G     XXXX   XXXXXXXXX   XXXXX      XXXX  XXXXX",
"XXX   X   XXXXXXX   XXXXXXX    XXXXXXXX      X     XXXXX",
"XXX  X   XXXXXXXXXX        XXXXXXXXXXXXXXXX    X G XXXXX",
"XXX     XXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXX XXXX   XXXXX",
"XXX  XXXXXXXXXXXXXXX        G      XXXXXXXX XXX    XXXXX",
"X     XX     G        X    XXXXXX   XXXXXXX XX  XXXXXXXX",
"XX X     XXX   XXX  XXX  XXXXXX     XXXXXXX XXX      XXX",
"XX    XX   XXXXXXXXXX   XXXXXXXXX      XXX  XXXXX    XXX",
"XX   XXX    XXX XXXX   XXXX       XXXXXX   XX          X",
"X  G XXX              XXXXX      XXXXXXX XX            X",
"X XX    XXXXX    XXXXXX     G        XXX XXX  XXXXXXXXXX",
"X XX  XXXXXX      XXX    XXXXX     XXXXX XXXX  XXXXXXXXX",
"X     XXXXX    XXXXXX G     XXXXX  XXXXX XX  G     XXXXX",
"XX  XXXXXXX    XXXX      XXXXXXXXX  XXXXXX     XXXXXXXXX",
"XX  XXXXX    XXXXXXXX   XXXXXXXXX  XXXXXXXX    XXXXX XXX",
"XX  XX    XXXXXXXXX    XXXXXXXXX  XXXXXXXXXX         XXX",
"XX    X   XXXXX     G    XXXXXXXXX  XXXXXXX    XXXXXX XX",
"XX  XX   XXXXX    XX    XXXXXX     G     XXX   XXXX   XX",
"XX  XXX   XXX   XXX    XXXXXX    XXXXX   XX  XXXXXX   XX",
"XX   XXX  XXXX   XXX        XX  XXXXXX      XXXXXXXXX  X",
"X   XXXX   XXX  XXXXX  G XXXX   XXXXXX    XXXXXXXXXX  XX",
"X    X XXXXX   XXXX   XXXX          XXXX    XXXXXXX  XXX",
"X         G    XXX             XXXXXXXXXXX            XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

levels.append(level_1)

walls = []
ghost_loc = []

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

def setup_maze(level):
    global walls,ghost_loc
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = 10 + (x*15)
            screen_y = 10 + (y*15)
            if character == "X":
                walls.append((screen_x,screen_y))
                draw.dot(14,0.5,0.3,0.1,screen_x,screen_y)
            if character == "G":
                ghost_loc.append((screen_x,screen_y))

class Player():
    def playerk(self,x,y):
        global koorx,koory
        self.koorx = koorx = x
        self.koory = koory = y
        draw.dot(14,1.0,1.9,0.0,koorx-1+left+right,koory+up+down)
        draw.dot(4,0.0,0.0,0.0,koorx-5+left+right,koory+4+up+down)
        draw.dot(4,0.0,0.0,0.0,koorx+3+left+right,koory+4+up+down)

        
        
        draw.dot(7,0.0,0.0,0.0,koorx-1+left+right,koory-3+up+down)
        draw.dot(7,0.0,0.0,0.0,koorx+left+right,koory-3+up+down)
        draw.dot(7,0.0,0.0,0.0,koorx+1+left+right,koory-3+up+down)
        draw.dot(7,0.0,0.0,0.0,koorx+2+left+right,koory-3+up+down)
        draw.dot(6,0.0,0.0,0.0,koorx+7+left+right,koory-3+up+down)
        draw.dot(6,0.0,0.0,0.0,koorx+13+left+right,koory-3+up+down)
        draw.dot(8,1.5,0.0,0.0,koorx+16+left+right,koory+2+up+down)
        draw.dot(8,1.5,0.0,0.0,koorx+16+left+right,koory-3+up+down)
        draw.dot(5,0.0,0.0,0.0,koorx+16+left+right,koory-3+up+down)
        draw.dot(5,0.0,0.0,0.0,koorx+19+left+right,koory-3+up+down)


       
        
       
        # draw.dot(7,0.0,0.0,0.0,koorx+42+left+right,koory+29+up+down)
        # draw.dot(7,0.0,0.0,0.0,koorx+57+left+right,koory+29+up+down)


    def player_movement(key,x,y):
        global up, down, left, right, koorxg, kooryg, p_mati
        p_mati == False
        if (koorx+left+right, koory+up+down+15) not in walls:
            if key == GLUT_KEY_UP:
                up += 15
                # print(koorx+left+right, koory+up+down)
        if (koorx+left+right, koory+up+down-15) not in walls:
            if key == GLUT_KEY_DOWN:
                down -= 15
                # print(koorx+left+right, koory+up+down)
        if (koorx+left+right+15, koory+up+down) not in walls:
            if key == GLUT_KEY_RIGHT:
                right += 15
                # print(koorx+left+right, koory+up+down)
        if (koorx+left+right-15, koory+up+down) not in walls:
            if key == GLUT_KEY_LEFT:
                left -= 15
                # print(koorx+left+right, koory+up+down)

        ### collision with ghost ###
        if (koorx+left+right, koory+up+down) == ((koorxg+leftg+rightg, kooryg+upg+downg)):
            print("Player dead")

class Ghost():
    def ghost(self):
        global upg,downg,leftg,rightg, koorxg, kooryg, ghost_loc, p_mati
        self.koorxg = koorxg 
        self.kooryg = kooryg 
        for (koorxg,kooryg) in ghost_loc:
        
        #     draw.dot(14,0,0,0.6,koorxg+leftg+rightg, kooryg+upg+downg)
        # # draw.dot(14,0,0,0.6,koorxg+leftg+rightg, kooryg+upg+downg)
            draw.dot(14,1.0,1.5,0.9,koorxg-1+leftg+rightg,kooryg+upg+downg)
            draw.dot(4,0.0,0.0,0.0,koorxg-5+leftg+rightg,kooryg+4+upg+downg)
            draw.dot(4,0.0,0.0,0.0,koorxg+3+leftg+rightg,kooryg+4+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg-5+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg-4+leftg+rightg,kooryg-3+upg+downg)

            draw.dot(7,0.0,0.0,0.0,koorxg-3+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg-2+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg-1+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg+1+leftg+rightg,kooryg-3+upg+downg)
            draw.dot(7,0.0,0.0,0.0,koorxg+2+leftg+rightg,kooryg-3+upg+downg)

    def g_dir(self):
        global change_dir, dirg
        self.change_dir = True
        self.dirg = dirg = choice(["up","down","right","left"])
        print(dirg)
        p_mati == False
        if (koorxg+leftg+rightg, kooryg+upg+downg) != (koorx+left+(right+15), koory+up+down):
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
                
            else:
            # elif(koorxg+leftg+rightg, kooryg+upg+downg) == (koorx+left+(right+15), koory+up+down):
                print("Player dead")

    def go_up(self,value):
        global upg
        self.upg = upg
        print(koorxg+leftg+rightg, kooryg+upg+downg+15)
        self.g_dir == True
        if (koorxg+leftg+rightg, kooryg+upg+downg+15) not in walls:
            upg += 15
            glutTimerFunc(550,self.go_up,0)
        else:
            self.g_dir == True
            self.g_dir()
            print("change")

    def go_down(self,value):
        global downg
        self.downg = downg
        print(koorxg+leftg+rightg, kooryg+upg+downg-15)
        self.g_dir == True
        if (koorxg+leftg+rightg, kooryg+upg+downg-15) not in walls:
            downg -= 15
            glutTimerFunc(550,self.go_down,0)
        else:
            self.g_dir == True
            self.g_dir()
            print("change")

    def go_left(self,value):
        global leftg
        self.leftg = leftg
        print(koorxg+leftg+rightg-15, kooryg+upg+downg)
        self.g_dir == True
        if (koorxg+leftg+rightg-15, kooryg+upg+downg) not in walls:
            leftg -= 15
            glutTimerFunc(550,self.go_left,0)
        else:
            self.g_dir == True
            self.g_dir()
            print("change")

    def go_right(self,value):
        global rightg
        self.rightg = rightg
        print(koorxg+leftg+rightg+15, kooryg+upg+downg)
        self.g_dir == True
        if (koorxg+leftg+rightg+15, kooryg+upg+downg) not in walls:
            rightg += 15
            glutTimerFunc(550,self.go_right,0)
        else:
            self.g_dir == True
            self.g_dir()
            print("change")


class ExitKey():
    def exitkey(self,x,y):
        global keylocx,keylocy,ambil_kunci
        self.keylocx = keylocx = x
        self.keylocy = keylocy = y
        draw.dot(10,255,0,255,keylocx,keylocy)
        draw.dot(4,0,0,0,keylocx,keylocy)
        draw.dot(6,255,0,255,keylocx+8,keylocy)
        draw.dot(6,255,0,255,keylocx+14,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy-3)
        if (keylocx,keylocy) == (koorx+(left-15)+(right+15), koory+(up+15)+(down-15)):
            ambil_kunci = True
            keylocx += 350
            keylocy += 80
            print(ambil_kunci,"kunci telah diambil")

    def text_kunci(xpos, ypos,text):
        glRasterPos2i(xpos,ypos)
        for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))

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
    glColor3f(255, 255, 255)
    ExitKey.text_kunci(850,350,"kunci")
    setup_maze(levels[1])
    player.playerk(25,25)
    exitkey.exitkey(keylocx,keylocy)
    # setup_maze(levels[1])
    ghosts.ghost()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("ini maze")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(Player.player_movement)
# ghosts.g_dir()
glutMainLoop()
