import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int

"""
    We choose to use the Simpson method to obtain the values of E(x). To ensure that we can always use this method,
    we fix the number of slices to be an even integer, say n = 200, for all values of x. As seen before, the Simpson method
    gives a much better result than the Trapezoid method. So, this choice allows us to get fairly accurate values for all 
    values of x in 0 to 3. 
"""

h = 0.1
x = np.arange(0, 3 + h, h) # We pass in 3 + h istead of 3, so that 3 is also included in the x-array
n = 200

def E(x):
    x_arr = np.linspace(0, x, n + 1) # To get n slices, we need n + 1 points
    y_arr = np.exp(-x_arr**2)
    
    return num_int(x_arr, y_arr, method = 'Simpson')

y = np.zeros(len(x))
for i in np.arange(0, len(x)):
    y[i] = E(x[i])

# Part (b), plotting E(x) vs x
plt.plot(x, y)
plt.title('Graph of E(x)')
plt.show()