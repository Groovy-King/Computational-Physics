import numpy as np

def fixed_point_multi_var(f, x0, e_max = 10**(-6), n_max = 50, args = [], print_err = False, multi_var = False):
    x = x0
    for i in range(0, n_max):
        if args == []:
            x_next = f(x)
        else:
            x_next = f(x, *args)
        
        if multi_var:
            err = max(abs(x - x_next))
        else:
            err = abs(x - x_next)
        
        if err <= e_max:
            break
        
        x = x_next
    if (i == n_max - 1) and print_err:
        print(f"The program failed to converge within {i} iterations")
    return x, i 
    