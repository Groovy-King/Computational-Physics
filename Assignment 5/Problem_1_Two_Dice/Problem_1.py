import numpy as np
from numpy.random import default_rng

"""
    Throughout this assignment, we use the random module from numpy to generate our random numbers.
"""

rng = default_rng()

def die_roll(n = 1):
    d1, d2 = rng.integers(low = 1, high = 7, size = (2, n))
    return (d1, d2)

d1, d2 = die_roll()
print(f'We roll two dice, and the observed results are:')
print(f'\t Die 1 rolled {d1[0]}')
print(f'\t Die 2 rolled {d2[0]}')

n = 10**6
compiled_results = die_roll(n)

count = 0
for i in range(n):
    d1 = compiled_results[0][i]
    d2 = compiled_results[1][i]
    if (d1 == 6) and (d2 == 6):
        count = count + 1

prob = count / n
print(f"\nThe expected fraction of double 6 rolls is 1/36, which is equal to: {np.round(1/36, 5)}")
print(f"The observed fraction of double 6 rolls is: {prob}")