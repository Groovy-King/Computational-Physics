import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

"""
    The problem asks us to plot the trajectory for a random walk with a million steps. However,
    the total number of available lattice points is roughly 10**4, which leads to a lot cluttering
    in the plot. So, to visualize the trajectories better, I have attached the results of random
    walks with thousand, ten thousand, hundred thousand and million steps. We can clearly see
    the trajectories becoming more and more complex as we increase the number of steps taken.
"""

# Defining the relevant parameters
L = 101
n_max = 10**6
# We start the particle in the middle of the grid
ini_point = np.array([L - 1, L - 1]) / 2
pos = np.zeros((2, n_max))
pos[0, 0] = ini_point[0]
pos[1, 0] = ini_point[1]

for i in range(n_max - 1):
    current_choices_horizontal = [np.array([1, 0]), np.array([-1, 0])]
    current_choices_vertical = [np.array([0, 1]), np.array([0, -1])]
    
    # If particle is at left/right wall, remove the option to go further left/right
    if pos[0, i] == 0:
        del current_choices_horizontal[1]
    elif pos[0, i] == L - 1:
        del current_choices_horizontal[0]
    
    # If particle is at top/bottom wall, remove the option to go further up/down
    if pos[1, i] == 0:
        del current_choices_vertical[1]
    elif pos[1, i] == L - 1:
        del current_choices_vertical[0]
        
    # Deining all the possible current choice
    current_choices = current_choices_horizontal + current_choices_vertical
    
    # Choose a direction for the random walk
    path = rng.choice(current_choices)
    
    # Update the position of the particle
    pos[0, i + 1] = pos[0, i] + path[0]
    pos[1, i + 1] = pos[1, i] + path[1]

plt.plot(pos[0], pos[1])
plt.scatter(ini_point[0], ini_point[1], color = 'red')
plt.xlim(0, L)
plt.ylim(0, L)
plt.title(f"Plot showing trajectory of random walk with $10^{int(np.log10(n_max))}$ steps")
plt.show()