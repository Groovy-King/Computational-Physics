import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_one_var

RC = [0.01, 0.1, 1]
h = 0.01

def V_in(t):
        if (int(2*t) % 2) == 0:
            return 1
        else:
            return -1

for rc in RC:
    def rhs(t, x):
        return (V_in(t) - x) / rc
    
    x_sol, y_sol = Runge_Kutta_one_var(rhs, x0 = 0, y0 = 0, x_min = 0, x_max = 10, h = h)
    plt.plot(x_sol, y_sol, label = f"RC = {rc}")

plt.xlabel("Time (in s)")
plt.ylabel("Output Voltage (in V)")
plt.title("Integrated solution to the low pass filter circuit")
plt.legend()
plt.show()