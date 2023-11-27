import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.QR_using_MGS import QR_MGS

"""
    The following program computes the QR decomposition of the given matrices using the
    Modified Gram-Schmidt method.
"""

# Part (b)
A = np.array([[1, 4, 8, 4],
              [4, 2, 3, 7],
              [8, 3, 6, 9],
              [4, 7, 9, 2]], float)

Q, R = QR_MGS(A, 4)
print("\nA = ")
print(A)

print("\nQ = ")
print(Q)

print("\nR = ")
print(R)

print("\nQ*R = ")
print(Q*R)

# Part (b): Finding Eigenvalues and Eigenvectors
from Import_Modules.Eigenvalues import Eigen

E_v, V = Eigen(A, 10**(-6))
n = E_v.shape[0]
e_v = [E_v[i, i] for i in range(0, n)]

print(f"\nThe eigenvalues of A are: {e_v}")

print("\nThe matrix of Eigenvectors is: ")
print(V)