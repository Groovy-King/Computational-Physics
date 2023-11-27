import sys
sys.path.insert(0, '.')

from Problem_11_Diffusion_Limited_Aggregation.DLA_class import DLA_Simulation

# We simulate 20 particles on a 101 x 101 lattice. We do not simulate fully, as it takes
# extremely long time for the program to complete.
Run_1 = DLA_Simulation(101)

Run_1.Simulate_Full(nmax = 3000)

# We now simulate the problem completely on a 75 x 75 lattice, as this takes much smaller time
# to finish.
#Run_2 = DLA_Simulation(75)

#Run_2.Simulate_Full(nmax = 1000)

