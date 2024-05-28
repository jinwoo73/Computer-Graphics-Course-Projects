class Light:
    def __init__(self,position,r,g,b):
        self.position = position
        self.r = r
        self.g = g
        self.b = b
class Sphere:
    def __init__(self,center,radius,material):
        self.center = center
        self.radius =radius
        self.material = material
    def intersect(self,ray):
        u = PVector.sub(ray.origin,self.center)
        dx,dy,dz = ray.direction.x,ray.direction.y,ray.direction.z
        ux,uy,uz =u.x,u.y,u.z
        r = self.radius
        a = dx*dx+dy*dy + dz*dz
        b =  2*dx*ux + 2*dy*uy + 2*dz*uz
        c = ux*ux + uy*uy +uz*uz - r*r
    
        disc =sqrt(b*b-4*a*c)
        if disc <0:
            return float('inf')
        result =  (-b + disc )/(2*a)
        potent =  (-b-disc)/(2*a)
        if potent >0 :
            result = potent
        return result
class Material:
    def __init__(self,diffusec,ambientc,specularc,specularpower,krefl):
        self.diffusec = diffusec
        self.ambientc = ambientc
        self.specularc = specularc
        self.specularpower = specularpower
        self.krefl = krefl
class Ray:
    def __init__(self,origin,direction):
        self.origin = origin
        self.direction =direction
class Hit:
    def __init__(self,cursphere,vector,tvalue,intersectpoint):
        self.cursphere = cursphere
        self.vector = vector
        self.tvalue = tvalue
        self.intersectpoint = intersectpoint
        
