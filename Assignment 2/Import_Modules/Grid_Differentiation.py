import numpy as np

def Derivative(data, h):
    der_x = np.zeros(data.shape)
    der_y = np.copy(der_x)
    n_x, n_y = der_x.shape
    for i in range(0, n_x):
        for j in range(0, n_y):
            if i == 0:
                der_x[n_x - 1 - i][j] = (data[i + 1][j] - data[i][j]) / h
            elif i == n_x - 1:
                der_x[n_x - 1 - i][j] = (data[i][j] - data[i - 1][j]) / h
            else:
                der_x[n_x - 1 - i][j] = (data[i + 1][j] - data[i - 1][j]) / (2 * h)
            
            if j == 0:
                der_y[n_x - 1 - i][j] = (data[i][j + 1] - data[i][j]) / h
            elif j == n_y - 1:
                der_y[n_x - 1 - i][j] = (data[i][j] - data[i][j - 1]) / h
            else:
                der_y[n_x - 1 - i][j] = (data[i][j + 1] - data[i][j - 1]) / (2 * h)
    
    return der_x, der_y