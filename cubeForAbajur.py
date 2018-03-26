from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class CubeForAbajur:
    def draw(self,scale,positions):
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix()
        glScale(1.3,2, 1.3)
        glTranslate(positions["x"], positions["y"], positions["z"])
        glutSolidCube(1)
        glPopMatrix()