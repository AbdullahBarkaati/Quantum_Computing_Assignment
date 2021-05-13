import math

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

def main():
    z1=defineComplex()
    z2=defineComplex()
    add=addPolar(z1,z2)
    sub=subPolar(z1,z2)
    pro=mulPolar(z1,z2)
    div=divPolar(z1,z2)
    print("Polar Of First...",polar(z1))
    print("Polar Of Second...",polar(z2))
    print("Addition...")
    display(add)
    print("Subtraction...")
    display(sub)
    print("Product...")
    display(pro)
    print("Divison...")
    display(div)



if __name__ == "__main__":
    main()


