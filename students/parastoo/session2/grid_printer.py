def print_grid():
    line_a = ("+" + "-" * 4 + "+" + "-" * 4 + "+")
    line_b = ("|" + " " * 4 + "|" + " " * 4 + "|")
    print (('\n' + line_a + '\n' + line_b ) * 2)
    print (line_a)
 def print_grid_size(l, w):
    ''' l = lenght (number of '-'), w = width (number of '|')'''
    line_a = (("+" + "-" * l) + "+")
    line_b = ('\n' + ("|" + " " * l) + "|") * w
    print (('\n' + line_a + line_b ) * 2)
    print (line_a)
 def print_grid_advance(n, m):
    ''' n = number of rows, m = number of columns'''
    line_a = (("+" + "-" * 4) * m + "+")
    line_b = (("|" + " " * 4) * m + "|")
    print (('\n' + line_a + '\n' + line_b ) * n)
    print (line_a)