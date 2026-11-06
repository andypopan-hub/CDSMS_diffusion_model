import numpy as np 
import matplotlib.pyplot as plt


def plot_profile(x, z, color = "r", title = None, output = None): 
    plt.figure()
    plt.plot(x, z, color)
    plt.xlabel("x")
    plt.ylabel("z")
    if title is not None:
        plt.title(title)
    if output is not None:
        plt.savefig(output)
plt.show()

D = 100 #D = Diffusivity
Lx = 300 #Lx = model domain

dx = 0.5 #grid spacing 
x = np.arange(start = 0, stop = Lx, step = dx) #the grid
nx = len(x) #number of grid nodes

z = np.zeros_like(x) #elevation
z_left = 500
z_right = 0
z[x <= Lx /2] = z_left #step
z[x > Lx/2] = z_right

plot_profile(x, z, title = "Inital Profile", output = "inital.png")

nt = 500 #number of time steps
dt = 0.5 * dx**2 / D #Time step

for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])

plot_profile(x,z, title = "Final Profile", color = "b", output = "final.png")