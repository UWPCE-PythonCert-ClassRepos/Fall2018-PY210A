def grid_2(n):
    
    print (
"""
As per homework, this gird work correctly for odd number of n.
The grid will be imbalance for even number of n
"""
    )
    
    for i in range(n+2):
        if (i == 0) or (i == n+1) or (i == int((n+1)/2)):
            print("+" + ("-")*int(n/2) + "+" + ("-")* int(n/2) + "+")
        else:
            print ("|" + (" ")*int(n/2) + "|" + (" ")*int(n/2) + "|")

    
grid_2(15)

#Output
'''
+-------+-------+
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
+-------+-------+
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
+-------+-------+
'''
