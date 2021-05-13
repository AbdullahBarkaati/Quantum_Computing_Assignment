def matVec():
    r=int(input("Enter Number Of Rows In Matrix...."))
    c=int(input("Enter Number Of Columns In Matrix...."))
    mat=[]
    for i in range(r):
        col=[]
        for j in range(c):
            col.append(int(input("Enter Matrix Element...")))
        mat.append(col)

    num=int(input("Enter Number Of Elements in vectors..."))
    vec=[]
    for i in range(num):
        vec.append(int(input("Enter Vector Elements....")))
    if num!=r:
        print("Given Action Can Not Be Perfomed Bcoz Dimension Not Matches...")
    else:
        pro=[]
        for i in range(r):
            res=0
            for j in range(c):
                res=res+mat[i][j]*vec[j]
            pro.append(res)
    return pro
def main():
    pr=matVec()
    print(pr)

if __name__ == "__main__":
    main()
