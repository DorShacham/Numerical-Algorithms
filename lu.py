from matrix import *
# return the discomposition of (L,U,P)
def lu(mat):
    mat = deepcopy(mat)
    L = eye(mat.hight())
    U = uniform(0,mat.hight(),mat.width())
    P = eye(mat.hight())

    n = min(mat.hight(),mat.width())
    for i in range(n):
        #find pivot and replace lines
        pivot = mat((i,),i).maxAbs()
        # if pivot[0] == 0: # all the coulme is zeros
        #     continue
        pivot = pivot[1][0] #takes the row from the arg
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
            
    return (L,U,P)
