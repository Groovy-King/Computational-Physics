import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int

"""
    We use the composite trapezoidal rule to integrate the velocity to obtain the displacement 
    as a function of time. We assume that the particle started at x = 0, when t = 0.
"""

data = pd.read_csv(r"velocities.txt", sep = '\t', header = None, names = ['Time', 'Velocity'])

T = data['Time']
V = data['Velocity']

n = len(T)
x = np.zeros(n)

for i in np.arange(1, n):
    x[i] = num_int(T[: i + 1], V[: i + 1])
    
plt.plot(T, V, c = 'b', label = 'Velocity')
plt.plot(T, x, c = 'k', label = 'Position')
plt.xlabel('t (in s)')
plt.title('Plot showing velocity and position together')
plt.legend()
plt.show()