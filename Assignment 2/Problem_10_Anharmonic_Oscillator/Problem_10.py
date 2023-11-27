import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from gaussxw import gaussxwab

"""
    We have: E = 1/2 m (dx/dt)**2 + V(x). This gives us:
        dx/dt = sqrt( 2*(E - V(x)) / m )
    Integrating this eqn. from t = 0 to t = T/4 gives:
        T/4 = int( sqrt( m / (2 * (E - V(x))) ), (x, 0, a) )
    The above equation gives us the expression for the time period T, as asked in part (a).
"""

# The foloowing program gives the time period for the potential V = x**4, for amplitude a.
N = 20
def Timeperiod(a):
    x, w = gaussxwab(N, 0, a)
    T = 4 * np.sum( np.sqrt( 1 / (2*(a**4 - x**4)) ) * w )
    return T

a = np.linspace(0, 2, 200)
T = np.zeros(200)
for i in range(0, 200):
    T[i] = Timeperiod(a[i])

plt.plot(a, T)
plt.xlabel("Amplitude")
plt.ylabel("Time Period")
plt.title("Plot showing Time Period vs Amplitude")
plt.show()