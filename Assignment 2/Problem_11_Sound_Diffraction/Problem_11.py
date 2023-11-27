import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from gaussxw import gaussxwab

"""
    This program computes the intensity of sound at different points as it gets diffracted around 
    the straight edge of a tower. Here, we assume that the wavelength is 1 m, and make a plot of the 
    intensity at z = 3 m from the edge of the building.
"""

l = 1
z = 3
N = 50

def Rel_intensity(x):
    u = np.sqrt(2 / (l*z)) * x
    y, w = gaussxwab(N, 0, u)
    C = np.sum(w * np.cos(np.pi * y**2 / 2))
    S = np.sum(w * np.sin(np.pi * y**2 / 2))
    return ( (2*C + 1)**2 + (2*S + 1)**2 ) / 8

x = np.linspace(-5, 5, 500)
I = np.ones(500)

for i in range(0, 500):
    I[i] = Rel_intensity(x[i])

plt.plot(x, I)
plt.xlabel("x")
plt.ylabel("Relative Intensity")
plt.title("Plot showing intensity of diffracted sound")
plt.show()