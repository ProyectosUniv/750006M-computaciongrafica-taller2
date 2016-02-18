# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

vertex = (-0.2, 0.3, 0.0)
showReflection = False
triangle1Color = (0.55, 0.9, 0.9)  # Scarlet
triangle2Color = (0.556863, 0.137255, 0.137255)  # Firebrick
triangle3Color = (1.0, 1.0, 1.0)  # White
triangle4Color = (0.90, 0.91, 0.98)  # Silver
triangle5Color = (0.0, 0.0, 0.0)  # Black
rectangularBaseColor = (0.53, 0.12, 0.47)  # Dark Purple
forward = 0
increase = 0
depth = 0.4
height = 0.3
side = 0.5


def InitGL():
    """ This function initialize the font color and the matrix mode."""
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_MODELVIEW)

# --------------------------------------------------------------

def showPrism():
    """ This function draws a rectangular prism."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawFigure()
    #  If we need to draw the reflection we do it with the reflection matrix.
    if showReflection:
        glPushMatrix()
        glScalef(-1.0, -1.0, 1.0)
        drawFigure()
        glPopMatrix()
    glutSwapBuffers()


# --------------------------------------------------------------

def drawFigure():
    # Right side
    glBegin(GL_POLYGON)
    glColor3f(triangle1Color[0], triangle1Color[1], triangle1Color[2])
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glEnd()
    # Back face
    glBegin(GL_POLYGON)
    glColor3f(triangle2Color[0], triangle2Color[1], triangle2Color[2])
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glEnd()
    # Superior face
    glBegin(GL_POLYGON)
    glColor3f(triangle3Color[0], triangle3Color[1], triangle3Color[2])
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glEnd()
    # Left side
    glBegin(GL_POLYGON)
    glColor3f(triangle4Color[0], triangle4Color[1], triangle4Color[2])
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glEnd()
    # Front face
    glBegin(GL_POLYGON)
    glColor3f(triangle5Color[0], triangle5Color[1], triangle5Color[2])
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] + (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glEnd()
    # Base
    glBegin(GL_POLYGON)
    glColor3f(rectangularBaseColor[0], rectangularBaseColor[1], rectangularBaseColor[2])
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glVertex3f(vertex[0] + (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] - (depth / 2))
    glVertex3f(vertex[0] - (side / 2), vertex[1] - (height / 2), vertex[2] + (depth / 2))
    glEnd()


# --------------------------------------------------------------

def keyPressed(*args):
    """ This function prints two matrices, according to the pressed keys. """
    key = args[0]
    global vertex, increase, forward, triangle1Color, triangle2Color, triangle3Color, triangle4Color, triangle5Color, showReflection
    global rectangularBaseColor
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
    # First transformation 2.2.1 (Rotate)
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
                    triangle5Color = [0.0, 0.0, 0.0]
                    rectangularBaseColor = [0.0, 1.0, 1.0]
    if key == "s" or key == "S":
        glScalef(0.3, 1.0, 1.1)
    if key == "f" or key == "F":
        showReflection = True


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
    window = glutCreateWindow("Prism")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(showPrism)
    glutIdleFunc(showPrism)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)
    InitGL()
    glutMainLoop()


if __name__ == "__main__":
    main()
