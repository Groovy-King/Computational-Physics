from numpy.random import default_rng
import math
from numpy import pi

"""
    The formulae for the inverse transformations of theta and phi are attached in the figure
    'Part (b) Inverse Transformations.png'. We generate the uniform random variables capital Theta
    and capital Phi, and use the formulae to obtain theta and phi with the distributions
    p(theta) and p(phi).
"""

rng = default_rng()

Theta, Phi = rng.uniform(low = 0, high = 1, size = 2)

theta = math.acos(2*Theta - 1)
phi = 2 * pi * Phi

print(f"The random number theta with distribution p(theta) = sin(theta) / 2 is: {theta}")
print(f"The random number theta with distribution p(phi) = 1 / (2*pi) is: {phi}")