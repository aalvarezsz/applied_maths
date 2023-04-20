# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:15:54 2022

@author: ander.alvarez
"""

# Import packages
import math
import matplotlib.pyplot as plt

# Different values of beta
# Different colors for each beta
beta_list = [0.5, 1, 2, 3]
color_list = ['r', 'g', 'b', 'k']

# Create list of values on the x-axis
x_values = []
for i in range(400):
    x_values.append(0 + 8 / 400 * i)

# Create a figure
# Draw axes on the figure
# Give a title for the axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Exponential densities')

# Plot density of exponential distribution for each beta
for i in range(len(beta_list)):
    beta = beta_list[i]
    
    y_values = []
    for x in x_values:
        y_values.append((1 / beta) * math.exp(-x / beta))
        
    ax.plot(x_values, y_values, linewidth=2, color=color_list[i], label = f'beta = {beta_list[i]}')

# Create the legend
# Show the figure
ax.legend()
plt.show()