import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var, Runge_kutta_Adaptive_step

# Defining the relevant parameters
sigma = 10
r = 28
b = 8/3

# Let v be the vector that represents (x, y, z)
def dxdt(t, v):
    x, y, z = v
    return sigma*(y - x)

def dydt(t, v):
    x, y, z = v
    return r*x - y - x*z

def dzdt(t, v):
    x, y, z = v
    return x*y - b*z

time, solution = Runge_Kutta_multi_var([dxdt, dydt, dzdt], x0 = 0, y0 = np.array([0, 1, 0]), x_min = 0, x_max = 50, h = 0.01)
#time, solution, p = Runge_kutta_Adaptive_step([dxdt, dydt, dzdt], x0 = 0, y0 = np.array([0, 1, 0]), xmin = 0, xmax = 50, emax = 0.02, h0 = 0.01)

plt.plot(time, solution[1])
plt.title("Integrated solution of Lorentz Equations")
plt.xlabel("Time")
plt.ylabel("y")
plt.show()

plt.plot(solution[0], solution[2])
plt.title("Plot of z vs x from solutions of Lorentz equations")
plt.xlabel("x")
plt.ylabel("z")
plt.show()