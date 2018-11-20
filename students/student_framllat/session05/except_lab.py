#!/usr/bin/env python3

def safe_input():
    try:
        lab_inp = input("Input please:")
    except KeyboardInterrupt:
        print()
        return None
    except EOFError:
        print()
        return None
#
safe_input()     
