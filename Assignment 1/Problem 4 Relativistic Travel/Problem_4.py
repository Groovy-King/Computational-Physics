from numpy import sqrt
"""
    An observer on earth sees the space ship travel at a speed v toward the planet x light years away. Thus, in this frame,
    the time taken to reach the destination would simply be (x light years) / v. However, in the spaceship frame, the distance 
    between Earth and the destination is Lorentz contracted by a factor 'g' ( = sqrt(1 / (1 - v**2/c**2)) ). The spaceship also sees 
    the Earth and the planet moving at a speed v. Therefore, the time elapsed in the spaceship frame would be (x light years) / (g * v),
    after accounting for the Lorentz contraction. This same result can also be obtained by arguing that as seen from the earth frame,
    the clock aboard the spaceship runs slower by a factor of 'g', and hence would read ( (x light years) / v ) / g, at the end of the 
    journey.
    
    The following program uses these results to calculate the time taken in each frame for such a journey, given the values of x and v.
"""

# Asking the user to input the relevant values
x = float(input("Please enter the distance between Earth and the planet (in light years): "))
beta = float(input("Please enter the speed of the spaceship (as a fraction of speed of light): ")) 

# Calculating the time taken in each frame
t_Earth = x / beta  # This gives the time taken in years

gamma = 1/sqrt(1 - beta**2)
t_Spaceship = t_Earth / gamma  # This also gives the time taken in years

print(f"\nThe time taken in Earth's reference frame is: {t_Earth} years") 
print(f"The time taken in the Spaceship's reference frame is: {t_Spaceship} years") 