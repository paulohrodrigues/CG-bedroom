from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Window:
	

	def draw(scale=1,pos={'x':0,'y':0,'z':0}):

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