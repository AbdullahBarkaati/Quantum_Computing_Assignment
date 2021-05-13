import math

def display(vs,dim):
    for i in range(dim):
        if (vs[i][1]<0):
            print(vs[i][0],vs[i][1],"i")
        else:
            print(vs[i][0],"+",vs[i][1],"i")

def inputVS(dim):
    v=[]
    #dim=int(input("Enter Number Of Vectors..."))
    for i in range(0,dim):
        x=float(input("Enter Real Part...."))
        y=float(input("Enter Imaginary Part...."))
        z=[x,y]
        v.insert(i,z)
    return v

def addition(v1,v2,dim):
    sum=[]
    for i in range (0,dim):
        z=[v1[i][0]+v2[i][0]]
        z.append(v1[i][1]+v2[i][1])
        sum.insert(i,z)
    return sum

def inverse(vs):
    res=[]
    c=[]
    for each in vs:
        c.append(-1*each[0])
        c.append(-1*each[1])
        res.append(c)
        c=[]
    return res

def inputScal():
    print("Enter Scalar Multiple...")
    s=[float(input("Enter Real Part..."))]
    s.append(float(input("Enter Imaginary Part...")))
    return s

def scalarMul(v,s):
    pro=[]
    i=0
    for each in v:
        z=[s[0]*each[0]-s[1]*each[1]]
        z.append(s[0]*each[1]+s[1]*each[0])
        pro.insert(i,z)
        i=i+1
    return pro

def main():

    dim=int(input("Enter Number Of Vectors In Vector Space"))
    print("Enter First Vector Space....")
    vs=inputVS(dim)
    print("Enter Second Vector Space...")
    vs2=inputVS(dim)
    sum=addition(vs,vs2,dim)
    s=inputScal()
    scal=scalarMul(vs,s)
    inv=inverse(vs)
    print("Addition....")
    display(sum,dim)
    print("Scalar Multiplication....")
    display(scal,dim)
    print("inverse...")
    display(inv,dim)

if __name__=="__main__":
    main()
