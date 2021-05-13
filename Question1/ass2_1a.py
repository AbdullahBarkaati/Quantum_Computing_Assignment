import math
import cmath
import matplotlib.pyplot as plt
import numpy as py

def defineComplex():
    x=float(input("Enter Real Part..."))
    y=float(input("Enter Imaginary Part..."))
    z=[x]
    z.append(y)
    return z

def display(z):
    if(z[1]<0):
        print(z[0],z[1],"i")
    else:
        print(z[0],"+",z[1],"i")

def addition(z1,z2):
    z=[z1[0]+z2[0]]
    z.append(z1[1]+z2[1])
    return z

def subtract(z1,z2):
    z=[z1[0]-z2[0]]
    z.append(z1[1]-z2[1])
    return z

def product(z1,z2):
    z=[(z1[0]*z2[0])-(z1[1]*z2[1])]
    z.append((z1[0]*z2[1])+(z1[1]*z2[0]))
    return z

def divide(z1,z2):
    first=(z1[0]*z2[0])+(z1[1]*z2[1])
    second=((z1[1]*z2[0])-(z1[0]*z2[1]))
    den=((z2[0]*z2[0])+(z2[1]*z2[1]))
    z=[first/den]
    z.append(second/den)
    print(first)
    print(second)
    print(den)
    return z
#-----------------------------------------------------------------------------------------------------------
sin={0:0,30:1/2,45:1/math.sqrt(2),60:math.sqrt(3)/2,90:1,180:0}
def polar(z):
    r=math.hypot(z[0],z[1])
    theta=math.atan(z[1]/z[0])
    theta=math.degrees(math.atan(z[1]/z[0]))
    if (theta<0):
        theta=90-theta

    z=[r]
    z.append(theta)
    return z

def addPolar(z1,z2):
    z=[z1[0]+z2[0]]
    z.append(z1[1]+z2[1])
    return z

def subPolar(z1,z2):
    z=[z1[0]-z2[0]]
    z.append(z1[1]-z2[1])
    return z

def mulPolar(z1,z2):
    c1=polar(z1)
    c2=polar(z2)

    r=c1[0]*c2[0]
    theta=c1[1]+c2[1]
    rad=math.radians(theta)
    cs=math.cos(rad)
    si=math.sin(rad)
    z=[r*cs]
    z.append(r*si)
    return z

def divPolar(z1,z2):
    c1=polar(z1)
    c2=polar(z2)

    r=c1[0]/c2[0]
    theta=c1[1]-c2[1]
    rad=math.radians(theta)
    cs=math.cos(rad)
    si=math.sin(rad)
    z=[r*cs]
    z.append(r*si)
    return z

def power(z,n):
    c=polar(z)

    r=c[0]**n
    theta=n*c[1]
    rad=math.radians(theta)
    cs=math.cos(rad)
    si=math.sin(rad)
    z=[r*cs]
    z.append(r*si)
    return z

def root(z):
    n=int(input("Enter Cube Root....."))
    c=polar(z)
    r=[]
    root=[]
    for i in range(0,n):
        root.append((1/n)*(c[1]+2*math.pi*i))
        r.append(c[0])
    return r,root

def plotComplex():
    z=defineComplex()
    plt.scatter(z[0],z[1],marker="*",color='red')
    plt.title('Complex Number')
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.show()


#z1=defineComplex()
#z2=defineComplex()
#p=int(input("Enter Power...."))
#n=int(input("Enter Cube Root"))
#z=power(z1,p)
#root(z1,n)
#display(z)
#add=addition(z1,z2)
#sub=subtract(z1,z2)
#pr=product(z1,z2)
#div=divide(z1,z2)

#display(z1)
#display(z2)
#display(add)
#display(sub)
#display(pr)
#display(div)
#p=polar(z1)
#print(p)
#pro=mulPolar(z1,z2)
#div=divPolar(z1,z2)
#display(pro)
#display(div)
plotComplex()
