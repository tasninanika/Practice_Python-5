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


a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))

flag = input("Enter flag (true/false): ").lower()

if (a >= 0 and b < 0 or a < 0 and b >= 0) and flag == "false":
    print("true")
elif a < 0 and b < 0 and flag == "true":
    print("true")
else:
    print("false")

