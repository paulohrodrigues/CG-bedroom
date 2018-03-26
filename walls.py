from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import * 

class Walls:
    def draw(self,scale,positions):
        glColor3f(0.3, 0.3, 0.3)
        glPushMatrix()
        glScale(10,1, 10)
        glTranslate(0, -3, 0)
        glutSolidCube(1)
        glPopMatrix()

        glColor3f(0.7, 0.5, 0.2)
        glPushMatrix()
        glScale(1,10, 10)
        glTranslate(5, 0.2, 0)
        glutSolidCube(1)
        glPopMatrix()

        glColor3f(0.7, 0.5, 0.2)
        glPushMatrix()
        glScale(1,10, 10)
        glTranslate(-5, 0.2, 0)
        glutSolidCube(1)
        glPopMatrix()

        glColor3f(0.7, 0.5, 0.2)
        glPushMatrix()
        glScale(10,10, 1)
        glTranslate(0, 0.2, -5)
        glutSolidCube(1)
        glPopMatrix()