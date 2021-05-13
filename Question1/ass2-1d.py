import math
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

def polar(z):
    r=math.hypot(z[0],z[1])
    theta=math.atan(z[1]/z[0])
    theta=math.degrees(math.atan(z[1]/z[0]))
    if (theta<0):
        theta=90-theta

    z=[r]
    z.append(theta)
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

def main():
    z1=defineComplex()
    p=int(input("Enter Power...."))
    z=power(z1,p)
    display(z)
    r,rt=root(z1)
    print(r,rt)


if __name__ == "__main__":
    main()

