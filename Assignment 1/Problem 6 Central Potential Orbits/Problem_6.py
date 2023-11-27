# pyright: reportGeneralTypeIssues = false
import sympy as smp
from decimal import Decimal

"""
    The expression for each of the required quantities is given in 'Kepler orbits 1/2.png', 
    attached in this folder. The detailed derivation for these expressions is given in Ch. 7,
    of "Introduction to Classical Mechanincs" by David Morin. 
    
    Using these expressions, the following program calculates the angular momentum, eccentricity
    and the orbital period. Further, since the properties of the gravitational orbits do not depend
    on the mass of the orbiting object, we assume that m = 1 for easier calculations.
"""

l1 = smp.sympify(input("Please enter the distance at the perihelion (in m): "))
v1 = smp.sympify(input("Please enter the velocity at the perihelion (in m/s): "))

M = 1.9891 * 10**(30)
G = 6.67 * 10**(-11)

L = l1 * v1
E = v1**2 / 2 - G * M / l1

# Solving for the eccentricity of the orbit
ecc = smp.sqrt(1 + 2 * E * L**2 / (G**2 * M**2))

# Solving for l2, v2
l2 = l1 * (1 + ecc) / (1 - ecc)
v2 = L / l2

print(f"\nThe distance at apohelion l_2 is {smp.N(l2)} m")
print(f"The velocity at apohelion v_2 is {smp.N(v2)} m/s")

# Solving for the Time period T
a = (l1 + l2) / 2
T = smp.sqrt(4 * smp.pi**2 * a**3 / (G * M))
print(f"The time period of motion T is {smp.N(T / (365 * 24 * 3600))} years ")
print(f"\nThe eccentricity of the orbit is: {ecc}")

