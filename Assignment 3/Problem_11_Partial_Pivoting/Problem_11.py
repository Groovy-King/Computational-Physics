import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.Gaussian_Elimination import Gaussian_Elim

"""
    The method Gaussian_Elim() that has been imported above has already been
    modified to implement partial pivoting as well. The argument pivoting can be changed
    when the method is called to decide whether pivoting is applied or not.
"""

# Part (a)
# We copy the relevant code from Problem_10.py here
# Defining the relevant constant
V_plus = 5.0 # in V

# Defining the Matrix A in the system Ax = b
A = np.array([[4, -1, -1, -1],
             [-1, 3, 0, -1],
             [-1, 0, 3, -1],
             [-1, -1, -1, 4]], float)

# Defning the vector b
b = np.array([V_plus, 0, V_plus, 0], float)


# Here, we call the method with the extra argument pivoting = 'Partial'
V = Gaussian_Elim(A, b, pivoting = 'Partial')
print("The solution to the system given in Problem 10 is (with partial pivoting):")
for i in range(0, 4):
    print(f"\tV{i + 1} = {V[i]} V")
"""
    It is clearly seen that the output here matches the one in Problem_10_Output.txt
"""

      
# Part (b)
# Defining the new matrix A
A = np.array([[0, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)

# Defning the new vector b
b = np.array([-4, 3, 9, 7], float)

print("\n\nThe given system is Ax = b, with:")
print("A = ")
print(A)
print("\nb = ")
print(b)

# Uncomment this part of the code to run  without pivoting
# This part is currently commented, as it leads to errors
# The output from this part is saved in Problem_11_Output.txt
"""
# Solving the system without pivoting
x = Gaussian_Elim(A, b, pivoting = 'None')
print("The solution to the given system is (with no pivoting):")
for i in range(0, 4):
    print(f"\tx{i + 1} = {x[i]} ")
"""

# Solving the system with partial pivoting
x = Gaussian_Elim(A, b, pivoting = 'Partial')
print("\nThe solution to the given system is (with partial pivoting):")
for i in range(0, 4):
    print(f"\tx{i + 1} = {x[i]}")

    
# To verify the solution, we check the value of Ax - b
check = np.matrix(A) * np.matrix(x).T - np.matrix(b).T
print("\nThe vector Ax - b is:")
print(check)