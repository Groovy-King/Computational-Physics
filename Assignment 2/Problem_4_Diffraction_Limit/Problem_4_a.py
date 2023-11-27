import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int

"""
    This program calculates the Besself function J(m, x), using the method num_int().
"""

# Part (a)
n = 1000
def J(m, x):
    theta_arr = np.linspace(0, np.pi, n + 1) # To use n slices, we need n + 1 points
    y_arr = np.cos(m*theta_arr - x*np.sin(theta_arr))
    
    return num_int(theta_arr, y_arr, method = 'Simpson') / (np.pi)

x = np.linspace(0, 20, 1000)

y_0 = np.zeros(1000)
y_1 = np.zeros(1000)
y_2 = np.zeros(1000)

for i in np.arange(0, 1000):
    y_0[i] = J(0, x[i])
    y_1[i] = J(1, x[i])
    y_2[i] = J(2, x[i])
    
plt.plot(x, y_0, label = 'J(0, x)')
plt.plot(x, y_1, label = 'J(1, x)')
plt.plot(x, y_2, label = 'J(2, x)')
plt.legend()
plt.title('Plot showing different Bessel Functions')
plt.show()