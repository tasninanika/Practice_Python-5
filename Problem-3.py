# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:24:24 2025

@author: Jarin
"""

# Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

#Return True for the following cases:

#Either a or b (not both) is non-negative and the flag is false.
#Both a and b are negative and the flag is true.
#Otherwise, return False.


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))


if a > 0 and b < 0 or a < 0 and b > 0:
    flag = "false"
    print("true")
elif a < 0 and b < 0:
    flag = "true"
    print("true")
elif a > 0 and b > 0:
    print("flase")
