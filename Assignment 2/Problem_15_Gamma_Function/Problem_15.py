import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

from math import factorial

import sys
sys.path.insert(0, '.')
from gaussxw import gaussxwab

"""
    In the first part, we plot the graphs of the integrand for x in 0 to 5, with a = 2, 3, and 4.
    The plot is stored in the figure "Plot of Integrand for various a's.png". Next, we have
    shown that the integrand attains a maxima at x = a - 1. The detailed derivation is given
    in the figure "Maxima of f.png". Finally, before implementing the Gamma function method,
    we talk about the change of variables and overflow issues in the figures 
    "Change of vars.png", and "Overflow Issues.png" respectively. 
    
    The integrand used below is the expression after the change of variables discussed in 
    part (c) has been implemented. The detailed derivation of this expression is given in
    the figure "Integral after change of vars.png".
"""

# Part (a)
x = np.linspace(0, 5, 1000)

def f(x, a):
    return x**(a - 1) * np.exp(-x)

y_2 = f(x, 2)
y_3 = f(x, 3)
y_4 = f(x, 4)

plt.plot(x, y_2, label = "a = 2")
plt.plot(x, y_3, label = "a = 3")
plt.plot(x, y_4, label = "a = 4")
plt.axhline(linewidth = 1, color='k')
plt.axvline(linewidth = 1, color='k')
plt.legend()
plt.title("Plot showing the integrand for various values of a")

plt.xticks(np.linspace(0, 5, 6))
plt.yticks(np.linspace(0, 1.5, 7))
plt.show()

# Part (e)
def Gamma(a):
    z, w = gaussxwab(100, 0, 1)
    def f(z):
        x = (a - 1) * z / (1 - z)
        return np.exp((a - 1) * np.log(x) - x) * ( (a - 1)/(1 - z) + (a - 1) * z/(1 - z)**2 )
    return np.sum(w * f(z))

print(f"The calculated value of Gamma(3/2) is: {Gamma(1.5)}")
print(f"The known value of Gamma(3/2) = sqrt(pi)/2 is: {np.sqrt(np.pi) / 2}")

# Part (f)
print(f"\nThe value of Gamma(a = 3) is: {Gamma(3)}")
print(f"The value of (a - 1)! is: 2! = {factorial(2)}")

print(f"\nThe value of Gamma(a = 6) is: {Gamma(6)}")
print(f"The value of (a - 1)! is: 5! = {factorial(5)}")

print(f"\nThe value of Gamma(a = 10) is: {Gamma(10)}")
print(f"The value of (a - 1)! is: 9! = {factorial(9)}")