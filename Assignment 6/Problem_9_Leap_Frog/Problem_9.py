import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Leap_Frog import Leap_Frog_Multi_Var

"""
    We first convert the given second order ODE into two first order ODEs. Then, we solve the 
    system by Leap Frog Method.
"""

# Let the vector v represent [x, dxdt]
def dvdt(t, v):
    x, dxdt = v
    xdot = dxdt # By definition
    x_doubledot = dxdt**2 - x - 5 # From given ODE
    
    return np.array([xdot, x_doubledot])

h = 0.001
t_max = 50
x0 = 1
dxdt0 = 0
ini_0 = np.array([x0, dxdt0])

# We approximate x(h/2) and dxdt(h/2) by Euler's method
der_0 = dvdt(0, [x0, dxdt0])
x_half = x0 + der_0[0]*h/2
dxdt_half = dxdt0 + der_0[1]*h/2
ini_half = np.array([x_half, dxdt_half])

# We now use Leap Frog method to integrate the ODE
time, solution, sol_half = Leap_Frog_Multi_Var(dvdt, 0, ini_0, ini_half, t_max, h)

plt.plot(time, solution[0])
plt.title("Plot showing Integrated Solution")
plt.xlabel("Time (in s)")
plt.ylabel("$x(t)$")
plt.show()