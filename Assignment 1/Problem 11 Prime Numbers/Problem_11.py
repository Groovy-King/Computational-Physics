# pyright: reportUnboundVariable = false
import numpy as np

"""
    As described in the problem, we create a list of primes in increasing order, and keep
    adding in new elements to the list by checking if elements less than or equal to sqrt(n)
    is a factor of n.
"""

primes = np.array([2])
print("2")

n = 3
while n <= 10000:
    test_list = primes[primes <= np.sqrt(n)]
    divisible = 0
    for i in test_list:
        if n % i == 0:
            divisible = 1
            break 
    
    if divisible == 0:
        primes = np.append(primes, [n])
    n = n + 1
    
# The list primes now contains all the primes below 10000 in inreasing order. 
# Since the list is too long, we shall directly print the output into "Problem_11_Output.txt"

output = open(r"Assignment 1\Problem 11 Prime Numbers\Problem_11_Output.txt", "r+")

output.seek(186) # Goes to the end of pre written text in the file, and writes/overwrites from there
for p in primes:
    output.write(f"{p}\n")

output.close()