# This is the provided code for the ray tracing project.
#
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

from __future__ import division
from classes import *
import traceback

lightsources = []
spheres = []
framevectors = []
uvector = PVector(0,0,0)
vvector = PVector(0,0,0)
wvector = PVector(0,0,0)
bgcolor = (0,0,0)
diffuseColor = (0,0,0)
ambientColor = (0,0,0)
specularColor = (0,0,0)

specularpower = 0
krefl = 0
fov = 0

curmaterial = Material(diffuseColor,ambientColor,specularColor,specularpower,krefl)
eyeposition = PVector(0,0,0)



    
debug_flag = False   # print debug information when this is True

def setup():
    size(320, 320) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    frameRate(30)

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# read and interpret a scene description .cli file based on which key has been pressed
def handleKeyPressed():
    if key == '1':
        interpreter("01_one_sphere.cli")
    elif key == '2':
        interpreter("02_three_spheres.cli")
    elif key == '3':
        interpreter("03_shiny_sphere.cli")
    elif key == '4':
        interpreter("04_many_spheres.cli")
    elif key == '5':
        interpreter("05_one_triangle.cli")
    elif key == '6':
        interpreter("06_icosahedron_and_sphere.cli")
    elif key == '7':
        interpreter("07_colorful_lights.cli")
    elif key == '8':
        interpreter("08_reflective_sphere.cli")
    elif key == '9':
        interpreter("09_mirror_spheres.cli")
    elif key == '0':
        interpreter("10_reflections_in_reflections.cli")

# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.

def interpreter(fname):
    global spheres,lightsources, framevectors, bgcolor, diffuseColor, ambientColor , \
specularColor , specularpower , krefl ,fov ,curmaterial, eyeposition,uvector,vvector,wvector
    reset_scene()  # you should initialize any data structures that you will use here
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse the lines in the file in turn
    for line in lines:
        words = line.split()  # split up the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
        
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            v = PVector(x,y,z)
            radius = float(words[1])
            # call your sphere making routine here
            # for example: create_sphere(x,y,z,radius)
            
            spheres.append(Sphere(v,radius,curmaterial))
            print(spheres)
        elif words[0] == 'fov':
            
            fov = float(words[1])
            pass
        elif words[0] == 'eye':
            ex = float(words[1])
            ey = float(words[2])
            ez = float(words[3])
            eyeposition =PVector(ex,ey,ez)
            pass
        elif words[0] == 'uvw':
            ux =float(words[1])
            uy =float(words[2])
            uz =float(words[3])
            vx=float(words[4])
            vy=float(words[5])
            vz=float(words[6])
            wx=float(words[7])
            wy=float(words[8])
            wz=float(words[9])
            
            uvector = PVector(ux,uy,uz)
            vvector = PVector(vx,vy,vz)
            wvector = PVector(wx,wy,wz)
            pass
        elif words[0] == 'background':
            r =float(words[1])
            g =float(words[2])
            b =float(words[3])
            
            bgcolor = (r,g,b)
            pass
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            v = PVector(x,y,z)
            newlight = Light(v, r, g, b)
            lightsources.append(newlight)
            pass
        elif words[0] == 'surface':
            dr = float(words[1])
            dg = float(words[2])
            db = float(words[3])
            diffuseColor = (dr,dg,db)
            
            ar = float(words[4])
            ag = float(words[5])
            ab = float(words[6])
            ambientColor = (ar, ag, ab)
            
            sr = float(words[7])
            sg = float(words[8])
            sb = float(words[9])
            specularColor = (sr, sg, sb)
            
            specularpower = float(words[10])
            krefl = float(words[11])
            curmaterial = Material(diffuseColor,ambientColor,specularColor,specularpower,krefl)
            pass
        elif words[0] == 'begin':
        
            pass
        elif words[0] == 'vertex':
        
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

# render the ray tracing scene
def render_scene():
    global debug_flag

    for j in range(height):
        for i in range(width):

            # Maybe set a debug flag to true for ONE pixel.
            # Have routines (like ray/sphere intersection)print extra information if this flag is set.
            debug_flag = False
            if i == 211 and j == 131:
            
                debug_flag = True
                
            d =  1/tan(radians(fov/2))
            u = (2*i/width) - 1
            v = (2*(height-j)/height) - 1
            raydx = -d*wvector.x + v*vvector.x + u*uvector.x
            raydy = -d*wvector.y + v*vvector.y + u*uvector.y
            raydz = -d*wvector.z + v*vvector.z + u*uvector.z
            raydirection = PVector(raydx,raydy,raydz).normalize()
        
             # change these variable names to match the rest of your code!
            
            newray = Ray(eyeposition,raydirection)
            hitobj = rayIntersectScene(newray)
            if debug_flag:
                print(u)
                print(v)
                print("raydirection",raydirection)
                print("rayorigin",eyeposition)
                print("U",uvector)
                print("V",vvector)
                print("W",wvector)
                print("FOV",fov)
                
                # print("tvalue",hitobj.tvalue)
                # print("diffusec",hitobj.cursphere.material.diffusec)
                # print("normvector",hitobj.vector)
                # print("intersect",hitobj.intersectpoint)
                
            # create an eye ray for pixel (i,j) and cast it into the scene
            pixColor = shade(hitobj) # you will calculate the correct pixel color here using ray tracing
            pix_color = color(*pixColor)
            set (i, j, pix_color)         # draw the pixel with the calculated color
def rayIntersectScene(eyeray):
    minT = float('inf')
    newhit = None

    for s in spheres:
        t = s.intersect(eyeray)
        if t!= None and t >0 and t <minT:
        
            interx = eyeray.origin.x + t * eyeray.direction.x
            intery = eyeray.origin.y + t*eyeray.direction.y
            interz = eyeray.origin.z + t*eyeray.direction.z
            interpoint = PVector(interx,intery,interz)
            normalv = PVector.sub(interpoint,s.center)
            newhit = Hit(s,normalv,t,interpoint)
            minT = t
    return newhit
# here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global lightsources,spheres,framevectors,uvector,vvector,wvector,bgcolor,diffuseColor,ambientColor,specularColor,specularPower,krefl,fov,curmaterial,eyeposition
    lightsources = []
    spheres = []
    framevectors = []
    uvector = PVector(0,0,0)
    vvector = PVector(0,0,0)
    wvector = PVector(0,0,0)
    bgcolor = (0,0,0)
    diffuseColor = (0,0,0)
    ambientColor = (0,0,0)
    specularColor = (0,0,0)

    specularpower = 0
    krefl = 0
    fov = 0

    curmaterial = Material(diffuseColor,ambientColor,specularColor,specularpower,krefl)
    eyeposition = PVector(0,0,0)
    
def shade(curhit):
    global debug_flag
    if curhit == None:
        return bgcolor
    normvector = PVector.sub(curhit.intersectpoint,curhit.cursphere.center).normalize()

    redtotal,greentotal,bluetotal = 0,0,0
    
    for light in lightsources:
        lvector = PVector.sub(light.position,curhit.intersectpoint).normalize()
        dotpro = max(normvector.dot(lvector),0)
        redtotal += curhit.cursphere.material.diffusec[0] *light.r *dotpro
        greentotal += curhit.cursphere.material.diffusec[1] *light.g *dotpro
        bluetotal += curhit.cursphere.material.diffusec[2] *light.b *dotpro
        if debug_flag:
                print "calculating contribution of the light whose position is: ", light.position
                print "normvector",normvector
                print "L: ", lvector
                print "light color: ", light.r,light.g,light.b
                print "surface's diffuse color: ", curhit.cursphere.material.diffusec
                print "totalcolor", redtotal,greentotal,bluetotal
    return (redtotal,greentotal,bluetotal)
        
# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
