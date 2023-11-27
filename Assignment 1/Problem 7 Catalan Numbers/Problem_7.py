"""
    This program implements a simple while loop to calculate the Catalan numbers upto one billion.
    Further, since (4n+2)/(n+2) is always greater than 1, the sequence of Catalan numbers is always 
    increasing.
"""

i = 0 # The index
C = 1 # The first Catalan number

while (C < 10**9):
    print(C)
    C = (4*i + 2) * C / (i + 2)
    i = i + 1