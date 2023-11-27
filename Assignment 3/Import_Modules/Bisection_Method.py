import numpy as np
import sympy as smp

from scipy.optimize import fsolve

def bisection_method(func, a, b, e_max, N_max = 50, TOL_Parameter = 'absolute', f_symbolic = False):   
    print("\n------------------------------------")
    print("\t Bisection Method")
    print("------------------------------------")
    
    # Converts symbolic function into python function
    if f_symbolic:
        x = func[0]
        func = func[1]
        func_num = smp.lambdify(x, func) 
    else:
        func_num = func
    
    # Initialize the variables p, up, down, the 'index' variable i and the success indicator
    p = 0
    up = b
    down = a
    i = 1
    success = 0
    
    # Iterate the bisection method algorithm up to a maximum of N_max iterations
    while (i < N_max):
        # Set p equal to the midpoint of the current interval 
        p = down + (up - down) / 2
        
        # Prints the value after ith iteration
        print(f"The approximate root after {i} iterations is: {p}")
        
        # Calculate the current error bound / tolerance level according to the parameter chosen by the user
        if TOL_Parameter.lower() == 'absolute':
            e = np.abs(up - down)/2
            
        elif TOL_Parameter.lower() == 'relative':
            e = np.abs((up - down) / min([np.abs(up), np.abs(down)]))
            
        else:
            print("Please enter a valid method to calculate the error")
            return
        
        # Check if p is a root, or if the desired tolerance level is achieved
        if (func_num(p)==0) or (e < e_max):
            success = 1
            break 
        
        # Checks if the root lies between down and p
        elif (( np.sign(func_num(p)) * np.sign(func_num(down)) ) < 0):
            up = p
        
        # If the above check was false, the root lies between p and up
        else:
            down = p
              
        # Increments the index i before the next iteration
        i = i + 1
       
    # Prints the output
    if (success == 1) is False:
        print(f"The program was unable to find any roots in the interval within {N_max} iterations")
           
    # Returns the obtained value
    return p