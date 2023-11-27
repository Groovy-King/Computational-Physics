from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

"""
    The Gaussian distribution with mean 0, and variance 1 is known as the normal distribution.
    We shall use this distribution to randomly generate the deltas given in the problem. For the
    exponential cooling scheme, we say that:
        T = T0 * exp(-t / tau)
    We calculate beta accordingly at each step, and use the value subsequently.
"""

def f(x):
    return x**2 - np.cos(4 * np.pi * x)

n_max = 10**5
def Simulated_Annealing(f, x0, T0, tau, sigma = 1, x_min = -10, x_max = 10):
    x = np.empty(n_max)
    x[0] = x0
    
    for i in range(n_max - 1):
        accept = 0
        T = T0 * np.exp(-i / tau)
        beta = 1 / T
        
        delta = rng.normal(loc = 0, scale = sigma)
        
        y_current = f(x[i])
        if (x[i] + delta > x_max) or (x[i] + delta < x_min):
            delta = -delta

        y_next = f(x[i] + delta)
        
        if y_next < y_current:
            accept = 1
        else:
            p = np.exp(-beta * (y_next - y_current))
            accept = rng.binomial(1, p)
        
        if accept == 1:
            x[i + 1] = x[i] + delta
        else:
            x[i + 1] = x[i]
        
    return  x

t = np.arange(n_max)
x0 = 2
T0 = 3
tau = n_max / 10

x = Simulated_Annealing(f, x0, T0, tau)

plt.plot(t, x, linestyle = 'dotted')
plt.title(f"Plot showing x vs t in Simulated Annealing")
plt.xlabel('Time')
plt.ylabel("x")
plt.show()

print("Part (a):")
print("-------------------")
print(f"The Minima of f(x) is obtained to be at: x = {x[-1]}")

# Part (b)
# Since x is in the range 0 to 50, our initial guess is around x0 = 25
x0 = 20
n_max = 10**6
tau = n_max / 8
t = np.arange(n_max)

from numpy import cos, sqrt

def g(x):
    return cos(x) + cos(sqrt(2) * x) + cos(sqrt(3) * x)

x_plot = np.linspace(0, 50, 1000)
y_plot = g(x_plot)

plt.plot(x_plot, y_plot)
plt.title("Plot of the more complicated function")
plt.show()

x = Simulated_Annealing(g, x0, T0, tau, sigma = 0.1, x_min = 0, x_max = 50)

plt.plot(t, x, linestyle = 'dotted')
plt.title(f"Plot showing x vs t in Simulated Annealing")
plt.xlabel('Time')
plt.ylabel("x")
plt.show()

print("\nPart (b):")
print("-------------------")
print(f"The Minima of g(x) is obtained to be at: x = {x[-1]}")