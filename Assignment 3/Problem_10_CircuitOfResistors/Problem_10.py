import numpy as np

import sys
sys.path.insert(0, '.')

from Import_Modules.Gaussian_Elimination import Gaussian_Elim

"""
    The system of equations for V1, V2, V3, and V4 is attached in the Figure
    'Part (a) System of Equations.png'. We use the method of Gaussian Elimination to solve
    this sytem.
"""
# Defining the relevant constant
V_plus = 5.0 # in V

# Defining the Matrix A in the system Ax = b
A = np.array([[4, -1, -1, -1],
             [-1, 3, 0, -1],
             [-1, 0, 3, -1],
             [-1, -1, -1, 4]], float)

# Defning the vector b
b = np.array([V_plus, 0, V_plus, 0], float)

V = Gaussian_Elim(A, b)
print("The solution to the given system is:")
for i in range(0, 4):
    print(f"\tV{i + 1} = {V[i]} V")

# To verify the result, we check the value of Ax and compare it with b
check = np.matrix(A) * np.matrix(V).T - np.matrix(b).T
print("\nThe vector Ax - b is:")
print(check)