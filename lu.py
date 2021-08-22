from matrix import *
# return the discomposition of (L,U,P)
def lu(mat, perm=True):
    mat = deepcopy(mat)
    L = eye(mat.hight())
    U = uniform(0,mat.hight(),mat.width())
    P = eye(mat.hight())

    n = min(mat.hight(),mat.width())
    for i in range(n):
        if perm==True:
            #find pivot and replace lines
            pivot = mat((i,),i).maxAbs()
            pivot = pivot[1][0] + i #takes the row from the arg
            tmp_line = mat(pivot,(0,))
            mat.edit(mat(i,(0,)),pivot,(0,))
            mat.edit(tmp_line,i,(0,))
            # now replace at the permutations matrix
            tmp_line = P(pivot,(0,))
            P.edit(P(i,(0,)),pivot,(0,))
            P.edit(tmp_line,i,(0,))
        
        U.edit(mat(i,(i,)),i,(i,))
        if (mat.data[i][i] != 0):
            L.edit((1/mat.data[i][i])*mat((i,),i),(i,),i)
        if i != (n-1):
            B = mat((i+1,),(i+1,)) - L((i+1,),i)*U(i,(i+1,))
            mat.edit(B,(i+1,),(i+1,))

    if perm==True:
        return (L,U,P)
    else:
        return(L,U)

def solve(matrix, vector):
    if (vector.hight() != matrix.hight()) or (vector.width() != 1):
        raise Exception("Matrix Exception: dimention error")
    (L,U,P) = lu(matrix)
    b = P*vector
    # forword switch
    z = uniform(0,L.width(),1)
    for i in range(L.hight()):
        for j in range(i):
            b.data[i][0] -= z.data[j][0]*L.data[i][j]
        z.data[i][0] = b.data[i][0]

    # backword switch
    y = uniform(0,U.width(),1)
    for i in range(U.hight()-1,0-1,-1):
        for j in range(U.width() -1,i-1,-1):
            z.data[i][0] -= y.data[j][0]*U.data[i][j]
        if U.data[i][i] == 0:
            raise Exception("Matrix Exception: Matrix is singuler")
        else:
            y.data[i][0] = z.data[i][0] / U.data[i][i]

    return y

def invers(mat):
    if mat.hight() != mat.width():
        raise Exception("Matrix Exception: Matrix is not squre")
    n = mat.hight()
    I = eye(n)
    set = []
    for i in range(n):
        set.append([])
    invers = matrix(set)
    for i in range(n):
        invers.appendRight(solve(mat,I((0,),i)))
    return invers