import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '.')
from Import_Modules.Electrostatics_of_a_Dipole import Potential

"""
    We first define a method Potential() to calculate the potential at point (x, y, z) due to
    the point charges givem. Then, we use the function pcolormesh() to create a density plot
    of the potential in the x-y plane. We also make a 3D surface plot of the potential for
    easier visualisation. Next, we calculate the Electric field by calculatig the gradient of 
    the potential.
    
    The method Potential is defined in the file "Electrostatic_of_a_Dipole.py", saved in the 
    Import_Modules folder.
"""

n = 101    
x = np.linspace(-0.5, 0.5, n)
y = np.copy(x)

xv, yv = np.meshgrid(x, y, indexing = 'ij')
Potential_val = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        Potential_val[i][j] = Potential(x[i], y[j], 0)

maximum = 0.0
for i in range(0, n):
    if maximum <= max(abs(Potential_val[i])):
        maximum = max(abs(Potential_val[i]))

Potential_val = Potential_val / maximum

# The 3D Plot has a singularity at the location of the point charges. 
# Use n = 100 to obtain a better plot. The figure '(a) 3D Plot of Potential.png' uses n = 100.
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(xv, yv, Potential_val)
ax.set_title("Plot showing Potential of points in x-y plane")
plt.show()

fig2 = plt.figure
plt.pcolormesh(xv, yv, Potential_val, vmax = 10**(-17), vmin = -10**(-17))
plt.colorbar()
plt.title("Color map showing Potential in the x-y plane")
plt.xlabel("x (in m)")
plt.ylabel("y (in m)")
plt.show()