import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var

"""
    The derivation of the expressions given in Part (a) is attached in the figures
    'Part (a) Derivation.png' and 'Part (a) Derivation Continued.png', saved in this folder. 
    We use these expressions in our program below.
"""

# Defning the relevant parameters
G = 1 # Specified units
L = 2
M = 10

# Let the list v represent [x, dxdt, y, dydt]
# We define the derivatives of each of these quantities below
def x_dot(t, v):
    return v[1] # x_dot is the same as dxdt

def x_double_dot(t, v): # Using result from part (a)
    return - G*M*v[0] / ((v[0]**2 + v[2]**2) * np.sqrt(v[0]**2 + v[2]**2 + L**2/4))

def y_dot(t, v):
    return v[3] # y_dot is the same as dydt

def y_double_dot(t, v): # Using result from part (a)
    return - G*M*v[2] / ((v[0]**2 + v[2]**2) * np.sqrt(v[0]**2 + v[2]**2 + L**2/4))

time, solution = Runge_Kutta_multi_var([x_dot, x_double_dot, y_dot, y_double_dot], x0 = 0, y0 = np.array([1, 0, 0, 1]), x_min = 0, x_max = 10, h = 0.01)


# For easier visualisation, we plot (roughyly) each revolution of the ball bearing in sequentially
# progressing colors. This makes the trajectory a bit more intutive to understand.

# We have calculated the position of the ball bearing at 2002 points. A quick plot shows
# us that there are roughly 8 revolutions in this time frame. We find afactor of 2002 that
# is closest to 8, which is 7. So we split up the plot into 7 different line segments and give
# each of them a sequential color, using the viridis color map.
linesegments = np.array([solution[0], solution[2]]).T.reshape(7, -1, 2)
cmap = cm.viridis(np.linspace(0, 0.75, linesegments.shape[0]))

line_collection = LineCollection(linesegments, colors = cmap, zorder = 3)

fig = plt.figure()
ax = plt.gca()

ax.add_collection(line_collection)
plt.hlines(0, -1.1, 1.1, color = 'black', linewidth = 1)
plt.vlines(0, -1.1, 1.1, color = 'black', linewidth = 1)
plt.xlim(min(solution[0]) - 0.1, max(solution[0]) + 0.1)
plt.ylim(min(solution[2]) - 0.1, max(solution[2]) + 0.1)
plt.title("Plot showing the trajectory of the ball bearing in the x-y Plane")

plt.show()