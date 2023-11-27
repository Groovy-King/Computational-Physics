import numpy as np
import cmath as cm
from math import factorial

def f(z):
    return cm.exp(2 * z)

j = complex(0, 1)
N = 10**4
Theta_k = np.arange(0, 2 * np.pi, 2 * np.pi / N)
Zk = np.array([cm.exp(j * theta) for theta in Theta_k])

for m in range(1, 21):
    der = 0
    for k in range(0, N):
        der += f(Zk[k]) * cm.exp(-j * 2 * np.pi * k * m / N)
    der = der * factorial(m) / N
    print(f"The {m}-order Derivative of f at zero is: {der.real}")
