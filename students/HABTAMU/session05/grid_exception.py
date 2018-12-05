#!/usr/bin/env python3
import sys

def print_rectangle(n) :
    """draws a grid with +, - and | lines"""
    for i in range(n+1):
        for j in range(n+1):
            if ((i in range (0,n+5,5) and j%5 == 0)) :
                print("+", end=" ")            
            elif ((i in range(0,n+5,5) and j > 0 and j < n)) :
                print("-", end=" ")            
            elif ((j in range(0,n+5,5) and i > 0 and i < n)) :
                print("|", end="     ")           
            else :
                print("", end=" ")
        print()
    return 0


def safe_input():
    """ A module of KeyboardInterrupt Exception """
    try:
        my_main()
    except KeyboardInterrupt as err:
        print()
        print("\n KeyboardInterrupt: {}".format(str(err)))
    return -1


def my_main():
    """ A module of ValueError, TypeError and  EOFError,
        Args:
            num_grid: the number which the grid computed
        Return:
            Grid square with num_grid X 5 '''
        Raise:
            ValueError, TypeError and EOFError if input is incorrect 
    """

    while True:
        try:
            num_grid = int(
                input("Enter an integer multiple of 5?:> ").strip())
            print_rectangle(num_grid)
        except ValueError as e:
            print("\n {}"\
                .format(e))
            return -1
        # safe_input()

if __name__ == "__main__":
    safe_input()


