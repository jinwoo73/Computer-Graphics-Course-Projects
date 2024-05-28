# Object Modeling Example Code

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        global time
        time += 0.01

        camera (0, 0, 200, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (200, 200, 255)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(50, 50, 50);
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)
    

        
        
        
    
            
        # drawBodies()
    
    
        drawCars()
    
    
        #fill (255, 0, 0)
        #pushMatrix()
        # translate (-30, 0, 0)
        # rotateX (time)
        # box(20)
        # popMatrix()

        # a green sphere
        # fill (0, 250, 0)
        # pushMatrix()
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        # sphere(10)
        # popMatrix()

        # a blue cylinder
        # fill (0, 0, 255)
        # pushMatrix()
        # translate (30, 0, 0)
        # rotateX (-time)
        # scale (10, 10, 10)
        # cylinder()
        # popMatrix()
        # if time <= 3:
        #     camera(0,0,100 + time * 30,0,0,0,0,1,0)
        # elif time < 11:
        #     camera((time-3)*-11,0,100,0,0,-400,0,1,0)
    except Exception:
        traceback.print_exc()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
def drawCars():
      # can make method to draw wheels , drawWhell(x,y,z) :pushmatrix
      pushMatrix()
      translate(0,0,90)
      #a rear left wheel
      fill(255,255,255)
      pushMatrix()
      translate(-2,4,-13)
    
        
      cylinder()
      popMatrix()
        
    #a rear right wheel
      fill(255,255,255)
      pushMatrix()
      translate(2,4,-13)
    
      cylinder()
      popMatrix()
        
    
    #a front left wheel
    #purple
      fill(255,0,255)
      pushMatrix()
      translate(2,4,3)
    
        
      cylinder()
      popMatrix()
        
    #a front right wheel
      fill(255,255,255)
      pushMatrix()
      translate(-2,4,3)
    
      cylinder()
      popMatrix()

      popMatrix()  
      
        
#underbody

      fill (255, 0, 0)
      pushMatrix()
      translate (-15, 20, 5)
      scale(50,20,50)
    
      box(1)
      popMatrix()
            #right headlight
      fill (134, 167, 0)
      pushMatrix()
      translate (-30, 20, -25)
      scale(15,10,5)
    
      box(1)
      popMatrix()
            #left headlight
      fill (134, 167, 0)
      pushMatrix()
      translate (0, 20, -25)
      scale(15,10,5)
   
      box(1)
      popMatrix()
            #upperbody
      fill (255, 0, 0)
      pushMatrix()
      translate (-15, 0, 0)
      scale(40,20,30)
        
      box(1)
      popMatrix()
            #frontwindow
      fill (255, 255, 255)
      pushMatrix()
      translate (-15, 0, -15)
      scale(30,18,3)
    
      box(1)
      popMatrix()
            #rearwindow
      fill (25, 55, 13)
      pushMatrix()
      translate (-15, 0, 15)
      scale(30,18,3)
    
      box(1)
      popMatrix()
        
            #rear license plate
      fill (255, 155, 12)
      pushMatrix()
      translate (-15 , 22, 25)
      scale(30,12,3)
    
      box(1)
      popMatrix()
        
       #rightwindow
      fill (255, 255, 255)
      pushMatrix()
      translate (6,-1,0)
      scale(2,16,26)
    
      box(1)
      popMatrix()
        
            #rightwindow
      fill (255, 0, 255)
      pushMatrix()
      translate (-36,-1,0)
      scale(2,16,26)
    
      box(1)
      popMatrix()
