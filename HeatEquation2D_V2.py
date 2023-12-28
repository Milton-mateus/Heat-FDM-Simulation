import numpy as np
import matplotlib.pyplot as plt
# Adição para plot de superfície
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Defining our problem

a = 110
length = 50 # mm
time = 4    # s
nodes = 50

# Initialization
dx = length / nodes
dy = length / nodes
dt = min(dx**2 / (4*a), dy**2 / (4*a)) # To ensure de estability
t_nodes = int(time/dt)

u = np.zeros((nodes, nodes)) + 20 # Plate is initially as 20 °C
flagBC = np.ones((nodes, nodes))

# Boundary conditions
u[0,:] = 100;   flagBC[0,:] = 0
u[-1,:] = 100;  flagBC[-1,:] = 0
u[25:,-1] = 100;  flagBC[25:,-1] = 0
u[:,0] = 20;    flagBC[:,0] = 0

# Visualizing with a plot
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap= plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)


# Simulating
counter = 0

while counter < time:
    w = u.copy()
    for i in range(nodes):
        for j in range(nodes):
            if flagBC[i, j] == 1:
                if i == 0:
                    dd_ux = (w[0, j] - 2*w[1, j] + w[2, j])/dx**2
                elif i == nodes-1:
                    dd_ux = (w[nodes-3, j] - 2*w[nodes-2, j] + w[nodes-1, j])/dx**2
                else:
                    dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2
                if j == 0:
                    dd_uy = (w[i, 0] - 2*w[i, 1] + w[i, 2])/dy**2
                elif j == nodes-1:
                    dd_uy = (w[i, nodes-3] - 2*w[i, nodes-2] + w[i, nodes-1])/dy**2
                else:
                    dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2

                u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]
    
    counter += dt

    # Write relatory
    print("t: {:.3f} [s], Avarage temperatura {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot
    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    # Apresenta o plot
    plt.pause(0.01)

plt.show()