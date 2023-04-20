# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:19:43 2022

@author: ander.alvarez
"""
import math
import matplotlib.pyplot as plt

# Randomly generated data
my_data = [0.66698806,  0.02581308, -0.77761941,  0.94863382,  0.70167179, -1.05108156,
           -0.36754812, -1.13745969, -1.32214752,  1.77225828, -0.34745899,  0.67014016,
           0.32227152,  0.06034293, -1.04345,    -1.00994188,  0.44173637,  1.12887685,
           -1.83806777, -0.93876863, -0.20184052,  1.04537128,  0.53816197,  0.81211867,
           0.2411063,  -0.95250953, -0.13626676,  1.26724821,  0.17363364, -1.22325477,
           1.41531998,  0.45771098,  0.72887584,  1.96843473, -0.54778801, -0.67941827,
           -2.50623032,  0.14696049,  0.60619549, -0.02253889,  0.01342226,  0.93594489,
           0.42062266,  0.41161964, -0.07132392, -0.04543758,  1.04088597, -0.09403473,
           -0.42084395, -0.55198856]

# Create a figure
# Draw axes on the figure
# Give a title for the axes
fig = plt.figure()
ax = plt.subplot(1, 1, 1)
ax.set_title('Histogram for my_data')

# Plot the histogram on the axes
ax.hist(my_data, bins='fd', density=True)

# Show the figure
plt.show()