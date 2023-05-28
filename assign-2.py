# -*- coding: utf-8 -*-
"""
Created on Sun May 28 20:18:39 2023

@author: Jessika Valencia
"""

# Write a Python program for Fibonacci series

num = int(input(" Enter the total no. of terms: "))
n1 = 0
n2 = 1
increment = 0
if num <= 0:
    print(" Enter a positive value")
elif num == 1:
    print(" Fibonacci series upto", num," : ", n1)
else:
    print(" fibonacci series upto", num, " : ")
    while increment < num:
        print(n1)
        result = n1 + n2
        n1 = n2
        n2 = result
        increment += 1
        
# Write a python program to print all positive numbers in a range

list1 = [ 12, -7, 5, 64, -14]
for i in list1:
    if i <0:
        list1.remove(i)
        print(list1)

list2 = [ 12, 14, -95, 3]
for i in list2:
    if i <0:
        list2.remove(i)
        print(list2)