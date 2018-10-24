def print_grid2(length, minus): 
    plus = "+"   
    minus_num = minus * "-" 
    pipe = "|" 
    space = minus * " "     	
    i = 0
    while (i < length):
    	line = plus + minus_num
    	line = line * length + "+"
    	column = (pipe + space) * length + pipe
    	column = ("\n" + column) * minus
    	print(line + column)
    	i += 1    
     
    line = line 
    print(line) 

if __name__ == "__main__":
	print_grid2(4,6)

    