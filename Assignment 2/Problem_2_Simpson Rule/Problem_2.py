import numpy as np

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int

"""
    We use the composite Simpson rule to integrate the given function x**4 - 2*x + 1 between 
    x = 0 and x = 2. First, we create a numpy array of given x-values, and then use the function 
    num_int() to calculate the value of the integral. 
"""

n = int(input("Enter the number of slices: "))
x = np.linspace(0, 2, n + 1) # To get n slices, we use n + 1 points in the x-array

y = x**4 - 2*x + 1

int_value_trap = num_int(x, y)
int_value_simp = num_int(x, y, method = 'Simpson')
print(f"The value of the integral (Simpson's method), using {n} slices is: {int_value_simp}")
print(f"The fractional error from the analytically obtained value is: {abs(4.4 - int_value_simp) / 4.4}")
print(f"\nThe value of the integral (Trapezoid method), using {n} slices is: {int_value_trap}")