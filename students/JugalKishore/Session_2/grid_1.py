def grid_1():
    for i in range(11):
        if (i == 0) or (i == 10) or (i == 5):
            print("+" + ("-")*4 + "+" + ("-")*4 + "+")
        else:
            print ("|" + (" ")*4 + "|" + (" ")*4 + "|")
    
grid_1()

# Output
'''
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
'''