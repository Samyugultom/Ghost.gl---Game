from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class dinding():
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