from numpy.random import default_rng
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import seaborn as sns
sns.set_style('darkgrid')

rng = default_rng()

def Dimer_covering(T0, Lx, Ly, title, exponential_cooling = False, tau = 5, n_max = 10**3, freq = 30):
    # We create a numpy array to store the positions of the dimers
    dimers = []
    occupied_points = []
    direction = ["horizontal", "vertical"]

    fig = plt.figure()
    ax = plt.gca()
    x_plot = np.arange(-0.5, Lx)
    y_plot = np.arange(-0.5, Ly)

    def clear_lattice():
        ax.set_xlim(-0.6, Lx - 0.4)
        ax.set_ylim(-0.6, Ly - 0.4)
        ax.vlines(x_plot, ymin = -0.6, ymax = Ly - 0.4, color = 'blue', linewidth = 0.2)
        ax.hlines(y_plot, xmin = -0.6, xmax = Lx - 0.4, color = 'blue', linewidth = 0.2)
    
    # We update the simulation once every freq steps
    def plot_anim(i):
        for j in range(freq):
            if exponential_cooling:
                T = T0 * np.exp(-(i*freq + j) / tau)
            else:
                T = T0
            beta = 1 / T
            
            x = rng.integers(low = 0, high = Lx)
            y = rng.integers(low = 0, high = Ly)
            
            current_choices_horizontal = [1, -1]
            current_choices_vertical = [1, -1]
            
            # If particle is at left/right end, remove the option to go further left/right
            if x == 0:
                del current_choices_horizontal[1]
            elif x == Lx - 1:
                del current_choices_horizontal[0]
            
            # If particle is at top/bottom wall, remove the option to go further up/down
            if y == 0:
                del current_choices_vertical[1]
            elif y == Ly - 1:
                del current_choices_vertical[0]
                
            # Choosing the second lattice point
            move = rng.choice(direction)
            if move == "horizontal":
                x_second = x + rng.choice(current_choices_horizontal)
                y_second = y
            else:
                x_second = x
                y_second = y + rng.choice(current_choices_vertical)
            
            if [[x, y], [x_second, y_second]] in dimers:
                # By removing a dimer, we increase the "energy" of the system by 1.
                # So, we accept this move with probability exp(-beta)
                p = np.exp(-beta)
                accept = rng.binomial(1, p)
                
                if accept == 1:
                    dimers.remove([[x, y], [x_second, y_second]])
                    occupied_points.remove([x, y])
                    occupied_points.remove([x_second, y_second])
            
            elif [[x_second, y_second], [x, y]] in dimers:
                # By removing a dimer, we increase the "energy" of the system by 1.
                # So, we accept this move with probability exp(-beta)
                p = np.exp(-beta)
                accept = rng.binomial(1, p)
                
                if accept == 1:
                    dimers.remove([[x_second, y_second], [x, y]])
                    occupied_points.remove([x, y])
                    occupied_points.remove([x_second, y_second])
            
            elif ( [x, y] not in occupied_points ):
                if ( [x_second, y_second] not in occupied_points ):
                    # Adding a dimer always lowers energy, so we accept this move everytime
                    dimers.append([[x, y], [x_second, y_second]])
                    occupied_points.append([x, y])
                    occupied_points.append([x_second, y_second])
        
        ax.cla()
        ax.set_title(title)
        ax.vlines(x_plot, ymin = -0.6, ymax = Ly - 0.4, color = 'blue', linewidth = 0.2)
        ax.hlines(y_plot, xmin = -0.6, xmax = Lx - 0.4, color = 'blue', linewidth = 0.2)
        for d in dimers:
            x1 = d[0][0]
            x2 = d[1][0]
            y1 = d[0][1]
            y2 = d[1][1]
            ax.plot([x1, x2], [y1, y2], color = 'black', marker = '.', markersize = 5, linewidth = 0.75)
            
    anim = ani.FuncAnimation(fig, plot_anim, frames = n_max // freq, interval = 10**(-2), init_func = clear_lattice, repeat = False)
    
    """
    The following line displays the simulations, but leads to incorrect gif being stored below.
    Please comment the following line if you wish to store the simulation, but do wish to see it
    while running the program
    """
    #plt.show()
    return anim, dimers

anim1, dimers1 = Dimer_covering(T0 = 1, Lx = 50, Ly = 50, title = "Simulation of Dimer Covering Problem", exponential_cooling = False, n_max = 10**4, freq = 100)
anim1.save(r"Problem_9_Dimer_Covering_Problem/Dimer_Simulation.gif", fps = 60)

anim2, dimers2 = Dimer_covering(T0 = 1, Lx = 50, Ly = 50, title = r"Simulation of Dimer Covering Problem with cooling, $\tau = 10^4$", exponential_cooling = True, n_max = 10**5, freq = 1000, tau = 10**4)
anim2.save(r"Problem_9_Dimer_Covering_Problem/Dimer_Simulation_with_Cooling.gif", fps = 60)

anim3, dimers3 = Dimer_covering(T0 = 1, Lx = 50, Ly = 50, title = r"Simulation of Dimer Covering Problem with cooling, $\tau = 10^2$", exponential_cooling = True, n_max = 5 * 10**3, freq = 50, tau = 10**2)
anim3.save(r"Problem_9_Dimer_Covering_Problem/Dimer_Simulation_with_Faster_Cooling.gif", fps = 60)

print(f"The number of dimers in the first simulation (without cooling) is: {len(dimers1)}")
print(f"The number of dimers in the second simulation (with slow cooling) is: {len(dimers2)}")
print(f"The number of dimers in the third simulation (with fast cooling) is: {len(dimers3)}")