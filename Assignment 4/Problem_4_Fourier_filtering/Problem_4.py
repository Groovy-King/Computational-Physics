import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

# Part (a)
data = np.loadtxt(r'dow.txt')
n = len(data)
x_plot = np.arange(0, n)

plt.plot(x_plot, data)
plt.xlabel('Day')
plt.ylabel('Dow Jones Average')
plt.title('Plot showing the Dow Jones Industrial Average')
plt.show()

# Part (b)
spectrum = rfft(data)
m = len(spectrum)

# Part (c)
for i in range(m // 10,  m):
    spectrum[i] = 0
    
# Part (d)
data_1 = irfft(spectrum)

plt.plot(x_plot, data, color = 'blue', label = 'Given data')
plt.plot(x_plot, data_1, color = 'red', label = r'10% Fourier Co-efficients')
plt.xlabel('Day')
plt.ylabel('Dow Jones Average')
plt.title(r'Plot showing Fourier Smoothening with 10% Co-efficients')
plt.legend()
plt.show()

# Part (e) - 2% Non-zero coefficients
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


# Fourier Analysis of Square Wave
def f(x):
    n = int(2 * x)
    if n % 2 == 0:
        return 1
    else:
        return -1
    
x_plot = np.linspace(0, 5, 1000)
y_plot = np.empty(1000)
for i in range(0, 1000):
    y_plot[i] = f(x_plot[i])
    
plt.plot(x_plot, y_plot)
plt.title('Waveevform of the given square wave')
plt.show()

# As seen above, the square waveform is periodic with period 1. Thus, we only work in the interval
# 0 to 1 henceforth.

x_plot = np.linspace(0, 1, 1000)
y_plot = np.empty(1000)
for i in range(0, 1000):
    y_plot[i] = f(x_plot[i])
    
spectrum = rfft(y_plot)
m = len(spectrum)

for i in range(10,  m):
    spectrum[i] = 0
    
y_plot_new = irfft(spectrum)

plt.plot(x_plot, y_plot, color = 'blue', label = 'Given data')
plt.plot(x_plot, y_plot_new, color = 'red', label = r'10 non-zero Fourier Co-efficients')
plt.title(r'Plot showing Fourier Smoothening of Square Waveform')
plt.legend()
plt.show()