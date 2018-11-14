#!/usr/bin/env python3
"""Wraps input function to handle exeptions
"""


def safe_input():
    """
        : returns : input from user or None if error
    """
    try:
        return input()
    except (EOFError, KeyboardInterrupt):
        return None


if __name__ == "__main__":
    safe_input()
