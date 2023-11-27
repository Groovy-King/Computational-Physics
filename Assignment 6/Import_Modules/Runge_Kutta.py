import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

def Runge_Kutta_one_var(func, x0, y0, x_min, x_max, h, print_out = False):      
    x_up = np.linspace(x0, x_max, int((x_max - x0) / h) + 1)
    x_down = np.linspace(x0, x_min, -int((x_min - x0) / h) + 1)
    
    n_up = len(x_up)
    n_down = len(x_down)
    
    y_up = np.empty(n_up)
    y_down = np.empty(n_down)
    
    y_up[0] = y0
    y_down[0] = y0
    
    for i in np.arange(1, n_up):
        K1 = h * func(x_up[i - 1], y_up[i - 1])
        K2 = h * func(x_up[i - 1] + h/2, y_up[i - 1] + K1/2)
        K3 = h * func(x_up[i - 1] + h/2, y_up[i - 1] + K2/2)
        K4 = h * func(x_up[i - 1] + h, y_up[i - 1] + K3)
        y_up[i] = y_up[i - 1] + (K1 + 2 * K2 + 2 * K3 + K4) / 6
            
    
    for j in np.arange(1, n_down):
        K1 = h * func(x_down[j - 1], y_down[j - 1])
        K2 = h * func(x_down[j - 1] - h/2, y_down[j - 1] - K1/2)
        K3 = h * func(x_down[j - 1] - h/2, y_down[j - 1] - K2/2)
        K4 = h * func(x_down[j - 1] - h, y_down[j - 1] - K3)
        y_down[j] = y_down[j - 1] - (K1 + 2 * K2 + 2 * K3 + K4) / 6
    
    x_down = np.flipud(x_down)
    y_down = np.fliplr(y_down)
    
    x_sol = np.concatenate( [x_down[0:-1], x_up] )
    y_sol = np.concatenate( [y_down[0:-1], y_up] )
    
    if print_out:
        plt.plot(x_sol, y_sol, label = f'h = {h}')
        plt.title(f"Plotting the obtained solution")
        plt.xlabel("x")
        plt.ylabel("y(x)")
        plt.legend()    
        plt.show()
    
    return x_sol, y_sol

def Runge_Kutta_multi_var(func, x0, y0, x_min, x_max, h):    
    n = len(y0)

    x_up = np.linspace(x0, x_max, int((x_max - x0) / h) + 1)
    m_up = len(x_up)
    y_up = np.zeros((n, m_up))
    
    K1 = np.zeros(n)
    K2 = np.zeros(n)
    K3 = np.zeros(n)
    K4 = np.zeros(n)

    for z in range(0, n): 
        y_up[z, 0] = y0[z]
    
    for j in np.arange(1, m_up):
        for i in np.arange(0, n):
            K1[i] = h * func[i] (x_up[j - 1], y_up[:, j - 1])
        
        for i in np.arange(0, n):
            K2[i] = h * func[i] (x_up[j - 1] + h/2, y_up[:, j - 1] + K1/2)
            
        for i in np.arange(0, n):
            K3[i] = h * func[i] (x_up[j - 1] + h/2, y_up[:, j - 1] + K2/2)
            
        for i in np.arange(0, n):
            K4[i] = h * func[i] (x_up[j - 1] + h, y_up[:, j - 1] + K3)
            
        y_up[:, j] = y_up[:, j - 1] + (K1 + 2*K2 + 2*K3 + K4) / 6
        
    x_down = np.linspace(x0, x_min, abs(int((x0 - x_min) / h)) + 1)
    m_down = len(x_down)
    y_down = np.zeros((n, m_down))
    
    K1 = np.zeros(n)
    K2 = np.zeros(n)
    K3 = np.zeros(n)
    K4 = np.zeros(n)

    for z in range(0, n): 
        y_down[z, 0] = y0[z]
    
    for j in np.arange(1, m_down):
        for i in np.arange(0, n):
            K1[i] = h * func[i] (x_down[j - 1], y_down[:, j - 1])
        
        for i in np.arange(0, n):
            K2[i] = h * func[i] (x_down[j - 1] + h/2, y_down[:, j - 1] + K1/2)
            
        for i in np.arange(0, n):
            K3[i] = h * func[i] (x_down[j - 1] + h/2, y_down[:, j - 1] + K2/2)
            
        for i in np.arange(0, n):
            K4[i] = h * func[i] (x_down[j - 1] + h, y_down[:, j - 1] + K3)
            
        y_down[:, j] = y_down[:, j - 1] + (K1 + 2*K2 + 2*K3 + K4) / 6

    x_down = np.flipud(x_down)
    y_down = np.fliplr(y_down)
    
    x_sol = np.concatenate( [x_down[0:-1], x_up] )
    y_sol = np.concatenate( [y_down[:, :-1], y_up], axis = 1 )
        
    return (x_sol, y_sol)

def Runge_Kutta_Higher_Order(func, x0, y0, x_min, x_max, h):
    """
        This function solves an n-th order ODE by converting into a system of n first order ODEs.
    """
    n = len(y0)
    f = []
    
    for i in range(n - 1):
        def g(t, x):
            return x[i + 1]
        f.append(g)
    
    f.append(func)
    # Now, the list f contains the system of n first order ODEs, which can be solved by the 
    # method Runge_Kutta_multi_var()
    
    return Runge_Kutta_multi_var(f, x0, y0, x_min, x_max, h)

def One_step_RK4(func, x, y, h):

    k1 = h * func(x, y)
    k2 = h * func(x + 0.5*h, y + 0.5*k1)
    k3 = h * func(x + 0.5*h, y + 0.5*k2)
    k4 = h * func(x + h, y + k3)
    
    return (k1 + 2*k2 + 2*k3 + k4)/6

def Runge_kutta_Adaptive_step(func, x0, y0, xmax, emax, h0 = 10**(-3)):
    x = np.array([x0])
    y = np.copy(y0).reshape(-1, 1)
    H = np.array([h0])
        
    while x[-1] <= xmax:
        h = H[-1]
        x_c = x[-1]
        y_c = y[:, -1]
        
        y_step1 = y_c + One_step_RK4(func, x_c, y_c, h)
        y_step2 = y_step1 + One_step_RK4(func, x_c + h, y_step1, h)
        y_step_2h = y_c + One_step_RK4(func, x_c, y_c, 2*h)
        
        error = np.sqrt( np.sum( (y_step2 - y_step_2h)**2 ) )
        rho = 30*h*emax/error
        
        if rho >= 16:
            H = np.concatenate([H, [2*h]])
            x = np.concatenate([x, [x_c + h, x_c + 2*h]])
            
            y = np.concatenate( [y, y_step1.reshape(-1, 1)], axis = 1 )
            y = np.concatenate( [y, y_step2.reshape(-1, 1)], axis = 1 )
            
        elif rho >= 1:
            H = np.concatenate([H, [h*rho**(1/4)]])
            x = np.concatenate([x, [x_c + h, x_c + 2*h]])

            y = np.concatenate( [y, y_step1.reshape(-1, 1)], axis = 1 )
            y = np.concatenate( [y, y_step2.reshape(-1, 1)], axis = 1 )
        else:
            H[-1] = h*rho**(1/4)
        
    return (x, y, H)