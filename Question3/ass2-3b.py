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

def isUnitary(mat,adj,dim):
    mul=[]
    for i in range(dim):
        pro=[]
        l=0
        res=0
        for j in range(dim):
            z=[(mat[i][j][0]*adj[j][0][0])-(mat[i][j][1]*adj[j][0][1])]
            z.append((mat[i][j][0]*adj[j][0][1])+(mat[i][j][1]*adj[j][0][0]))
            pro.insert(l,z)
            l=l+1
        sumr=0
        sumi=0
        for i in range(dim):
            sumr=sumr+pro[i][0]
            sumi=sumi+pro[i][1]
        z=[sumr]
        z.append(sumi)
        mul.insert(i,z)

    muli=[]
    for i in range(dim):
        prod=[]
        l=0
        for j in range(dim):
            z=[(mat[i][j][0]*adj[j][1][0])-(mat[i][j][1]*adj[j][1][1])]
            z.append((mat[i][j][0]*adj[j][1][1])+(mat[i][j][1]*adj[j][1][0]))
            #print(z)
            prod.insert(l,z)
            l=l+1
        sumr=0
        sumi=0
        for i in range(dim):
            sumr=sumr+prod[i][0]
            sumi=sumi+prod[i][1]
        r=[sumr]
        r.append(sumi)
        #print(r)
        muli.insert(i,r)
    res=mul
    res.append(muli)
    for i in range(dim):
        for j in range(dim):
            if(i==j):
                if(res[i][j]!=1):
                    return 0
            else:
                if(res[i][j]!=0):
                    return 0
        return 1

def main():
    dim=int(input("Enter Dimension...."))
    mat=inputMat(dim)
    adj=conj(transpose(mat,dim),dim)
    pro=isUnitary(mat,adj,dim)
    if(pro==1):
        print("Unitary")
    else:
        print("Not Unitary")

if __name__=="__main__":
    main()


