import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.Gaussian_Elimination import Gaussian_Elim

# Copying the relevant code from Problem_10.py
# Defining the relevant constant
V_plus = 5.0 # in V

# Defining the Matrix A in the system Ax = b
A = np.array([[4, -1, -1, -1],
             [-1, 3, 0, -1],
             [-1, 0, 3, -1],
             [-1, -1, -1, 4]], float)

# Defning the vector b
b = np.array([V_plus, 0, V_plus, 0], float)

V = np.linalg.solve(A, b)
print("The solution to the given system is (using numpy.linalg.solve):")
for i in range(0, 4):
    print(f"\tV{i + 1} = {V[i]} V")
    
V = Gaussian_Elim(A, b)
print("\nThe solution to the given system is (using code from Problem 10):")
for i in range(0, 4):
    print(f"\tV{i + 1} = {V[i]} V")