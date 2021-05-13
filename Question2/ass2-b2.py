import math

def inputVS(row,col):
    v=[]
    #dim=int(input("Enter Number Of Vectors..."))
    for i in range(row):
        c=[]
        for j in range(col):
            x=float(input("Enter Real Part...."))
            y=float(input("Enter Imaginary Part...."))
            z=[x,y]
            c.append(z)
        v.append(c)
    return v

def addition(v1,v2,row,col):
    sum=[]
    for i in range (row):
      c=[]
      for j in range(col):
        z=[v1[i][j][0]+v2[i][j][0]]
        z.append(v1[i][j][1]+v2[i][j][1])
        c.append(z)
      sum.insert(i,c)
    print("SUM", sum)

def inverse(vs,row,col):
    res=[]
    for i in range(row):
        c=[]
        for j in range(col):
            a=[-1*vs[i][j][0]]
            a.append(-1*vs[i][j][1])
            c.append(a)
        res.insert(i,c)
    print(res)

def inputScal():
    print("Enter Scalar Multiple....")
    s=[float(input("Enter Real Part...."))]
    s.append(float(input("Enter Imaginary Part...")))
    return s

def scalarMul(v,s):
    pro=[]
    i=0
    for each in v:
        c=[]
        for every in v[i]:
            z=[s[0]*every[0]-s[1]*every[1]]
            z.append(s[0]*every[1]+s[1]*every[0])
            c.append(z)
        pro.insert(i,c)
        i=i+1
    return pro

def main():
    rows=int(input("Enter Number Of Rows...."))
    col=int(input("Enter Number Of Columns..."))
    print("Enter First Vector Space....")
    vs=inputVS(rows,col)
    print("Enter Seond Vector Space...")
    vs2=inputVS(rows,col)
    print("Addition....")
    addition(vs,vs2,rows,col)
    print("Inverse....")
    inverse(vs,rows,col)
    s=inputScal()
    product=scalarMul(vs,s)
    print("Scalar Multiplication....")
    print(product)

if __name__ == "__main__":
    main()

