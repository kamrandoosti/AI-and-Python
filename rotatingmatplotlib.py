#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 03:47:44 2024

@author: kamran
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the data
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot the initial surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Animated 3D Surface Plot')

# Function to update the surface plot for animation
def update(frame):
    ax.view_init(elev=30., azim=frame)
    return surf,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50, blit=False)

# Display the animation

plt.savefig('/home/kamran/plt.pdf',dpi=300)

plt.show()