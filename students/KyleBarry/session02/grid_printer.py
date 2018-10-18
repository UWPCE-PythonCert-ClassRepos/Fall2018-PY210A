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

grid_adjusted(14)
