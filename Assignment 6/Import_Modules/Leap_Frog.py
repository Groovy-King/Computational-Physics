import numpy as np
import matplotlib.pyplot as plt

def Leap_Frog_Multi_Var(func, x0, y0, y_half, xmax, h):
    n = len(y0)
    
    x_sol = np.linspace(x0, xmax, int((xmax - x0) / h) + 1)
    m = len(x_sol)
    
    y_sol = np.zeros((n, m))
    y_sol_half = np.copy(y_sol)
    
    y_sol[:, 0] = y0
    y_sol_half[:, 0] = y_half
    
    for i in range(1, m):
        y_sol[:, i] = y_sol[:, i - 1] + h*func(x_sol[i - 1] + h/2, y_sol_half[:, i - 1])
        y_sol_half[:, i] = y_sol_half[:, i - 1] + h*func(x_sol[i], y_sol[:, i])
    
    return x_sol, y_sol, y_sol_half

def Verlet(func, x0, y0, v_half, xmax, h):
    n = len(y0)
    
    x_sol = np.linspace(x0, xmax, int((xmax - x0) / h) + 1)
    m = len(x_sol)
    
    y_sol = np.zeros((n, m))
    v_sol_half = np.copy(y_sol)
    v_sol = np.copy(y_sol)
    
    y_sol[:, 0] = y0
    v_sol_half[:, 0] = v_half
    v_sol[:, 0] = v_half
    
    for i in range(1, m):
        y_sol[:, i] = y_sol[:, i - 1] + h*v_sol_half[:, i - 1]
        
        k = h*func(x_sol[i], y_sol[:, i])
        v_sol_half[:, i] = v_sol_half[:, i - 1] + k
        v_sol[:, i] = v_sol_half[:, i - 1] + k/2
    
    return x_sol, y_sol, v_sol, v_sol_half 