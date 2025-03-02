# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:02:50 2025

@author: Jarin
"""

# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

def max_min_arr(arr):
    max_num = arr[0]
    for i in range(1, 4, 1):
        if max_num < arr[i]:
            max_num = arr[i]
    
    min_num = arr[0]
    for i in range(1, 4, 1):
        if min_num > arr[i]:
            min_num = arr[i]
    
    return max_num, min_num

arr = [65, 44, 11, 22]

max_num, min_num = max_min_arr(arr)
    
print(max_num, min_num)
    