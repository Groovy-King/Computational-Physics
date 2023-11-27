from scipy.constants import h, c, k, pi, Wien
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

"""
    The expression for the derivative dI/dl is given in the figure 'Derivative of I(l).png', which
    is computed using the library sympy. To calculate the wavelength of maximum intensity,
    we set the derivative equal to zero, and solve for l. This is implemented below.
"""

T = 1000
A = h * c / (k * T)

def I(x):
    return  2 * pi * h * c**2 * x**(-5) / (np.exp(A/x) - 1)

def f(x):
    sum1 = A * np.exp(A/x) / ( x**7 * (np.exp(A/x) - 1)**2 )
    sum2 = -5 / (x**6 * (np.exp(A/x) - 1))
    return 2 * pi * h * c**2 * (sum1 + sum2)

# Creates an array to denote the wavelengths in the interval 10 nm to 1 micrometer
x = np.linspace(10**(-7), 10**(-5), 1000)
y = I(x)

plt.plot(x, y)
plt.title("Plot showing I($\lambda$) vs $\lambda$")
plt.xlabel("$\lambda$")
plt.ylabel("I($\lambda$)")
plt.show()

y = f(x)

plt.plot(x, y)
plt.title("Plot showing dI($\lambda$)/d$\lambda$ vs $\lambda$")
plt.xlabel("\lambda")
plt.ylabel("dI($\lambda$)/d$\lambda$")
plt.show()

"""
    As is evident from both the above plots, the maxima of I lies between 2 and 4 micrometers.
    Thus, we apply the bisection method using this bracketing interval.
"""

import sys
sys.path.insert(0, '.')

from Import_Modules.Bisection_Method import bisection_method
x_min = 2 * 10**(-6)
x_max = 4 * 10**(-6)
e_max = 10**(-6)

root = bisection_method(f, x_min, x_max, e_max = e_max, TOL_Parameter = 'Relative')
Wien_approx = root * T
print(f"The maxima of I occurs at l_max = {root} m")
print(f"\nThe value of Wien's constant is: b = l_max T = {Wien_approx} K-m")
print(f"The standard value of Wien's constant is: b = {Wien} K-m")

# Part (b)
""" 
    The equation defining Wien's constant can be rearranged to give:
        T = b / l_max 
    We calculate the temperature of the Sun using this expression.
"""
l_Sun = 502 * 10**(-9)
T_Sun = Wien_approx / l_Sun

print(f"\nThe Temperature of the Sun's surface is: T_Sun = {T_Sun} K")
print(f"The standard value obtained from scientific literature is: T_Sun = 5778 K")