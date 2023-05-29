# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:02:21 2023

@author: Jessika Valencia
"""

# write python code to create a function called most_frequent that takes string and prints the letters in decreasing order.



def most_frequent(string):
    import operator
    d = {}
    
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
        d_lower = {k.lower(): v for k, v in d.items()}
        d_sorted = dict(sorted(d.items(), key = operator.itemgetter(1),reverse = True))
        
    return d_sorted


input = input("Please enter a string ")
print(most_frequent(input))
 