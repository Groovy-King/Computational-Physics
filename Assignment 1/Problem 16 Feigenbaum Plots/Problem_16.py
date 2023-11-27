import numpy as np
import matplotlib.pyplot as plt

"""
    We use the algorithm mentioned in the comment to efficiently solve this problem. We 
    initialze the first array at x = 0.5, and subsequently set each value to x = r*x*(1-x).
    Each point obtained is then marked on a scatter plot using matplotlib, and finally displayed
    at the end.
"""

R = np.arange(1, 4, 0.01)
x = np.ones(len(R)) * 0.5

for i in np.arange(0, 1000): # First 1000 iterations for stability
    x = R * x * (1 - x)

for i in np.arange(0, 1000):
    x = R * x * (1 - x)
    plt.scatter(R, x, c = 'k', s = 0.5)

plt.grid()
plt.title("Feigenbaum Plot")
plt.xlabel("r")
plt.ylabel("x")
plt.show()