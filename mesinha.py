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
        glScalef(3, 0.1, 2) 
        glutSolidCube(1.0)
        glPopMatrix()

        # pé  direito 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1.8, 2) 
        glTranslate(-14,-0.5,0)
        glutSolidCube(1.0)
        glPopMatrix()

        # pé  esquerdo 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1.8, 2) 
        glTranslate(14,-0.5,0)
        glutSolidCube(1.0)
        glPopMatrix()

    def __banco(self):
        # assento 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(1, 0.1, 1) 
        glTranslate(0,-8,2)
        glutSolidCube(1.0)
        glPopMatrix()

        # perna 1 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1, 0.1)
        glTranslate(4.8,-1.3,16) 
        glutSolidCube(1.0)
        glPopMatrix()

        # perna 2 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1, 0.1)
        glTranslate(-4.8,-1.3,16) 
        glutSolidCube(1.0)
        glPopMatrix()

        # perna 3 
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1, 0.1)
        glTranslate(4.8,-1.3,24) 
        glutSolidCube(1.0)
        glPopMatrix()

        # perna 4
        glColor3f(.6, 0.4, 0.3)
        glPushMatrix() 
        glScalef(0.1, 1, 0.1)
        glTranslate(-4.8,-1.3,24) 
        glutSolidCube(1.0)
        glPopMatrix()


    def __notebook(self):

        #base
        glColor3f(.0, 0.0, 0.0)
        glPushMatrix() 
        glScalef(1.5, 0.1, 1)
        glTranslate(0,1,0)
        glutSolidCube(1.0)
        glPopMatrix()

        #tela
        glColor3f(.0, 0.0, 0.0)
        glPushMatrix() 
        glScalef(1.5, 1, 0.1)
        glTranslate(0,0.6,-5)
        glutSolidCube(1.0)
        glPopMatrix()

        #teclado
        glColor3f(.1, 0.1, 0.1)
        glPushMatrix() 
        glScalef(1, 0.1, -0.5)
        glTranslate(0,1.1,0)
        glutSolidCube(1.0)
        glPopMatrix()

        #visor
        glColor3f(.3, 0.3, 0.3)
        glPushMatrix() 
        glScalef(1.3, 0.9, 0.1)
        glTranslate(0,0.6,-4.9)
        glutSolidCube(1.0)
        glPopMatrix()
