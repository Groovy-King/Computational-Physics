"""
    As given in the problem, we define a recursive method to determine the nth Catalan number (part a),
    and to implement Euclid's Algorithm to calculate the GCD of two integers.
"""

# Part a)
def Catalan(n):
    if n == 0:
        return 1
    else:
        return (4 * n  - 2) * Catalan(n - 1) / (n + 1) 

# Printing the value of C_100
print(f"The 101st Catalan number is: C_100 = {Catalan(100)}")

# Part b)
def GCD(m, n):
    if n == 0:
        return m
    else:
        return GCD(n, m % n)
    
# Printing the value of gcd(108,192)
print(f"\nThe GCD of 108 and 192 is: {GCD(108, 192)}")