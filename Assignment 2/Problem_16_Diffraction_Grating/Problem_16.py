import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')
from gaussxw import gaussxwab

"""
    The relation between alpha and the slit separation d is derived in the figure
    "Slit Visualization.png". The method q(u, d) returns the transmission function for slit
    separation d. We then apply the method Gaussian Quadrature to calculate the relative 
    intensity at various points on the screen, and create a density plot to model the observation.
"""

# Part (b), use d = 20 while calling the function
def q(u, d):
    # d is in micro meter
    alpha = np.pi / d
    return np.sin(alpha * u)**2
v_max = 0.1

# Part (e), various slit patterns
# Uncomment these definitions to get the different patterns
"""
def q(u, d):
    # d is in micro meter
    alpha = np.pi / d
    beta = alpha / 2
    return np.sin(alpha * u)**2 * np.sin(beta * u)**2
v_max = 0.1
"""

# Part (e).ii) The assumed slit pattern is shown in the 
# figure "Assumed Slit Pattern for Part e.ii.png"
"""
def q(u, d): # The extra argument d is just so that other parts of the code remain unchanged
    return np.piecewise(u, [u < -45, u >= -45, u >= -35, u >= 25, u >= 45], [0, 1, 0, 1, 0])
v_max = 1
"""

n = 10
# Number of slits
l = 0.5 
# Wavelength in micro meter
foc = 1
# Focal length in meters
d = 20
# Slit separation in micro meters
w = (n - 1) * d
# Total length of grating is number of separations times length of separation

# Defining the integrand
def f(u, x):
    j = complex(0, 1)
    return np.sqrt(q(u, d)) * cm.exp(2 * j * np.pi * x * u / (l * foc))

"""
    We use the method of Gaussian Quadrature to evaluvate the integral given in the problem.
    This method allows us to easily integrate accurately over any interval. Further, using 
    N = 100, allows us to get the exact result upto to the x**99 term in the Taylor expansion
    of the integrand, as discussed in a previous problem. Thus, I think this method is suitable
    for calculating the integral here.
"""
U, w = gaussxwab(100, -w/2, w/2)

# Defining the relative intensity at point x on the screen
def I(x):
    int_val = 0
    for u in U:
        int_val += w[U == u] * f(u, x)
        
    return abs(int_val)**2

X = np.linspace(-0.05, 0.05, 1500)
Brightness_1D = np.zeros(1500)
for i in range(0, 1500):
    Brightness_1D[i] = I(X[i])

# Normalizing the array
Brightness_1D = Brightness_1D / max(Brightness_1D)

plt.plot(X, Brightness_1D)
plt.xlabel("$x$")
plt.ylabel("Relative Intensity")
plt.title("Plot showing Relative Intensity as a function of x")
plt.show()
    
# Creating a 2-D lattice and assigning brightness values
Y = np.linspace(-1, 1, 100)

xv, yv = np.meshgrid(X, Y)
Brightness_2D = np.zeros((100, 1500))
for i in range(0, 100):
    Brightness_2D[i] = np.copy(Brightness_1D)

fig = plt.figure(figsize = (12, 0.8))

fig.add_subplot(111)
plt.pcolormesh(xv, yv, Brightness_2D, vmax = v_max)
plt.yticks([])
plt.show()