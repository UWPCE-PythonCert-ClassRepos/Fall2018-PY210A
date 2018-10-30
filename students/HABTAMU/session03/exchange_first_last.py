#!/usr/bin/env python3
def exchange_first_last(a_string):
    """
    Get the basics of sequence slicing down.
    Args:
        a_string: Take a sequence as an argument
    Returns:
        z_string: Return a copy of that sequence with the first and last items exchanged.
    """
    a_string = input("Pls enter a sequence of string").strip()
    
    # Change sequence of input string to list to make it mutable.
    str_list = list(a_string)

    # Assign a name for the first list.
    str_1st = str_list[0]

    # Assign the first list value with the last list value.
    str_list[0]=str_list[-1]

    # Swap the last list value with the first list value.
    str_last[-1]=str_1st

# Conver the final list to sequence of string.
    answer = "".join(tuple(a_string))

# Print out the list joined string.
    return answer

def main():
    exchange_first_last()

if __name__ == '__main__':
    main()
