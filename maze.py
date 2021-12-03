##########################
import math
import sys
# from random import randrange

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

# keylocx = randrange(10,160,15)
# keylocy = randrange(10,160,15)
keylocx = 40
keylocy = 25
print(keylocy)
print(keylocx)

ambil_kunci = False
levels = [""]
left = 0
right = 0
up = 0
down = 0

### MAZE ###
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP        XXXXXXXXX                       XXXXXXXXXXXXX",
"X XX XXXX XXXXXXXXX                       XXXXXXXXXXXXX",
"X X     X XXXXXXXXX                       XXXXXXXXXXXXX",
"X XXXXX X XXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     X X XXXXXXXXX                       XXXXXXXXXXXXX",
"XX XX XXX XXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  X  XXXXXXXXXXXXX                     XXXXXXXXXXXXXXX",
"X                                         XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                             XXXXXXXXX",
"X     XXXXXXXXXXXXX                      XXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                           XXXXXXXXX",
"X     XXXXXXXXXXXXX                        XXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X                                         XXXXXXXXXXXXX",
"X                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXXXXXXXXXXX                       XXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
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


def setup_maze(level):
    global screen_x, screen_y, walls
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = 10 + (x*15)
            screen_y = 10 + (y*15)
            if character == "X":
              walls.append((screen_x,screen_y))
              draw.dot(15,255,0,0,screen_x,screen_y)

class Player():
    def playerk(self,x,y):
        global koorx,koory
        self.koorx = koorx = x
        self.koory = koory = y
        draw.dot(14,0,0,200,koorx+left+right,koory+up+down)

    def player_movement(key,x,y):
        global up, down, left, right
        # print(koorx+left+right, koory+up+down)
        if (koorx+left+right, koory+up+down+15) not in walls:
            if key == GLUT_KEY_UP:
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
        
        # if (koorx+(left-15)+(right+15), koory+(up+15)+(down-15)) == (keylocx,keylocy):
        #     exitkey.taken_by_player(keylocx,keylocy)
        #     print("kunci telah diambil")
            
        
        if (koorx+(left-15)+(right+15), koory+(up+15)+(down-15)) == (koorxg+(left-15)+(right+15), kooryg+(up+15)+(down-15)):
            print("kunci telah diambil")

    # def is_colliding_key(self,other):
    #     a = self.koorx - other[0]
    #     b = self.koory- other[1]
    #     distance = math.sqrt((a**2)+(b**2))
    #     if distance < 5:
    #         print("Taken")
    #         return True
    #     else:
    #         return False

# def check_col():
#     if player.is_colliding_key((keylocx,keylocy)):
#         (print("nice"))

class ExitKey():
    def exitkey(self,x,y):
        global keylocx,keylocy,ambil_kunci
        self.keylocx = keylocx = x
        self.keylocy = keylocy = y
        draw.dot(10,255,0,255,keylocx,keylocy)
        draw.dot(6,255,0,255,keylocx+8,keylocy)
        draw.dot(6,255,0,255,keylocx+14,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy)
        draw.dot(6,255,0,255,keylocx+20,keylocy-3)
        if (keylocx,keylocy) ==(koorx+(left-15)+(right+15), koory+(up+15)+(down-15)):
            ambil_kunci = True
            keylocx += 800
            keylocy += 300
            print(ambil_kunci,"kunci telah diambil")

    def taken_by_player(self,keylocx, keylocy):
        self.keylocx = keylocx + 500
        self.keylocy = keylocy + 500


class Ghost():
  def ghost(self,xg,yg):
    global koorxg,kooryg
    self.koorxg = koorxg = xg
    self.kooryg = kooryg = yg
    draw.dot(14,0,255,255,koorxg+left+right, kooryg+up+down)

### class instance ###
draw = Draw()
player = Player()
exitkey = ExitKey()
ghost1 = Ghost()

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
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    setup_maze(levels[1])
    player.playerk(25,25)
    ghost1.ghost(40,40)
    exitkey.exitkey(keylocx,keylocy)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("ini maze")
glutDisplayFunc(showScreen)
glutSpecialFunc(Player.player_movement)
glutIdleFunc(showScreen)
glutMainLoop()
