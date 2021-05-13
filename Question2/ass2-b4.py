import math

def inputVec(dim):
    vec=[]
    for i in range(dim):
        z=[int(input("Enter Real Part...."))]
        z.append(int(input("Enter Imaginary Part...")))
        vec.insert(i,z)
    return vec

def display(z):
    if(z[1]<0):
        print(z[0],z[1],"i")
    else:
        print(z[0],"+",z[1],"i")

def transpose(vec):
    tr=[]
    i=0
    for each in vec:
       z=[each]
       tr.insert(i,z)
       i=i+1
    return tr

def conj(vec):
    con=[]
    i=0
    for each in vec:
        each[1]=-1*each[1]
        con.insert(i,each)
        i=i+1
    return con 

def inner(vec1,vec2,dim):
    pro=[]
    for i in range(dim):
        z=[(vec1[i][0]*vec2[i][0])-(vec1[i][1]*vec2[i][1])]
        z.append((vec1[i][0]*vec2[i][1])+(vec1[i][1]*vec2[i][0]))
        pro.insert(i,z)
    sumr=0
    sumi=0
    for i in range(dim):
        sumr=sumr+pro[i][0]
        sumi=sumi+pro[i][1]
    z=[sumr]
    z.append(sumi)
    return z
            
def main():
    dim=int(input("Enter Dimension Of Vectors..."))
    print("Enter First Vector....")
    vec1=inputVec(dim)
    print("Enter Second Vector....")
    vec2=inputVec(dim)
    con=conj(vec1)
    z=inner(con,vec2,dim)
    print("Inner Product Is....")
    display(z)

if __name__== "__main__":
    main()
