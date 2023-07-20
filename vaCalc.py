# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:48:22 2022
@title: VA Benefits Calculator
@author: Tj
@date: 29 November 2022
@description: Takes user arguments as percentages and calculates total
VA Benefits percentage based on table at https://www.benefits.va.gov/compensation/rates-index.asp

NOTE: Due to floating-point behavior, Python rounds to nearest
 even num, so 0.85 -> 0.8 instead of 0.9. Therefore, the program may slightly 
 underestimate 
 EX. (50 20 20 20 20 10 10 10 10 10 10 10 10) gives 90 instead of 91. 
 Both still result in 90% compensation because the VA rounds to the 
 nearest 10.
"""

""" Rounding Trick (not used, but useful to learn how to implement a "ceil"):
https://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten"""


import numpy as np
import sys


def vaCalc(p1, p2)->float:
    return ((p1 + p2) - (p1 * p2)).round(2)


if __name__ == "__main__":
    # Get line arguments
    num_args = len(sys.argv)
    if num_args > 2:
        args = sys.argv
        values = np.empty(num_args - 1)
        
        # Populate array
        for i in range(1, num_args):
            values[i-1] = float(args[i])
    
        values = np.flip(np.sort(values))  # sort array greatest to least
        values = values * (10 ** -2)
        
        # Calculate percentages
        output = values[0] 
        for j in range(values.shape[0] - 1):
            output = vaCalc(output, values[j +1])
            # print(output)
        # Prep print-out
        output = int((output * 100).round(0))
        
        if output % 10 < 5:
            vaPert = int(output / 10) * 10
        else:
            vaPert = int((output + 10) / 10) * 10
    
        print(f'\nVA Table Percentage is {output}.\nBenefits Garnered: \
{vaPert}% Compensation')
    else:
        print("Not enough arguments.")
