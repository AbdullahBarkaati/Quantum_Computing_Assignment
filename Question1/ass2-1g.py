import math
import matplotlib.pyplot as plt
import numpy as py

def defineComplex():
    x=float(input("Enter Real Part..."))
    y=float(input("Enter Imaginary Part..."))
    z=[x]
    z.append(y)
    return z

def polar(z):
    r=math.hypot(z[0],z[1])
    theta=math.atan(z[1]/z[0])
    theta=math.degrees(math.atan(z[1]/z[0]))
    if (theta<0):
        theta=90-theta

    z=[r]
    z.append(theta)
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
    r,rt=root(z)
    plt.scatter(r,rt,marker="*",color='red')
    plt.title('Complex Number')
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.show()

def main():
    plotComplex()

if __name__ == "__main__":
    main()

