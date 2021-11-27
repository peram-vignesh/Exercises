import math
def circumference(radius):
    c=math.pi*2*radius
    c=float('{0:.2f}'.format(c))
    return c
def perimeter(length, breadth):
    p=length+breadth
    p=2*length+breadth
    return p
def area_cir (radius):
    a=math.pi*radius*radius
    a=float('{0:.2f}'.format(a))
    return a
def area_rect (length,breadth):
    r=length*breadth
    return r
def surface(radius,height):
    b=circumference(radius)
    s=b*height
    b=b*2
    s+=b
    return s
def volume(radius,height):
    v=area_cir(radius)
    v=v*height
    return v
def triangle(base,height):
    t=base*height
    t=t/2
    return t
shape=input()
output=input()
if shape=='circle':
    rad=int(input())
    if output=='area':
        print(area_cir(rad))
    else:
        print(circumference(rad))
elif shape=='rectangle':
    l=int(input())
    b=int(input())
    if output=='area':
        print(area_rect(l,b))
    else:
        print(perimeter(l,b))
elif shape=='cylinder':
    rad=int(input())
    h=int(input())
    if output=='volume':
        print(volume(rad,h))
    else:
        print(surface(rad,h))
elif shape == 'triangle':
    h=int(input())
    base=int(input())
    print(triangle(base,h))
else:
    print("Entered wrong figure")
    
    
    
 
