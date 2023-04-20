# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:04:20 2022

@author: ander.alvarez
"""

# Import packages
import math
import matplotlib.pyplot as plt

# Given data - DO NOT MODIFY
my_norm_data = [1.63019808,  1.10073589,  2.06223012,  0.46401601,  1.65206334,  0.25922487,
                -0.46316407, -1.46398247, -0.30532938,  1.11649215,  1.92491589, -0.253509,
                1.3647869,   1.65219977, -1.94616457,  1.41985742,  0.58905056,  0.62443324,
                -0.18635681,  0.12747123, -0.17307431, -1.7567247,   2.13330145, -0.30926192,
                -0.50763542, -1.21583688, -0.93831764, -1.18553654,  1.10623614,  0.181178,
                -0.0650886,   0.64435754,  0.78327881, -0.06288281, -0.15177811, -0.1747229,
                0.66276697, -0.04781049, -0.08995647, -0.52939899,  0.87630499,  0.64584007,
                -0.72299889,  0.25349786, -1.4222941,  -0.21634908, -0.96742654,  0.68114803,
                -0.79128242, -0.68585123,  2.36783368, -0.05585545,  0.58075107, -0.4991764,
                0.5140605,  -0.61785086,  0.47382545, -0.64576212, -0.29909176,  1.42641698,
                -1.05657461, -1.09308421, -1.91279634,  1.6167223,   0.07624055,  0.30728674,
                -0.88151405,  1.83890825,  0.19009995, -0.90866029, -0.8531006,   0.88882339,
                2.28926927, -1.29422313, -0.69997783, -0.80655444, -0.27459588,  0.06108991,
                0.55304006, -1.46720348, -0.65689031, -0.0098607,  -1.18834767, -0.43941531,
                -0.4687906,  -0.01616325, -0.22354459,  1.93468057,  0.48944633,  0.42773085,
                -0.30233738,  0.86817489, -1.06404795,  0.27319666, -0.48523957, -0.03863856,
                0.62969042, -0.98132641, -0.19735913,  0.21067031, -0.62317565, -1.26142085,
                -0.21391804,  0.18939428,  0.17550555, -0.91122093,  0.76005489, -0.18217718,
                0.32034907,  0.59530016, -0.50491964,  0.50488128,  1.38085663,  0.96297755,
                1.3799329,  -0.99993727,  1.49259734, -1.09999539,  0.98506758, -0.21675019,
                -0.13919721, -0.05249682,  1.38350375, -0.71563502, -1.50099077, -0.59385063,
                0.1862516,   0.35092607, -1.28670678,  0.58895599, -0.37948455, -0.40923911,
                -0.58537418,  0.13813463,  0.64134916, -0.67030436, -0.02967847, -0.29702066,
                -0.34011984, -1.0674362, -1.57824187,  0.96011477,  0.03735634, 1.05114322,
                -0.12865731,  0.90883497,  0.01693048,  0.29704706, -0.3048463,   0.07830598,
                0.73364995,  0.93760414,  0.53271371, -0.56959324, -1.19688745,  0.57768536,
                -0.84382202,  0.53347977, -0.49224397, -0.24976479, -0.22475676,  0.36746481,
                1.51503006, -1.41723367, -0.43209908, -0.43328085, -1.41739211, -0.02040517,
                -1.04324073,  1.41239199,  0.83557289, -1.23326606,  2.04351217, -0.37898166,
                1.34651754, -0.58090518,  1.40061085, -0.82781836, -0.46388403, -2.21167915,
                -1.63059353, -0.89209998, -0.18933422,  1.29697635,  0.56702193,  0.74244869,
                1.11733287, -0.32323721,  0.34507202,  1.20487174, -1.9655566,   0.0764207,
                0.21201638, -0.93769603,  1.90010053, -1.57748233, -1.12699338, -1.14676241,
                0.50090028,  1.27070076]


# Create a figure
# Draw axes on the figure
# Give a title for the axes
fig = plt.figure()
fig.suptitle("Histogram for my_data with normal densities")




# Different values of mu and sigma
# Different colors for each mu-sigma combination
mu_list = [0, -0.5, 0.5, 1]
sigma_list = [1, 1, 0.8, 0.8]
color_list = ['r', 'g', 'b', 'k']

# Create list of values on the x-axis
x_values = []
for i in range(150):
    x_values.append(-3 + 20 / 500 * i)

#################################################################################
ax = plt.subplot(2, 2, 1)
ax.set_title('mu=0 and sigma=1')

# Plot the histogram on the axes
ax.hist(my_norm_data, bins='fd', density=True)

mu=0
sigma=1
# Plot density of normal distribution
# for each mu-sigma combination
    
y_values = []
for x in x_values:
    #aqui se define la funcion
    y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
    
ax.plot(x_values, y_values, linewidth=2, color='r', label = f'mu = {mu}, sigma = {sigma}')

#################################################################################
ax = plt.subplot(2, 2, 2)
ax.set_title('mu=-0.5 and sigma=1')

# Plot the histogram on the axes
ax.hist(my_norm_data, bins='fd', density=True)

mu=-0.5
sigma=1
# Plot density of normal distribution
# for each mu-sigma combination
    
y_values = []
for x in x_values:
    #aqui se define la funcion
    y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
    
ax.plot(x_values, y_values, linewidth=2, color='r', label = f'mu = {mu}, sigma = {sigma}')


#################################################################################
ax = plt.subplot(2, 2, 3)
ax.set_title('mu=0.5 and sigma=0.8')

# Plot the histogram on the axes
ax.hist(my_norm_data, bins='fd', density=True)

mu=0.5
sigma=0.8
# Plot density of normal distribution
# for each mu-sigma combination
    
y_values = []
for x in x_values:
    #aqui se define la funcion
    y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
    
ax.plot(x_values, y_values, linewidth=2, color='r', label = f'mu = {mu}, sigma = {sigma}')


#################################################################################
ax = plt.subplot(2, 2, 4)
ax.set_title('mu=1 and sigma=0.8')

# Plot the histogram on the axes
ax.hist(my_norm_data, bins='fd', density=True)

mu=1
sigma=0.8
# Plot density of normal distribution
# for each mu-sigma combination
    
y_values = []
for x in x_values:
    #aqui se define la funcion
    y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
    
ax.plot(x_values, y_values, linewidth=2, color='r', label = f'mu = {mu}, sigma = {sigma}')
# Create the legend
# Show the figure
#ax.legend()
fig.tight_layout(pad=1.5)
plt.show()