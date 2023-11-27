import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Quantum_Harmonic_Oscillator import psi
from gaussxw import gaussxwab

"""
    From the first part, we see that the wavefunction almost vanishes for |x| > 5. Thus, we set
    the lower and upper bound of the integral as $\pm$ 10, and apply the gaussin quadrature to 
    evaluvate the integral.
"""

X = np.linspace(-15, 15, 1000)
y = np.zeros(1000)
n = 5
for x in X:
    y[X == x] = psi(n, x)

plt.plot(X, x**2 * y**2, label = "State with n = 5")
plt.axhline(y = 0, c = 'k', linewidth = 0.5)
plt.axvline(x = 0, c = 'k', linewidth = 0.5)
plt.xlabel("x")
plt.ylabel("$\psi_n(x)$")
plt.title("Plot showing Integrand in the interval $|x| < 15$")
plt.legend()
plt.show()

def uncertainty(n):
    X, w = gaussxwab(100, -10, 10)
    integrand = np.zeros(100)
    for x in X:
        integrand[X == x] = x**2 * psi(n, x)**2
    return np.sqrt( np.sum(w * integrand) )

print(f"The uncertainty of x**2 in the state n = 5 is: {uncertainty(5)}")