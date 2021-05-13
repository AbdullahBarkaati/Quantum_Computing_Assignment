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
    return z

def main():
    z1=defineComplex()
    z2=defineComplex()
    add=addition(z1,z2)
    sub=subtract(z1,z2)
    pr=product(z1,z2)
    div=divide(z1,z2)
    print("Addition....")
    display(add)
    print("Subtraction...")
    display(sub)
    print("Product....")
    display(pr)
    print("Divison...")
    display(div)


if __name__ == "__main__":
    main()

