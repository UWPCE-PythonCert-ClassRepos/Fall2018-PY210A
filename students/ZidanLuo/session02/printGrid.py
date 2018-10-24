import sys

def print_grid(x,y):
    count = 1
    #count all the possible number of lines
    lines = (y + 1) * x + 1
    plus = "+"
    minus = "-"
    shu = "|"
    empty = " "
    #draw the horizontal and vertical lines
    Horizontal = (plus + y * minus) * x +plus
    Vertical = (shu + y * empty) * x + shu
    
    #Use while loop to loop through all the possible lines
    while count <= lines :
    	if (count % (y + 1)) == 1:
             print (Horizontal)
    	else:
    	     print (Vertical)
    	count += 1
#Take arguments in Command Lines
print_grid(int(sys.argv[1]),int(sys.argv[2]));
