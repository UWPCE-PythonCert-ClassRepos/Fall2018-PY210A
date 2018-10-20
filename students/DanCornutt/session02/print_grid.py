def dline(n):
    print('+' + (n * '-') + '+' + (n * '-') + '+')

def empline(n):
    print('|' + (n * ' ') + '|' + (n * ' ') + '|')

def print_grid(size):
    if size < 3:
        size = 3
    elif size == 11:
        size = 9
    mid = int((size - 1) / 2)
    dline(mid)
    for i in range(mid):
        empline(mid)
    dline(mid)
    for i in range(mid):
        empline(mid)
    dline(mid)

def str_build(outer, inner, anchor, middle):
    str = anchor
    for i in range(outer):
        str = str + (inner * middle) + anchor
    return str

def print_grid2(outer,inner):
    if outer < 1 or inner < 1:
        print('I cannot make a grid with those dimensions.')
    else:
        for j in range(outer * inner + outer + 1):
            if j == 0 or j % (inner + 1) == 0:
                anchor, middle = '+', ' - '
            else:
                anchor, middle = '|', '   '
            print(str_build(outer, inner, anchor, middle))
