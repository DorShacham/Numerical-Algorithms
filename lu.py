from matrix import *

mat = eye(7)
# mat.print()
mat2 = mat(0,0)
mat2.data[0][0] = 7
mat.print()