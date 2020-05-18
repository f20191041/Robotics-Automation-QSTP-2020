# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import math

def p_to_c():
    x1=r*math.cos(angrad)
    y1=r*math.sin(angrad)
    co=(x1,y1)
    print("Cartesian coordinates are- ",co)
    
def c_to_p():
    r12=((x*x)+(y*y))
    r1=math.sqrt(r12)
    ang=float(y)/float(x)
    angrad1=math.atan(ang)
    po=(r1,angrad1)
    print("Polar coordinates are- ",po)
    
opt=input("Enter 1 for polar to catesian conversion and 2 for vice-versa: ")
if opt=='1':
    r=float(input("Enter distance from origin- "))
    angrad=float(input("Enter radian angle- "))
    p_to_c()
elif opt=='2':
    x=float(input("Enter x-coordinate- "))
    y=float(input("Enter y-coordinate- "))
    c_to_p()