import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

import sys
sys.path.insert(0, '.')
from gaussxw import gaussxwab
from Import_Modules.Electrostatics_of_a_Dipole import Electric_Field

"""
    The expression for the potential has been derived in the figure 'Square Charge Derivation.png'
"""

q0 = 100 # C/m**2
L = 0.1
k = 1 / (4 * np.pi * epsilon_0)

def sigma(x, y, z):
    if (z == 0) is False:
        return 0
    return q0 * np.sin(2 * np.pi * x / L) * np.sin(2 * np.pi * y / L)

u, w = gaussxwab(20, -L/2, L/2)
n = len(u)

def Potential(x, y, z):
    V = 0
    for i in range(0, n):
        r = np.sqrt((x - u[i])**2 + (y - u)**2 + z**2)
        V += np.sum(k * w[i] * w * sigma(u[i], u, 0) / r)
    return V

m = 100
X = np.linspace(-0.5, 0.5, m)
Y = np.copy(X)
V = np.zeros((m, m))

for i in range (0, m):
    for j in range(0, m):
        V[j][i] = Potential(X[i], Y[j], 0)
        
xv, yv = np.meshgrid(X, Y)

maximum = 0
for i in range(0, m):
    if maximum <= max(V[i]):
        maximum = max(V[i])

V = V / maximum        

cutoff = 0.01
plt.pcolormesh(xv, yv, V, vmax = cutoff, vmin = -cutoff)
plt.title("Potential of Square Charge Distribution")
plt.colorbar()
plt.show()

E = np.zeros((m, m))
theta = np.copy(E)
h = 0.01
Ex = np.copy(E)
Ey = np.copy(E)
Ez = np.copy(E)

for i in range(0, m):
    for j in range(0, m):
        Ex[j][i], Ey[j][i], Ez[j][i] = Electric_Field(X[i], Y[j], 0, h, f = Potential)
        E[j][i] = np.sqrt(Ex[j][i]**2 + Ey[j][i]**2 + Ez[j][i]**2)
        theta[j][i] = np.arctan2(Ey[j][i], Ex[j][i])

maximum = 0.0
for i in range(0, n):
    if maximum <= max(abs(E[i])):
        maximum = max(abs(E[i]))

E = E / maximum

plt.pcolormesh(xv, yv, E, cmap = 'jet')
plt.title("Electric Field Magnitude on the xy plane")
plt.colorbar()
plt.show()

plt.pcolormesh(xv, yv, theta, cmap = 'hsv')
plt.title("Electric Field Direction on the xy plane")
plt.colorbar()
plt.show()

plt.streamplot(xv, yv, Ex, Ey)
plt.title("Visualizing Electric Field of Square Charge")
plt.show()