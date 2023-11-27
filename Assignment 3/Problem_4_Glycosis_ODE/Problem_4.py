import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.Fixed_point import fixed_point_multi_var

"""
    We solve for the values at the stationary point using fixed point iteration method.
    We set the maximum number of iterations to 50, and say that the algorithm doesn't 
    converge if it doesn't converge within 50 iterations. We use x = y = 1 as our initial
    guess, as nothing is mentioned.
"""
ini_guess = [1, 1]
a = 1
b = 2
n_max = 50
e_max = 10**(-6)

print(f"The analytical solution to the stationary point is:")
print(f"\t x = {b}")
print(f"\t y = {b / (a + b**2)}\n")

def rhs(X, a, b):
    x, y =  X
    return np.array([y * (a + b**2) , b / (a + x**2)])

x_root, i = fixed_point_multi_var(rhs, ini_guess, multi_var = True, args = [a, b], print_err = True, n_max = 100)

"""
    Rewriting the system as:
        x = b
        y = b / (a + x**2)
    leads to convergence of the fixed point method. We implement this below:
"""
def rhs(X, a, b):
    x, y =  X
    return np.array([b , b / (a + x**2)])

x_root, i = fixed_point_multi_var(rhs, ini_guess, multi_var = True, args = [a, b], print_err = True, n_max = 100)

print(f"\nThe program converged within {i} iterations!")
print(f"The root of the given system of equations is: {x_root}")