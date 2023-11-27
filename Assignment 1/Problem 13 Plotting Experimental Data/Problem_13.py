# pyright: reportGeneralTypeIssues = false
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
    We use the library pandas to import the given dataset into python, and use matplotlib to
    subsequently plot the given data. The library numpy has also been used whenever any 
    manipulations were required.
"""

sunspots_data = pd.read_csv(r'Assignment 1\sunspots.txt', sep = '\t', header = None, names = ['Month', 'Sunspot_Number'])

# Part (a)
plt.plot(sunspots_data['Month'], sunspots_data['Sunspot_Number'])

plt.grid()
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title('Plot of Sunspot Number vs Month, since Jan 1749')
plt.show()

# Part (b): First 1000 points
plt.plot(sunspots_data.loc[0:999, 'Month'], sunspots_data.loc[0:999, 'Sunspot_Number']) # The slicing [0:999] includes both indices 0 and 999. It has exactly 1000 points.

plt.grid()
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title('Plot showing only the first 1000 points')
plt.show()


# Part (c): Runnning average with r = 5
y_data = sunspots_data.loc[0:999, 'Sunspot_Number'].copy()
r = 5

for i in np.arange(r, 999 - r):
    y_data[i] = np.sum(sunspots_data.loc[i - r: i + r, 'Sunspot_Number']) / (2*r + 1) # Assuming the sum goes from -r to r, there are 2r + 1 entries

plt.plot(sunspots_data.loc[0:999, 'Month'], sunspots_data.loc[0:999, 'Sunspot_Number'], label = 'Observed Data', linewidth = 0.75)
plt.scatter(sunspots_data.loc[0:999, 'Month'], y_data, c = 'k', marker = 'x', label = 'Running Average', s = 10)

plt.grid()
plt.xlabel('Month')
plt.ylabel('Sunspot Number')
plt.title('Plot showing data points and running average')
plt.legend()
plt.show()