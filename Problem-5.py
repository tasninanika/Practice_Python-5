# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:44:25 2025

@author: Jarin
"""

#In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

#The validation rules are as follows:

#The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
#In any other case the string is not valid.

def validate(str):
    for i in range(1, len(str), 1):
        if str[0].islower() and (str[i] == '!' or str[i] == '@' or str[i] == '#' or str[i] == '$' or str[i] == '%'):
            return 'true'
        else:
            return 'false'

str = 'asdsab234'
result = validate(str)

print(result)
