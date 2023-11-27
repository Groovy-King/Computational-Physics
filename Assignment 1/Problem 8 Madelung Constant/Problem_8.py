from numpy import arange, sqrt
import time

"""
    To calculate the Madelung constant, we execute three nested for loops, 
    and add the contribution of each atom in the lattice. Further, to reduce the 
    number of computations, we observe that the contribution of an atom at (-i, j, k) and 
    (i, j, k) are equal. So, we multiply the contribution of an atom (i, j, k) by 2, whenever
    i is not zero, i.e., the atom has a distinct counterpart at (-i, j, k). By doing this, we
    just use the limits i, j, k in 0 to L, rather than -L to L, significantly reducing run time.  
    
    The program below implements this algorithm.
"""

L = int(input("Please enter the value of L: "))

start_time = time.time() # To calculate runtime of program
M = 0
for i in arange(0, L + 1):
    if i == 0:
        I = 1
    else:
        I = 2
    for j in arange(-L, L + 1):
        if j == 0:
            J = 1
        else:
            J = 2
        for k in arange(-L, L + 1):
            if k == 0:
                K = 1
            else:
                K = 2
            if (i == 0) and (j == 0) and (k == 0):
                continue
            elif (i + j + k)%2 == 0:
                M = M + I * J * K / sqrt(i**2 + j**2 + k**2)
            else:
                M = M - I * J * K / sqrt(i**2 + j**2 + k**2)
                
print(f"The Madelung constant is calculated to be: {M}")
print(f"The runtime of this program is: {time.time() - start_time} seconds.")