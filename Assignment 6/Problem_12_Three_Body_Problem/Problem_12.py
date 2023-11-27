import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.') 

from Import_Modules.Runge_Kutta import Runge_kutta_Adaptive_step

G = 1 # Given units
M1 = 150 # Given units
M2 = 200 # Given units
M3 = 250 # Given units

# Let the vector v represent [x1, dx1dt, y1, dy1dt, x2, dx2dt, y2, dy2dt, x3, dx3dt, y3, dy3dt]
# Then the derivative method is:
def dvdt(t, v):
    x1, dx1dt, y1, dy1dt, x2, dx2dt, y2, dy2dt, x3, dx3dt, y3, dy3dt = v
    x1dot = dx1dt # By definition
    x2dot = dx2dt # By definition
    y1dot = dy1dt # By definition
    y2dot = dy2dt # By definition
    x3dot = dx3dt # By definition
    y3dot = dy3dt # By definition
    
    r12 = np.linalg.norm( np.array([x1 - x2, y1 - y2]) )
    r23 = np.linalg.norm( np.array([x2 - x3, y2 - y3]) )
    r31 = np.linalg.norm( np.array([x3 - x1, y3 - y1]) )
    
    x1doubledot = G*M2 * (x2 - x1)/r12**3 + G*M3 * (x3 - x1)/r31**3
    x2doubledot = G*M3 * (x3 - x2)/r23**3 + G*M1 * (x1 - x2)/r12**3
    x3doubledot = G*M1 * (x1 - x3)/r31**3 + G*M2 * (x2 - x3)/r23**3
    y1doubledot = G*M2 * (y2 - y1)/r12**3 + G*M3 * (y3 - y1)/r31**3
    y2doubledot = G*M3 * (y3 - y2)/r23**3 + G*M1 * (y1 - y2)/r12**3
    y3doubledot = G*M1 * (y1 - y3)/r31**3 + G*M2 * (y2 - y3)/r23**3
    
    return np.array([x1dot, x1doubledot, y1dot, y1doubledot, x2dot, x2doubledot, y2dot, y2doubledot, x3dot, x3doubledot, y3dot, y3doubledot])

# We create the array to hold the given initial conditions
x0 = 0
y0 = np.array([3, 0, 1, 0, -1, 0, -2, 0, -1, 0, 1, 0])

time, solution, H = Runge_kutta_Adaptive_step(dvdt, x0, y0, xmax = 2, emax = 10**(-3))

x1 = solution[0]
y1 = solution[2]
x2 = solution[4]
y2 = solution[6]
x3 = solution[8]
y3 = solution[10]

plt.plot(x1, y1, label = "Planet M1")
plt.scatter(x1[-1], y1[-1], color = 'black', s = 30, edgecolors = 'black')
plt.plot(x2, y2, label = "Planet M2")
plt.scatter(x2[-1], y2[-1], color = 'black', s = 30, edgecolors = 'black')
plt.plot(x3, y3, label = "Planet M3")
plt.scatter(x3[-1], y3[-1], color = 'black', s = 30, edgecolors = 'black')
plt.title("Plot showing the trajectory of the 3-body system")
plt.legend()
plt.show()
    