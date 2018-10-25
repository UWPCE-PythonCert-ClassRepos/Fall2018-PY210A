def print_grid(m=2,n=4):
	init_str="+"
	mid_str="-"*n
	partial_line=init_str+mid_str
	line=partial_line*m+init_str
	side_str="|"
	side_middle=" "*n
	mid_partial=side_str+side_middle
	mid_line=mid_partial*m+side_str
	for j in range (m):
		print (line)
		for i in range(n):
			print (mid_line)
	print (line)	
	pass

print_grid(3,4)	

	