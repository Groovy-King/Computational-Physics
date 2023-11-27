import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var, Runge_kutta_Adaptive_step

k = 6 # Given units
m = 1 # Given units

def First_order_ODEs(F):
    n = len(F)
    # Let the list v represent [x1, x2, ... xn, dx1dt, dx2dt, ... dxndt]
    # We convert the given system to system of 2n First order ODEs below
    
    # This function creates a function that can return the velocity of the i-th particle
    def Create_func_velocity(i):
        def g(t, v):
            # Derivative of xi is dxidt, which is at position i+n
            return v[i + n]
        return g
    
    f = [0] * (2*n)
    for i in range(n):
        f[i] = Create_func_velocity(i)
        
    # Defining the x double dots
    # Since the accelerations of the first and last particle do not follow the general equation,
    # we add these separately
    def acceleration_1(t, v):
        return k*(v[1] - v[0])/m + F[0](t, v)/m
    f[n] = acceleration_1
    
    def Create_func_acceleration(i):
        def g(t, v):
            return k*(v[i + 1] + v[i - 1] - 2*v[i])/m + F[i](t, v)/m
        return g
        
    # We now append the accelerations of particles 2 to n-1
    for i in range(1, n - 1):
        f[i + n] = Create_func_acceleration(i)
    
    # Finally, we add the acceleration of the last sparticle
    def acceleration_n(t, v):
        return k*(v[n - 2] - v[n - 1])/m + F[-1](t, v)/m
    f[2*n - 1] = acceleration_n      
        
    return f

# We define the relevant parameters of the model, and solve using Runge Kutta method for N = 5
N = 5
omega = 2
F = [0] * N

# We now define the driving forces
# We have a non-zero driving force on the first particle
def f_dr_1(t, v):
    return np.cos(omega * t)
F[0] = f_dr_1

def f_dr_others(t, v):
    return 0

for i in range(1, N):
    F[i] = f_dr_others
    
# We define the rhs of our system below
system = First_order_ODEs(F)

# We setup the initial conditions below. We assume that each particle was at rest and that each 
# spring was in its natural state at t = 0. The presence of a driving force causes the system to
# evolve accordingly.
ini_conds = np.zeros(2*N)

time, solution = Runge_Kutta_multi_var(system, x0 = 0, y0 = ini_conds, x_min = 0, x_max = 20, h = 0.01)
#time, solution, H = Runge_kutta_Adaptive_step(system, x0 = 0, y0 = ini_conds, xmin = 0, xmax = 20, emax = 10**(-4), h0 = 0.01)

colors = cm.copper(np.linspace(0, 1, N))

fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw = {'height_ratios': [10, 1]})
fig.suptitle("Plot showing the trajectories of all springs")
fig.subplots_adjust(bottom = 0.1)

for i in range(N):
    ax1.plot(time, solution[i], color = colors[i])

bounds = np.arange(N + 1) - 0.5
cmap = mpl.cm.copper
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
ticks = np.arange(N)

fig.colorbar(mpl.cm.ScalarMappable(norm = norm, cmap = cmap),
             cax = ax2,
             orientation='horizontal',
             ticks = ticks,
             label="Color map of each particle")

plt.show()
