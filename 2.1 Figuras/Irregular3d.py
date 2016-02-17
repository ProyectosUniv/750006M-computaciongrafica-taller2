# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

vertex = (0.0, 0.0, 0.0)


def InitGL():
    """ This function initialize the font color and the matrix mode."""
    glClearColor(0.53, 0.53, 0.53, 0)
    glMatrixMode(GL_MODELVIEW)


# --------------------------------------------------------------

def showPyramid():
    """ This function draws a figure with 2 triangles with different sides
    and 3 rectangular figures; also with 3 different sides."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Triangle 1
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)  # White
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glEnd()
    # First Rectangular face right
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)  # Black
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)
    glEnd()
    # Second Rectangular face down
    glBegin(GL_POLYGON)
    glColor3f(0.0,1.0,1.0) # Scarlet
    glVertex3f(vertex[0] + 0.5, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glEnd()
    # Triangle 2
    glBegin(GL_TRIANGLES)
    glColor3f(0.78, 0.1, 0.0)
    glVertex3f(vertex[0] + 0.6, vertex[1] - 0.2, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glEnd()
    # Third Rectangular face left
    glBegin(GL_POLYGON)
    glColor3f(0.847059,0.847059,0.74902)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.2, vertex[2] + 0.4)
    glVertex3f(vertex[0] - 0.2, vertex[1] - 0.1, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.4, vertex[2] + 0.0)
    glVertex3f(vertex[0] + 0.0, vertex[1] + 0.3, vertex[2] + 0.4)

    glEnd()
    glutSwapBuffers()




# --------------------------------------------------------------
def keyPressed(*args):
    """ This function prints two matrices, according to the pressed keys. """
    key = args[0]
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


def mouseClicked(*args):
    """ This function rotate de object 30° in the vector 1,1,0"""
    key = args[0];
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
    glutDisplayFunc(showPyramid)
    glutIdleFunc(showPyramid)
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(mouseClicked)
    InitGL()
    glutMainLoop()


if __name__ == "__main__":
    main()
