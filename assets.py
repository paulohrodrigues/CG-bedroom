from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Window:
	
	def draw(self,scale=1,pos={'x':0,'y':0,'z':0}):

		#==================================
		glPushMatrix()
		glScale(scale, scale, scale)
		glTranslate(pos['x'], pos['y'], pos['z'])
		#==================================

		glColor3f(.6, .6, 1)
		glPushMatrix()
		glRotatef(90, 1.0, 0.0, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f( .5, 0.0, -.5)
		glVertex3f( .5, 0.0,  .5)
		glVertex3f(-.5, 0.0,  .5)
		glVertex3f(-.5, 0.0, -.5)
		glEnd()
		glPopMatrix()

		#frame
		glColor3f(1, .5, .2)
		glPushMatrix()
		glTranslate(0.0, -0.5, 0.0)
		glScale(10, 1, 1)
		glutSolidCube(.1)
		glPopMatrix()
		#frame
		glPushMatrix()
		glTranslate(0.0, 0.5, 0.0)
		glScale(10, 1, 1)
		glutSolidCube(.1)
		glPopMatrix()
		#frame
		glPushMatrix()
		glScale(10, 1, 1)
		glutSolidCube(.1)
		glPopMatrix()
		#frame
		glPushMatrix()
		glScale(1, 10, 1)
		glutSolidCube(.1)
		glPopMatrix()
		#frame
		glPushMatrix()
		glTranslate(0.5, 0.0, 0.0)
		glScale(1, 10, 1)
		glutSolidCube(.1)
		glPopMatrix()
		#frame
		glPushMatrix()
		glTranslate(-0.5, 0.0, 0.0)
		glScale(1, 10, 1)
		glutSolidCube(.1)
		glPopMatrix()

		#============================
		glPopMatrix()
		#============================


class Flower:
	
	def draw(self,scale=1,pos={'x':0,'y':0,'z':0}):

		#==================================
		glPushMatrix()
		glScale(scale, scale, scale)
		glTranslate(pos['x'], pos['y'], pos['z'])
		#==================================

		# VASO ==================
		glColor3f(0.8, 0.4, 0.2)
		glPushMatrix()
		glTranslate( .1, 0, 0)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( -.1, 0, 0)
		glutSolidCube(.1)
		glPopMatrix()
    
		glPushMatrix()
		glTranslate( 0, 0, .1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( 0, 0, -.1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( .1, .1, 0)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( -.1, .1, 0)
		glutSolidCube(.1)
		glPopMatrix()
    
		glPushMatrix()
		glTranslate( 0, .1, .1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( 0, .1, -.1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( 0, .2, 0)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( 0, .2, -.1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( 0, .2, .1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( .1, .2, 0)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( -.1, .2, 0)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( -.1, .2, .1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( -.1, .2, -.1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( .1, .2, -.1)
		glutSolidCube(.1)
		glPopMatrix()

		glPushMatrix()
		glTranslate( .1, .2, .1)
		glutSolidCube(.1)
		glPopMatrix()
		# VASO ==================

		# CAULE ==================
		glColor3f(0.372, 0.827, 0.333)
		glPushMatrix()
		glTranslate( 0, .3, 0)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( 0, .4, 0)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( 0, .5, 0)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( 0, .6, 0)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( .1, .3, 0)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( -.1, .4, 0)
		glutSolidCube(.1)
		glPopMatrix()
		# caule ==================

		# petalas ==================
		glColor3f(1, 0.952, 0.258)
		glPushMatrix()
		glTranslate( 0, .5, .1)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( .1, .6, .1)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( -.1, .6, .1)
		glutSolidCube(.1)
		glPopMatrix()
		glPushMatrix()
		glTranslate( 0, .7, .1)
		glutSolidCube(.1)
		glPopMatrix()

		# meio ==================
		glColor3f(0.372, 0.290, 0.149)
		glPushMatrix()
		glTranslate( 0, .6, .1)
		glutSolidCube(.1)
		glPopMatrix()

		#============================
		glPopMatrix()
		#============================