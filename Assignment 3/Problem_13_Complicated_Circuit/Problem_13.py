import numpy as np
import cmath as cm

"""
    The system of equations to be solved in given in the Figure 
    'Part (a) System of Equations Derivation.png'. We define a numpy array to model this system
    and then use np.linalg.solve to get the solution for the Vj's. We then use abs(), cmath's 
    phase method to get the amplitude, and phase of the resulting Voltages.
"""

# Defining the relevant constants
R1 = 10**3 # in Ohms
R3 = 10**3 # in Ohms
R5 = 10**3 # in Ohms
R2 = 2 * 10**3 # in Ohms
R4 = 2 * 10**3 # in Ohms
R6 = 2 * 10**3 # in Ohms
C1 = 10**(-6) # in Farads
C2 = 0.5 * 10**(-6) # in Farads
x_plus = 3 # in Volts
w = 1000 # in s**(-1)
j = 1j # Defining the complex number i

eq1 = np.array([1/R1 + 1/R4 + j*w*C1, -j*w*C1, 0])
eq2 = np.array([-j*w*C1, 1/R2 + 1/R5 + j*w*(C1 + C2), -j*w*C2])
eq3 = np.array([0, -j*w*C2, 1/R3 + 1/R6 + j*w*C2])

x = np.linalg.solve(np.array([eq1, eq2, eq3]), np.array([x_plus/R1, x_plus/R2, x_plus/R3]))
print("The solution to the given system is: ")
print(f"\tx1 = {x[0]}")
print(f"\tx2 = {x[1]}")
print(f"\tx3 = {x[2]}")

print("\n\nThe Amplitudes and Phases of these solutions are: ")
print(f"\tV1: Amplitude = {np.round(abs(x[0]), 4)} V, Phase = {np.round(cm.phase(x[0]) * 180 / np.pi, 4)} degrees")
print(f"\tV2: Amplitude = {np.round(abs(x[1]), 4)} V, Phase = {np.round(cm.phase(x[1]) * 180 / np.pi, 4)} degrees")
print(f"\tV3: Amplitude = {np.round(abs(x[2]), 4)} V, Phase = {np.round(cm.phase(x[2]) * 180 / np.pi, 4)} degrees")

print("\n\nThe Voltages as a function of time are: ")
print(f"\t V1(t) = {np.round(abs(x[0]), 4)} exp(iwt + {np.round(cm.phase(x[0]), 4)})")
print(f"\t V2(t) = {np.round(abs(x[1]), 4)} exp(iwt + {np.round(cm.phase(x[1]), 4)})")
print(f"\t V3(t) = {np.round(abs(x[2]), 4)} exp(iwt + {np.round(cm.phase(x[2]), 4)})")