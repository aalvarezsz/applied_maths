# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:06:46 2022

@author: ander.alvarez
"""

# Import packages
import math
import matplotlib.pyplot as plt

# Different values of mu and sigma
# Different colors for each mu-sigma combination
mu_list = [0, -1, -1, 3, 3]
sigma_list = [1, 1, 2, 2, 5]
color_list = ['r', 'g', 'b', 'k', 'y']

# Create list of values on the x-axis
x_values = []
for i in range(500):
    x_values.append(-10 + 20 / 500 * i)

# Create a figure
# Draw axes on the figure
# Give a title for the axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Normal densities')

# Plot density of normal distribution
# for each mu-sigma combination
for i in range(len(mu_list)):
    mu = mu_list[i]
    sigma = sigma_list[i]
    
    y_values = []
    for x in x_values:
        y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
        
    ax.plot(x_values, y_values, linewidth=2, color=color_list[i], label = f'mu = {mu_list[i]}, sigma = {sigma_list[i]}')

# Create the legend
# Show the figure
ax.legend()
plt.show()