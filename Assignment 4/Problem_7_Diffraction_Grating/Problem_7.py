import numpy as np
import cmath as cm
from numpy.fft import fft
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

from gaussxw import gaussxwab

# Defining the relevant constants
d = 20 * 10**(-6) # in m
l = 500 * 10**(-9) # Wavelength in m
w = 2 * 10**(-4) # in m
W = 10 * w
f = 1 # in m
x_max = 5 * 10**(-2) # Screen limit in cm

# Defining the modified transmission function
def q(u):
    alpha = np.pi / d
    temp = np.sin(alpha * u)**2 
    return np.piecewise(u, [u <= 0, u <= w, u >= w], [0, temp, 0])

"""
    We expect around 400 points in the range -5 <= x_k <= 5, while using W = 10w. In the 
    following implementation, we only calculate the values for x >= 0, as k is non-negative. Thus,
    only k <= 200 gives points on the screen. I thus think using 500 points for the DFT would give
    acccurate results.
"""
n = 500
u = np.linspace(0, W, n)
y = np.empty(n)

for i in range(0, n):
    y[i] = np.sqrt( q(u[i]) )

c_k = fft(y)
I_k = W**2 * abs(c_k)**2 / n**2

n_max = int( W * x_max / (l * f) )
x_k = l * f * np.arange(0, n_max) / W

# Normalizing the array
I_k = I_k / max(I_k)

x_k = np.concatenate( (np.flipud(-x_k), x_k) )
I_k = np.concatenate( (np.flipud(I_k[: n_max]), I_k[: n_max]) )

"""
    The following section of the code is copied from the previous assignment's solution
"""
def q_new(u):
    alpha = np.pi / d
    return np.sin(alpha * u)**2 

# Defining the integrand
def F(u, x):
    j = complex(0, 1)
    return np.sqrt(q_new(u)) * cm.exp(2 * j * np.pi * x * u / (l * f))

U, w = gaussxwab(100, -w/2, w/2)

# Defining the relative intensity at point x on the screen
def I(x):
    int_val = 0
    for u in U:
        int_val += w[U == u] * F(u, x)
        
    return abs(int_val)**2

X = np.linspace(-0.05, 0.05, len(I_k))
Brightness_1D = np.zeros(len(I_k))
for i in range(0, len(I_k)):
    Brightness_1D[i] = I(X[i])

# Normalizing the array
Brightness_1D = Brightness_1D / max(Brightness_1D)
"""
    End of code taken from previous solution.
"""

fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 1]}, sharex = True)

ax1.plot(x_k, I_k)
ax1.set_ylabel("Relative Intensity")
ax1.set_title("Intensity plot obtained by FFT")

ax2.plot(X, Brightness_1D)
ax2.set_xlabel("$x$")
ax2.set_ylabel("Relative Intensity")
ax2.set_title("Plot obtained in previous assignment")

plt.show()

# Making an image of the obtained diffraction pattern
# Creating a 2-D lattice and assigning brightness values
Y = np.linspace(-1, 1, int(n / 15))

xv, yv = np.meshgrid(X, Y)
I_k2D = np.zeros((int(n / 15), len(I_k)))
for i in range(0, int(n / 15)):
    I_k2D[i] = np.copy(I_k)

fig, ax = plt.subplots(figsize = (12, 0.8))

ax.pcolormesh(xv, yv, I_k2D, vmax = 0.1)
ax.set_yticks([])

plt.show()