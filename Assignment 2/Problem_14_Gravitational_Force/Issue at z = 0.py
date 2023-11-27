import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Depicting the issue at z = 0
def f(x, y, z):
    return z / (x**2 + y**2 + z**2)**(3/2)

x = np.linspace(-5, 5, 100)
y = np.copy(x)

X, Y = np.meshgrid(x, y)

fig = plt.figure()

ax = fig.add_subplot(2, 2, 1, projection = '3d')
ax.plot_surface(X, Y, f(X, Y, 0), cmap = cm.coolwarm)
ax.set_title("z = 0")

ax = fig.add_subplot(2, 2, 2, projection = '3d')
ax.plot_surface(X, Y, f(X, Y, 1), cmap = cm.coolwarm)
ax.set_title("z = 1")

ax = fig.add_subplot(2, 2, 3, projection = '3d')
ax.plot_surface(X, Y, f(X, Y, 3), cmap = cm.coolwarm)
ax.set_title("z = 3")

ax = fig.add_subplot(2, 2, 4, projection = '3d')
ax.plot_surface(X, Y, f(X, Y, 5), cmap = cm.coolwarm)
ax.set_title("z = 5")

plt.tight_layout()
fig.subplots_adjust(wspace = -0.3, hspace = 0.5)
plt.show()