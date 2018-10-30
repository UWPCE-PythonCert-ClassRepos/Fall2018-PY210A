#!/usr/bin/env python3
def exchange_first_last():
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

    str_1st = str_list[0]
    str_list[0]=str_list[-1]
    str_list[-1]=str_1st

    # Conver the final list to sequence of string.
    answer = "".join(tuple(str_list))

    # Print out the list joined string.
    print(answer)

def main():
    exchange_first_last()

if __name__ == '__main__':
    main()
