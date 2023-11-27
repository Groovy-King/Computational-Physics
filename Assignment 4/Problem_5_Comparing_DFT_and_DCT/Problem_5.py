import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

from dcst import *

# Part (a)
data = np.loadtxt(r'dow2.txt')
n = len(data)
x_plot = np.arange(0, n)

plt.plot(x_plot, data)
plt.xlabel('Day')
plt.ylabel('Dow Jones Average')
plt.title('Plot showing the Dow Jones Industrial Average')
plt.show()

spectrum = rfft(data)
m = len(spectrum)

for i in range(m // 50,  m):
    spectrum[i] = 0
    
data_1 = irfft(spectrum)

plt.plot(x_plot, data, color = 'blue', label = 'Given data')
plt.plot(x_plot, data_1, color = 'red', label = r'2% Fourier Co-efficients')
plt.xlabel('Day')
plt.ylabel('Dow Jones Average')
plt.title(r'Plot showing Fourier Smoothening with 2% Co-efficients')
plt.legend()
plt.show()

# Implementing the DCT
spectrum = dct(data)
m = len(spectrum)

for i in range(m // 50,  m):
    spectrum[i] = 0
    
data_1 = idct(spectrum)

plt.plot(x_plot, data, color = 'blue', label = 'Given data')
plt.plot(x_plot, data_1, color = 'red', label = r'2% Fourier Cosine Coefficients')
plt.xlabel('Day')
plt.ylabel('Dow Jones Average')
plt.title(r'Plot showing Fourier Cosine Smoothening with 2% Co-efficients')
plt.legend()
plt.show()