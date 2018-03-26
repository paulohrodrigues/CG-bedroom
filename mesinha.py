from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import *  


class Mesinha:
    def draw(self,scale,positions):
        glTranslate(positions['x'],positions['y'],positions['z'])
        self.__mesa()
        self.__banco()
        self.__notebook()



    def __mesa(self):
        # Tabuas superior 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(40, 1, 20) 
        glutSolidCube(0.1)
        glPopMatrix()

        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1,20, 20) 
        glTranslate(-1.9,-0.05,0)
        glutSolidCube(0.1)
        glPopMatrix()


        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1,20, 20) 
        glTranslate(1.9,-0.05,0)
        glutSolidCube(0.1)
        glPopMatrix()

    def __banco(self):
        # assento 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(10, 1, 10) 
        glTranslate(0,-0.5,0.2)
        glutSolidCube(0.1)
        glPopMatrix()

        # perna 1 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1, 15, 1)
        glTranslate(0.5,-0.08,1.5) 
        glutSolidCube(0.1)
        glPopMatrix()

        # perna 2 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1, 15, 1)
        glTranslate(-0.5,-0.08,1.5)
        glutSolidCube(0.1)
        glPopMatrix()

        # perna 3 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1, 15, 1)
        glTranslate(0.5,-0.08,2.5) 
        glutSolidCube(0.1)
        glPopMatrix()

        # perna 4
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1, 15, 1)
        glTranslate(-0.5,-0.08,2.5)
        glutSolidCube(0.1)
        glPopMatrix()


    def __notebook(self):

        #base
        glColor3f(.0, 0.0, 0.0)
        glPushMatrix() 
        glScalef(15, 1, 11)
        glTranslate(0,0.1,0)
        glutSolidCube(0.1)
        glPopMatrix()

        #tela
        glColor3f(.0, 0.0, 0.0)
        glPushMatrix() 
        glScalef(15, 11, 1)
        glTranslate(0,0.05,-0.5)
        glutSolidCube(0.1)
        glPopMatrix()

        #teclado
        glColor3f(.1, 0.1, 0.1)
        glPushMatrix() 
        glScalef(12, 1, 7)
        glTranslate(0,0.11,0)
        glutSolidCube(0.1)
        glPopMatrix()

        #visor
        glColor3f(.3, 0.3, 0.3)
        glPushMatrix() 
        glScalef(12, 10, 1)
        glTranslate(0,0.05,-0.49)
        glutSolidCube(0.1)
        glPopMatrix()