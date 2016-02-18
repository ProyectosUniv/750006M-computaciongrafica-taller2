# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

vertex = (0.0, 0.0, 0.0)
showReflection = False
increase = 0
forward = 0
rectangular1Color = [0.0, 0.0, 0.0]  # Color Black
rectangular2Color = [0.0, 1.0, 1.0]  # Color Scarlet
rectangular3Color = [0.847059, 0.847059, 0.74902]  # Color Wheat
triangle1Color = [1.0, 1.0, 1.0]  # Color White
triangle2Color = [0.30, 0.30, 1.0]  # Color Neon Blue


def InitGL():
    """ This function initialize the font color and the matrix mode."""
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_MODELVIEW)


# --------------------------------------------------------------
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)

def showIrregularPolygon3d():
    """ This function draws a figure with 2 triangles with different sides
    and 3 rectangular figures; also with 3 different sides."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.4, 0.0, 5.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0)
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
    # Triangle 1
    glBegin(GL_TRIANGLES)

    glColor3f(triangle1Color[0], triangle1Color[1], triangle1Color[2])  # White
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glEnd()
    # First Rectangular face right
    glBegin(GL_POLYGON)
    glColor3f(rectangular1Color[0], rectangular1Color[1], rectangular1Color[2])  # Black
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)
    glEnd()
    # Second Rectangular face down
    glBegin(GL_POLYGON)
    glColor3f(rectangular2Color[0], rectangular2Color[1], rectangular2Color[2])
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glEnd()
    # Triangle 2
    glBegin(GL_TRIANGLES)
    glColor3f(triangle2Color[0], triangle2Color[1], triangle2Color[2])
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glEnd()
    # Third Rectangular face left
    glBegin(GL_POLYGON)
    glColor3f(rectangular3Color[0], rectangular3Color[1], rectangular3Color[2])
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)

    glEnd()


#  --------------------------------------------------------------

def keyPressed(*args):
    """ This function prints two matrices, according to the pressed keys. """
    key = args[0]
    global vertex, increase, forward, rectangular1Color, rectangular2Color, rectangular3Color, triangle1Color, triangle2Color, showReflection
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
                    rectangular1Color = [1.0, 1.0, 1.0]
                    rectangular2Color = [1.0, 1.0, 1.0]
                    rectangular3Color = [0.0, 0.0, 0.0]
                    triangle1Color = [1.0, 1.0, 1.0]
                    triangle2Color = [0.0, 0.0, 0.0]
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
        glRotatef(10, 1, 1, 0)
        glTranslatef(-vertex[0], -vertex[1], -vertex[2])


def main():
    """ Main function that provides that initialize window's variables and execute the program."""
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow("Irregular polygon 3d")
    glEnable(GL_DEPTH_TEST)
    InitGL()
    glutDisplayFunc(showIrregularPolygon3d)
    glutReshapeFunc(reshape)
    glutIdleFunc(showIrregularPolygon3d)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)

    glutMainLoop()


if __name__ == "__main__":
    main()
