import sympy as smp
import numpy as np

def num_int(x, y, method = 'Trapezoidal'):
    allowed_methods = ['trapezoidal', 'simpson']
    if method.lower() not in allowed_methods:
        raise ValueError("Please enter a valid method to evaluvate the integral nemrically!")
    
    n = len(x)
    h = (max(x) - min(x)) / (n - 1)
    
    if method.lower() == 'trapezoidal':
        int_num = h*( np.sum(y) ) - h*( y[0] + y[n - 1] ) / 2
    elif method.lower() == 'simpson':
        if n%2 == 0:
            raise ValueError("The number of desired subintervals must be even to apply Simpson's Rule!")
        sum = y[0] + y[n - 1]
        for i in np.arange(1, n - 1):
            if i%2 == 0:
                sum = sum + 2*y[i]
            else:
                sum = sum + 4*y[i]
        int_num = h * sum / 3
    
    return int_num 


def Romberg(a, b, eps, nmax, func):
    h = np.zeros(nmax)
    err = np.copy(h)
    for i in range(0, nmax):
        h[i] = (b - a)/(2**i)
    r = np.zeros( ( nmax, nmax ) )
    r[0, 0] = (b - a) * ( func(a) + func(b )) / 2
    for j in range(1, nmax):
        subtotal = 0
        for i in range(0, 2**(j -1)):
            subtotal = subtotal + func (a + (2*i + 1) * h[j])
        r[j, 0] = r[j - 1, 0]/2 + h[j] * subtotal
        for k in range(1, j + 1):
            r[j, k] = (4**(k) * r[j, k - 1] - r[j - 1, k - 1]) / (4**(k) - 1)
            
        err[j] = abs(r[j, j - 1] - r[j - 1, j - 1]) / abs(2**(2*j) - 1)
        if err[j] <= eps:
            break
    return r, j, err     
    
def Trapz(f, a, b):
    h = abs(b - a) / 2
    return h * (f(a) + f(b))

def Recursive_Trapz(f, a, b, err, int_whole):
    c = (a + b) / 2
    h = abs(c - a) / 2
    int_left = h * (f(a) + f(c))
    int_right = h * (f(c) + f(b))
    if abs(int_left + int_right - int_whole) <= 15 * err:
        return int_left + int_right + (int_left + int_right - int_whole) / 15
    else:
        return Recursive_Trapz(f, a, c, err/2, int_left) + Recursive_Trapz(f, c, b, err/2, int_right)

def Adaptive_Trapz(f, a, b, err):
    """
        This method calculates the integral using the adaptive quadrature for trapezoid rule. It
        calls upon the function Recursive_Trapz(), which recursively calculates the integral by
        trapezoidal rule for each sub-interval determined by the adaptive quadrature.
    """
    h = abs(b - a) / 2
    int_whole = h * (f(a) + f(b))
    
    return Recursive_Trapz(f, a, b, err, int_whole)

def Simpson(f, a, b):
    c = (a + b) / 2
    h = abs(b - a) / 6
    return h * (f(a) + 4 * f(c) + f(b))

def Recursive_Simpson(f, a, b, err, int_whole):
    c = (a + b) / 2
    int_left = Simpson(f, a, c)
    int_right = Simpson(f, c, b)
    if abs(int_left + int_right - int_whole) <= 15 * err:
        return int_left + int_right + (int_left + int_right - int_whole) / 15
    else:
        return Recursive_Simpson(f, a, c, err/2, int_left) + Recursive_Simpson(f, c, b, err/2, int_right)

def Adaptive_Simpson(f, a, b, err):
    """
        This method calculates the integral using the adaptive quadrature for Simpson rule. It
        calls upon the function Recursive_Simpson(), which recursively calculates the integral by
        Simpson rule for each sub-interval determined by the adaptive quadrature.
    """
    int_whole = Simpson(f, a, b)
    
    return Recursive_Trapz(f, a, b, err, int_whole)

def Trapz_Error(f, a, b, n):
    x_1 = np.linspace(a, b, n + 1) # To get n slices, we use n + 1 points in the x-array
    y_1 = f(x_1)
    I_1 = num_int(x_1, y_1)

    x_2 = np.linspace(a, b, 2*n + 1) # To get n slices, we use n + 1 points in the x-array
    y_2 = f(x_2)
    I_2 = num_int(x_2, y_2)

    h_1 = (max(x_1) - min(x_1)) / 10
    h_2 = (max(x_2) - min(x_2)) / 20

    e = (I_1 - I_2) * h_2**2 / (h_2**2 - h_1**2)
    return abs(e), I_1, I_2

def Simpson_Error(f, a, b, n):
    x_1 = np.linspace(a, b, n + 1) # To get n slices, we use n + 1 points in the x-array
    y_1 = f(x_1)
    I_1 = num_int(x_1, y_1, method = 'Simpson')

    x_2 = np.linspace(a, b, 2*n + 1) # To get n slices, we use n + 1 points in the x-array
    y_2 = f(x_2)
    I_2 = num_int(x_2, y_2, method = 'Simpson')

    h_1 = (max(x_1) - min(x_1)) / 10
    h_2 = (max(x_2) - min(x_2)) / 20

    e = (I_1 - I_2) * h_2**4 / (h_2**4 - h_1**4)
    return abs(e), I_1, I_2