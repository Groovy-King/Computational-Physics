import numpy as np

# Potential due to charges -1C at x = -5cm, and 1C at x = 5cm
def Potential(x, y, z):
    k = 1 # We set k = 1, to avoid any possible overflow errors
    r_Minus = np.sqrt(((x + 0.05)**2 + y**2 + z**2))
    r_Plus = np.sqrt(((x - 0.05)**2 + y**2 + z**2))
    if (r_Plus == 0) or (r_Minus == 0):
        return np.nan
    else:
        V_Minus = k * (-1) / r_Minus
        V_Plus = k * (1) / r_Plus
        return V_Plus + V_Minus
    
def Electric_Field(x, y, z, h, f = Potential):
    Ex = (f(x + h/2, y, z) - f(x - h/2, y, z)) / h
    Ey = (f(x, y + h/2, z) - f(x, y - h/2, z)) / h
    Ez = (f(x, y, z + h/2) - f(x, y, z - h/2)) / h
    return (-Ex, -Ey, -Ez)