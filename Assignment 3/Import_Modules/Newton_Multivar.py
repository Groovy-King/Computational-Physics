import sympy as smp
import numpy as np

def Newton_MultiVar(X, F, x_0, e_max, N_max = 50, TOL_Parameter = 'Absolute', print_out = False):
    if len(X) == len(F) is False:
        raise ValueError("Number of Unknowns is not equal to number of Equations!")
    
    x_prev = x_0
    success = 0
    
    n = len(X)
    J = []
    F_num = []
    for i in range(0, n):
        J.append([])
        F_num.append(smp.lambdify(X, F[i]))
        for j in range(0, n):
            J[i].append(smp.lambdify(X, smp.diff(F[i], X[j])))
    
    J_current = np.zeros((n, n))
    F_current = np.zeros(n)
    for k in range(0, N_max):
        for i in range(0, n):
            x_list = x_prev.tolist()
            F_current[i] = F_num[i](*x_list)
            for j in range(0, n):
                J_current[i, j] = J[j][i](*x_list)
        x_current = x_prev - np.array((np.linalg.inv(J_current) * np.matrix(F_current).T).T)[0]
        
        # Calculate the current error bound / tolerance level according to the parameter chosen by the user
        if TOL_Parameter.lower() == 'absolute':
            e = max(abs(x_current - x_prev))
            
        elif TOL_Parameter.lower() == 'relative':
            e = max(abs((x_current - x_prev) / x_current))
        
        # Update the value for the next iteration
        x_prev = x_current
        
        if print_out:
            # Prints the value after ith iteration
            print(f"The approximate root after {k} iterations is: {x_current}, with error: {e}")
        
        # Check if the desired tolerance level is achieved
        if (e < e_max):
            success = 1
            break
        
    if print_out: 
    # Prints the output
        if (success == 1):
            print(f"\nThe program successfully terminated in {k} iterations \nThe obtained root, within {TOL_Parameter.lower()} tolerance {e_max} is: {np.round(x_current, np.abs(int(np.log10(e_max))) + 1)}")

        else:
            print(f"The program was unable to find any roots in the interval within {N_max} iterations")

    # Returns the obtained value
    return x_current