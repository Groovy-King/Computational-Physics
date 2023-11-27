from numpy import sqrt, pi
from sympy import N

"""
    We assume that the gravitational influence of the Sun and other heavenly bodies is negligible
    in our problem. The potential experienced by the satellite is then the usual 1/r central potential
    centered around the Earth's Center of Mass (assuming the Earth is much more massive than the satellite).
    
    Then, the velocity of a satellite in a Keplerian orbit around a mass at a distance R is given by:
        v = sqrt(G*M/R)
    Thus, the time period is:
        T = 2*pi*R/v = 2 * pi * R**(3/2) / sqrt(G*M)
    where G is the Universal Gravitational constant, and M is the mass of the earth. Inverting this equation gives:
        R = ( sqrt(G*M) * T / (2*pi) )**(2/3)                       (*)
    
    The following program asks the user to enter the desired time period, and uses Eqn (*) above to determine the necessary distance.
"""

# Defining the relevant constants (in SI units)
G = 6.67 * 10**-11
M = 5.97 * 10**24

# Getting the desired Time period
t = float(input("Please enter the desired Time period: "))

# Defning the dictionary to convert units
scale = {'sec': 1, 'min': 60, 'hr': 60*60, 'day': 60*60*24}

# Getting the unit from the user
unit = input("Please enter the unit used in the above input (sec/min/hr/day): ").lower()

if unit not in ['sec', 'min', 'hr', 'day']:
    raise ValueError("Please enter a valid choice of unit!")

# Converting the time to SI units
T = t * scale[unit]

# Using the result to obtain the required distance
R = ( sqrt(G*M) * T / (2*pi) )**(2/3)

r_Earth = 6400 # in km

print(f"The satellite would have a time period of {t} {unit} at a distance of {N(R/1000 - r_Earth, 5)} km from the Earth's surface.")
if R/1000 - r_Earth <=0:
    print("Such a satellite is not possible!")