##########################
import sys
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
### 23 Column 40 rows ###
levels = [""]
### MAZE ###
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XX                   XXXXXXXXXXXX                XXXXXXX",
"XX XXXXXX XXXXXXXXX     XXXXXXXXXXXXXXXXXXX    XXXXXXXXX",
"XX XXX   X XXXXXXX                             XXXXXXXXX",
"XX XXXX X XXXX    XXX  XXXXX      XXXXX             XXXX",
"XX       XXX   XXXXX   XXXXXXX      XXXX  XXXXXXXX  XXXX",
"XX  XXX X  XXX  XXXXXX   XXXXXXXXX     XX           XXXX",
"XX  XXX XXXX  XXXXX       XXXXXXX       XXXXXXXX   XXXXX",
"XXX  XXX XXX  XXXXXX   XXXXXXXX   XXX    XXXXXXXXX  XXXX",
"XX  XX         XXXX   XXXXXXXXX   XXXXX      XXXX  XXXXX",
"XXX   X   XXXXXXX   XXXXXXX    XXXXXXXX      X     XXXXX",
"XXX  X   XXXXXXXXXX        XXXXXXXXXXXXXXXX    X   XXXXX",
"XXX     XXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXX",
"XXX  XXXXXXXXXXXXXXX               XXXXXXXXXXXX    XXXXX",
"X     XX              X    XXXXXX   XXXXXXX  X  XXXXXXXX",
"XX X     XXX   XXX   XX  XXXXXX     XXXX    XXX      XXX",
"XX    XX   XXXXX  XXX   XXXXXXXXX      XXXXXXXXXX    XXX",
"XX   XXX    XXX XXXX   XXXX       XXXXXXXXXXX         ZZ",
"X    XXX              XXXXX      XXXXXXXXXX           ZZ",
"X XX    XXXXX    XXXXXX              XXXXXXX  XXXXXXXXXX",
"X XX  XXXXXX      XXX    XXXXX     XXXXXXXXXX  XXXXXXXXX",
"X     XXXXX    XXXXXX       XXXXX  XXXXXXXX        XXXXX",
"XX  X  XXXX    XXXX      XXXXXXXXX  XXXXX      XXXXXXXXX",
"XX  X XXX    XXXXXXXX   XXXXXXXXX  XXXXXXXX    XXXXX XXX",
"XX  XX    XXXXXXXXX    XXXXXXXXX  XXXXXXXXXX         XXX",
"XX    X   XXXXX          XXXXXXXXX  XXXXXXX    XXXXXX XX",
"XX  XX   XXXXX    XX    XXXXXX           XXX   XXXX   XX",
"XX  XXX   XXX   XXX    XXXXXX    XXXXX   XX  XXXXXX   XX",
"XX   XXX  XXXX   XXX        XX  XXXXXX      XXXXXXXXX  X",
"XX   XXX   XXX  XXXXX    XXXX   XXXXXX    XXXXXXXXXX  XX",
"XX     XXXXX   XXXX   XXXX          XXXX    XXXXXXX  XXX",
"XX             XXX             XXXXXXXXXXX            XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
3
levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = 10 + (x*14)
            screen_y = 10 + (y*14)
            if character == "X":
                glPointSize(14)
                glBegin(GL_POINTS)
                glColor3ub(0,0,150)
                glVertex2f(screen_x, screen_y)
                glEnd()
            elif character == "Z":
                glPointSize(14)
                glBegin(GL_POINTS)
                glColor3f(1.0, 0.0, 3.0)
                glVertex2f(screen_x, screen_y)
                glEnd()              


def iterate():
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()

def rasiocanvas(): # membuat fungsi untuk kanvasnya
    glClearColor(0.0,1.0,0.0,1.0) # menampilkan warna dasar kanvas dengan RGBa
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode (GL_MODELVIEW)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rasiocanvas()
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 3.0)
    setup_maze(levels[1])
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("Maze2")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()