import sys
sys.path.insert(0, '.')

from Problem_11_Diffusion_Limited_Aggregation.DLA_Original import DLA_Original

# Finally, we simulate the original DLA Problem mentioned in the question.
Run_3 = DLA_Original(101)

Run_3.New_Particle(1000)
Run_3.plot()