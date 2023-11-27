import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.Gaussian_Elimination import Gaussian_Elim

"""
    The system of equations modelling the given circuit is attached in the figure
    'Part (a) System of Equations derivation.png'. Below, we set up the matrix A for a general
    integer N, and then solve the system for N = 6 and N = 10**4.
"""

# Defining the constant V_plus
V_plus = 5 # in V

def A_gen(n):
    """
        This method generates the matrix A modelling the circuit given in the problem, 
        for a given value of n. 
    """
    A = np.zeros((n, n))
    for i in range(1, n - 1):
        A[i, i - 1] = -1
        A[i, i] = 4
        A[i, i + 1] = -1
        if (i == 1) is False:
            A[i, i - 2] = -1
        if (i == n - 2) is False:
            A[i, i + 2] = -1
    
    A[0, 0] = 3
    A[0, 1] = -1
    A[0, 2] = -1
    
    A[-1, -1] = 3
    A[-1, -2] = -1
    A[-1, -3] = -1
    
    return A

# Part (b): Solving for n = 6
n = 6

A = A_gen(n)        
w = np.zeros(n)
w[0] = V_plus
w[1] = V_plus

V = Gaussian_Elim(A, w, banded = 2)
print("The solution to the given system is: ")
for i in range(0, n):
    print(f"\tV_{i + 1} = {np.round(V[i], 5)} V")
    
# Part (c)
"""
    The method Gaussian_Elim() has already been modified to incorporate banded calculations,
    if the user wishes to do so.
"""

n = 10**4

A = A_gen(n)        
w = np.zeros(n)
w[0] = V_plus
w[1] = V_plus

V = Gaussian_Elim(A, w, banded = 2)

file_out = open(r'Problem_14_Another_Circuit\potentials.txt', 'w')
# To prevent the program from writing out the result multiple times, we seek the position 0
# before writing the output
file_out.seek(0)

file_out.write("The solution to the given system is: \n")
for i in range(0, n):
    file_out.write(f"\tV_{i + 1} = {np.round(V[i], 5)} V\n")
    
file_out.close()
print(f"\nThe minimum obtained voltage for this circuit is: {min(V)} V")
print(f"The maximum obtained voltage for this circuit is: {max(V)} V")