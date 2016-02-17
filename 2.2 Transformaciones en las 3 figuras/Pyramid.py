# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

vertex = (0.15, 0.3, 0.0)
increase = 0
def InitGL():
    """ This function initialize the font color and the matrix mode."""
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_MODELVIEW)


# --------------------------------------------------------------

def showPyramid():
    """ This function draws a pyramid with 4 triangles and his base."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    # Triangle 1
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    # Triangle 2
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] + 0.25)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    # Triangle 3
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.25, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    glVertex3f(vertex[0] - 0.25, vertex[1] - 0.25, vertex[2] - 0.25)
    # Triangle 4
    glColor3f(1.0, 1.0, 1.0)
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
    glutSwapBuffers()


# --------------------------------------------------------------
def keyPressed(*args):
    """ This function prints two matrices, according to the pressed keys. """
    key = args[0]
    global vertex, increase
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
        if 0<= increase <=9:
            glTranslatef(vertex[0], vertex[1], vertex[2])
            glRotatef(30, 0, 0, 1)
            glTranslatef(-vertex[0], -vertex[1], -vertex[2])
            increase +=1
            if increase == 9:
                increase =-9
        else:
            glTranslatef(vertex[0], vertex[1], vertex[2])
            glRotatef(-30, 0, 0, 1)
            glTranslatef(-vertex[0], -vertex[1], -vertex[2])
            increase +=1


def mouseClicked(*args):
    """ This function rotate de object 30° in the vector 1,1,0"""
    key = args[0];
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
