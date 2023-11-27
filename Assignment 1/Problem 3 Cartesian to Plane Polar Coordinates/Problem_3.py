# pyright: reportGeneralTypeIssues = false
# pyright: reportUnboundVariable = false
from sympy import sqrt, atan, pi, N

"""
    We assume that both the x- and y-axes are scaled to 1 m per unit length in the Cartesian coordinate system.
    We use the following relations to obtain the values of r and theta:
        r = sqrt(x**2 + y**2)
        tan(theta) = y/x
    We assume that theta takes values in the range [0, 2*pi) (where 0 is included, but 2*pi is excluded). The explicit expressions
    for obtaining theta is given in 'Plane Polar Coordinates.png', saved in this folder. We use these expressions in the program below.
    
    Note that sympy's atan2() method chooses the correct quadrant and returns the right value of theta for given values of x, y.
    However, for the purposes of this exercise, we only use the ordinary atan() method, and choose the quadrant ourselves. 
"""

# Obtaining the values of x, y from the user
x = float(input("Please enter the value of x (in m): "))
y = float(input("Please enter the value of y (in m): "))

# Obtaining the values of r, theta
r = sqrt(x**2 + y**2)

# The output of the atan() method lies in the range (-pi/2, pi/2). Different cases for each quadrant are handled below:
if (x > 0) and (y > 0):
    theta = atan(y/x)
elif (x < 0) and (y > 0):
    theta = atan(y/x) + pi
elif (x < 0) and (y < 0):
    theta = atan(y/x) + pi
elif (x > 0) and (y < 0):
    theta = atan(y/x) + 2*pi
    
# We also handle the cases on the x- and y-axes
elif x == 0:
    if y == 0:
        raise ValueError("The value of Theta is undefined at the origin")
    elif y > 0:
        theta = pi/2
    else:
        theta = 3*pi/2

elif y == 0:
    if x > 0:
        theta = 0
    else:
        theta = pi
        
# We now convert the theta to degrees
theta_d = theta * 180 / pi 

print(f"The given point in Cartesian Coordinates is: \n\tx = {x} m \n\ty = {y} m \n")
print(f"The same point in Plane Polar Coordinates is: \n\tr = {N(r, 5)} m \n\ttheta = {N(theta_d, 5)} degrees")