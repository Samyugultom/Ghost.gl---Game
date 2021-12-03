import sys
from random import randrange
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

up = 0
down = 0
left = 0
right = 0

vertg = 0
horig = 0

def BgColor():
    glBegin(GL_POLYGON)
    glColor3ub(0, 50, 100)
    glVertex2f(0, 0) #G
    glVertex2f(0, 500) #H
    glVertex2f(1000, 500) #
    glVertex2f(1000, 0) #F
    glEnd()

def Border():
    glLineWidth(10)
    glBegin(GL_LINES)
    glColor3ub(100, 0, 0)

    glVertex2f(0, 0) #G
    glVertex2f(0, 500) #H
    
    glVertex2f(0, 500) #H
    glVertex2f(1000, 500) #I

    glVertex2f(1000, 500) #H
    glVertex2f(1000, 0) #I

    glVertex2f(1000, 0) #H
    glVertex2f(0, 0) #I
    glEnd()

def VertSplit():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3ub(200, 0, 0)

    glVertex2f(0, 125) #G
    glVertex2f(1000, 125) #H
    
    glVertex2f(0, 250) #G
    glVertex2f(1000, 250) #H
    
    glVertex2f(0, 375) #G
    glVertex2f(1000, 375) #H
    glEnd()

def HoriSplit():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3ub(200, 0, 0)

    glVertex2f(125, 0) #G
    glVertex2f(125, 500) #H
    
    glVertex2f(250, 0) #G
    glVertex2f(250, 500) #H

    glVertex2f(375, 0) #G
    glVertex2f(375, 500) #H

    glVertex2f(500, 0) #G
    glVertex2f(500, 500) #H

    glVertex2f(625, 0) #G
    glVertex2f(625, 500) #H

    glVertex2f(750, 0) #G
    glVertex2f(750, 500) #H

    glVertex2f(875, 0) #G
    glVertex2f(875, 500) #H
    
    glEnd()

def ghost(kibxg,kibyg,kiaxg,kiayg,kaaxg,kaayg,kabxg,kabyg):
    global horig, vertg
    glBegin(GL_QUADS)
    glColor3ub(200,100,0)
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
    global up,down,left,right
    if key == GLUT_KEY_UP:
        up += 10
    if key == GLUT_KEY_DOWN:
        down -= 10
    if key == GLUT_KEY_LEFT:
        left -= 10
    if key == GLUT_KEY_RIGHT:
        right += 10

def Ghost_movement(value):
    global vertg, horig
    vertg = randrange(-10,10,10)
    horig = randrange(-10,10,10)
    glutTimerFunc(100,Ghost_movement,10)


def iterate():
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    BgColor()
    Border()
    HoriSplit()
    VertSplit()
    player(10,10,10,30,30,30,30,10)
    ghost(200,200,200,230,230,230,230,200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(100, 50)
wind = glutCreateWindow("Ghost.gl")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(Player_movement)
Ghost_movement(10)
glutMainLoop()
