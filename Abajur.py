from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Abajur:
    def draw(self,scale,positions):
        '''Cylinder of Abajur'''
        glColor3f(1.0, 0.4, 0.0)
        glPushMatrix()
        glRotatef(-90, 0.1, 0.0, 0.0)
        glTranslate(positions["x"],positions["y"],(scale*-0.8)+positions["z"])
        glScale( scale, scale, scale)
        glutSolidCylinder(0.1, 0.8, 20, 20)
        glPopMatrix()

        '''Top of Abajur'''
        glPushMatrix()
        glRotatef(-90, 1.0, 0.0, 0.0)
        glTranslate(0,0,(scale*-0.01))
        glTranslate(positions["x"],positions["y"],positions["z"])
        glScale( scale, scale, scale)
        cont = 1
        while (cont <= 30):
            cont += 1
            glutSolidTorus(0.06,0.5,50,50)
            glTranslate( 0.0, 0.0, 0.02)
            glScale( 0.99, 0.99, 1)
        glPopMatrix()

        '''Bottom of Abajur'''
        glPushMatrix()
        glRotatef(-90, 1.0, 0.0, 0.0)
        glTranslate(positions["x"], positions["y"], -0.8*(scale)+positions["z"])
        glScale( scale, scale, scale)
        cont = 1
        while (cont <= 30):
            cont += 1
            glutSolidTorus(0.06,0.5,50,50)
            glTranslate( 0.0, 0.0, 0.01)
            glScale( 0.93, 0.93, 1)
        glPopMatrix()