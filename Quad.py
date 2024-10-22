#Carson Scarboro - Quad. py - 3.1
#This program once ran will complete the quadratic formula given

import math

#returns the deivative of the quadratic 
def der(a,b,c):
    d = math.sqrt(b * b - 4 * a * c)
    if d > 0:
        f = first(d)
        sec = second(d)
        return f, "and" , sec
    
#collects the first root and then calls the second root if d does not equal 0
def first(d):
    x = - b + d
    r = x / (a * 2)
    return (r)
    if d != 0:
        second(d)
        
# colects the second root given the information collected previously
def second (d):
    y = - b - d
    sec = y / (a * 2)
    return (sec)

#These are the variables for the quadratic formula

a = float( input("Eneter Coefficiant A: "))
b = float( input("Eneter Coefficiant B: "))
c = float( input("Eneter Coefficiant C: "))
d = (b**2 - 4 * a * c)
f = float()
r = float()
s = float()

#This is the Main code for the assignment
if d < 0:
    print ("Sorry that has complex roots")
else:
    print ("This Quadratic has two roots", der(a,b,c))




