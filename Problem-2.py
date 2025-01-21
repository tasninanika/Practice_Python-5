# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:41:23 2025

@author: Jarin
"""

# You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

n = int(input("Enter a number: "))

if n > 0:
    for i in range(n-1, -1, -1):
        print(i)
elif n < 0:
    for i in range(n, 0, 1):
        print(i)
        if i == -1:
            print(0)
else:
    print("already zero")
