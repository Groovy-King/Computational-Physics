from numpy.random import default_rng
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

"""
    To calculate the number of atoms decaying in each step, we first clearly understand what
    p(t) signifies. p(t) is the probability that a given atom has decayed before time t. We 
    see that p(t) -> 0 as t -> 0, and p(t) -> 1, as t -> infinity. This clearly shows that p(t)
    is the probability that the atom has decayed before time t. So, to calculate the 
    probability, P_decay(t), that the atom decays between time t and t + dt, we write:
        P_decay(t) = p(t + dt) - p(t)
    This can be written as:
        P_decay(t) = dp/dt * delta t
    Thus, from the given expression p(t) = 1 - 2**(-t/tau), we get:
        P_decay(t) = 2**(-t/tau) * ln(2) * delta t / tau
        
    Now, at each time instant, a given atom decays with probability P_decay(t). This is a 
    Bernoulli trial with probability of success P_decay(t). Therefore, the total number of
    atoms of a given kind that decay at time t is a binomial random variable, with the number
    of trials equal to the number of atoms of that kind at time t. We use numpy's binomial rng
    to generate the number of atoms that decay at each time instant.
"""

rng = default_rng()

# We define therelevant parameters
n_total = 10**4
dt = 1
t_final = 2 * 10**4
T = np.arange(0, t_final, dt)
# Half-lives of [Bi-213, Tl-209, Pb-209]
tau = 60 * np.array([46, 2.2, 3.3])
# Bi-213 Branch probability
p_bi_to_tl = 0.0209

# Array to store numbers of each type of atom at all times
# n = [Bi-213[t], Tl-209[t], Pb-209[t], Bi-209[t]]
n = np.zeros((4, len(T)), dtype = int)  

# Setting up the initial state
n[0, 0] = n_total

for i in range(len(T) - 1):
    p = 2**(-T[i] / tau) * dt * np.log(2) / tau
    
    # Decay of Pb-209
    pb_decay = rng.binomial(n = n[2, i], p = p[2])
    n[2, i + 1] = n[2, i] - pb_decay
    n[3, i + 1] = n[3, i] + pb_decay
    
    # Decay of Tl-209
    tl_decay = rng.binomial(n = n[1, i], p = p[1])
    n[1, i + 1] = n[1, i] - tl_decay
    n[2, i + 1] = n[2, i + 1] + tl_decay
    
    # Decay of Bi-213
    bi_decay = rng.binomial(n = n[0, i], p = p[0])
    bi_to_tl = rng.binomial(n = bi_decay, p = p_bi_to_tl)
    bi_to_pb = bi_decay - bi_to_tl
    n[0, i + 1] = n[0, i] - bi_decay
    n[1, i + 1] = n[1, i + 1] + bi_to_tl
    n[2, i + 1] = n[2, i + 1] + bi_to_pb

# Calculating the total number of atoms at each instant
N = np.sum(n, axis = 0)

fig, ax1 = plt.subplots(nrows = 1, ncols = 1)
ax1.plot(T, n[0], c = 'blue', label = 'Bi-213')
ax1.plot(T, n[1], c = 'red', label = 'Tl-209')
ax1.plot(T, n[2], c = 'green', label = 'Pb-209')
ax1.plot(T, n[3], c = '0.25', label = 'Bi-209')
ax1.plot(T, N, c = 'black', linestyle = 'dashed', label = 'Total number of atoms')
ax1.legend()
ax1.set_title("Plot showing number of each kind of atom")
ax1.set_xlabel("t (in s)")
ax1.set_ylabel("Number of atoms")

plt.show()