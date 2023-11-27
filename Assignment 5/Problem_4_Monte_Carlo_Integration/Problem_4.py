from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

# Part (a): Hit-or-miss method
# Defining the number of trials
n_max = 10**4
count = 0
# Area of the rectangle
A = 2

def f(x):
    return np.sin(1 / (x * (2 - x)))**2

for i in range(n_max):
    x = rng.uniform(low = 0, high = 2)
    y = rng.uniform(low = 0, high = 1)
    
    if y < f(x):
        count += 1
        
I_hit = count * A / n_max
print(f"The integral obtained by hit-or-miss method is: {I_hit}")

"""
    The expression for the error in hit-or-miss is derived in the lecture slides to be:
        sigma = sqrt(var k) * A / n_max = sqrt(I * (A - I)) / sqrt(N)
        
    Similarly, for the mean value method, the error is given by:
        sigma = (b - a) * sqrt(var f / N)
"""

e_hit = np.sqrt(I_hit * (A - I_hit) / n_max)
print(f"The error in hit-or-miss method is: {e_hit}")

# Part (b): Mean value method
# The integral is approximated as: I = <f> * (b - a)

x = rng.uniform(low = 0, high = 2, size = n_max)

f_vals = f(x)
f_avg = np.sum(f_vals) / n_max
I_mean = (2 - 0) * f_avg

print(f"\nThe integral obtained by mean value method is: {I_mean}")

f_sq = f(x)**2
var_f = np.sum(f_sq) / n_max - f_avg**2
e_mean = (2 - 0) * np.sqrt( var_f / n_max )
print(f"The error in mean value method is: {e_mean}")