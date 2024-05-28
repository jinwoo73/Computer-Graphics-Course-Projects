# Your Matrix Stack Library

# you should modify the provided empty routines to complete the assignment
import math 
def gtInitialize():
    I = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    global stack
    stack = []
    stack.append(I)
    ctm = stack[-1]
    

def gtPopMatrix():
    global stack
    if len(stack)>1:
        stack.pop()
    else:
        print("cannot pop the matrix stack")

def gtPushMatrix():
    global stack
    ctm = stack[-1]
    stack.append(ctm)


def gtScale(x,y,z):
    global stack
    curctm = stack[-1]
    scalem = [[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]]
    newctm = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newctm[i][j] += curctm[i][k] * scalem[k][j]
    stack[-1] = newctm
    

def gtTranslate(x,y,z):
    global stack
    curctm = stack[-1]
    transm = [[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]
    newctm = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newctm[i][j] += curctm[i][k] * transm[k][j]
    stack[-1] = newctm

def gtRotateX(theta):
    global stack
    curctm = stack[-1]
    degree = math.radians(theta)
    rotatexm = [[1,0,0,0],[0,math.cos(degree),-math.sin(degree),0],[0,math.sin(degree),math.cos(degree),0],[0,0,0,1]]
    newctm = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newctm[i][j] += rotatexm[i][k] * curctm[k][j]
    stack[-1] = newctm

def gtRotateY(theta):
    global stack
    curctm = stack[-1]
    degree = math.radians(theta)
    rotateym = [[math.cos(degree),0,math.sin(degree),0],[0,1,0,0],[-math.sin(degree),0,math.cos(degree),0],[0,0,0,1]]
    newctm = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newctm[i][j] += curctm[i][k] * rotateym[k][j]
    stack[-1] = newctm

def gtRotateZ(theta):
    global stack
    curctm = stack[-1]
    degree = math.radians(theta)
    rotatezm = [[math.cos(degree),-math.sin(degree),0,0],[math.sin(degree),math.cos(degree),0,0],[0,0,1,0],[0,0,0,1]]
    newctm = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                newctm[i][j] += curctm[i][k] * rotatezm[k][j]
    stack[-1] = newctm

def print_ctm():

    ctm = stack[-1]
    for row in ctm:
        print(row)
    
    print("")
        
