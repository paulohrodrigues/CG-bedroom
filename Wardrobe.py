
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Wardrobe:
    def __init__(self, scale, positions):
        self.side    = 1.5
        self.scale   = scale
        self.halfPos = +self.side/2
        self.halfNeg = -self.side/2

        self.x = positions['x']
        self.y = positions['y']
        self.z = positions['z']

    def shape(self):

        for i in range(3):
            glColor3f(1.0, 0.4, 0.0)
            glPushMatrix()
            glScale(self.scale, self.scale, self.scale)
            glTranslate(self.x, self.y + i * self.side, self.z)
            glutSolidCube(self.side)
            glPopMatrix()

    def border(self):
        glColor3f(.0, .0, .0)
        glScale(self.scale, self.scale, self.scale)        
        glBegin(GL_LINE_LOOP)
        glVertex3f(self.halfNeg + self.x             , self.halfNeg + self.y     , self.halfPos + self.z)
        glVertex3f(self.halfNeg + self.x             , self.halfPos * 5 + self.y , self.halfPos + self.z)
        glVertex3f(self.halfNeg + self.x + self.side , self.halfPos * 5 + self.y , self.halfPos + self.z)
        glVertex3f(self.halfNeg + self.x + self.side , self.halfNeg + self.y     , self.halfPos + self.z)
        glEnd()
        glFlush()

    def door(self):
        glColor3f(.0, .0, .0)
        glBegin(GL_LINES)
        glVertex3f(self.x, self.halfNeg + self.y, self.halfPos + self.z + 0.01)
        glVertex3f(self.x, self.halfPos * 5 + self.y, self.halfPos + self.z + 0.01)
        glEnd()
        glFlush()

    def puller(self, diff):
        
        glPushMatrix()
        glColor3f(1.0, 0.3, 0.0)
        glTranslate(self.x - diff, self.halfPos * 0.5, self.halfPos + self.z + 0.1)
        glutSolidSphere(0.09, 20, 15)
        glPopMatrix()

    def foot(self, posX, posY, posZ):
        
        glPushMatrix()
        glColor3f(1.0, 0.3, 0.0)
        glTranslate(self.halfNeg + self.x + posX, self.halfNeg + self.y - posY, self.halfPos + self.z - posZ)
        glRotatef(-90, 1, 0, 0)
        glutSolidCylinder(0.06, 0.18, 15, 10)
        glPopMatrix()

    def draw(self):
        self.shape()
        self.border()
        self.door()
        self.puller(+0.1)
        self.puller(-0.1)

        self.foot(.07, .18, .1)
        self.foot(self.side - 0.07, .18, 0.1)
        self.foot(.07, .18, self.side - 0.1)
        self.foot(self.side - 0.07, .18, self.side - 0.1)
