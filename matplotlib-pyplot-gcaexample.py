#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 03:28:32 2024

@author: kamran
"""

import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot some data
ax.plot([1, 2, 3], [1, 4, 9])

# Set the face color of the current axes using gca()
plt.gca().set_facecolor('lighgreen')

# Show the plot
plt.show()