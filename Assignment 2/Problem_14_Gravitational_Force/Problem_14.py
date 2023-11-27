import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.constants import G
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from gaussxw import gaussxwab

"""
    The derivation of the expression to the force experienced by a test particle along the z-axis
    is given in the figure "Gravitational Force Derivation.png", stored in this folder.
    
    We use the method of Gaussian Quadrature to calculate the force experienced by the test mass, 
    by evaluvating the integral given in the problem.
"""

L = 10
M = 10 * 10**3 # Converting to kg
sigma = M / L**2
N_x = 100
N_y = 100

x, w_x = gaussxwab(N_x, -L/2, L/2)
y, w_y = gaussxwab(N_y, -L/2, L/2)

def Force_Grav(z):
    sum = 0.0
    for x_sum in x:
        for y_sum in y:
            sum += w_x[x == x_sum] * w_y[y == y_sum] * G * sigma * z / (x_sum**2 + y_sum**2 + z**2)**(3/2)
    
    return sum

m = 1000
z = np.linspace(0, 10, m)
F_z = np.zeros(m)
for i in range(0, m):
    F_z[i] = Force_Grav(z[i])

#plt.plot(z, F_z)
plt.scatter(z, F_z, s = 0.7) # Scatter Plot shows us the drop to zero clearly
plt.xlabel("$z$ (in m)")
plt.ylabel("$F_z$ (in N)")
plt.title("Plot depicting Force along z-axis vs distance z")
plt.show()
