def grid(row, col, size):
  sep = '' + ('+' + (" - "*size))*col + '+\n'
  return sep + ((('|' + "   "*size)*col + '|\n') * size + sep)*row

print(grid(5,5,10))