import numpy as np
import cmath as cm
from numpy.fft import rfft2, irfft2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import sys

#sns.set_style('darkgrid')
sys.path.insert(0, '.')

data = np.loadtxt(r'blur.txt')

nx, ny = data.shape
x = np.arange(0, nx)
y = np.arange(ny, 0, -1)

xv, yv = np.meshgrid(x, y)

plt.grid(False)
plt.pcolormesh(xv, yv, -data, cmap = 'Greys')
plt.xticks([])
plt.yticks([])
plt.title("Blurred Image before Deconvolution")
plt.show()


# Defining the preset variance of the gaussian
sigma = 25

def f(x, y):
    """
        Returns the gaussian point spread function for values in the range 0 < x < K,
        0 < y < L. We assume that the function obeys the form given in the problem for the
        range -K/2 < x < K/2, and -L/2 < y < L/2.
    """
    if (x < nx/2):
        temp_x = x
    else:
        temp_x = x - nx
    
    if (y < ny/2):
        temp_y = y
    else:
        temp_y = y - ny
        
    return np.exp( -(temp_x**2 + temp_y**2) / (2 * sigma**2) )

spread = np.empty(data.shape)

for i in range(0, nx):
    for j in range(0, ny):
        spread[i, j] = f(x[i], y[j])

plt.grid(False)
plt.pcolormesh(xv, yv, -spread, cmap = 'Greys')
plt.xticks([])
plt.yticks([])
plt.title("Gaussian Point Spread function")
plt.show()

data_spectrum = rfft2(data)
spread_spectrum = rfft2(spread)

e_max = 10**(-3)
new_sprectrum = np.empty(data_spectrum.shape, dtype = complex)
for i in range(0, data_spectrum.shape[0]):
    for j in range(0, data_spectrum.shape[1]):
        if spread_spectrum[i, j] <= e_max:
            new_sprectrum[i, j] = data_spectrum[i, j] / (nx * ny)
        else:
            new_sprectrum[i, j] = data_spectrum[i, j] / (nx * ny * spread_spectrum[i, j])

unblur_data = irfft2(new_sprectrum)

plt.grid(False)
plt.pcolormesh(xv, yv, -unblur_data, cmap = 'binary')
plt.xticks([])
plt.yticks([])
plt.title("Unblurred Image after Deconvolution")
plt.show()