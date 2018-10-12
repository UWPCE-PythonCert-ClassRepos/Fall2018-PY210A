def nameerror(one=1):
    try:
        print(one * two)
    except NameError:
        print('NameError')


def typeerror(one='one', two=[]):
    try:
        print(one * two)
    except TypeError:
        print('TypeError')


def attributeerror(one=1):
    try:
        one.format(one)
    except AttributeError:
        print('AttributeError')

def syntaxerror(message='hello world'):
    while print(message)