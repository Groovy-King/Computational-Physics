import numpy as np

"""
    We first define a method to calculate the binomial coefficient, given values of n and k.
    Then, we define another method to print the first m lines of Pascal's triangle, using the first
    method. Finally, we again use the first method to calculate the desired probabilities.
"""

def binomial(n = 1, k = 1):
    if (n < k) or (k < 0):
        return 0
    elif k == 0:
        return 1
    else:
        res = 1
        for i in np.arange(1, k + 1):
            res = res / i 
            res = res * (n - k + i)
        
        return int(res) # Since we know that nCk is always an integer, 
                        # this type casting does not have any roundoff errors
    
def Pascal_Triangle(m = 5):
    for n in np.arange(1, m + 1):
        out = []
        
        for k in np.arange(0, n + 1):
            out.append(binomial(n, k))
        
        print(*out)
        
# Now, we ask the user to choose which subpart of the problem they need to solve
# And the corresponding method is called.

sub_part = input("Please enter the subpart you wish to solve: ")
allowed_Sub_parts = ['a', 'b', 'c']
if sub_part.lower() not in allowed_Sub_parts:
    raise ValueError("Please enter a valid subpart!")

if sub_part.lower() == 'a':
    n = int(input("Please enter the value of n: "))
    k = int(input("Please enter the value of k: "))
    print(f"\nThe value of {n}C{k} is: {binomial(n, k)}")
    
elif sub_part.lower() == 'b':
    m = int(input("Please enter the desired number of lines: "))
    print()
    Pascal_Triangle(m)
    
elif sub_part.lower() == 'c':
    N = int(input("Please enter the total number of coins: "))
    k = int(input("Please enter the cutoff number of heads: "))
    
    def P_exact(N, k):
        return binomial(N, k) / 2**N
    
    print(f"\nThe probability of obtaining exactly {k} heads out of {N} coins is: {np.round(P_exact(N, k), 4)}")
    
    P_atleast = 0
    for n in np.arange(k, N + 1):
        P_atleast = P_atleast + P_exact(N, n)
    
    print(f"The probability of obtaining atleast {k} heads out of {N} coins is: {np.round(P_atleast, 4)}")