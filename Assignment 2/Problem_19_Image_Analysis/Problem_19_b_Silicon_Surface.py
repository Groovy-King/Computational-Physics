import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.path.insert(0, '.')
from Import_Modules.Grid_Differentiation import Derivative

Data = np.loadtxt("stm.txt")
nx, ny = Data.shape
h = 2.5

Der_x, Der_y = Derivative(Data, h)

# Part (b)
phi = np.pi / 4
Intensity = (np.cos(phi) * Der_x + np.sin(phi) * Der_y) / np.sqrt(Der_x**2 + Der_y**2 + 1)

x = np.linspace(1, -1, nx)
y = np.linspace(1, -1, ny)

plt.pcolormesh(-Intensity, cmap = 'binary')
plt.title("3D Like Image of Silicon Surface")
plt.colorbar()
plt.show()