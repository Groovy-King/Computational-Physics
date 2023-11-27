import numpy as np
from math import factorial

def Hermite_poly(n, x):
    if isinstance(n, int) is False:
        raise TypeError("Please enter an integer in the first argument")
    elif n < 0:
        raise ValueError("Order of Hermite Polynomial cannot be negative!")
    
    H_Poly = np.zeros(n + 1)
    H_Poly[0] = 1
    if n >= 1:
        H_Poly[1] = 2 * x
    if n >= 2:
        for i in range(2, n + 1):
            H_Poly[i] = 2 * x * H_Poly[i - 1] - 2 * (i - 1) * H_Poly[i - 2]
    return H_Poly[n]

def psi(n, x):
    return np.exp(- x**2 / 2) * Hermite_poly(n, x) / (np.sqrt(2**n) * np.sqrt(float(factorial(n))) * np.pi**(1/4))
