def grid():
    """Part I: printing the grid"""
    plus = '+'
    hyphen = ' -'
    empties = '  '
    
    plus_line = plus + (hyphen*4) + ' ' + plus + (hyphen*4) + ' ' + plus + '\n'
    no_plus_line = '|' + empties*4 + ' ' + '|' + empties*4 + ' ' + '|' + '\n'
    
    print(plus_line + (no_plus_line*4) + plus_line +
    (no_plus_line*4) + plus_line)

def grid_adjusted(n):
    """Part II: adjusting the size of the grid"""
    plus = '+'
    hyphen = ' -'
    empties = '  '
    
    plus_line = plus + (hyphen*n) + ' ' + plus + (hyphen*n) + ' ' + plus + '\n'
    no_plus_line = '|' + empties*n + ' ' + '|' + empties*n + ' ' + '|' + '\n'
    
    print(plus_line + (no_plus_line *n) + plus_line +
    (no_plus_line *n) + plus_line)

def grid_boxes(d, c):
    """Part III: print out grid with rows, columns as first param and
    length of cells as second param"""
    plus = '+'
    hyphen = ' -'
    empties = '  '

    plus_line = plus + (hyphen*c) + ' '
    no_plus_line = '|' + (empties*c) + ' '

    full_lines = plus_line*d + plus + '\n'
    next_lines = no_plus_line*d + '|' + '\n'

    alls = full_lines+next_lines*c
    print(alls*d + full_lines)

grid_boxes(4, 1)


















