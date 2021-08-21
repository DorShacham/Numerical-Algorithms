from matrix import *
from lu import *

A = eye(4)
(L,U,P) = lu(A)
print("L:")
L.print()
print("U:")
U.print()
print("P:")
P.print()