import sympy as smp
import numpy as np

import sys
sys.path.insert(0, '.')

from Import_Modules.Newton_Multivar import Newton_MultiVar

"""
    The derivation to the system of equations used below is attached in the figure 
    'Part (a) System of Equations.png'. The method Newton_Multivar() implements Newton's
    method that has been generalized to a system of N variables. The code is saved in the folder
    Import_Modules, in the file Newton_Multivar.py. Also, since no initial guess is given, we use
    V1 = V2 = V_plus / 2 as the initial guess.
"""

# Defining the relevant constants
V_plus = 5 # in V
R1 = 1 * 10**3 # in Ohms
R2 = 4 * 10**3 # in Ohms
R3 = 3 * 10**3 # in Ohms
R4 = 2 * 10**3 # in Ohms
I0 = 3 * 10**(-9) # in Amperes
V_T = 0.05 # in V

V1, V2 = smp.symbols('V_1 V_2')
eq1 = V1 / R2 + (V1 - V_plus) / R1 + I0 * ( smp.exp((V1 - V2) / V_T) - 1 )
eq2 = V2 / R4 + (V2 - V_plus) / R3 - I0 * ( smp.exp((V1 - V2) / V_T) - 1 )

# Setting up the initial guess
ini_guess = np.array([V_plus/2, V_plus/2])

# Setting up the desired error tolerance
e_max = 10**(-6)


V_sol = Newton_MultiVar([V1, V2], [eq1, eq2], ini_guess, e_max, print_out = True)

print(f"The Voltage at Junction 1 is: {V_sol[0]} V")
print(f"The Voltage at Junction 2 is: {V_sol[1]} V")

# Part (b)
print(f"\nThe difference in potential between Junction 1 and 2 is: {V_sol[0] - V_sol[1]} V")