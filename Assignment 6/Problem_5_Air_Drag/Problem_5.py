import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var

"""
    The derivation of the expressions given in Part (a) is attached in the figure
    'Part (a) Derivation.png', saved in this folder. We use these expressions in our program below.
"""

# Defning the relevant parameters
C = 0.47
rho = 1.22 # in kg/m^3
R = 0.08 # in m
M = [0.25, 0.5, 1, 2, 4] # in kg
theta = np.pi/6 # 30 degrees converted to radians
v0 = 100 # in m/s 
g = 9.81 # in m/s^2

for m in M:
    # Let the list v represent [x, dxdt, y, dydt]
    # We define the derivatives of each of these quantities below
    def x_dot(t, v):
        return v[1] # x_dot is the same as dxdt

    def x_double_dot(t, v): # Using result from part (a)
        return - np.pi * R * rho * C * v[1] * np.sqrt(v[1]**2 + v[3]**2) / (2*m)
    
    def y_dot(t, v):
        return v[3] # y_dot is the same as dydt

    def y_double_dot(t, v): # Using result from part (a)
        return -g - np.pi * R * rho * C * v[3] * np.sqrt(v[1]**2 + v[3]**2) / (2*m)
    
    # We now have four first order ODEs, that we solve using Runge Kutta method
    # Without air drag, the ball reaches the ground again in time 2*v0*sin(theta)/g
    # Assuming the effects of air drag is small, we integrate upto time 2.5*v0*sin(theta)/g
    time, solution = Runge_Kutta_multi_var([x_dot, x_double_dot, y_dot, y_double_dot], x0 = 0, y0 = np.array([0, v0*np.cos(theta), 0,  v0*np.sin(theta)]), x_min = 0, x_max = 2.5*v0*np.sin(theta)/g, h = 0.01)
    
    plt.plot(solution[0], solution[2], label = f"Mass m = {m}")
    plt.plot(solution[0, -1], solution[2, -1], marker = 'o', markeredgecolor = 'black', markersize = 2)
    
    if m == 1:
        time2 = np.copy(time)
        solution2 = np.copy(solution)
    
plt.title("Plotting trajectories for different masses")
plt.xlabel("$x$ (in m)")
plt.ylabel("$y$ (in m)")
plt.legend()
plt.show()

plt.plot(solution2[0], solution2[2])
plt.title("Plotting trajectories of spherical cannonball with air drag")
plt.xlabel("$x$ (in m)")
plt.ylabel("$y$ (in m)")
plt.show()

    