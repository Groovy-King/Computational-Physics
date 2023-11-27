import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var
from Import_Modules.Root_finder import Root_finder
from Import_Modules.Integration import num_int

from scipy.constants import m_e, e, hbar
a = 10**(-11) # in m
V0 = 50*e # in J

L = 10*a

def V(x): # The potential
    return V0 * x**4 / a**4

# We convert the Schrodinger Eigenvalue equation into two first order equations
# Let the vector v represent [psi, dpsidx]
def dpsidx(x, v, E):
    psi, dpsidx = v
    psi_prime = dpsidx # By definition
    
    return psi_prime

def d2psidx2(x, v, E):
    psi, dpsidx = v
    psi_double_prime = (2*m_e/hbar**2) * (V(x) - E) * psi
    
    return psi_double_prime

def psi_right(E, return_psi = False):
    def f1_e(x, v):
        return dpsidx(x, v, E)
    
    def f2_E(x, v):
        return d2psidx2(x, v, E)
    
    system = [f1_e, f2_E]
    ini_guess = np.array([0, 1]) # Psi(x=0) = 0, and we set the derivative to 1, as the value doesn't matter
    x_0 = -10*a
    xmin = x_0
    if return_psi:
        xmax = 0
    else:
        xmax = 10*a
    h = (xmax - xmin)/999
    
    xsol, ysol = Runge_Kutta_multi_var(system, x_0, ini_guess, xmin, xmax, h)

    psi = ysol[0]
    if return_psi:
        return xsol, psi
    
    return psi[-1]

# We use the same bracketing guesses as in part (b)
E_guess1 = 150*e
E_guess2 = 250*e
E_ground = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

# Since we do not know the energy levels of an anharmonic oscillator, we employ
# trial and error to ginf suitable guesses.
E_guess1 = 300*e
E_guess2 = 500*e
E_first_excited = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

# Similarly, for the second excited state, we again guess the bracketing values
E_guess1 = 900*e
E_guess2 = 1100*e
E_second_excited = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

i = 0
for Energy in [E_ground, E_first_excited, E_second_excited]:
    x_plot, y_plot = psi_right(Energy, return_psi = True)
    x_plot = x_plot / a
    normalisation = 2*num_int(x_plot[:-1], y_plot[:-1]**2, method = 'Simpson')
    y_plot = y_plot / np.sqrt(normalisation)
    x_plot = np.concatenate([x_plot, -np.flipud(x_plot)])
    y_plot = np.concatenate([y_plot, (-1)**i * np.flipud(y_plot)])
    print(x_plot)
    plt.plot(x_plot[abs(x_plot) <= 5], y_plot[abs(x_plot) <= 5], label = f'Energy = {np.round(Energy/e, 4)} eV')
    i = i + 1

plt.title(f"Plots of Normalized Wavefunctions for the first three states")
plt.xlabel('$x$ (in units of $a$)')
plt.ylabel('$\psi(x)$')
plt.legend()
plt.show()
