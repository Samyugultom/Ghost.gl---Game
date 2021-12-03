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

### class instance ###
draw = Draw()

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
            #   glPointSize(15)
            #   glBegin(GL_POINTS)
            #   glColor3f(255,0,0)
            #   glVertex2f(screen_x, screen_y)
            #   glEnd()


class Player():
    def playerk(x,y):
        global koorx,koory
        koorx = x
        koory = y
        draw.dot(14,0,0,200,koorx+left+right,koory+up+down)
        # glPointSize(14)
        # glBegin(GL_POINTS)
        # glColor3f(0,0,200)
        # glVertex2f(koorx+left+right, koory+up+down)
        # glEnd()


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

    def is_colliding(other):
        a = koorx+left+right - keylocx
        b = koory+up+down - keylocy
        distance = math.sqrt((a**2)+(b**2))

        if distance < 5:
            return True
        else:
            return False

class ExitKey():
    def exitkey():
        global keylocx,keylocy
        draw.dot(14,255,255,255,keylocx,keylocy)
        # glPointSize(14)
        # glBegin(GL_POINTS)
        # glColor3f(255,255,255)
        # glVertex2f(keylocx,keylocy)
        # glEnd()

    def taken_by_player(keylocx,keylocy):

        keylocx += 500
        keylocy += 500


class Ghost():
  def ghost(xg,yg):
    koorxg = xg
    kooryg = yg
    draw.dot(14,0,255,255,koorxg+left+right, kooryg+up+down)
    # glPointSize(14)
    # glBegin(GL_POINTS)
    # glColor3f(0,255,255)
    # glVertex2f(koorxg+left+right, kooryg+up+down)
    # glEnd()

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
    Player.playerk(25,25)
    Ghost.ghost(400,400)
    ExitKey.exitkey()
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