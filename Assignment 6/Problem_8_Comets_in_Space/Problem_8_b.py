import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')
import time as Time

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var
from astropy.constants import M_sun, G

start = Time.time()

m_to_km = 10**(-3) # To convert from meters to km
s_to_year = 1 / (60*60*24*365) # To convert from seconds to years

G = G.value
G = G * m_to_km**3 / s_to_year**2
M_sun = M_sun.value

# As done before, we convert the given system into first order ODEs.
# Let v represent [x, dxdt, y, dydt]
# We now define the derivatives of each of these parameters
def x_dot(t, v):
    return v[1]

def x_double_dot(t, v):
    r = np.sqrt(v[0]**2 + v[2]**2)
    return -G*M_sun * v[0] / r**3

def y_dot(t, v):
    return v[3]

def y_double_dot(t, v):
    r = np.sqrt(v[0]**2 + v[2]**2)
    return -G*M_sun * v[2] / r**3

# Since we are working with astronomical systems, using SI could lead to overflow/underflow issues.
# Instead, we use year as the unit of time, and kilometers for distance.
x0 = 4 * 10**9 # 4 billion kms

vy0 = 500 * m_to_km / s_to_year # in km per year

system = [x_dot, x_double_dot, y_dot, y_double_dot]
ini_conds = np.array([x0, 0, 0, vy0])

time, solution = Runge_Kutta_multi_var(system, x0 = 0, y0 = ini_conds, x_min = 0, x_max = 100, h = 0.001)

x = solution[0]
y = solution[2]

plt.plot(x, y)
plt.plot(0, 0, marker = 'o', markeredgecolor = 'red', markersize = 4, markerfacecolor = 'red', label = 'Sun')
plt.title("Plotting trajectory of the Comet")
plt.legend()
plt.xlabel("$x$ (in km)")
plt.ylabel("$y$ (in km)")
plt.show()

time, solution = Runge_Kutta_multi_var(system, x0 = 0, y0 = ini_conds, x_min = 0, x_max = 100, h = 0.0005)

x = solution[0]
y = solution[2]

plt.plot(x, y)
plt.plot(0, 0, marker = 'o', markeredgecolor = 'red', markersize = 4, markerfacecolor = 'red', label = 'Sun')
plt.title("Plotting trajectory of the Comet")
plt.legend()
plt.xlabel("$x$ (in km)")
plt.ylabel("$y$ (in km)")
plt.show()

end = Time.time() - start
print(f"Time taken = {end} s")
