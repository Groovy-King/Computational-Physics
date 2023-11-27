import numpy as np
import cmath
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

"""
    We implement FFT by splitting the given data into two sub-arrays, the even and the odd
    terms. The equations outlining the algorithm implemented below is given in the figure
    'Explaining the Algorithm.png'
"""

# Defining the complex number j
j = 1j

# Defining my custom fft method using recursion
def my_fft(x):
    n = len(x)
    
    if n == 1:
        return x
    elif n % 2 == 1:
        raise ValueError('Length of data must be a power of 2!')
    else:
        even = my_fft(x[: : 2])
        odd = my_fft(x[1: : 2])
        
        """
            We use the idea of DFT for real functions discussed in class,
            and only evaluvate the values for 0 <= k <= n/2
            For the other values k', we have:
                c_k' = conjugate(c_{n - k'})
        """        
        spectrum = [0] * n
        for k in range(0, (n // 2)):
            spectrum[k] = even[k] + cmath.exp(-2 * j * np.pi * k / n) * odd[k]
            spectrum[k + (n // 2)] = even[k] - cmath.exp(-2 * j * np.pi * k / n) * odd[k]
        
        return np.array(spectrum)

data = np.loadtxt('pitch.txt')

x_plot = np.arange(0, len(data))

my_spectrum = my_fft(data)
spectrum = fft(data)
freq = fftfreq(len(data))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex = True)
fig.suptitle("Plots showing my FFT and Numpy's FFT")

ax1.plot(freq, abs(my_spectrum), color = 'red', label = 'My FFT Spectrum')
ax1.set_title('My FFT spectrum')

ax2.plot(freq, abs(spectrum), color = 'blue', label = 'Numpy FFT Spectrum')
ax2.set_title('Numpy FFT Spectrum')
ax2.set_xlabel('Frequency')

plt.show()      
        