#!/usr/bin/env python
"""
creates a safer input function called safe_input()
"""

def safe_input():
    """
    :returns: user input or None if Exception
    """
    try:
        return input()
    except(EOFError, KeyboardInterrupt):
        return None

if __name__ == '__main__':
    print(safe_input())
