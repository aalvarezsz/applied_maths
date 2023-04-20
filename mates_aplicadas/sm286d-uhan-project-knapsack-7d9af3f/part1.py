# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:49:11 2022

@author: ander.alvarez
"""
'''EJEMPLOS DE UTILIZACION DE LOS DICCIONARIOS'''
# https://docs.python.org/fr/3.6/tutorial/datastructures.html

def ejemplo_prints_diccionarios():
    print(value['gold bar'])
    #5185
    
    value['ander alvarez']=21 #años
    print(value)
    #{'gold bar': 5185, 'silver bar': 475, 'platinum bar': 10781, 'ander alvarez': 21}
    
    del(value['ander alvarez'])
    print(value)
    #{'gold bar': 5185, 'silver bar': 475, 'platinum bar': 10781}
    
    #en un diccionario, el texto ese que esta entre comillas es una KEY
    print(list(value.keys()))
    #['gold bar', 'silver bar', 'platinum bar']
    
    print(sorted(value.keys())) #x orden alfabetico del primer caracter del KEY
    #['gold bar', 'platinum bar', 'silver bar']
    
    print(sorted(value.values())) #x orden alfabetico del primer caracter del KEY
    # lo mismo pero con valores
    
    print('aimar' in value)
    #False
    
    print('aimar' not in value)
    #True
def ejemplo_loops_diccionarios():
    for k, v in value.items():
        print(k, v)
    # gold bar 5185
    # silver bar 475
    # platinum bar 10781
    
    
    for k, v in zip(value, weight):
        print('value of {0} and weight of {1}'.format(k,v))
    # value is gold bar and weight is gold bar
    # value is silver bar and weight is silver bar
    # value is platinum bar and weight is platinum bar
    
    for (k,v), (k2,v2) in zip(value.items(), weight.items()):
        print('value of {0} is {1}'.format(k,v))
        print('weight of {0} is {1}'.format(k2,v2))
    # value of gold bar is 5185
    # weight of gold bar is 100
    # value of silver bar is 475
    # weight of silver bar is 700
    # value of platinum bar is 10781
    # weight of platinum bar is 10

############################################################

# Value in dollars
value = {
    'gold bar': 5185,
    'silver bar': 475,
    'platinum bar': 10781
}

# Weight in grams
weight = {
    'gold bar': 100,
    'silver bar': 700,
    'platinum bar': 10
}

# Number of bars and coins in the vault
available = {
    'gold bar': 4,
    'silver bar': 7,
    'platinum bar': 11   
}

# Maximum weight the knapsack can hold
max_weight = 3000


'''
new_feasible_solution = {
    'gold bars': number of gold bars,
    'silver bars': number of silver bars,
    'platinum bars': number of platinum bars,
    'total value': total value of combination,
    'total weight': total weight of combination
}
'''



def heist(value, weight, available, max_weight):
    list_of_solutions=[]
    count1=0;
    count2=0;
    count3=0;
    for (k,v), (k2,v2), (k3, v3) in zip(value.items(), weight.items(), available.items()):
        sum_value=v[0]+v[1]+v[2]
        count1+=count1;
        count2+=count2;
        count3+=count3;
        sum_weight=v2[0]+v2[1]+v2[2]
                
                
        sum0 = k3[0]+k3[1]+k3[2]
        sum1 = k3[0]+k3[1]
        sum2 = k3[1]+k3[2]
        sum2 = k3[0]+k3[2]
        if (count1 <= v3):
            print('ns q cojones hacer')
        else:
            break
        
        if (sum_weight<=max_weight):
            new_feasible_solution = {
                'gold bars': count1,
                'silver bars': count2,
                'platinum bars': count3,
                'total value': sum_value,
                'total weight': sum_weight
            }
        
        list_of_solutions.append(new_feasible_solution)
        
    print(list_of_solutions)
    
heist(value, weight, available, max_weight)