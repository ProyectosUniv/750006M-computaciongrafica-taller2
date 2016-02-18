# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

vertex = (0.15, 0.3, 0.0)
triangle1Color = (1.0, 0.0, 0.0)
triangle2Color = (0.0, 1.0, 0.0)
triangle3Color = (0.0, 0.0, 1.0)
triangle4Color = (1.0, 1.0, 1.0)
baseColor = (0.0, 0.0, 0.0)
forward = 0
showReflection = False
increase = 0
#  glulookAt data.
eyeX = -0.5
eyeY = 0.0
eyeZ = 0.0
centerX = 0.0
centerY = 0.5
centerZ = 0.0
upX = 0.5
upY = 0.3
upZ = 0.2
j = 0
#  Parallel projection data and frustum
left = -0.4
right = 0.4
btm = -0.1
top = 0.1
near = 0.5
far = -0.5

def InitGL():
    """ This function initialize the font color and the matrix mode."""
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# --------------------------------------------------------------

def showPyramid():
    """ This function draws a pyramid with 4 triangles and his base."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    createFigure()
    if showReflection:
        glPushMatrix()
        glScalef(-1.0, -1.0, 1.0)
        createFigure()
        glPopMatrix()
    glutSwapBuffers()


# --------------------------------------------------------------

def createFigure():
    glBegin(GL_TRIANGLES)
    # Triangle 1
    glColor3f(triangle1Color[0], triangle2Color[1], triangle3Color[2])
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    # Triangle 2
    glColor3f(triangle2Color[0], triangle2Color[1], triangle2Color[2])
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    # Triangle 3
    glColor3f(triangle3Color[0], triangle3Color[1], triangle3Color[2])
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    # Triangle 4
    glColor3f(triangle4Color[0], triangle4Color[1], triangle4Color[2])
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glEnd()
    # Base
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glEnd()


# --------------------------------------------------------------

def keyPressed(*args):
    """ This function prints two matrices, according to the pressed keys. """
    key = args[0]
    global vertex, increase, forward, showReflection, triangle1Color, triangle2Color, triangle3Color, triangle4Color, baseColor
    global centerY, eyeY, eyeX, centerX, left, right, btm, far
    if key == "v" or key == "V":
        matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        print "Model view matrix: ", matrix
        for row in matrix:
            print "{} {} {} {}".format(row[0], row[1], row[2], row[3])
    if key == "p" or key == "P":
        matrix = glGetFloatv(GL_PROJECTION_MATRIX)
        print "Projection matrix: ", matrix
        for row in matrix:
            print "{} {} {} {}".format(row[0], row[1], row[2], row[3])
    if key == "r" or key == "R":
        if 0 <= increase <= 9:
            glTranslatef(vertex[0], vertex[1], vertex[2])
            glRotatef(30, 0, 0, 1)
            glTranslatef(-vertex[0], -vertex[1], -vertex[2])
            increase += 1
            if increase == 9:
                increase = -9
        else:
            glTranslatef(vertex[0], vertex[1], vertex[2])
            glRotatef(-30, 0, 0, 1)
            glTranslatef(-vertex[0], -vertex[1], -vertex[2])
            increase += 1
    # Second transformation 2.2.2 (Translate)
    if key == "t" or key == "T":
        if 0 <= forward <= 2:
            glTranslate(0.1, 0.0, 0.0)
            forward += 1
            if forward == 3:
                forward = -8
        else:
            if -8 <= forward <= -2:
                glTranslate(0.0, 0.05, 0.0)
                forward += 1
            else:
                if forward == -1:
                    triangle1Color = [1.0, 1.0, 1.0]
                    triangle2Color = [1.0, 1.0, 1.0]
                    triangle3Color = [0.0, 0.0, 0.0]
                    triangle4Color = [1.0, 1.0, 1.0]
                    baseColor = [0.0, 0.0, 0.0]
    if key == "s" or key == "S":
        glScalef(0.3, 1.0, 1.1)
    if key == "f" or key == "F":
        showReflection = True
    # PROJECTIONS
    # glulookAt 2.3.1
    if key == "g" or key == "G":
        glScalef(0.2,0.2,0.2)
        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    if key == "a" or key == "A":
        glScalef(0.2,0.2,0.2)
        eyeY = 0.8
        centerY = -0.4
        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    if key == "u" or key == "U":
        glScalef(0.2,0.2,0.2)
        eyeX = 0.6
        centerX = 0.4
        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    # glOrtho 2.3.2
    if key == "h" or key == "H":
        glScalef(0.1,0.1,0.1)
        glOrtho(left, right, btm, top, near, far)
    if key == "i" or key == "I":
        glScalef(0.1,0.1,0.1)
        left = 0.9
        right = 0.2
        glOrtho(left, right, btm, top, near, far)
    if key == "e" or key == "E":
        glScalef(0.1,0.1,0.1)
        left = -0.9
        right = 0.8
        glOrtho(left, right, btm, top, near, far)
    # glFrustrum 2.3.3
    if key == "w" or key == "W":
        glScalef(0.1,0.1,0.1)
        left = 0.05
        right = 0.50
        far = 0.75
        glFrustum(left, right, btm, top, near, far)
    if key == "x" or key == "X":
        glScalef(0.1,0.1,0.1)
        left = 0.09
        right = 0.60
        far = 0.15
        glFrustum(left, right, btm, top, near, far)
    if key == "z" or key == "Z":
        glScalef(0.01,0.01,0.01)
        left = 0.02
        right = 0.8
        far = 0.25
        glFrustum(left, right, btm, top, near, far)
    # gluPerspective 2.3.4
    if key == "q" or key == "Q":
        glScalef(0.01,0.01,0.01)
        gluPerspective(30,(right/top),1, 10)


def mouseClicked(*args):
    """ This function rotate de object 30° in the vector 1,1,0"""
    key = args[0]
    global vertex
    if key == GLUT_LEFT_BUTTON:
        glTranslatef(vertex[0], vertex[1], vertex[2])
        glRotatef(30, 1, 1, 0)
        glTranslatef(-vertex[0], -vertex[1], -vertex[2])


def main():
    """ Main function that provides that initialize window's variables and execute the program."""
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow("Pyramid")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showPyramid)
    glutIdleFunc(showPyramid)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)
    InitGL()
    glutMainLoop()


if __name__ == "__main__":
    main()
