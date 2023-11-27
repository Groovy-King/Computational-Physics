import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var

# Defining the relevant parameters
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

def rabbit_growth(t, population):
    rabbit, fox = population
    return alpha*rabbit - beta*rabbit*fox

def fox_growth(t, population):
    rabbit, fox = population
    return gamma*rabbit*fox - delta*fox

time, population = Runge_Kutta_multi_var([rabbit_growth, fox_growth], x0 = 0, y0 = np.array([2, 2]), x_min = 0, x_max = 30, h = 0.01)

plt.plot(time, population[0], label = "rabbit")
plt.plot(time, population[1], label = "fox")
plt.xlabel("Time")
plt.ylabel("Population (in thousands)")
plt.title("Plot showing the integrated solution of the Lotka-Volterra model")
plt.legend()
plt.show()