
import numpy as np
import matplotlib.pyplot as plt


def plot_profile(x, z, color="r", title=None, output=None):
    plt.figure()
    plt.plot(x, z, color)
    plt.xlabel("x")
    plt.ylabel("z")

    if title is not None:
        plt.title(title)

    if output is not None:
        plt.savefig(output)

    plt.show()


def calculate_stable_time_step(dx, diffusivity):
    return 0.5 * dx**2 / diffusivity


# Model parameters
D = 100  # Diffusivity
Lx = 300  # Model domain

dx = 0.5  # Grid spacing
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)

# Initial elevation
z = np.zeros_like(x)
z_left = 500
z_right = 0

z[x <= Lx / 2] = z_left
z[x > Lx / 2] = z_right

# Plot initial profile
plot_profile(x, z, title="Initial Profile", output="initial.png")

# Time stepping
nt = 500
dt = calculate_stable_time_step(dx, D)

for t in range(nt):
    z[1:-1] += D * dt / dx**2 * (
        z[:-2] - 2*z[1:-1] + z[2:]
    )

# Plot final profile
plot_profile(x, z, title="Final Profile",
             color="b", output="final.png")