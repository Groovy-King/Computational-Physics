from sympy import sqrt, N

"""
    For the Quantum step potential, the coefficients of reflection and transmission are:
        r_p = (p - p') / (p + p')
        t_p = 2*p / (p + p')
    where p and p' are the momenta on either side of the barrier. The corresponding probabilities are:
        R_p = |r_p|**2
        T_p = p' * |t_p|**2 / p 
    The values of these momenta are:
        p = sqrt( 2mE )
        p' - sqrt( 2m*(E-V) )
    The derivation of these results is given in 'Quantum Step Potential Derivation 1/2.png' attached in this folder.    
    
    This program asks the user to input the mass of the particle, the energy of the particle, and the potential barrier. 
    It then computes and prints the probabilities of reflection and transmission.
"""

m = float(input("Please enter the mass of the particle (in terms of electron mass): "))
E = float(input("Please enter the energy of the particle (in eV): "))
V = float(input("Please enter the potential barrier (in eV): "))

"""
    Note that it is not necessary to convert all quantities into their SI units. Since the coefficients are rational homogenous 
    functions of the momenta, we get the right answer as long as both momenta are calculated in the same units. 
"""

p_left = sqrt( 2*m*E )
p_right = sqrt( 2*m*(E - V) )

r_p = (p_left - p_right) / (p_left + p_right)
t_p = 2*p_left / (p_left + p_right)

R_p = abs(r_p)**2
T_p = p_right * abs(t_p)**2 / p_left

print(f"\nThe probability of Reflection is: {N(R_p, 5)}")
print(f"The probability of Transmission is: {N(T_p, 5)}")

print(f"For verification, the total probability is printed below: \n\tR_p + T_p = {N(R_p + T_p, 5)}")