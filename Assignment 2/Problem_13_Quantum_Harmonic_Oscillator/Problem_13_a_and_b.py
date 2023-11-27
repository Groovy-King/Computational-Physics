import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Quantum_Harmonic_Oscillator import psi

X = np.linspace(-4, 4, 1000)
for i in range(0, 4):
    y = np.zeros(1000)
    for x in X:
        y[X == x] = psi(i, x)
    plt.plot(X, y, label = f"State with n = {i}")
    
plt.axhline(y = 0, c = 'k', linewidth = 0.5)
plt.axvline(x = 0, c = 'k', linewidth = 0.5)
plt.xlabel("x")
plt.ylabel("$\psi_n(x)$")
plt.title("Plot showing wave-function of different states")
plt.legend()
plt.show()


# Part (b)
X = np.linspace(-10, 10, 1000)
y = np.zeros(1000)
n = 30
for x in X:
    y[X == x] = psi(n, x)

plt.plot(X, y, label = "State with n = 30")
plt.axhline(y = 0, c = 'k', linewidth = 0.5)
plt.axvline(x = 0, c = 'k', linewidth = 0.5)
plt.xlabel("x")
plt.ylabel("$\psi_n(x)$")
plt.title("Plot showing wave-function of state n = 30")
plt.legend()
plt.show()