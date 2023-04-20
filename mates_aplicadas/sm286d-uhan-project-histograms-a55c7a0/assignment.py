# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:27:51 2022

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
fig.suptitle("Histogram for my_norm_data with normal densities")




# Different values of mu and sigma
# Different colors for each mu-sigma combination
mu_list = [0, -0.5, 0.5, 1]
sigma_list = [1, 1, 0.8, 0.8]
color_list = ['r', 'g', 'b', 'k']

# Create list of values on the x-axis
x_values = []
for i in range(125):
    x_values.append(-2.5 + 20 / 500 * i)

# Plot density of normal distribution
# for each mu-sigma combination
    
k=1
for i in range(len(mu_list)):
    mu = mu_list[i]
    sigma = sigma_list[i]
    
    
    ax = fig.add_subplot(2, 2, k)
    k=k+1
    
    #DYNAMIC TITLE!!!!!!!!!!!!!!
    ax.set_title('mu=%1.1f and sigma = %1.1f' % (mu_list[i], sigma_list[i]))
    
    # Plot the histogram on the axes
    ax.hist(my_norm_data, bins='fd', density=True)
    
    y_values = []
    for x in x_values:
        #aqui se define la funcion
        y_values.append(1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2 * sigma**2)))
        
    ax.plot(x_values, y_values, linewidth=2, color=color_list[i], label = f'mu = {mu_list[i]}, sigma = {sigma_list[i]}')
# Create the legend
# Show the figure
#ax.legend()
fig.tight_layout(pad=1.5)
plt.show()



################################################################

# Given data - DO NOT MODIFY
my_exp_data = [1.86460822e+00, 2.14303480e+00, 7.34146234e-01,
               1.53539195e+00, 2.15547160e+00, 1.47604160e+01, 2.78047567e+00,
               1.54664268e+00, 2.73695174e+00, 5.37323410e-01, 1.07690926e+00,
               3.72891527e+00, 1.04056286e+00, 1.28703300e+00, 2.36298272e+00,
               4.09535284e-01, 1.41434837e-01, 1.94726777e+00, 1.83767980e+00,
               4.07191544e+00, 1.08164421e-01, 1.68359395e+00, 1.03951368e+00,
               3.24417089e+00, 3.07769843e+00, 3.01658760e+00, 1.94201209e-01,
               6.39713545e+00, 3.71531649e+00, 6.34016333e-01, 1.29828052e+00,
               1.29844972e+00, 2.12763995e+00, 4.48915436e-01, 9.40592498e-01,
               6.53147368e-01, 7.85419508e-01, 1.63754151e+00, 3.93801316e+00,
               5.91096689e+00, 1.21302725e+00, 1.25363865e+00, 5.23742369e+00,
               2.72906048e-01, 3.88293238e-01, 1.26141355e+00, 5.85927205e+00,
               1.72934137e+00, 2.94743489e-03, 8.44588396e-02, 1.09658899e+00,
               2.55009361e+00, 3.21184594e+00, 2.05923156e+00, 1.94260456e-01,
               1.21460765e+00, 4.59743584e-01, 2.42704244e+00, 4.76243487e-01,
               6.17142636e-02, 7.02617627e-02, 5.78125635e-01, 4.78452233e-01,
               1.37472537e+00, 1.95082874e+00, 4.93150440e-01, 3.51437304e+00,
               3.79806420e-01, 2.95770670e+00, 3.40655333e-01, 2.78832988e+00,
               3.09990586e+00, 1.15844491e+00, 7.08409864e-01, 7.27706390e-01,
               1.67529983e+00, 1.09085582e+00, 4.30879714e-02, 2.33531012e-02,
               3.08125639e-02, 5.01669907e+00, 5.41449395e+00, 5.57730790e-02,
               7.24442607e+00, 1.92165631e+00, 2.15419170e+00, 1.10183973e+00,
               2.22875119e-01, 1.74714676e+00, 3.96621873e-01, 1.02090391e+01,
               2.74734474e+00, 6.10594344e-01, 1.21882349e+00, 1.72193033e+00,
               4.86843007e-01, 5.84929463e-01, 1.86511659e+00, 4.34551090e-02,
               5.67273753e-01, 1.80961186e+00, 1.35952576e+00, 1.05097888e-01,
               9.68733325e-01, 4.11726127e-01, 1.32210765e+00, 5.48277485e-02,
               2.35811029e+00, 1.29927671e+00, 3.17964526e+00, 3.64962744e+00,
               4.50947319e+00, 2.13188686e-01, 4.27848965e+00, 9.14194538e-01,
               1.79277203e+00, 3.05929650e-01, 1.24200463e+00, 6.14246627e-02,
               3.52754107e+00, 4.55081812e+00, 2.83811914e-01, 5.39387674e+00,
               1.04832013e-01, 3.39365206e-01, 1.40769175e-01, 2.38857911e-01,
               6.24265731e+00, 6.09348537e-01, 4.47385461e-01, 2.35674002e+00,
               3.89500327e+00, 3.61150995e-01, 5.14201649e-01, 9.08220585e-01,
               3.48305660e+00, 2.85899451e-01, 2.19894983e-01, 1.71721675e+00,
               1.02152512e+00, 4.98662668e+00, 4.46535706e+00, 2.48511985e+00,
               3.33445877e+00, 4.18347425e-01, 2.04787670e+00, 2.42086436e+00,
               2.66664542e+00, 6.57488917e+00, 5.02966283e+00, 2.99679419e-01,
               8.86494934e-01, 2.38074116e+00, 9.38115700e-01, 2.21985115e+00,
               1.07804446e+00, 4.21828365e+00, 7.84706173e-01, 7.07295010e-02,
               9.39211064e-01, 2.71065966e+00, 1.03538765e+00, 5.95800357e-01,
               5.16890264e+00, 2.58439639e+00, 4.62183376e-01, 2.13317672e-02,
               1.96774569e+00, 5.08287399e-01, 3.50698938e-01, 4.10351583e-01,
               1.85725780e+00, 1.14079541e-01, 4.68072825e-01, 3.01690829e+00,
               2.70572856e-02, 1.20070729e+00, 3.29518069e-01, 9.85593774e-01,
               1.88690544e+00, 7.65451886e-01, 4.22309274e+00, 1.44090272e+00,
               4.62601872e+00, 1.17119905e+00, 8.89013179e+00, 1.50082840e+00,
               1.94230596e+00, 5.59101539e-02, 2.99481288e+00, 2.51889898e+00,
               4.12410236e-01, 3.15352692e+00, 6.17465658e+00, 2.92949982e+00,
               4.40471131e+00, 3.84974622e-01, 2.04193732e+00, 4.72578827e-01]

# Create a figure
# Draw axes on the figure
# Give a title for the axes
fig = plt.figure()
fig.suptitle("Histogram for my_exp_data with normal densities")




# Different values of mu and sigma
# Different colors for each mu-sigma combination
beta_list = [0.5, 1, 2, 4]
color_list = ['r', 'g', 'b', 'k']

# Create list of values on the x-axis
x_values = []
for i in range(900):
    x_values.append(0 + 8 / 400 * i)

# Plot density of normal distribution
# for each mu-sigma combination
    
k=1
for i in range(len(beta_list)):
    beta = beta_list[i]
    
    
    ax = fig.add_subplot(2, 2, k)
    k=k+1
    
    #DYNAMIC TITLE!!!!!!!!!!!!!!
    ax.set_title('beta=%1.1f ' % (mu_list[i]))
    
    # Plot the histogram on the axes
    ax.hist(my_exp_data, bins='fd', density=True)
    
    y_values = []
    for x in x_values:
        #aqui se define la funcion
        y_values.append((1 / beta) * math.exp(-x / beta))
        
    ax.plot(x_values, y_values, linewidth=2, color=color_list[i], label = f'beta = {beta_list[i]}')
# Create the legend
# Show the figure
#ax.legend()
fig.tight_layout(pad=1.5)
plt.show()