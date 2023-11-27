from numpy.random import default_rng
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as ani

cmap = mpl.cm.viridis
rng = default_rng()


class DLA_Original():
    fig, (ax, cbar) = plt.subplots(2, 1, gridspec_kw = {'height_ratios': [6, 1]})
    fig2, ax2 = plt.subplots()
    choices = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
    complete = 0
    
    def __init__(self, L):
        # Defining the relevant parameters
        self.L = L      
        self.x_plot = np.arange(-0.5, L)
        self.y_plot = np.arange(-0.5, L)
        self.anchor_points = [np.array([L - 1, L - 1]) / 2 ]
        self.center = np.array([L - 1, L - 1]) / 2
        
    def New_Particle(self, nmax = 1):
        for k in range(nmax):
            # We choose a point randomly on the circle of radius r, and then choose the 
            # nearest grid point
            theta = rng.uniform(low = -np.pi, high = np.pi)
            R = len(self.anchor_points) + 1
            if R >= int(self.L/4):
                self.complete = 1
                return
            
            x = (self.L - 1) / 2 + R * np.cos(theta)
            y = (self.L - 1) / 2 + R * np.sin(theta)
            
            p1 = np.array([int(x) + 1, int(y)])
            p2 = np.array([int(x), int(y) + 1])
            p3 = np.array([int(x) + 1, int(y) + 1])
            
            r1 = np.sum( (p1 - self.center)**2 )
            r2 = np.sum( (p2 - self.center)**2 )
            r3 = np.sum( (p3 - self.center)**2 )
            
            if min(r1, r2) >= R**2:
                if r1 <= r2:
                    self.ini_point = np.array([int(x) + 1, int(y)])
                    r = np.sqrt(r1)
                else:
                    self.ini_point = np.array([int(x), int(y) + 1])
                    r = np.sqrt(r2)
            else:
                self.ini_point = np.array([int(x) + 1, int(y) + 1])
                r = np.sqrt(r3)
            
            self.ax2.scatter(self.ini_point[0], self.ini_point[1], s = 5, c = 'k')
            self.ax2.set_title(f"Scatter Plot showing the random initial points")
            self.ax2.set_xlim(-0.6, self.L - 0.4)
            self.ax2.set_ylim(-0.6, self.L - 0.4)
            self.ax2.vlines(self.x_plot, ymin = -0.6, ymax = self.L - 0.4, color = '0.7', linewidth = 0.1)
            self.ax2.hlines(self.y_plot, xmin = -0.6, xmax = self.L - 0.4, color = '0.7', linewidth = 0.1)
            
            pos = np.empty((1, 2))
            pos[0, :] = self.ini_point
            anchored = False
            
            anch_points_set = set( (tuple(i) for i in self.anchor_points) )
            adjacent = set( (tuple(pos[0, :] + c) for c in self.choices) )
            
            if len(adjacent.intersection(anch_points_set)) == 1:
                anchored = True
                self.anchor_points.append(pos[0, :])
                self.current_path = pos
                continue
            
            i = 0
            
            while (r < 2*R) and (not anchored):               
                # Choose a direction for the random walk. Since we set R < L/4, we do not
                # worry about the particle getting near the edges.
                path = rng.choice(self.choices)
                temp = pos[i, :] + path
                pos = pos.tolist()
                pos = pos + [temp]
                pos = np.array(pos)
                i = i + 1
                
                self.current_path = pos
                
                r = np.sqrt( np.sum((pos[i, :] - self.center)**2) )
                        
                adjacent = set( (tuple(pos[i, :] + c) for c in self.choices) )
                    
                if len(adjacent.intersection(anch_points_set)) == 1:
                    anchored = True
                    self.anchor_points.append(pos[i, :])
                elif r >= 2 * R:
                    break
    
    
    def clear_lattice(self):
        n = len(self.anchor_points)
        self.ax.cla()
        self.ax.set_title(f"Diffusion Limited Aggregation with {n} points anchored")
        self.ax.set_xlim(-0.6, self.L - 0.4)
        self.ax.set_ylim(-0.6, self.L - 0.4)
        self.ax.vlines(self.x_plot, ymin = -0.6, ymax = self.L - 0.4, color = '0.5', linewidth = 0.1)
        self.ax.hlines(self.y_plot, xmin = -0.6, xmax = self.L - 0.4, color = '0.5', linewidth = 0.1)
    
    def plot(self):
        self.clear_lattice()
        
        n = len(self.anchor_points)
        temp = np.array(self.anchor_points)
        x_anchor = temp[:, 0]
        y_anchor = temp[:, 1]
        norm = mpl.colors.Normalize(vmin = 0, vmax = n - 1)
        self.ax.scatter(x_anchor, y_anchor, s = 10, c = np.arange(n), cmap = cmap, norm = norm)
        #self.ax.plot(self.current_path[:, 0], self.current_path[:, 1], color = 'blue', linewidth = 0.3)
        self.fig.colorbar(mpl.cm.ScalarMappable(norm = norm, cmap = cmap), orientation = 'horizontal', label = 'Age of Particle', cax = self.cbar)
        
        plt.show()
            
    def Simulate_Full(self, nmax = 500):
        self.New_Particle(nmax)
        self.plot()
        
        if self.complete == 0:
            raise RuntimeError(f"Raidus of half lattice was not reached even with {len(self.anchor_points)} particles on the board!")
