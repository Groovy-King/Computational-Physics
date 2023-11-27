from numpy.random import default_rng
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as ani

cmap = mpl.cm.viridis
rng = default_rng()

class DLA_Simulation():
    fig, (ax, cbar) = plt.subplots(2, 1, gridspec_kw = {'height_ratios': [6, 1]})
    anchored_points = []
    choices = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
    origin_anchored = False

    def __init__(self, L):
        # Defining the relevant parameters
        self.L = L
        # We start the particle in the middle of the grid
        self.ini_point = np.array([L - 1, L - 1]) / 2       
        self.x_plot = np.arange(-0.5, L)
        self.y_plot = np.arange(-0.5, L)
        
    def New_particle(self, n = 1):
        for k in range(n):
            pos = np.empty((1, 2))
            pos[0, :] = self.ini_point
            i = 0
            anchored = False
            anch_points_set = set( (tuple(i) for i in self.anchored_points) )
            adjacent = set( (tuple(pos[0, :] + c) for c in self.choices) )
            
            if len(adjacent.intersection(anch_points_set)) == 1:
                self.origin_anchored = True
                self.anchored_points.append(pos[0, :])
                self.current_path = pos
                return None
            
            while not anchored:
                step = rng.choice(self.choices)
                temp = pos[i, :] + step
                pos = pos.tolist()
                pos = pos + [temp]
                pos = np.array(pos)
                i = i + 1
                
                self.current_path = pos
                        
                adjacent = set( (tuple(pos[i, :] + c) for c in self.choices) )
                    
                if len(adjacent.intersection(anch_points_set)) == 1:
                    anchored = True
                    self.anchored_points.append(pos[i, :])
                
                cond1 = ( pos[i, 0] == 0 )
                cond2 = ( pos[i, 0] == (self.L - 1) )
                cond3 = ( pos[i, 1] == 0 )
                cond4 = ( pos[i, 1] == (self.L - 1) )
                
                if True in [cond1, cond2, cond3, cond4]:
                    anchored = True
                    self.anchored_points.append(pos[i, :])
                    
    
    def clear_lattice(self):
        n = len(self.anchored_points)
        self.ax.cla()
        self.ax.set_title(f"Diffusion Limited Aggregation with {n} points anchored")
        self.ax.set_xlim(-0.6, self.L - 0.4)
        self.ax.set_ylim(-0.6, self.L - 0.4)
        self.ax.vlines(self.x_plot, ymin = -0.6, ymax = self.L - 0.4, color = '0.5', linewidth = 0.1)
        self.ax.hlines(self.y_plot, xmin = -0.6, xmax = self.L - 0.4, color = '0.5', linewidth = 0.1)
    
    def plot(self):
        self.clear_lattice()
        
        n = len(self.anchored_points)
        temp = np.array(self.anchored_points)
        x_anchor = temp[:, 0]
        y_anchor = temp[:, 1]
        norm = mpl.colors.Normalize(vmin = 0, vmax = n - 1)
        self.ax.scatter(x_anchor, y_anchor, s = 10, c = np.arange(n), cmap = cmap, norm = norm)
        self.ax.plot(self.current_path[:, 0], self.current_path[:, 1], color = 'blue', linewidth = 0.3)
        self.fig.colorbar(mpl.cm.ScalarMappable(norm = norm, cmap = cmap), orientation = 'horizontal', label = 'Age of Particle', cax = self.cbar)
        
        plt.show()
            
    def Simulate_Full(self, nmax = 500):
        self.New_particle(nmax)
        self.plot()
        
        if not self.origin_anchored:
            raise RuntimeWarning(f"Origin not anchored even after {nmax} particles on board!")
            
        


            
        
        
        
        
