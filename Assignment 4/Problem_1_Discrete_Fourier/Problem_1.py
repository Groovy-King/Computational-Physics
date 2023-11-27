import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

"""
    We use the np.fft method fft() to calculate the DFT of the given functions and plot them.
"""

# Defining the number of points N
N = 10**3

# Part (a) - Square wave
# For a single cycle of the square wave, 
#   yn = -1/2 for 0 <= n < N/2
#      = 1/2 for N/2 <= n < N

xn = np.linspace(0, 1, N, endpoint = False)
yn = np.empty(N)
for i in range(0, N):
    if i < N/2:
        yn[i] = -1/2
    else:
        yn[i] = 1/2

spectrum = fft(yn)
freq = fftfreq(N)

fig = plt.figure(layout = 'constrained', frameon = False)

fig.add_subplot(211)
plt.plot(xn, yn)
plt.xlabel(r'$x/L$')
plt.ylabel('$y(x)$')
plt.title('Square Wave Cycle')

fig.add_subplot(212)
plt.plot(freq, abs(spectrum))
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform')
plt.show()


# Part (b) - Sawtooth Wave
# Given: yn = n

xn = np.linspace(0, 1, N, endpoint = False)
yn = np.empty(N)
for i in range(0, N):
    yn[i] = i + 1

spectrum = fft(yn)
freq = fftfreq(N)

fig = plt.figure(layout = 'constrained', frameon = False)

fig.add_subplot(211)
plt.plot(xn, yn)
plt.xlabel(r'$x/L$')
plt.ylabel('$y(x)$')
plt.title('Saw tooth Wave')

fig.add_subplot(212)
plt.plot(freq, abs(spectrum))
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform')
plt.show()


# Part (c) - Modulated Sine Wave
# Given: yn = sin(pi*n/N) * sin(20*pi*n/N)

xn = np.linspace(0, 1, N, endpoint = False)
yn = np.empty(N)
for i in range(0, N):
    yn[i] = np.sin(np.pi * i / N) * np.sin(20 * np.pi * i / N)

spectrum = fft(yn)
freq = fftfreq(N)

fig = plt.figure(layout = 'constrained', frameon = False)

fig.add_subplot(211)
plt.plot(xn, yn)
plt.xlabel(r'$x/L$')
plt.ylabel('$y(x)$')
plt.title('Modulated Sine wave')

fig.add_subplot(212)
plt.plot(freq, abs(spectrum))
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform')
plt.show()