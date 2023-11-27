import numpy as np

"""
    Since the question asks for multiple modifications of the program, we create four different
    methods (one for each sub-part). The first method is the simplest one, it calculates the 
    Binding energy, given the values of A and Z. Each of the next methods calls on this method to
    calculate and the print the relevant results.
"""

# Defining the appropriate constants
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

def binding_energy(A, Z):
    if A % 2 == 1:
        a5 = 0
    elif Z % 2 == 0:
        a5 = 12
    else:
        a5 = -12
    
    B = a1 * A - a2 * A**(2/3) - a3 * Z**2 / A**(1/3) - a4 * (A - 2*Z)**2 / A + a5 / A**(1/2)
    return B

def binding_energy_per_nucleon(A, Z):
    B = binding_energy(A, Z)
    return B / A

def stable_nucleus(Z):
    A = np.arange(Z, 3*Z + 1)
    b = []
    for a in A:
        b.append(binding_energy_per_nucleon(a, Z))
    A_stable = A[b == max(b)]
    return [A_stable, max(b)]

def maximum_binding_energy():
    Z = np.arange(1, 101)
    A_stable = []
    b_max = []
    
    for z in Z:
        a, b = stable_nucleus(z)
        A_stable.append(a)
        b_max.append(b)
        print(f"The most stable nucleus with Z = {z} has mass number A = {a}")
    
    Z_max = Z[b_max == max(b_max)]    
    return Z_max[0], max(b_max)

# Now, we ask the user to choose which subpart of the problem they need to solve
# And the corresponding method is called.

sub_part = input("Please enter the subpart you wish to solve: ")
allowed_Sub_parts = ['a', 'b', 'c', 'd']
if sub_part.lower() not in allowed_Sub_parts:
    raise ValueError("Please enter a valid subpart!")

if sub_part.lower() == 'a':
    A = int(input("Please enter the mass number: "))
    Z = int(input("Please enter the atomic number: "))
    print(f"\nThe binding energy of an atom with A = {A}, and Z = {Z}, is: {np.round(binding_energy(A, Z), 4)} MeV")

elif sub_part.lower() == 'b':
    A = int(input("Please enter the mass number: "))
    Z = int(input("Please enter the atomic number: "))
    print(f"\nThe binding energy per nucleon of an atom with A = {A}, and Z = {Z}, is: {np.round(binding_energy_per_nucleon(A, Z), 4)} MeV/nucleon")
    
elif sub_part.lower() == 'c':
    Z = int(input("Please enter the atomic number: "))
    A, b = stable_nucleus(Z)
    print(f"\nThe mass number of the most stable nucleus with Z = {Z} is A = {A[0]}")
    print(f"The binding energy per nucleon of such an atom is: {b}")

elif sub_part.lower() == 'd':
    print()
    z_max, b_max = maximum_binding_energy()
    print(f"\nThe most stable nucleus with Z <= 100 is: Z = {z_max}")
    print(f"The binding energy per nucleon of the most stable nucleus is: {b_max} MeV/nucleon")
    