import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '.')
from Import_Modules.Electrostatics_of_a_Dipole import Potential, Electric_Field

n = 101   
x = np.linspace(-0.5, 0.5, n)
y = np.copy(x)

xv, yv = np.meshgrid(x, y)
Potential_val = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        Potential_val[j][i] = Potential(x[i], y[j], 0)

h = x[1] - x[0]
E = np.zeros((n, n))
theta = np.copy(E) 
Ex = np.copy(E)
Ey = np.copy(E)
Ez = np.copy(E)       
for i in range(0, n):
    for j in range(0, n):
        # Calculating Partial Derivative using central difference
        # The method Electric_Field() is defined in the file Electrostatics_of_a_Dipole.py,
        # stored in the folder Import_Modules
        Ex[j][i], Ey[j][i], Ez[j][i] = Electric_Field(x[i], y[j], 0, h)
        theta[j][i] = np.arctan2(Ey[j][i], Ex[j][i])
        E[j][i] = np.sqrt(Ex[j][i]**2 + Ey[j][i]**2)

maximum = 0.0
for i in range(0, n):
    if maximum <= max(abs(E[i])):
        maximum = max(abs(E[i]))

E = E / maximum

plt.pcolormesh(xv, yv, E, cmap = 'jet', vmax = 0.05)
plt.title("Electric Field Magnitude on the xy plane")
plt.colorbar()
plt.show()

plt.pcolormesh(xv, yv, theta, cmap = 'hsv')
plt.title("Electric Field Direction on the xy plane")
plt.colorbar()
plt.show()

plt.streamplot(xv, yv, Ex, Ey)
plt.title("Visualizing Electric Field of Dipole")
plt.show()