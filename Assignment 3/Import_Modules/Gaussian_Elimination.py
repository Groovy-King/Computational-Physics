import numpy as np

def Gaussian_Elim(M, w, pivoting = 'None', banded = None):
    """
        This function solves the system of linear equations: Ax = b using the method of 
        Gaussian Elimination. We assume that the system given is consistent and has a unique 
        solution.
    """
    A = np.copy(M)
    b = np.copy(w)
    if pivoting.lower() not in ['none', 'partial']:
        raise ValueError("Enter a valid pivoting method!")
    
    n = len(b)
    x = np.empty(n)
    
    # Getting the row reduced form
    for i in range(0, n):
        if pivoting.lower() == 'partial':
            i_temp = i + np.argmax(abs(A[i:n, i]))
            temp_A = np.copy(A[i])
            temp_b = b[i]
            A[i] = np.copy(A[i_temp])
            b[i] = b[i_temp]
            A[i_temp] = np.copy(temp_A)
            b[i_temp] = temp_b
            
        # We now set all the diagonal entries to 1
        b[i] = b[i] / A[i, i] 
        A[i] = A[i] / A[i, i] 

        # If the given matrix is banded with b rows below the ith row,
        # we only need to perform the algorithm on the next b rows.
        if banded == None:
            m = n
        else:
            m = min(i + 1 + banded, n)
        
        # This loop diagonalizes the matrix A    
        for j in range(i + 1, m):
            b[j] = b[j] - b[i] * A[j, i] 
            A[j] = A[j] - A[i] * A[j, i]            
    
    # We now perform backsubstitution to get the solution x
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i, j] * x[j]

    return x