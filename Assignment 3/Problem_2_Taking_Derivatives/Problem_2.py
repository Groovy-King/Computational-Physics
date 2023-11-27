import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

"""
    The following program calculates the derivative of the function 
        f(x) = x * (x - 1) = x**2 - x
    by first computing the forward difference with the limit d -> 0. Then, we compare the
    obtained result to the analytic value, calculated using f'(x) = 2*x - 1.
    
    Next, we take d to be smaller and smaller, and observe the accuracy of the results obtained.
"""

def f(x):
    return x * (x - 1)

def derivative(f, x, d):
    return ( f(x + d) - f(x) ) / d

# Part (a)
x = 1
d = 10**(-2)

der = derivative(f, x, d)
print(f"The value of the derivative is computed to be: {der}")
der_true = 2 * x - 1
print(f"The true value of the derivative is: {der_true}")
print(f"The difference between the computed and true value is: {abs(der - der_true)}\n")

# Part (b)
ind = np.arange(-4, -15, -2)
d = 10.0**( ind )

der = derivative(f, x, d)
for i in range(0, len(der)):
    print(f"The value of the derivative, computed using d = {d[i]} is: {der[i]}")

plt.scatter(np.log10(d), abs(der - der_true))
plt.xlabel('x')
plt.xlim(-15, -3)
plt.xticks(ind, ["$10^{-4}$", "$10^{-6}$", "$10^{-8}$", "$10^{-10}$", "$10^{-12}$", "$10^{-14}$"])
plt.ylabel('Error in Derivative')
plt.title("Plot showing Error in Computed Value for different values of d")
plt.show()