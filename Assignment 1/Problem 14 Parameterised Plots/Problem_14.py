import numpy as np
import matplotlib.pyplot as plt

"""
    In this problem, we take advantage of numpy arrays, which allow us to perform element-wise
    operations on entire arrays seamlessly. We use the method np.linspace() to create the desired
    array of theta values, and then use python expressions to subsequently calculate x, y, r and 
    the transformations.
"""

# Part (a)
theta = np.linspace(0, 2*np.pi, 1000, endpoint = False) # 2pi not included, as mentioned in problem

x = 2 * np.cos(theta) + np.cos(2*theta)
y = 2 * np.sin(theta) - np.sin(2*theta)

plt.plot(x, y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parameterised Plot')
plt.show()

# Part (b)
# We first create an array for theta. Then, using this array, we calculate the values of r.
# Using these two arrays, we subsequently transform to cartesian coordinates.
theta = np.linspace(0, 10*np.pi, 1000, endpoint = True)
r = theta**2

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(left = -800, right = 800)
plt.ylim(bottom = -800, top = 800)
plt.title('Galilean Spiral')
plt.show()

# Part (c)
# We follow the same steps as before
theta = np.linspace(0, 24*np.pi, 1000, endpoint = True)
r = np.exp(np.cos(theta)) - 2 * np.cos(4*theta) + np.sin(theta/12)**5

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Fey's Function")
plt.show()