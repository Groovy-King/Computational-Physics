import numpy as np
import matplotlib.pyplot as plt

"""
    We use the numpy method loadtxt() to read the given data. Then, we use matplotlib's
    pcolomesh() to generate the density plot.
"""

data = np.loadtxt(r"Assignment 1\stm.txt")

plt.pcolormesh(data)
plt.title("STM showing surface of Silicon crystal")
plt.show()

c = plt.pcolormesh(data, cmap = 'Reds')
plt.title("STM showing surface of Silicon crystal")
plt.colorbar(c)
plt.show()
