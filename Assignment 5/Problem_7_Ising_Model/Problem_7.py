from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

"""
    We assume that periodic boundary conditions apply to the given problem. So, the atoms
    at the edges of our lattice need not be considered as a separate case, as they are equivalent 
    to any other lattice point.
"""

J = 1

# Part (a)
def Energy(S):
    nx, ny = S.shape
    E = 0
    for i in range(nx):
        for j in range(ny):
            E += S[i, j] * ( S[(i + 1) % nx, j] + S[(i - 1) % nx, j] )
            E += S[i, j] * ( S[i, (j + 1) % ny] + S[i, (j - 1) % ny] )
    
    # Since each pair of adjacent atoms only contributes once to the sum, we divide
    # the value of E by 2 to account for overcounting.
    E = -J * E / 2
    return E

# Part (b)
dx = 20
dy = 20
n_max = 10**6
l = np.log10(n_max)

def Metropolis_Simulation(T):
    beta = 1 / T
    S = rng.choice([-1, 1], size = (dx, dy))
    S0 = np.copy(S)
    M = np.empty(n_max)
    M[0] = np.sum(S, axis = (0, 1))

    for t in range(1, n_max):
        i = rng.integers(low = 0, high = dx)
        j = rng.integers(low = 0, high = dy)
        
        """
            We calculate the change in energy if the bit at (i, j) is flipped. Then we use the 
            Metropolis Algorithm formula to determine the flipping is valid or not. To calculate 
            this efficiently, we only consider the 4 pairs of adjacent atoms that involve our given
            atom. This is implemented below.
                E_new = -J * (-S[i, j]) * (other atoms)
                E_old = -J * (S[i, j]) * (other atoms)
                Delta_E = 2 * J * (S[i, j]) * (other atoms)
        """
        other_atoms = S[(i + 1) % dx, j] + S[(i - 1) % dx, j]
        other_atoms +=  S[i, (j + 1) % dy] + S[i, (j - 1) % dy]
        Delta_E = 2 * J * S[i, j] * other_atoms
        
        # If change in energy is negative, we accept the flip
        if Delta_E <= 0:
            accept = 1
        # If not, we accept the flip with probability exp(-beta*Delta_E)
        else:
            p = np.exp(-beta * Delta_E)
            accept = rng.binomial(1, p)
        
        if accept == 1:
            S[i, j] = -S[i, j]
            
        if t <= int(10**(l/3)):
            S1 = np.copy(S)
        elif t <= int(10**(2*l/3)):
            S2 = np.copy(S)
        else:
            S3 = np.copy(S)
        
        M[t] = np.sum(S, axis = (0, 1))

    t = np.arange(n_max)        
    plt.plot(t, M)
    plt.title("Magnetization as a function of time")
    plt.xlabel("Time")
    plt.ylabel("Total Magnetization")
    plt.show()
    
    print(f"The Temperature of the system is: {T}")
    print(f"The final Magnetization of the system is: {M[-1]}")
    
    # Part (c)
    xv, yv = np.meshgrid(np.arange(dx), np.arange(dy))
    fig, axes = plt.subplots(nrows = 2, ncols = 2)
    
    sgn = np.sign(M[-1])
    
    axes[0][0].grid(False)
    axes[0][0].pcolormesh(xv, yv, -sgn * S0, cmap = 'Paired')
    axes[0][0].set_title("Lattice at t = 0")
    axes[0][0].set_xticks([])
    axes[0][0].set_yticks([])
    
    axes[0][1].grid(False)
    axes[0][1].pcolormesh(xv, yv, -sgn * S1, cmap = 'Paired')
    axes[0][1].set_title(f"Lattice at t = {int(10**(l/3))}")
    axes[0][1].set_xticks([])
    axes[0][1].set_yticks([])
    
    axes[1][0].grid(False)
    axes[1][0].pcolormesh(xv, yv, -sgn * S2, cmap = 'Paired')
    axes[1][0].set_title(f"Lattice at t = {int(10**(2*l/3))}")
    axes[1][0].set_xticks([])
    axes[1][0].set_yticks([])
    
    axes[1][1].grid(False)
    axes[1][1].pcolormesh(xv, yv, S3, cmap = 'Paired')
    axes[1][1].set_title(f"Lattice at t = {int(10**l)}")
    axes[1][1].set_xticks([])
    axes[1][1].set_yticks([])
    
    plt.show()

T = [1, 1, 1, 1, 2, 3]    
for i in range(6):
    print(f"Run {i + 1}:")
    print("------------------- ")
    Metropolis_Simulation(T[i])
    print()
