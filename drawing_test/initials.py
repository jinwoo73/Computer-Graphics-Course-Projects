# The routine below should draw your initials in perspective

from matrix_stack import *
from drawlib import *

def persp_initials():
    #draw all line in xy plane, then translate it into negative z, give little rotations,
    #perspect 
    # draw J
    gtInitialize()
    gtPerspective (60,-100,-100)

    gtBeginShape ()
    gtTranslate(40,20,-200.0)
    gtRotateZ(15)
    gtRotateX(45)
    gtRotateY(35)
    gtVertex (-70, -50, 0)
    gtVertex (-50, -50, 0)
    
    gtVertex (-50, -50, 0)
    gtVertex (-50, 50, 0)
    
    gtVertex (-30, 50, 0)
    gtVertex (-70, 50,0)
    #drawp
    gtTranslate(40,0,0)
    gtVertex(-30,50,0)
    gtVertex(-10,50,0)
    
    gtVertex(-30,30,0)
    gtVertex(-10,30,0)
    
    gtVertex(-30,50,0)
    gtVertex(-30,30,0)
    
    gtVertex(-10,50,0)
    gtVertex(-10,30,0)
    
    gtVertex(-30,30,0)
    gtVertex(-30,-50,0)
    
    gtEndShape()
