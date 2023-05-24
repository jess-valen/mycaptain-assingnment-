# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:49:24 2023

@author: Jessika Valencia
"""

# Area of the circle

r = int(input(" The radius of the circle is: "))
pi = 3.14159265
a = pi*r*r
print(" The area of the circle is: ",a )

# Write a python program to accept a Filename and print the Extension of that

Filename = input(" Enter the filename : ")
exten = Filename.split(".")
print(" The extension of the file : ", exten [-1])