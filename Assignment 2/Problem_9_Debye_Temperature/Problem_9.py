import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import  k
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from gaussxw import gaussxwab

# Part (a)
def Cv(T, V, rho, T_Db, N):
    cv = np.zeros(len(T))
    def f(x):
        return x**4 * np.exp(x) / (np.exp(x) - 1)**2
    for t in T:
        x, w = gaussxwab(N, 0, T_Db/t)
        cv[T == t] = 9 * V * rho * k * (t / T_Db)**3 * np.sum(w * f(x))
    return cv


# Part (b)
T = np.linspace(5, 500, 500)
plt.plot(T, Cv(T, 10**(-3), 6.022 * 10**(28), 428, 50))
plt.title("Plot of Specific Heat vs Temperature")
plt.xlabel("T (in K)")
plt.ylabel("$C_V$ ( in J/$(kg-K$) )")
plt.savefig(fname = "Specific Heat.png")
plt.show()