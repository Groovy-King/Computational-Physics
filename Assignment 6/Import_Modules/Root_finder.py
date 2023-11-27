import numpy as np
import sympy as smp

from scipy.optimize import fsolve

def Root_finder(func, guess_1, guess_2 = 0, e_max = 10**(-6), N_max = 50, TOL_Parameter = 'absolute', method = 'secant', f_symbolic = False, print_out = False):
    allowed_methods = ['secant', 'regula falsi', 'newton', 'modified newton', 'fixed point']
    if not(method.lower() in allowed_methods):
        print("Please give a valid input method")
        return
    
    if print_out:
        print("\n------------------------------------")
        print(f"\t {method.capitalize()} Method")       
        print("------------------------------------")
    
    # Converts symbolic function into python function
    if f_symbolic:
        x = func[0]
        func = func[1]
        func_num = smp.lambdify(x, func) 
    else:
        func_num = func

    # Initialize the variables to store current and previous values, the 'index' variable i and the success indicator
    x_next = 0
    i = 1
    success = 0
    
    # Finds the derivative symbolically and then converts it into a python function
    if method.lower() == 'newton':
        dfdx = smp.diff(func, x)
        dfdx_num = smp.lambdify(x, dfdx)
        x_prev = guess_1
        x_current = x_prev - func_num(x_prev)/dfdx_num(x_prev)
        
    # Finds the first and second derivatives symbolically and then converts it into python functions
    elif method.lower() == 'modified newton':
        dfdx = smp.diff(func, x)
        dfdx_num = smp.lambdify(x, dfdx)
        d2fdx2 = smp.diff(func, x, 2)
        d2fdx2_num = smp.lambdify(x, d2fdx2)
        x_prev = guess_1
        y_prev = func_num(x_prev)
        y_prime_prev = dfdx_num(x_prev)
        y_prime_2_prev = d2fdx2_num(x_prev)
        x_current = x_prev - y_prev*y_prime_prev / (y_prime_prev**2 - y_prev*y_prime_2_prev)
    
    # Initializes the first iteration using the second guess for secant method
    elif method.lower() == 'secant':
        x_prev = guess_1
        x_current = guess_2
        y_prev = func_num(guess_1)    
    
    # Checks where the root is located and appropriately chooses the fixed point
    elif method.lower() == 'regula falsi':
        y_1 = func_num(guess_2)
        y_0 = func_num(guess_1)
        x_current = guess_2 - y_1 * (guess_2 - guess_1) / (y_1 - y_0)
        if (np.sign(func_num(x_current)) * np.sign(y_0) < 0):
            fixed_x = guess_1
            fixed_y = y_0
            x_prev = fixed_x
        elif (func_num(x_current) == 0):
            i = -1
            success = 1
        else:
            fixed_x = guess_2
            x_prev = fixed_x
            fixed_y = y_1
            
    elif method.lower() == 'fixed point':
        x_prev = (guess_1 + guess_2) / 2
        x_current = func_num(x_prev)
            
     
    # Iterate the bisection method algorithm up to a maximum of N_max iterations
    while (i <= N_max) and (i >= 0):
        # Calculate the value of f(x) at the current guess
        y_current = func_num(x_current)
        
        # Calculate the current error bound / tolerance level according to the parameter chosen by the user
        if TOL_Parameter.lower() == 'absolute':
            e = np.abs(x_current - x_prev)
            
        elif TOL_Parameter.lower() == 'relative':
            e = np.abs((x_current - x_prev) / x_current)
            
        else:
            print("Please enter a valid method to calculate the error")
            return
        
        if print_out:
            # Prints the value after ith iteration
            print(f"The approximate root after {i} iterations is: {x_current}, with error: {e}")
        
        # Check if x_current is a root, or if the desired tolerance level is achieved
        if (y_current == 0) or (e < e_max):
            success = 1
            break
        
        # If x_current is NOT a root, we update all the values in the variables according to the algorithm of secant method
        if method.lower() == 'secant':
            x_next = x_current - y_current * (x_current - x_prev) / (y_current - y_prev)
            x_prev = x_current
            x_current = x_next
            y_prev = y_current
            
        elif method.lower() == 'regula falsi':
            x_prev = x_current
            x_current = x_current - y_current * (x_current - fixed_x) / (y_current - fixed_y)
            
        elif method.lower() == 'newton':
            y_prime_current = dfdx_num(x_current)
            if y_prime_current == 0:
                print("Divide by zero encountered. Please try a different method")
                success = -1
                break
            else:
                x_prev = x_current
                x_current = x_current - y_current/y_prime_current
        
        elif method.lower() == 'modified newton':
            y_prime_current = dfdx_num(x_current)
            y_prime_2_current = d2fdx2_num(x_current)
            x_prev = x_current
            x_current = x_current - y_current*y_prime_current / (y_prime_current**2 - y_current*y_prime_2_current)
            
        elif method.lower() == 'fixed point':
            x_prev = x_current
            x_current = y_current
               
        # Finally, we increment the iterator variable before proceeding to the next iteration
        i = i + 1
    
    if print_out: 
        # Prints the output
        if (success == 1):
            print(f"\nThe program successfully terminated in {np.abs(i)} iterations \nThe obtained root, within {TOL_Parameter.lower()} tolerance {e_max} is: {np.round(np.array(x_current), np.abs(int(np.log10(e_max))) + 1)}")
            p_std = fsolve(func_num, x_current, xtol = e_max*0.01)
            print(f"The root obtained using standard python library function fsolve is: {np.round(np.array(p_std[0]), np.abs(int(np.log10(e_max))) + 1)}")
        
        else:
            print(f"The program was unable to find any roots in the interval within {N_max} iterations")
    
    # Returns the obtained value
    return x_current