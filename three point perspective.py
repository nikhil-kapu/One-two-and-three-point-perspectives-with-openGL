from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



#########         NIKHIL KAPU
########            
#########   kindly go through the comments.......






window = 0                                             # glut window number
width, height = 1350, 750                               # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

    # first thought of making a cube using rectangle but then didnt workout
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                            # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                    # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()       # done drawing a rectangle



###############################################                  MAIN FUNCTION          ################################################################
# the following function creates a cube like object for which we are going to show the vanishing points
def on_draw():
 
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0.5, 0.0, 1.0)
 
        
        glBegin(GL_LINES)

        # this draws the first vertical line

        glVertex2i(450, 550)
        glVertex2i(450, 400)
        

        glVertex2i(600, 450)              # 2nd verticle line i.e middle one
        glVertex2i(600, 250)

        glVertex2i(750, 520)            # 3rd verticle line i.e last one
        glVertex2i(750, 410)

        glVertex2i(450, 550)               # connects tops of 1st and 2nd verticle lines              
        glVertex2i(600, 450)

        glVertex2i(600, 450)        # connects tops of 2nd and 3rd verticle lines
        glVertex2i(750, 520)

        glVertex2i(450, 400)               #connects bottom of 1st and 2nd verticle lines
        glVertex2i(600, 250)

        glVertex2i(600, 250)       ## connects bottoms of 2nd and 3rd verticle lines
        glVertex2i(750, 410)

        glVertex2i(750, 520)     ## connects top of 3rd and verticle line to a new point
        glVertex2i(640, 560)

        glVertex2i(450, 550)               ## connects top of 1st verticle line to the new point created previously
        glVertex2i(640, 560)

        
        glEnd()


## the following function creates the two, left and right vanishing points. It also connects these
        # vanishing points to the vertices . i.e the lines from these vertices would intersect at their respective vanishing points.
def pers_draw():

    glColor3f(0.5, 1.0, 1.0)
    
    glBegin(GL_LINES)

    #connects the vertices of left side to the left Vanishing point
    glVertex2i(450, 550)
    glVertex2i(20, 700)

    glVertex2i(20, 700)
    glVertex2i(450, 400)
    
    glVertex2i(20, 700)
    glVertex2i(640, 560)

    

    #connects the vertices of right side to the right Vanishing point
    glVertex2i(1350, 700)
    glVertex2i(750, 520)


    glVertex2i(1350, 700)
    glVertex2i(750, 410)


    glVertex2i(1350, 700)
    glVertex2i(640, 560)

    ## connects bottom vertices to the bottom vanishing point
    
    glVertex2i(600, 10)
    glVertex2i(450, 400)


    glVertex2i(600, 10)
    glVertex2i(600, 250)


    glVertex2i(600, 10)
    glVertex2i(750, 410)

    

    #connects the left and right vanishing points

    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(1350, 700)
    glVertex2i(20, 700)


    

    #connects the left and bottom vanishing points

    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(600, 10)
    glVertex2i(20, 700)

    #connects the right and bottom vanishing points

    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(600, 10)
    glVertex2i(1350, 700)
    
    glEnd()
    
def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()     
    refresh2d(width, height)

    
    on_draw()
    pers_draw()

    
    
    glutSwapBuffers()                                  
    


glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("three point perspective of a cube----NIKHIL K")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     
glutMainLoop()































