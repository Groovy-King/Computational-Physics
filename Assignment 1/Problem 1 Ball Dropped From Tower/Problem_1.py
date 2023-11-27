from numpy import sqrt, round

"""
    We know that the position of a body under free fall is given by:
        y = u*t + (1/2)*g*t**2
    where y is defined in 'Ball on tower.png', u is the initial velocity,and g is the acceleration
    due to gravity. Using this result, the time taken for a ball to travel a 'h' meters,
    under free fall (u = 0) is:
        t_FreeFall = sqrt(2*h/g)
    The following program asks the user to input the height of the tower in meters, and using 
    g = 9.81 m/s**2 in the above result, calculates and prints the time taken to hit the ground. 
"""

# Defining the acceleration due to gravity
g = 9.81

# Getting the height of the tower from the user
h = float(input("Please enter the height of the tower in meters: "))

t_FreeFall = sqrt(2 * h / g)

print(f"The time taken for a ball to fall freely from a tower of height {h} m is: {round(t_FreeFall, 4)} s")

