def inputMat(dim):
    mat=[]
    for i in range(dim):
        c=[]
        for j in range(dim):
            z=[int(input("Enter Real Part..."))]
            z.append(int(input("Enter Imaginary Part...")))
            c.append(z)
        mat.insert(i,c)
    return mat

def transpose(mat,dim):
    tr=[]
    for i in range(dim):
        z=[]
        for j in range(dim):
            z.append(mat[j][i])
        tr.insert(i,z)
    return tr

def conj(mat,dim):
    con=[]
    for i in range(dim):
        c=[]
        for j in range(dim):
            z=[mat[i][j][0]]
            z.append(-1*mat[i][j][1])
            c.append(z)
        con.insert(i,c)
    return con

def checkDiag(mat,dim):
    for i in range(dim):
        for j in range(dim):
            if(i==j):
                if(mat[i][j][1]!=0):
                    return 0
    return 1

def isHermition(mat,dim):
    trans=transpose(mat,dim)
    con=conj(mat,dim)
    if(checkDiag(mat,dim)==1):
        for i in range(0,dim):
            for j in range(0,dim):
                if(trans[i][j][0]!=con[i][j][0] or trans[i][j][1]!=con[i][j][1]):
                    return 0    
        return 1
    else:
        return 0

def main():
    dim=int(input("Enter Dimension...."))
    mat=inputMat(dim)
    val=isHermition(mat,dim)   
    if(val==1):
        print("Mat",mat,"Is Hermition...")
    else:
        print("Mat",mat,"Is Not Hermition...")

if __name__ == "__main__":
    main()
