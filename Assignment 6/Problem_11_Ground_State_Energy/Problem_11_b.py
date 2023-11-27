import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')

from Import_Modules.Runge_Kutta import Runge_Kutta_multi_var
from Import_Modules.Root_finder import Root_finder

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

def psi_right(E):
    def f1_e(x, v):
        return dpsidx(x, v, E)
    
    def f2_E(x, v):
        return d2psidx2(x, v, E)
    
    system = [f1_e, f2_E]
    ini_guess = np.array([0, 1]) # Psi(x=0) = 0, and we set the derivative to 1, as the value doesn't matter
    x_0 = -10*a
    xmin = x_0
    xmax = 10*a
    h = (xmax - xmin)/999
    
    xsol, ysol = Runge_Kutta_multi_var(system, x_0, ini_guess, xmin, xmax, h)

    psi = ysol[0]    
    return psi[-1]

# We use the same bracketing guesses as in part (a)
E_guess1 = 100*e
E_guess2 = 200*e

E_ground = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

print(f"\nThe Ground State Energy of the given AnHarmonic Oscillator is: {E_ground/e} eV")

# For a Harmonic Oscillator, the ground state energy is hbar*omega/2, 
# while the next energy levels are (3/2)*hbar*omega, (5/2)*hbar*omega

# So, for the first excited state, we expect the energy to be around 3*E_ground, 
# which is close to 400 eV. We use appropriate guesses.
E_guess1 = 300*e
E_guess2 = 500*e

E_first_excited = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

print(f"The First Excited State Energy of the given AnHarmonic Oscillator is: {E_first_excited/e} eV")

# Similarly, for the second excited state, we expect the energy to be around 5*E_ground, 
# which is close to 700 eV. We use appropriate guesses.
E_guess1 = 900*e
E_guess2 = 1100*e

E_second_excited = Root_finder(psi_right, E_guess1, E_guess2, method = 'Secant', TOL_Parameter = 'Relative')

print(f"The Second Excited State Energy of the given AnHarmonic Oscillator is: {E_second_excited/e} eV")

print(f"\nThe spacing between the energy levels is:")
print(f"\t\t E_first - E_Ground = {E_first_excited/e - E_ground/e} eV")
print(f"\t\t E_second - E_first = {E_second_excited/e - E_first_excited/e} eV")