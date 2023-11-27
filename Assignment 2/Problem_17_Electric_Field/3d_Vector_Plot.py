from vpython import *
import numpy as np
from scipy.constants import epsilon_0

k = 1 / (4 * np.pi * epsilon_0)
Q_Plus = sphere(pos = vector(0.05, 0, 0), radius = 0.01, color = color.red)
Q_Minus = sphere(pos = vector(-0.05, 0, 0), radius = 0.01, color = color.blue)

x = np.linspace(-0.5, 0.5, 11)
y = np.copy(x)

Q_Plus.q = 1
Q_Minus.q = -1

r = 0.1
theta = 0
N_theta = 12
dtheta = 2 * np.pi / N_theta

while theta <= 2 * np.pi:
    r0 = r * vector(np.cos(theta), np.sin(theta), 0)
    r_Plus = r0 - Q_Plus.pos
    r_Minus = r0 - Q_Minus.pos

    E_Plus = k * Q_Plus.q * r_Plus / mag(r_Plus)**3
    E_Minus = k * Q_Minus.q * r_Minus / mag(r_Minus)**3
    E = E_Plus + E_Minus

    E_Scale = 10**(-14)
    E_Arrow = arrow(pos = r0, axis = E_Scale * E, round = True)
    theta += dtheta

# Plotting in the x-z plane
theta = 0    
while theta <= 2 * np.pi:
    r0 = r * vector(np.cos(theta), 0, np.sin(theta))
    r_Plus = r0 - Q_Plus.pos
    r_Minus = r0 - Q_Minus.pos

    E_Plus = k * Q_Plus.q * r_Plus / mag(r_Plus)**3
    E_Minus = k * Q_Minus.q * r_Minus / mag(r_Minus)**3
    E = E_Plus + E_Minus

    E_Scale = 10**(-14)
    E_Arrow = arrow(pos = r0, axis = E_Scale * E, round = True)
    theta += dtheta
    
# Plotting a second layer of vectors
r = 0.2
N_theta = 16
while theta <= 2 * np.pi:
    r0 = r * vector(np.cos(theta), np.sin(theta), 0)
    r_Plus = r0 - Q_Plus.pos
    r_Minus = r0 - Q_Minus.pos

    E_Plus = k * Q_Plus.q * r_Plus / mag(r_Plus)**3
    E_Minus = k * Q_Minus.q * r_Minus / mag(r_Minus)**3
    E = E_Plus + E_Minus

    E_Scale = 5 * 10**(-14) # Scale changed for visibility
    E_Arrow = arrow(pos = r0, axis = E_Scale * E, round = True)
    theta += dtheta

# Plotting in the x-z plane
theta = 0    
while theta <= 2 * np.pi:
    r0 = r * vector(np.cos(theta), 0, np.sin(theta))
    r_Plus = r0 - Q_Plus.pos
    r_Minus = r0 - Q_Minus.pos

    E_Plus = k * Q_Plus.q * r_Plus / mag(r_Plus)**3
    E_Minus = k * Q_Minus.q * r_Minus / mag(r_Minus)**3
    E = E_Plus + E_Minus

    E_Scale = 5 * 10**(-14) # Scale changed for visibility
    E_Arrow = arrow(pos = r0, axis = E_Scale * E, round = True)
    theta += dtheta