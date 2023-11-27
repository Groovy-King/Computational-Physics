from numpy.random import default_rng
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

"""
    The mean value of a function f inside a hyper cubical region is:
        <f> = (1 / L**n)  * integral(f)
    where L is the length of the hypercube, and n is the number of dimensions (L**n is the 
    hypervolume of the region). We use this expression to approximate integral(f).
"""

# The following function determines if the point x lies inside or outside the hypersphere
def f(x):
    r = np.sum(x**2)
    if r < 1:
        return 1
    else:
        return 0

n_max = 10**6
d = 10

random_points = rng.uniform(low = -1, high = 1, size = (n_max, d))

f_vals = np.array([f(x) for x in random_points])
f_avg = np.sum(f_vals) / n_max

I = 2**d * f_avg

print(f"The Volume of {d}-dimensional unit hypersphere, obtained by Monte Carlo Integration is: {I}")

V_std = np.pi**(d/2) / (math.gamma(d/2 + 1))
print(f"The standard value of Volume of {d}-dimensional unit hypersphere is: {V_std}")
