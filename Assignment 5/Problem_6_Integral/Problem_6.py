from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

"""
    The derivation for the results used below are given in the figure 'Part (a) Derivation.png' 
    and in 'Part (b) Integral Formula.png'.
    
    We note that since z = sqrt(x), and x lies between 0 and 1, z also lies between 0 and 1.
"""

n_max = 10**6
z = rng.uniform(low = 0, high = 1, size = n_max)
x = z**2

# Defining the function g(x) = f(x) / w(x)
def g(x):
    return 1 / (np.exp(x) + 1)

# Defning the integral of the weight function
# I_w = integral(x**(-1/2), 0, 1) = 2
I_w = 2

I = np.sum(g(x)) * I_w / n_max

print(f"The value of the integral, obtained by Monte Carlo method, is: {I}")