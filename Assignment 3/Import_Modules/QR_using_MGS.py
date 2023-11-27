import numpy as np

"""
    This module defines the function QR_MGS(), which calculates the QR decomposition of a matrix
    using the Modified Gram-Schimdt method.
"""

def QR_MGS(A, n):
    v = []
    R = np.zeros((n, n))
    Q = np.empty((n, n))
    for i in range(0, n):
        v.append(A[:, i])
        
    for i in range(0, n):
        R[i, i] = np.linalg.norm(v[i])
        Q[i] = v[i] / R[i, i]
        
        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[i], v[j])
            v[j] = v[j] - R[i, j] * Q[i]
    
    Q = np.matrix(Q).transpose()
    R = np.matrix(R)
    
    return Q, R