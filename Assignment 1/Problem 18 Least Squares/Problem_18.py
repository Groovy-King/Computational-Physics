import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
    Here, we use the method of least squares to fit observed data from a 
    historic experiment on the photoelectric effect performed by Millikan. The data is given in
    the file 'millikan.txt', which would be read using the pandas module. Then, we use the
    expressions given in the problem to obtain the line of best fit.
"""

data = pd.read_csv(r"Assignment 1\millikan.txt", sep = ' ', header = None, names = ['Frequency', 'Voltage'])

# Part (b)
N = len(data['Frequency'])
Ex = np.sum(data['Frequency']) / N
Ey = np.sum(data['Voltage']) / N
Exx = np.sum(data['Frequency']**2) / N
Eyy = np.sum(data['Voltage']**2) / N
Exy = np.sum(data['Frequency'] * data['Voltage']) / N

m = (Exy - Ex * Ey) / (Exx - Ex**2)
c = (Exx * Ey - Ex * Exy) / (Exx - Ex**2)

print(f"From Least squares, we get:\n\t m = {m}\n\t c = {c} V/Hz") 


# Part (a)
plt.scatter(data['Frequency'], data['Voltage'], c = 'k', label = 'Given Data')
plt.grid()
plt.xlabel('Frequency (in Hz)')
plt.ylabel('Voltage (in V)')
plt.title('Observed Data for Photoelectric effect')
plt.show()

# Part (c)
y_fit = m * data['Frequency'] + c

plt.scatter(data['Frequency'], data['Voltage'], c = 'k', label = 'Given Data')
plt.plot(data['Frequency'], y_fit, c = 'b', label = 'Least Squares Fit')
plt.grid()
plt.xlabel('Frequency (in Hz)')
plt.ylabel('Voltage (in V)')
plt.title('Least Squares Fitting for Photoelectric effect')
plt.legend()
plt.show()

# Part (d)
# Using the given equation, the slope of the V-f plot is: h/e
# Thus, the value of h can be calculated as: h = slope * e
e = 1.602 * 10**(-19)
h_calc = m * e
print(f"\nThe Calculated value of Planck's constant is: h = {h_calc} J-s")

h_std = 6.626 * 10**(-34)
print(f"The Standard value of Planck's constant is: h_std = {h_std} J-s")

print(f"The deviation in the calculated value of h is: {np.abs(h_std - h_calc) * 100 / h_std} %")