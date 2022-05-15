# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:59:15 2022

@author: shashi
"""

#the digits after decimal point are optional if they are zero
no_decimal = 09.

#Complex Numbers
comp1 = 3.14j
comp2 = 34+4J
comp3 = 2e+5j

print("The complex number 3.14j: ", comp1)
print("The complex number 34 + 4j: ", comp2)
print("The complex number 2e+5j: ", comp3)

print("To Delete the references to complex numbers created use del comp1, comp2, comp3")
del comp1, comp2, comp3
