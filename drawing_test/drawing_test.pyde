# Test the Projection, Transformation and Line Drawing Routines

import traceback
from matrix_stack import *
from drawlib import *
from initials import *

def setup():
    size (750, 750)
    background (255, 255, 255)  # background is white
    stroke (0, 0, 0)            # lines are black

def draw():
    pass

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# call different drawing routines, depending on which number the user types
def handleKeyPressed():
    background (255, 255, 255)
    if (key == '1'):
        ortho_test()
    elif (key == '2'):
        ortho_test_scale()
    elif (key == '3'):
        ortho_test_rotate()
    elif (key == '4'):
        face_test()
    elif (key == '5'):
        faces()
    elif (key == '6'):
        ortho_cube()
    elif (key == '7'):
        ortho_cube2()
    elif (key == '8'):
        persp_cube()
    elif (key == '9'):
        persp_multi_cubes()
    elif (key == '0'):
        persp_initials()
    else:
        print 'key not recognized: ', key

def ortho_test():
    gtInitialize()
    gtOrtho (-100, 100, -100, 100, -100, 100)
    square()

def ortho_test_scale():
    gtInitialize()
    gtScale(1,0.5,1)
    gtOrtho (-100, 100, -100, 100, -100, 100)
    square()

def ortho_test_rotate():
    gtInitialize()
    gtRotateZ(20)
    gtOrtho (-100, 100, -100, 100, -100, 100)
    square()

def ortho_cube():
    gtInitialize()
    gtOrtho (-2, 2, -2, 2, -2, 2)
    gtPushMatrix()
    gtRotateY(17)
    cube()
    gtPopMatrix()

def ortho_cube2():
    gtInitialize()
    gtOrtho (-2, 2, -2, 2, -2, 2)
    gtPushMatrix()
    gtRotateZ(5)
    gtRotateX(25)
    gtRotateY(20)
    cube()
    gtPopMatrix()

def persp_cube():
    gtInitialize()
    gtPerspective (60, -100, 100)
    gtPushMatrix()
    gtTranslate(0, 0, -4)
    cube()
    gtPopMatrix()

def persp_multi_cubes():
    gtInitialize()
    gtPerspective (60, -100, 100)
    
    gtPushMatrix()
    gtTranslate(0, 0, -20)
    print("ctm after translate: ", stack[-1])
    gtRotateZ(5)
    print("ctm after zrotation: ", stack[-1])
    gtRotateX(25)
    print("ctm after xrotation: ", stack[-1])
    gtRotateY(20)
    print("ctm after yrotation: ", stack[-1])
    # draw many cubes in three lines (x, y, z)
    for delta in range(-12,13,3):
        gtPushMatrix()
        gtTranslate(delta, 0, 0)
        cube()
        gtPopMatrix()
        gtPushMatrix()
        gtTranslate(0, delta, 0)
        cube()
        gtPopMatrix()
        gtPushMatrix()
        gtTranslate(0, 0, delta)
        cube()
        gtPopMatrix()
        
    gtPopMatrix()

# cirle of radius one
def circle():
    steps = 64
    xold = 1
    yold = 0
    gtBeginShape()
    for i in range(steps+1):
        theta = 2 * 3.1415926535 * i / float(steps)
        x = cos(theta)
        y = sin(theta)
        gtVertex (xold, yold, 0)
        gtVertex (x, y, 0)
        xold = x
        yold = y
    gtEndShape()

def square():
  
  gtBeginShape ()

  gtVertex (-50, -50, 0)
  gtVertex (-50, 50, 0)

  gtVertex (-50, 50, 0)
  gtVertex (50, 50, 0)

  gtVertex (50, 50, 0)
  gtVertex (50, -50, 0)

  gtVertex (50, -50, 0)
  gtVertex (-50, -50, 0)

  gtEndShape()

def cube():
    gtBeginShape()
    
    # top square
    
    gtVertex (-1.0, -1.0,  1.0)
    gtVertex (-1.0,  1.0,  1.0)

    gtVertex (-1.0,  1.0,  1.0)
    gtVertex ( 1.0,  1.0,  1.0)

    gtVertex ( 1.0,  1.0,  1.0)
    gtVertex ( 1.0, -1.0,  1.0)

    gtVertex ( 1.0, -1.0,  1.0)
    gtVertex (-1.0, -1.0,  1.0)

    # bottom square
    
    gtVertex (-1.0, -1.0, -1.0)
    gtVertex (-1.0,  1.0, -1.0)
    
    gtVertex (-1.0,  1.0, -1.0)
    gtVertex ( 1.0,  1.0, -1.0)
    
    gtVertex ( 1.0,  1.0, -1.0)
    gtVertex ( 1.0, -1.0, -1.0)
    
    gtVertex ( 1.0, -1.0, -1.0)
    gtVertex (-1.0, -1.0, -1.0)
    
    # connect the top square to the bottom one
    
    gtVertex (-1.0, -1.0, -1.0)
    gtVertex (-1.0, -1.0,  1.0)
    
    gtVertex (-1.0,  1.0, -1.0)
    gtVertex (-1.0,  1.0,  1.0)
    
    gtVertex ( 1.0,  1.0, -1.0)
    gtVertex ( 1.0,  1.0,  1.0)
    
    gtVertex ( 1.0, -1.0, -1.0)
    gtVertex ( 1.0, -1.0,  1.0)
    
    gtEndShape()

def face_test():
    gtInitialize()
    gtOrtho (0, 1, 0, 1, -1, 1)
    face()

# draw a face using modified circles
def face():
    
    # head
    gtPushMatrix()
    gtTranslate (0.5, 0.5, 0)
    gtScale (0.4, 0.4, 1.0)
    circle()
    gtPopMatrix()

    # right eye
    gtPushMatrix()
    gtTranslate (0.7, 0.7, 0.0)
    gtScale (0.1, 0.1, 1.0)
    circle()
    gtPopMatrix()

    # left eye
    gtPushMatrix()
    gtTranslate (0.3, 0.7, 0.0)
    gtScale (0.1, 0.1, 1.0)
    circle()
    gtPopMatrix()

    # nose
    gtPushMatrix()
    gtTranslate (0.5, 0.5, 0.0)
    gtScale (0.07, 0.07, 1.0)
    circle()
    gtPopMatrix()

    # mouth
    gtPushMatrix()
    gtTranslate (0.5, 0.25, 0.0)
    gtScale (0.2, 0.1, 1.0)
    circle()
    gtPopMatrix()

# draw four faces
def faces():
    gtInitialize ()
    
    gtOrtho (0, 1, 0, 1, -1, 1)
    
    gtPushMatrix()
    gtTranslate (0.75, 0.25, 0.0)
    gtScale (0.5, 0.5, 1.0)
    gtTranslate (-0.5, -0.5, 0.0)
    face()
    gtPopMatrix()
    
    gtPushMatrix()
    gtTranslate (0.25, 0.25, 0.0)
    gtScale (0.5, 0.5, 1.0)
    gtTranslate (-0.5, -0.5, 0.0)
    face()
    gtPopMatrix()
    
    gtPushMatrix()
    gtTranslate (0.75, 0.75, 0.0)
    gtScale (0.5, 0.5, 1.0)
    gtTranslate (-0.5, -0.5, 0.0)
    face()
    gtPopMatrix()
    
    gtPushMatrix()
    gtTranslate (0.25, 0.75, 0.0)
    gtScale (0.5, 0.5, 1.0)
    gtRotateZ (30)
    gtTranslate (-0.5, -0.5, 0.0)
    face()
    gtPopMatrix()
    
