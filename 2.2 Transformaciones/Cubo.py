from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *


# Se asigno a la letra M la sentencia asociada a mostrar la matriz de modelado y de proyeccion
# Se asigno a la letra C la sentencia asociada a variar el movimiento de la camara

# Para el manejo de las proyecciones, manejamos unos arreglos con los valores que reciben las funciones, ya que
# son las mismas entradas, pero para cada proyeccion tenemos unos valores correspondientes. En caso de utilizar
# una proyeccion especifica, se debe antes de ejecutar el archivo, verificar que los arreglos de valores sean
# los correspondientes a esa proyeccion. Al igual que se debe verificar la funcion glOrtho (Paralela) o
# glFrustum (Perspectiva)

def main():
    global window, left, right, btm, top, near, far, i, eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ, j

    # Estos valores son para la proyeccion paralela, por favor quitar "#" cuando se vaya a utilizar esta proyeccion.
    # En caso de utilizar la proyeccion perspectiva, por favor ponerle "#" en caso de no tenerlo.

    left = array([-1, 3, -5])
    right = array([1, -3, 5])
    btm = array([-1, 4, 1])
    top = array([1, -4, -1])
    near = array([1, 2, -3])
    far = array([-2, -4, 6])

    # Estos valores son para la proyeccion perspectiva, por favor quitar "#" cuando se vaya a utilizar esta proyeccion.
    # En caso de utilizar la proyeccion paralela, por favor ponerle "#" en caso de no tenerlo.

    # left = array ([-1, 3, -5])
    # right = array ([1, -3, 5])
    # btm = array ([-1, 4, 1])
    # top = array ([1, -4, -1])
    # near = array ([0.25, 0.6, 0.15])
    # far = array ([0.35, 0.2, 0.4])


    # Este iterador lo cambiamos para variar la proyeccion paralela o perspectiva, los valores estan entre 0 y 2.
    # Hay que hacerlo manualmente ya que la proyeccion se inicializa al crear la ventana :)
    i = 2

    eyeX = array([0, 0, 0])
    eyeY = array([0, 0, 0])
    eyeZ = array([0, 0, 0])
    centerX = array([1, 3, 5])
    centerY = array([1, 2, 2])
    centerZ = array([1, 10, -1])
    upX = array([1, 3, 2])
    upY = array([1, 3, 3])
    upZ = array([0, 1, 4])
    j = 0

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    window = glutCreateWindow('Taller 3 - Cubo 3D')

    InitGL(500, 500)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(mostrarEscena)
    glutIdleFunc(mostrarEscena)
    glutKeyboardFunc(keyPressed)
    glutMainLoop()


def InitGL(Width, Height):
    glClearColor(0.53, 0.53, 0.53, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(left[i],right[i],btm[i],top[i],near[i],far[i])
    #glFrustum(left[i]/5, right[i]/5, btm[i], top[i], near[i]/5, far[i]/5)


def mostrarEscena():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    gluLookAt(0.0, 0.0, 5.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0)
    #gluLookAt(eyeX[j], eyeY[j], eyeZ[j], centerX[j], centerY[j], centerZ[j], upX[j], upY[j], upZ[j]);

    # LADO DELANTERO
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 0);
    glVertex3f(0.25, -0.25, 0.25);
    glVertex3f(0.25, 0.25, 0.25);
    glVertex3f(-0.25, 0.25, 0.25);
    glVertex3f(-0.25, -0.25, 0.25);
    glEnd();

    # LADO TRASERO
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 1);
    glVertex3f(0.25, -0.25, -0.25);
    glVertex3f(0.25, 0.25, -0.25);
    glVertex3f(-0.25, 0.25, -0.25);
    glVertex3f(-0.25, -0.25, -0.25);
    glEnd();

    # LADO DERECHO
    glBegin(GL_POLYGON);
    glColor3f(0, 1, 0);
    glVertex3f(0.25, -0.25, 0.25);
    glVertex3f(0.25, 0.25, 0.25);
    glVertex3f(0.25, 0.25, -0.25);
    glVertex3f(0.25, -0.25, -0.25);
    glEnd();

    # LADO IZQUIERDO:
    glBegin(GL_POLYGON);
    glColor3f(1, 0, 0);
    glVertex3f(-0.25, -0.25, 0.25);
    glVertex3f(-0.25, 0.25, 0.25);
    glVertex3f(-0.25, 0.25, -0.25);
    glVertex3f(-0.25, -0.25, -0.25);
    glEnd();

    # LADO SUPERIOR:
    glBegin(GL_POLYGON);
    glColor3f(0, 1, 1);
    glVertex3f(0.25, 0.25, 0.25);
    glVertex3f(0.25, 0.25, -0.25);
    glVertex3f(-0.25, 0.25, -0.25);
    glVertex3f(-0.25, 0.25, 0.25);
    glEnd();

    # LADO INFERIOR:
    glBegin(GL_POLYGON);
    glColor3f(1, 0, 1);
    glVertex3f(0.25, -0.25, 0.25);
    glVertex3f(0.25, -0.25, -0.25);
    glVertex3f(-0.25, -0.25, -0.25);
    glVertex3f(-0.25, -0.25, 0.25);
    glEnd();

    glFlush()
    glutSwapBuffers();


def keyPressed(*args):
    global j

    key = args[0];

    if (key == "m" or key == "M"):
        print("La matriz de proyeccion es: \n %s" % glGetFloatv(GL_PROJECTION_MATRIX))
        print("La matriz de modelado es: \n %s" % glGetFloatv(GL_MODELVIEW_MATRIX))

    elif (key == "c" or key == "C"):
        if (j >= 2):
            j = 0
        else:
            j = j + 1

    glutPostRedisplay();


if __name__ == "__main__":
    main()
