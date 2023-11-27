import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Fixed_point import fixed_point_multi_var

"""
    We compute the solution to the equation x = 1 - exp(-c*x) using the fixed point iteration
    method. Since the initial guess is not given, we use x0 = 1 (using x0 = 0 is trivial, as 0 
    is a solution). We solve the above system for various values of c, and plot the solutions
    as a function of c. The desired accuracy is given as 10**(-6), which is calculated as the 
    absolute error |x_{n+1} - x_{n}|.
"""
x0 = 1
e_max = 10**(-6)
c = 2

def rhs(x, c):
    return 1 - np.exp(-c * x)

x_root, i = fixed_point_multi_var(rhs, x0, e_max, args = [c])
print(f"The fixed point iteration algorithm converged in {i} iterations")
print(f"The root obtained for the case c = 2 is: {x_root}")
print(f"The value of the RHS at this point is: {rhs(x_root, c)}")

# Part (b)
c = np.arange(0, 3.001, 0.01)
x = np.zeros(len(c))

for i in range(0, len(c)):
    x[i] = fixed_point_multi_var(rhs, x0, e_max, args = [c[i]])[0]

plt.plot(c, x)
plt.xlabel('c')
plt.ylabel('x_solution')
plt.title('Plot showing the solution to the equation $x = 1 - e^{-cx}$')
plt.show()

"""
    To apply the acceleration, we rewrite the equation as:
        x + exp(-c*x) - 1 = 0
    We call the LHS g(x). Now, we apply the fixed point method on the equation:
        x = x + r*g(x)
    where r satisfies:
        1 + r*g'(x0) = 0
"""
x0 = 1
c = 2

# Computing Derivative of g(x)
def g_p(x, c):
    return 1 - c * np.exp(-c * x)

r0 = -1 / g_p(x0, c)

def rhs2(x, c):
    return x + r0 * (x + np.exp(-c * x) - 1)

x_root, i = fixed_point_multi_var(rhs2, x0, e_max, args = [c])
print(f"\nThe fixed point iteration algorithm converged in {i} iterations")
print(f"The root obtained for the case c = 2 is: {x_root}")
print(f"The value of the new RHS at this point is: {rhs2(x_root, c)}")