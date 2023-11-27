import numpy as np
import matplotlib.pyplot as plt
import time

"""
    We plot a 2D pcolor graph to display the Mandelbrot set. We first create a 2D array to depict
    points in the plane, and then assign either 0 or 1 to each point, to denote if it belongs to
    the Mandelbrot set.
"""
start_time = time.time()

n = 1000
black_white = np.ones((n, n))
color = np.zeros((n, n))

X = np.linspace(-2, 2, n)
Y = np.linspace(-2, 2, n)

grid_x, grid_y = np.meshgrid(X, Y, sparse = True)

x_index = 0

for i in np.arange(0, n):
    for j in np.arange(0, n):
        c = complex(X[i], Y[j]) # Python 3.9's built in complex() method handles complex numbers
        z = 0
        for k in np.arange(0, 100):
            z = z**2 + c
            if np.abs(z) >= 2:
                black_white[j][i] = 0
                color[j][i] = k
                break
            elif k == 99:
                color[j][i] = 99

plt.pcolormesh(grid_x, grid_y, black_white, cmap = 'Greys')
plt.grid()
plt.title("Mandelbrot Set Generation")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
#plt.show()

plt.pcolormesh(grid_x, grid_y, color, vmin = 0, vmax = 99, cmap = 'hot')
plt.axvline(x=0, c="gray", linewidth = 0.5)
plt.axhline(y=0, c="gray", linewidth = 0.5)
plt.title("Mandelbrot Set Generation with color")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()

plt.pcolormesh(grid_x, grid_y, color, vmin = 0, vmax = 99, cmap = 'jet')
plt.axvline(x=0, c="yellow", linewidth = 0.4)
plt.axhline(y=0, c="yellow", linewidth = 0.4)
plt.title("Mandelbrot Set Generation with color")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()