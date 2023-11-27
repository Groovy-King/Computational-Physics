import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
import seaborn as sns
sns.set_style('darkgrid')

x = smp.symbols('x')
p_x = 924 * x**6 - 2772 * x**5 + 3150 * x**4 - 1680 * x**3 + 420 * x**2 - 42 * x + 1
p_num = smp.lambdify(x, p_x)

x_plot = np.linspace(0, 1, 1000)
y_plot = p_num(x_plot)

plt.plot(x_plot, y_plot)
plt.axhline(y = 0, xmin = 0, xmax = 1, c = 'r')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Plot showing the polynomial in the domain $0 \leq x \leq 1$')
plt.show()

"""
    From the above plot, we eyeball the approximate value of the roots to find our initial Guesses.
    We use the following values:
        0.05, 0.2, 0.4, 0.6, 0.8, 0.95
"""
# Importing the solver to implement Newton's method
import sys
sys.path.insert(0, '.')

from Import_Modules.Root_finder import Root_finder
# Setting the error tolerance to get accurate result upto 10 decimal places
e_max = 5 * 10**(-11)
# Setting the maximum number of iterations
N_max = 50

ini_guesses = [0.05, 0.2, 0.4, 0.6, 0.8, 0.95]

for ini in ini_guesses:
    x_root = Root_finder([x, p_x], ini, e_max = e_max, N_max = N_max, TOL_Parameter = 'Absolute',method = 'Newton', f_symbolic = True)
    print(f"The root near {ini} is {x_root}")