import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_Higher_Order

# Defining the relevant parameters
omega = 1

# Defining the function modelling the rhs of the ODE
def d2xdt2(t, v):
    return -omega**2 * v[0]

time, solution = Runge_Kutta_Higher_Order(d2xdt2, x0 = 0, y0 = np.array([1, 0]), x_min = 0, x_max = 50, h = 0.01)

plt.plot(time, solution[0])
plt.title("Integrated solution showing x vs t")
plt.xlabel("Time (in s)")
plt.ylabel("Position $x$")
plt.show()

time2, solution2 = Runge_Kutta_Higher_Order(d2xdt2, x0 = 0, y0 = np.array([2, 0]), x_min = 0, x_max = 50, h = 0.01)

plt.plot(time2, solution2[0], label = "A = 2")
plt.plot(time, solution[0], color = 'red', linestyle = 'dashed', label = "A = 1")
plt.title("Integrated solution for higher amplitude")
plt.xlabel("Time (in s)")
plt.ylabel("Position $x$")
plt.legend()
plt.show()

# As seen in the figure 'Part (b) Integrated solution with higher amplitude.png', it is clear that
# the time period of both waveforms are identical.

def d2xdt2_new(t, v):
    return -omega**2 * v[0]**3

time_new, solution_new = Runge_Kutta_Higher_Order(d2xdt2_new, x0 = 0, y0 = np.array([1, 0]), x_min = 0, x_max = 50, h = 0.01)
time_new2, solution_new2 = Runge_Kutta_Higher_Order(d2xdt2_new, x0 = 0, y0 = np.array([2, 0]), x_min = 0, x_max = 50, h = 0.01)

plt.plot(time_new2, solution_new2[0], label = "A = 2")
plt.plot(time_new, solution_new[0], color = 'black', label = "A = 1")
plt.title("Integrated solution for Anharmonic Oscillator")
plt.xlabel("Time (in s)")
plt.ylabel("Position $x$")
plt.legend()
plt.show()

# Plotting the Phase space diagram of Harmonic Oscillator
plt.plot(solution[0], solution[1])
plt.hlines(0, -1.1, 1.1, color = 'black')
plt.vlines(0, -1.1, 1.1, color = 'black')
plt.xlabel("Position $x$")
plt.ylabel("Velocity $v$")
plt.title("Phase Space Diagram of Harmonic Oscillator")
plt.show()

# Plotting the Phase space diagram of Anharmonic Oscillator
plt.plot(solution_new[0], solution_new[1])
plt.hlines(0, -1.1, 1.1, color = 'black')
plt.vlines(0, -omega - 0.1, omega + 0.1, color = 'black')
plt.xlabel("Position $x$")
plt.ylabel("Velocity $v$")
plt.title("Phase Space Diagram of Anharmonic Oscillator")
plt.show()

# The Von der Pol Oscillator
Mu = [1, 2, 4]
omega = 1

for mu in Mu:
    def d2xdt2_van_der_pol(t, v):
        return mu*(1 - v[0]**2)*v[1] - omega**2 * v[0]
    
    time, solution = Runge_Kutta_Higher_Order(d2xdt2_van_der_pol, x0 = 0, y0 = np.array([1, 0]), x_min = 0, x_max = 20, h = 0.005)
    plt.plot(solution[0], solution[1], label = f"mu = {mu}")

# Plotting the Phase space diagram of Van der Pol Oscillator
plt.hlines(0, min(solution[0]) - 0.1, max(solution[0]) + 0.1, color = 'black')
plt.vlines(0, min(solution[1]) - 0.1, max(solution[1]) + 0.1, color = 'black')
plt.xlabel("Position $x$")
plt.ylabel("Velocity $v$")
plt.title("Phase Space Diagram of Van der Pol Oscillator")
plt.legend()
plt.show()

# Plotting position vs time for Van der Pol Oscillator
plt.plot(time, solution[0])
plt.title("Integrated solution showing x vs t")
plt.xlabel("Time (in s)")
plt.ylabel("Position $x$")
plt.show()