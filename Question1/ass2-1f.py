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

def product(z1,z2):
    z=[(z1[0]*z2[0])-(z1[1]*z2[1])]
    z.append((z1[0]*z2[1])+(z1[1]*z2[0]))
    return z
def main():
    z1=defineComplex()
    z2=defineComplex()
    pr=product(z1,z2)
    print("Product....")
    display(pr)


if __name__ == "__main__":
    main()


