import numpy as np
from scipy.constants import hbar, e, m_e, pi

import sys
sys.path.insert(0, '.')

"""
    In the following problem, we use the expressions derived in the figures saved in the folder 
    to calculate the First six lowest energies of the Finite Potential Well. 
"""

w = 10**(-9) # in m
V = 20 # in eV
n = 0

def f(E):
    if n % 2 == 0:
        return np.sqrt( (V - E) / E ) - np.tan( w * np.sqrt(2 * m_e * E * e) / (2 * hbar) )
    else:
        return np.sqrt( (V - E) / E ) + 1 / np.tan( w * np.sqrt(2 * m_e * E * e) / (2 * hbar) )

# Importing the function to implement False Position Method
from Import_Modules.Root_finder import Root_finder

# Setting the maximum number of iterations
N_max = 50
#Setting the desired tolerance level
e_max = 0.001

for n in range(0, 6):
    if n % 2 == 0:
        # We adjust the values slightly to avoid divide by zero error
        E_min = (2 * n * pi * hbar / w)**2 / (2 * m_e * e) + 0.0001
        E_max = ((2*n + 1) * pi * hbar / w)**2 / (2 * m_e * e) - 0.0001
    else:
        E_min = ((2*n + 1) * pi * hbar / w)**2 / (2 * m_e * e) + 0.0001
        E_max = ((2*n + 2) * pi * hbar / w)**2 / (2 * m_e * e) - 0.0001
    
    if E_min >= V:
        print(f"There are only {n} bound States!")
        break
    elif E_max >= V:
        E_max = V
    
    E_n = Root_finder(f, E_min, E_max, e_max, N_max, method = 'Regula Falsi')
    print(f"The energy corresponding to n = {n} is: {E_n} eV")
        
