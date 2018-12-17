#!/usr/bin/env python3

def safe_input():
    try:
        check = input('Input >>>')
        return check
    except(EOFError, KeyboardInterrupt):
        print('Error: EOF error or KeyboardInterrupt')
        return None

if __name__ == '__main__':
    check = safe_input()
    print(f'your answer is {check}')
