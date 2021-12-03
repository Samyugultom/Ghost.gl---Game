import sys
from random import randrange
from Dinding import dinding
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''
ERROR: PyOpenGL not installed properly.
        ''')
  sys.exit()

w,h= 1000,500

Ghost_meter = 0
baterai = 0

up = 0
down = 0
left = 0
right = 0

vertg = 0
horig = 0

def ghost(kibxg,kibyg,kiaxg,kiayg,kaaxg,kaayg,kabxg,kabyg):
    global horig, vertg
    glBegin(GL_QUADS)
    glColor4f(200,0,100,Ghost_meter)
    glVertex2f(kibxg+horig,kibyg+vertg)
    glVertex2f(kiaxg+horig,kiayg+vertg)
    glVertex2f(kaaxg+horig,kaayg+vertg)
    glVertex2f(kabxg+horig,kabyg+vertg)
    glEnd()

def player(kibx,kiby,kiax,kiay,kaax,kaay,kabx,kaby):
    glBegin(GL_QUADS)
    glColor3ub(0,100,0)
    glVertex2f(kibx+left+right,kiby+up+down)
    glVertex2f(kiax+left+right,kiay+up+down)
    glVertex2f(kaax+left+right,kaay+up+down)
    glVertex2f(kabx+left+right,kaby+up+down)
    glEnd()

def Player_movement(key, x, y):
    global up,down,left,right,Ghost_meter
    if key == GLUT_KEY_UP:
        up += 10
    if key == GLUT_KEY_DOWN:
        down -= 10
    if key == GLUT_KEY_LEFT:
        left -= 10
    if key == GLUT_KEY_RIGHT:
        right += 10
    
    if Ghost_meter == 0:
        if key == GLUT_KEY_END:
            Ghost_meter += 1

    elif Ghost_meter == 1:
        if key == GLUT_KEY_END:
            Ghost_meter -= 1
        

### Pengurangan baterai belum selesai ###
def minbaterai(value):
    global baterai
    baterai -= 10
    glutTimerFunc(1000,minbaterai,0)

def gbr_baterai():
### BATERAI ###
    glBegin(GL_QUADS)
    glColor3f(100,100,0)

    glVertex2f(45,525)
    glVertex2f(45,545)
    glVertex2f(135-baterai,545)
    glVertex2f(135-baterai,525)

    glVertex2f(30,530)
    glVertex2f(30,540)
    glVertex2f(38,540)
    glVertex2f(38,530)
    
    glEnd()

    glBegin(GL_LINES)
    glColor3f(100,100,0)
    glVertex2f(40,520)
    glVertex2f(40,550)

    glVertex2f(40,550)
    glVertex2f(140,550)

    glVertex2f(140,550)
    glVertex2f(140,520)

    glVertex2f(140,520)
    glVertex2f(40,520)
    
    glEnd()

def Ghost_movement(value):
    global vertg, horig
    vertg = randrange(-10,10,10)
    horig = randrange(-10,10,10)
    glutTimerFunc(100,Ghost_movement,10)

def iterate():
    glViewport(0, 0, 1000, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    dinding.BgColor()
    dinding.Border()
    dinding.HoriSplit()
    dinding.VertSplit()
    gbr_baterai()
    player(10,10,10,30,30,30,30,10)
    ghost(200,200,200,230,230,230,230,200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 600)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Ghost.gl")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(Player_movement)
# Ghost_movement(0)
glutMainLoop()