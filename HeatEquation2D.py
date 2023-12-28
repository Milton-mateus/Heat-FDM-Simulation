import numpy as np
import matplotlib.pyplot as plt


# Defining our problem

a = 110
length = 50 # mm
time = 4    # s
nodes = 30

# Initialization
dx = length / nodes
dy = length / nodes
dt = min(dx**2 / (4*a), dy**2 / (4*a)) # To ensure de estability
t_nodes = int(time/dt)

u = np.zeros((nodes, nodes)) + 20 # Plate is initially as 20 °C

# Boundary conditions
u[0,:] = 100
u[-1,:] = 100

# Visualizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap= plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulating
counter = 0

while counter < time:
    w = u.copy()
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):
            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]
    
    counter += dt

    # Write relatory
    print("t: {:.3f} [s], Avarage temperatura {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot
    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)

plt.show()