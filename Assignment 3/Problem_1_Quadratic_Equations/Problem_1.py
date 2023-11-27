import numpy as np

"""
    The following program calculates the roots of a Quadratic Equation using two mathematically
    equivalent expressions. However, the answers obtained are not identical due to machine 
    round-off errors, and can give significantly different results, as seen below.
    
    The last method uad_roots_accurate() calculates the roots using both methods, and prints
    the more accurate root.
"""

# Part (a)
def quad_roots(a, b, c):
    x1 = ( -b + np.sqrt(b**2 - 4 * a * c) ) / (2 * a)
    y1 = a * x1**2 + b * x1 + c
    x2 = ( -b - np.sqrt(b**2 - 4 * a * c) ) / (2 * a)
    y2 = a * x2**2 + b * x2 + c
    return (x1, x2, y1, y2)

x1, x2, y1, y2 = quad_roots(0.001, 1000, 0.001)
print(f"The roots of the equation 0.001x**2 + 1000x + 0.001 = 0 are: {x1} and {x2}")
print(f"The value of the function at these points is:")
print(f"\t f(x1) = {y1}")
print(f"\t f(x2) = {y2}")

# Part (b)
def quad_roots_rationalized(a, b, c):
    x1 = 2 * c / (-b - np.sqrt(b**2 - 4 * a * c))
    y1 = a * x1**2 + b * x1 + c
    x2 = 2 * c / (-b + np.sqrt(b**2 - 4 * a * c))
    y2 = a * x2**2 + b * x2 + c
    return (x1, x2, y1, y2)
    
x1, x2, y1, y2 = quad_roots_rationalized(0.001, 1000, 0.001)
print(f"\nThe roots of the equation 0.001x**2 + 1000x + 0.001 = 0, obtained by the rationalised expression, are: {x1} and {x2}")
print(f"The value of the function at these points is:")
print(f"\t f(x1) = {y1}")
print(f"\t f(x2) = {y2}")

# Part (c)
def quad_roots_accurate(a, b, c):
    x1, x2, y1, y2 = quad_roots(a, b, c)
    x1_r, x2_r, y1_r, y2_r = quad_roots_rationalized(a, b, c)
    if abs(y1) < abs(y1_r):
        x_out_1 = x1
        y_out_1 = y1
    else:
        x_out_1 = x1_r
        y_out_1 = y1_r
    
    if abs(y2) < abs(y2_r):
        x_out_2 = x2
        y_out_2 = y2
    else:
        x_out_2 = x2_r
        y_out_2 = y2_r
    
    return (x_out_1, x_out_2, y_out_1, y_out_2)

x1, x2, y1, y2 = quad_roots_accurate(0.001, 1000, 0.001)
print(f"\nThe roots of the equation 0.001x**2 + 1000x + 0.001 = 0, obtained by the more accurate method, are: {x1} and {x2}")
print(f"The value of the function at these points is:")
print(f"\t f(x1) = {y1}")
print(f"\t f(x2) = {y2}")