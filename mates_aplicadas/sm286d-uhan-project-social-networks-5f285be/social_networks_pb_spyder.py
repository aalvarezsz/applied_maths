# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:27:26 2023

@author: ander.alvarez
"""

# Import numpy  
import numpy as np

# Define a dictionary that maps numbers to names
# a * next to a name indicates that the person is suspected of using a false ID
names = {
    0: 'Mohamed Atta',
    1: 'Nawaf Alhazmi',
    2: 'Hani Hanjour',
    3: 'Marwan Al-Shehhi',
    4: 'Ziad Jarrah',
    5: 'Mustafa al-Hisawi',
    6: 'Salem Alhazmi*',
    7: 'Lotfi Raissi',
    8: 'Saeed Alghamdi*',
    9: 'Abdul Aziz Al-Omari*',
    10: 'Hamza Alghamdi',
    11: 'Ramzi Bin al-Shibh',
    12: 'Said Bahaji',
    13: 'Ahmed Al Haznawi',
    14: 'Zakariya Essabar',
    15: 'Agus Budiman',
    16: 'Khalid Al-Mihdhar',
    17: 'Ahmed Alnami',
    18: 'Mounir El Motassadeq',
    19: 'Fayez Ahmed',
    20: 'Mamoun Darkazanli',
    21: 'Zacarias Moussaoui',
    22: 'Ahmed Khalil Ibrahim Samir Al-Ani',
    23: 'Abdussattar Shaikh',
    24: 'Osama Awadallah',
    25: 'Mohamed Abdi',
    26: 'Rayed Mohammed Abdullah',
    27: 'Bandar Alhazmi',
    28: 'Faisal Al Salmi',
    29: 'Mohand Alshehri*',
    30: 'Majed Moqed',
    31: 'Waleed Alshehri',
    32: 'Nabil al-Marabh',
    33: 'Raed Hijazi',
    34: 'Ahmed Alghamdi',
    35: 'Satam Suqami',
    36: 'Wail Alshehri'
}

# Initialize matrix of zeros
A = np.zeros([37,37])

# Change entries to reflect edges
A[0, [3, 9, 20, 14, 12, 11, 18, 21, 15, 22, 7, 4, 5, 2, 1]] = 1
A[1, [0, 6, 2, 16, 24, 23, 25, 17, 10, 8]] = 1
A[2, [1, 16, 30, 28, 27, 26, 7, 0, 4, 3]] = 1
A[3, [19, 6, 2, 4, 7, 0, 15, 11, 18, 12, 14, 20, 9, 5]] = 1
A[4, [13, 6, 2, 7, 15, 11, 0, 12, 14, 3]] = 1
A[5, [19, 3, 0, 31]] = 1
A[6, [1, 4, 3]] = 1
A[7, [2, 26, 0, 3, 4]] = 1
A[8, [32, 17, 10, 1, 13, 33]] = 1
A[9, [3, 0, 31]] = 1
A[10, [34, 17, 1, 13, 29, 8]] = 1
A[11, [3, 0, 4, 15, 21, 18, 12, 14]] = 1
A[12, [0, 11, 18, 20, 14, 3, 4]] = 1
A[13, [8, 10, 4]] = 1
A[14, [3, 4, 0, 11, 12]] = 1
A[15, [4, 11, 3, 0]] = 1
A[16, [23, 24, 2, 1]] = 1
A[17, [1, 10, 8]] = 1
A[18, [11, 12, 3, 0]] = 1
A[19, [29, 3, 5]] = 1
A[20, [3, 0, 12]] = 1
A[21, [11, 0]] = 1
A[22, [0]] = 1
A[23, [24, 16, 1]] = 1
A[24, [16, 1, 23]] = 1
A[25, [1]] = 1
A[26, [28, 27, 7, 2]] = 1
A[27, [26, 2]] = 1
A[28, [26, 2]] = 1
A[29, [19, 10]] = 1
A[30, [2]] = 1
A[31, [35, 5, 9, 36]] = 1
A[32, [34, 8, 33, 35]] = 1
A[33, [32, 8, 35]] = 1
A[34, [10, 32]] = 1
A[35, [32, 33, 31, 36]] = 1
A[36, [31, 35]] = 1

# Import networkx
import networkx as nx

# Define graph G using adjacency matrix A
G = nx.Graph(A)

# Print nodes and edges
print(f'Nodes: {G.nodes()}')
print(f'Edges: {G.edges()}')