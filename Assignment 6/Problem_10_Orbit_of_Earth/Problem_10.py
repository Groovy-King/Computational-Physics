import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Leap_Frog import Verlet

"""
    We convert the given system of 2 Second order ODEs to 4 First ODEs, and then apply Verlet's method
    to integrate the ODEs.
"""

G = 6.6738 * 10**(-11) # in m^3 kg^(-1) s^(-2)
M = 1.9891 * 10**(30) # in kg

# Let the vector r represent [x, y], and the vector v represent [dxdt, dydt]
# For the Verlet method, we only need to define the method to calculate dvdt.
# The equation drdt = v is already taken into account in the algorithm itself.
def dvdt(t, R):
    x, y = R
    r = np.sqrt(x**2 + y**2)
    return np.array([-G*M * x/ r**3, -G*M * y/ r**3])

# Let's assume that the perihelion of the planet is on the x-axis, 
# and the planet is currently moving toward the positive y-axis tangentially.
ini_position = np.array([1.4710 * 10**(11), 0]) # in m
ini_velocity = np.array([0, 3.0287 * 10**4]) # in m/s

# Unit conversions
year = 365*24*60*60 # number of seconds in a year
hour = 60*60 # number of seconds in a hour

# We integrate from t = 0 to t = 5 years
time, position, velocity, vel_half = Verlet(dvdt, 0, ini_position, ini_velocity, 5*year, hour)

plt.plot(position[0], position[1])
plt.plot(0, 0, marker = '.', markerfacecolor = 'red', markeredgecolor = 'red', markersize = 15, label = 'Sun', linestyle = None)
plt.title("Plot showing Integrated Trajectory of Planet")
plt.xlabel("$x$ (in m)")
plt.ylabel("$y$ (in m)")
plt.legend()
plt.show()

x = position[0]
y = position[1]
vx = velocity[0]
vy = velocity[1]

r = np.sqrt(x**2 + y**2)
v = np.sqrt(vx**2 + vy**2)

m = 5.9722 * 10**(22) # in kg
Potential = -G*M*m/r # in J
Kinetic = 0.5*m*v**2

plt.plot(time[1:]/(60*24), Potential[1:], label = 'Potential Energy')
plt.plot(time[1:]/(60*24), Kinetic[1:], label = 'Kinetic Energy')
plt.plot(time[1:]/(60*24), Potential[1:] + Kinetic[1:], label = 'Total Energy')
plt.xlabel('Time (in days)')
plt.ylabel('Energy')
plt.title('Plot showing different Energies vs Time')
plt.legend()
plt.show()

plt.plot(time[1:]/(60*24), Potential[1:] + Kinetic[1:], label = 'Total Energy')
plt.xlabel('Time (in days)')
plt.ylabel('Energy')
plt.title('Plot showing Total Energy vs Time')
plt.show()
