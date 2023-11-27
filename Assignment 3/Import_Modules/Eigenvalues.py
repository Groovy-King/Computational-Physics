import numpy as np
import sys
sys.path.insert(0, '.')

from Import_Modules.QR_using_MGS import QR_MGS

def Eigen(A, e_max, N_max = 20):
    n = A.shape[0]
    temp = np.copy(A)
    success = 0
    
    V = np.matrix(np.identity(n))
    
    for k in range(0, N_max):
        Q, R = QR_MGS(np.array(temp), n)
        temp = R*Q
        V = V*Q
        
        test = np.copy(temp)
        for i in range(0, n):
            test[i, i] = 0
        
        if abs(test).max() < e_max:
            success = 1
            break
    
    if success == 0:
        print(f'The program failed to converge within {N_max} iterations!')
        return
    else:
        return temp, V