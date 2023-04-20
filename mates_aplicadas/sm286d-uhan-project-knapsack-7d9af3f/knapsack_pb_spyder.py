# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:22:42 2023

@author: ander.alvarez
"""

# Value in dollars
value = {
    'gold bar': 5185,
    'silver bar': 475,
    'platinum bar': 10781,
    'gold coin': 805,
    'silver coin': 194,
    'platinum coin': 1087
}

# Weight in grams
weight = {
    'gold bar': 100,
    'silver bar': 700,
    'platinum bar': 10,
    'gold coin': 15,
    'silver coin': 30,
    'platinum coin': 25
}


# Volume in cm3/item
volume = {
    'gold bar': 6,
    'silver bar': 67,
    'platinum bar': 1,
    'gold coin': 1,
    'silver coin': 3,
    'platinum coin': 2
}

# Number of bars and coins in the vault
available = {
    'gold bar': 4,
    'silver bar': 7,
    'platinum bar': 11,
    'gold coin': 27,
    'silver coin': 49,
    'platinum coin': 22  
}

# Maximum weight the knapsack can hold
max_weight = 3000
max_volume = 200

best_value = 0
best_weight = 0
best_volume = 0
best_items = None

nb_feasible_solutions=0
for nb_gold in range(available['gold bar']+1):
    for nb_silver in range(available['silver bar']+1):
        for nb_platinum in range(available['platinum bar']+1):
            for nb_goldcoin in range(available['gold coin']+1):
                for nb_silvercoin in range(available['silver coin']+1):
                    for nb_platinumcoin in range(available['platinum coin']+1):
                
                        total_weight = nb_gold * weight['gold bar'] + nb_silver * weight['silver bar'] + nb_platinum * weight['platinum bar'] + nb_goldcoin * weight['gold coin']+ nb_silvercoin * weight['silver coin']+ nb_platinumcoin * weight['platinum coin']
                        total_volume = nb_gold * volume['gold bar'] + nb_silver * volume['silver bar'] + nb_platinum * volume['platinum bar'] + nb_goldcoin * volume['gold coin']+ nb_silvercoin * volume['silver coin']+ nb_platinumcoin * volume['platinum coin']
                        if total_weight<=max_weight and total_volume<=max_volume:
                            nb_feasible_solutions+=1
                            total_value = nb_gold * value['gold bar'] + nb_silver * value['silver bar'] + nb_platinum * value['platinum bar']+ nb_goldcoin * value['gold coin']+ nb_silvercoin * value['silver coin']+ nb_platinumcoin * value['platinum coin']
                            if total_value>best_value:
                                best_weight = total_weight
                                best_value = total_value
                                best_volume = total_volume
                                new_feasible_solution = {'gold bar': nb_gold, 'silver bar': nb_silver, 'platinum bar': nb_platinum, 'gold coin': nb_goldcoin, 'silver coin': nb_silvercoin, 'platinum coin': nb_platinumcoin}


print('Nb of feasible solutions: {}'.format(nb_feasible_solutions))
print('Total weight: {}g, total value: {}$ and total volume: {}'.format(best_weight, best_value, best_volume))
print(new_feasible_solution)
