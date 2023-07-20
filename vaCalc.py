# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:48:22 2022
@title: VA Benefits Calculator
@author: Tj
@date: 19 July 2023
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

import os


def clear_console():
    """
    Clears terminal window
    
    Source:
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def vaCalc(p1: float, p2: float) -> float:
    """Returns the VA Table value given two percentages."""
    return round((p1 + p2) - (p1 * p2), 2)


def main():
    """
    Loops until a valid input is obtained. 
    
    Performs calculation on provided values and outputs them to the console.
    """
    clear_console()
    print("Total VA Percentage Calculator")
    print("Creator: Terrance Williams\n")
    print('\nVA Benefits calculation based on the table at'
          '\nhttps://www.benefits.va.gov/compensation/rates-index.asp\n')
          
    valid = False
    while not valid:
        percentages = input("Please input your VA percentages "
                            "(ex. \"10 40 20 50\" etc.):\n>>> ").split()
        try:
            percentages = [int(num) for num in percentages]
            if not percentages:
                raise IndexError
            if not all((0 <= x <= 100 for x in percentages)):
                raise ValueError
        except ValueError:
            print("\nError: All entries must be numbers between 0 and 100 (inclusive)\n")
        except IndexError:
            print("\nError: Must include at least one number.\n")
        else:
            valid = True
            percentages = sorted([num/100 for num in percentages], reverse=True)
        
    # Calculate percentages
    output = percentages[0]
    for j in range(len(percentages) - 1):
        output = vaCalc(output, percentages[j + 1])
        
    # Prep print-out
    output = int(round(output * 100))

    if output % 10 < 5:
        vaPert = int(output / 10) * 10
    else:
        vaPert = int((output + 10) / 10) * 10
        
    # Print the Information.
    print(f'\nVA Table Value is {output}.\n'
          f'Benefits Garnered: {vaPert}% Compensation')
    
    
if __name__ == "__main__":
    
    """
    Allow the user to reuse the program without manually initializing it again.
    """
    exiting = False
    while not exiting:
        main()
        retry = input("\nRun program again? (y/n): ").lower()
        if not(retry == 'y' or retry == "yes"):
            exiting = True
        else:
            print()

