import numpy as np

import sys
sys.path.insert(0, '.')

from Import_Modules.Integration import num_int, Trapz_Error, Romberg

cnvrg = 0
err_des = 10**(-6)
def f(x):
    return np.sin(np.sqrt(100 * x))**2

for i in np.arange(1, 15):
    x = np.linspace(0, 1, 2**i)
    y = f(x)
    I = num_int(x, y, method = 'Trapezoidal')
    err, I1, I2 = Trapz_Error(f, 0, 1, 2**i)
    print(f"n = {2**i} \tI = {I}\terr = {err}")
    if err <= err_des:
        cnvrg = 1
        break

if cnvrg == 0:
    print("\nThe intergral did not converge to within the desired error limit even with 2**15 intervals!")
else:
    print(f"\nAfter {i} iterations, the integral converged with {2**i} intervals.")
    print(f"The value of the integral is: I = {I}, and the error is: err = {err}")
    
# Part (b) Romberg Integration
print("\n----------------------------------")
print("\tRomberg Integration")
print("----------------------------------")
r, j, err = Romberg(0, 1, 10**(-6), 10, f)
for i in range(0, j + 1):
    print(*r[i, 0 : i])
    
print(f"\nThe value obtained from Romberg Integration is: I = {r[j, j]}, with error, err = {err[j]}")