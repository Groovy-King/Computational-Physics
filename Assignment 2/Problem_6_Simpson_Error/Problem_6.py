import numpy as np

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import Simpson_Error

"""
    The explanation for obtaining the error term is attached in this folder as "Error term.png".
    The following program calculates the error as described in the question. The method 
    Simpson_error() from the file Integration.py, implements the argument presented in the image 
    mentioned above.
"""

def f(x):
    return x**4 - 2*x + 1

e, I_1, I_2 = Simpson_Error(f, 0, 2, 10)
print(f"The value of the Integral is: {I_2}")
print(f"The error in the Simpson integral is: {abs(e)}")
print(f"The error found by subtraction from true value is: {abs(4.4 - I_2)}")