# Drawing Routines that are similar to those in OpenGL

from matrix_stack import *
gleft = 0
gright = 0
gbottom = 0
gtop = 0
gnear = 0
gfar = 0
gfov = 0
orthopro = 0
perspro = 0
vertices = []
s = getMatrix()
def gtOrtho(left, right, bottom, top, near, far):
    global gleft
    global gright
    global gbottom
    global gtop
    global perspro
    global orthopro
    gleft = float(left)
    gright = float(right)
    gbottom = float(bottom)
    gtop = float(top)
    perspro = 0
    orthopro = 1
    
def gtPerspective(fov, near, far):
    global orthopro
    global perspro
    global gfov
    global gnear
    global gfar
    
    gfov = math.radians(fov)
    gnear = float(near)
    gfar = float(far)
    perspro = 1
    orthopro = 0

def gtVertex(x, y, z):

    global vertices
    global orthopro
    global perspro
    global s
    
    s = getMatrix()

    result = [[0],[0],[0],[0]]

    originalvertex =[[x],[y],[z],[1]]
    for i in range(4):
        for j in range(1):
            for k in range(4):
                result[i][j] += s[i][k] * originalvertex[k][j]
    curx,cury,curz = result[0][0],result[1][0],abs(result[2][0])
    addx,addy = curx,cury
    if orthopro==1:
        addx = (curx-gleft)*((width)/(gright-gleft))
        addy = (cury-gbottom)*((height)/(gtop-gbottom))
    elif perspro == 1:
        k = math.tan(gfov/2)
        firstx = curx/curz
        firsty = cury/curz
        addx = (firstx +k)*(width/(2*k))
        addy = (firsty + k) *(height/(2*k))
    toadd = [addx,addy,curz]
    vertices.append(toadd)
    
    

def gtBeginShape():
    global vertices 
    vertices = []


def gtEndShape():
    i= 0
    n= len(vertices)
    while i<n:
        firstvertex = vertices[i]
        secondvertex =vertices[i+1]
        firstx,firsty,firstz = firstvertex[0],firstvertex[1],firstvertex[2]
        secondx,secondy,secondz = secondvertex[0],secondvertex[1],secondvertex[2]
        line(firstx,height - firsty,secondx,height-secondy)
        i+= 2
    
