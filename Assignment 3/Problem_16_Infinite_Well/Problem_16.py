import numpy as np
from scipy.constants import hbar, e, m_e
from num2words import num2words
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import sys
sys.path.insert(0, '.')
from Import_Modules.Integration import num_int

"""
    This program calculates the ground state energies and corresponding wave functions using
    the method outlined in the problem.
"""

# Part (b)
# Defining the constants a and L
a = 10 * e # in J
L = 5 * 10**(-10) # in m

def Hmn(m, n):
    if m == n:
        H = (n * hbar * np.pi)**2 / (2 * m_e * L**2) + a / 2
    elif (m % 2) == (n % 2):
        H = 0
    else:
        H = -8 * a * m * n / ( np.pi**2 * (m**2 - n**2)**2 )
        
    return H

# Part (c)
size = 10
H = np.empty((size, size))

for m in range(0, size):
    for n in range(0,size):
        H[m, n] = Hmn(m + 1, n + 1)
        
eig_val = np.sort( np.linalg.eigvals(H) / e)
print("Using a 10x10 Matrix: \n")
for i in range(0, size):
    print(f"The {num2words(i + 1, ordinal = True).capitalize()} energy level is: {np.round(eig_val[i], 4)} eV")
    
# Part (d)
# We repeat the entire calculation again, but with size = 100
size = 100    
H = np.empty((size, size))

for m in range(0, size):
    for n in range(0,size):
        H[m, n] = Hmn(m + 1, n + 1)
        
eig_val_2 = np.sort( np.linalg.eigvals(H) / e)
print("\n\nUsing a 100x100 Matrix: \n")
for i in range(0, 10):
    print(f"The {num2words(i + 1, ordinal = True).capitalize()} energy level is: {np.round(eig_val_2[i], 4)} eV")
    
print(f"\nThe maximum relative discrepancy between the two calculations is: {max(abs(eig_val - eig_val_2[0: 10]) / eig_val)}")

# Part (e)
# As seen above, using size = 10 agrees very closely with using size = 100. Thus, we use size = 10
# in the following calculation
size = 10
H = np.empty((size, size))

for m in range(0, size):
    for n in range(0,size):
        H[m, n] = Hmn(m + 1, n + 1)
        
eig_vals, eig_vecs = np.linalg.eig(H)

def psi(x, V):
    n = len(V)
    y = 0
    for i in range(0, n):
        y = y + V[i] * np.sin(i * np.pi * x / L)
    
    return y

x_plot = np.linspace(0, L, 1001)
# The term np.sqrt(2 / L) below is added so that the resulting wavefunction is normalised.
# This is coming from the fact that integral(sin(n*pi*x/L)**2, 0, L) = 2 / L
psi_0 = np.sqrt(2 / L) * psi(x_plot, eig_vecs[0])
psi_1 = np.sqrt(2 / L) * psi(x_plot, eig_vecs[1])
psi_2 = np.sqrt(2 / L) * psi(x_plot, eig_vecs[2])


plt.plot(x_plot / L, psi_0**2, label = 'Ground State')
plt.plot(x_plot / L, psi_1**2, label = 'First Excited State')
plt.plot(x_plot / L, psi_2**2, label = 'Second Excited State')
plt.axhline(0, c = 'k')
plt.axvline(0, c = 'k')
plt.axvline(1, c = 'k')
plt.xlabel('$\dfrac{x}{L}$')
plt.ylabel('$|\psi(x)|^2$')
plt.title('Plot showing the probability distibution for various states')
plt.legend()
plt.show()

# As a check, we use simpson method to calculate the integral of |psi(x)|**2 from 0 to L
print(f"\nThe integral of |psi_0(x)|**2 from 0 to L is: {num_int(x_plot, psi_0**2, method = 'Simpson')}")
print(f"The integral of |psi_1(x)|**2 from 0 to L is: {num_int(x_plot, psi_1**2, method = 'Simpson')}")
print(f"The integral of |psi_2(x)|**2 from 0 to L is: {num_int(x_plot, psi_2**2, method = 'Simpson')}")