import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k, c, sigma, hbar 
# Importing relevant constants to calculate Stefan Boltzmann constant
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from gaussxw import gaussxwab

"""
    The derivation of the expression of total power emitted by a black body of unit area is given
    in the figure "BlackBody Emission Derivation.png", attached in this folder. To evaluvate the
    integral given, we use the method of gaussian quadrature, with N = 100. Taylor expanding the 
    given expression, the gaussian quadrature method allows us to obtain the exact value of the 
    integral upto the x**99 term. Further, it is quite easy to integrate over any interval using
    this method, as it just a linear map between [a, b] to [-1, 1]. The analytic value of the 
    integral, as given by Mathematica is: (np.pi**4) / 15. We print both these values below for 
    comparison. 
    
    Also, since it is not possible to integrate to infinity numerically, we set an upper limit
    as high as possible, say x = 10**3, while preventing underflow/overflow errors. This is possible, as the 
    integrand in the given problem goes to zero as x goes to infinity. Thus, the contibution of 
    the interval [10**3, Inf] can be neglected.
"""

def f(x):
    return x**3 * np.exp(-x) / (1 - np.exp(-x))
       
# f(x) is defined this way to prevent overflow error while calling np.exp() at large x.

x, w = gaussxwab(100, 0, 1.5 * 10**3)
int_val = np.sum(w * f(x))
print(f"The value of the integral, by Gaussian Quadrature is: I = {int_val}")
print(f"Solving the integral analytically, using Mathematica, gives: I = {np.pi**4 / 15}")

# Part (c): Stefan Boltzmann Constant
sig = k**4 * int_val * c / (4 * np.pi**2 * (c * hbar)**3) 
# Written this way to prevent overflow/underflow
print(f"\nThe value of Stefan Boltzmann constant obtained is: {np.round(sig, 16)}")
print(f"The standard value this constant is: {sigma}")
print(f"\nThe relative error is: {abs(sigma - sig) / sigma}")
