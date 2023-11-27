import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.path.insert(0, '.')
from Import_Modules.Grid_Differentiation import Derivative

# Part (a)
Data = np.loadtxt('altitude.txt')
nx, ny = Data.shape
h = 3 * 10**4

"""
    While calculating the derivative, we employ the method difference, since it gives a
    better approximation than the methods of forward and backward differences. However,
    at the end points, it is not possible to employ the method of central differences. Thus,
    at the left end, we use forward difference, while at the right end, we use backward difference
    to calculate the derivative. This method is defined in the file Grid_Differentiation.py, 
    stored in the folder Import_Modules.
"""
Der_x, Der_y = Derivative(Data, h)

# Part (b)
phi = np.pi / 4
Intensity = (np.cos(phi) * Der_x + np.sin(phi) * Der_y) / np.sqrt(Der_x**2 + Der_y**2 + 1)

x = np.linspace(1, -1, nx)
y = np.linspace(1, -1, ny)

plt.pcolormesh(-Intensity, cmap = 'Greys')
plt.title("3D Like Image of World Map")
plt.colorbar()
plt.show()