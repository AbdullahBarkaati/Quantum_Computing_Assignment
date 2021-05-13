def inputMat(dim):
    mat=[]
    for i in range(dim):
        c=[]
        for j in range(dim):
            z=[float(input("Enter Real Part..."))]
            z.append(float(input("Enter Imaginary Part...")))
            c.append(z)
        mat.insert(i,c)
    return mat

def product(z1,z2):
    z=[z1[0]*z2[0]-z1[1]*z2[1]]
    z.append(z1[0]*z2[1]+z1[1]*z2[0])
    return z

def getProduct(z,mat,dim):
    pro=[]
    for i in range(dim):
        row=[]
        for j in range(dim):
            row.append(product(z,mat[i][j]))
        pro.insert(i,row)
    return pro

def tensor(mat1,mat2,dim1,dim2):
    ten=[]
    for i in range(dim1):
        for j in range(dim1):
            pr=getProduct(mat1[i][j],mat2,dim1)
            ten.append(pr)
    return ten

def main():
    dim1=int(input("Enter Dimension Of First Matrix..."))
    mat1=inputMat(dim1)
    dim2=int(input("Enter Dimension Of Second Matrix..."))
    mat2=inputMat(dim2)
    tens=tensor(mat1,mat2,dim1,dim2)
    for each in tens:
        print(each)

if __name__ == "__main__":
    main()
