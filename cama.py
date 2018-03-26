from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Cama:
    def draw(self,scale,positions):
        glPushMatrix() 
        glRotatef(-90, 0.0, 1.0, 0.0)
        glTranslate(positions['x'],positions['y'],positions['z'])
        glScalef(scale,scale,scale)
        #base
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(2.1, 0.4, 1)
        glutSolidCube(1.0)
        glPopMatrix()

        #pes
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1.2, 1) 
        glTranslate(-10,0.1,0)
        glutSolidCube(1.0)
        glPopMatrix()
        
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 0.7, 1) 
        glTranslate(9.5,-.25,0)
        glutSolidCube(1.0)
        glPopMatrix()

        #Colchao
        glColor3f(1, 1, 1)
        glPushMatrix() 
        glScalef(1.88, 0.25 , 0.88)
        glTranslate(0,1,0) 
        glutSolidCube(1.0)
        glPopMatrix()

        #travesseiro
        glColor3f(0.69, 0.88, 0.9)
        glPushMatrix()
        glScalef(.88, 0.2, 1.2)
        glTranslate(-.88,2.2,0)
        glutSolidCube(0.5)
        glPopMatrix()
        glPopMatrix()