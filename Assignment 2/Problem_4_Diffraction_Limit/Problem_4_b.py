import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int

"""
    This program generates a density plot showing the diffraction pattern due to a point source.
    We assume that along both the x- and y-axes, 1 unit corresponds to 1 micrometer.
"""

l = 0.5 # Wavelength of light
k = 2 * np.pi / l

# Pasting the code of J(m, x) from part (a)
n = 1000
def J(m, x):
    theta_arr = np.linspace(0, np.pi, n + 1) # To use n slices, we need n + 1 points
    y_arr = np.cos(m*theta_arr - x*np.sin(theta_arr))
    
    return num_int(theta_arr, y_arr, method = 'Simpson') / (np.pi)

m = 300
x = np.linspace(-1, 1, m)
y = np.linspace(-1, 1, m)

x_grid, y_grid = np.meshgrid(x, y)
brightness = np.zeros((m, m))

for i in np.arange(0, m):
    for j in np.arange(0, m):
        r = np.sqrt(x_grid[i][j]**2 + y_grid[i][j]**2)
        if r == 0:
            brightness[j][i] == 1/4
        else:
            brightness[j][i] = ( J(1, k*r) / (k*r) )**2

plt.pcolormesh(x_grid, y_grid, brightness, vmax = 0.01)
plt.show()