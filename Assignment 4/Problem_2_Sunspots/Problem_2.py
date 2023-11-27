import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

data = np.loadtxt(r'sunspots.txt')
time = data[:, 0]
number = data[:, 1]

plt.plot(time, number)
plt.axvline(1046, color = 'k', linewidth = 1.5, linestyle = '--')
plt.axvline(1181, color = 'k', linewidth = 1.5, linestyle = '--')
plt.xlabel('Month')
plt.ylabel('Number of Sunspots')
plt.title('Plot showwing number of sunspots and approximating Period')
plt.show()

# From the above figure, the rough period of the sunspots is 135 months.

# Part (b) - Implement fft
n = len(number)

spectrum = fft(number)
frequency = fftfreq(n)

# We mark the peat at non-zero frequency to highlight the local maxima in the spectrum
x0 = 0.0080
y0 = 2.03 * 10**9

plt.plot(frequency, abs(spectrum)**2)
plt.scatter([-x0, x0], [y0, y0], color = 'red', s = 15)
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform of Sunspot Numbers')
plt.show()

# Part (c)
"""
    From the above plot, we see that the approximate value of k at the local maxima is:
        k_max = 8 * 10**(-3)
    The corresponding time period of the sine wave would be:
        T = 1 / k_max 
    The following code prints out the time period calculated by the DFT method.
"""
print(f"The approximate time period obtained by DFT of the sunspot numbers is: {np.round(1 / x0)} months")