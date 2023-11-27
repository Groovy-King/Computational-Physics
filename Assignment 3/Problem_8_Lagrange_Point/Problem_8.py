"""
    As given in the figure 'Part (a) Derivation.png', the distance to the Lagrange point r
    satisfies:
        GM/r - Gm/(R - r) = w**2 r
"""
# Defning the relevant constants
G = 6.674 * 10**(-11)
M_earth = 5.974 * 10**(24)
M_moon = 7.348 * 10**(22)
R = 3.844 * 10**(8)
w = 2.662 * 10**(-6)

def eq(r):
    return G * M_earth / r - G * M_moon / (R - r) - w**2 * r

# Importing the solver to implement secant method
import sys
sys.path.insert(0, '.')

from Import_Modules.Root_finder import Root_finder

# Setting up the initial guesses
r_min = 6.4 * 10**(6)
r_max = 0.98 * R

# Setting up the error tolerance
e_max = 5 * 10**(-5) # We shall use relative error to get up to 4 sig figs

r = Root_finder(eq, r_min, r_max, e_max = e_max, TOL_Parameter = 'Relative', method = 'Secant', print_out = True)

print(f"\nThe distance to the Lagrange point from Earth's center is: {'{:.5E}'.format(r)} m")