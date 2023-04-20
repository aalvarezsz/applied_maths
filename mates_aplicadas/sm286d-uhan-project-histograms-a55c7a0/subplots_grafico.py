# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:24:44 2022

@author: ander.alvarez
"""

# Import packages
import matplotlib.pyplot as plt

# Create figure with a title
fig = plt.figure()
fig.suptitle("Two oriented lines")

# Make the first of 2 plots in a 1x2 array of plots inside our figure
ax = fig.add_subplot(1, 2, 1)
ax.plot([0,1], [1,1], 'r')
ax.set_title("Horizontal segment")

# Make the second of 2 plots in a 1x2 array of plots inside our figure
ax = fig.add_subplot(1, 2, 2)
ax.plot([1,1], [0,1], 'r')
ax.set_title("Vertical segment")

# Display figure
plt.show()