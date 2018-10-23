# PART 1
plus = "+ "
minus = "- "
v = "|         "

def printG():
    for i in range(0,2):
        print(plus+minus*4+plus+minus*4+plus)
        for i in range(0,4):
            print(v+v+v)
    print(plus+minus*4+plus+minus*4+plus)

printG()

# PART 2
print("PART 2 START")
plus = "+ "
minus = "- "
v = "|"
s = " "

def print_grid(n):
    N = int((n-1)/2)
    for i in range(0,2):
        print(plus+minus*N+plus+minus*N+plus)
        for i in range(0,N):
            print(v+s*n+v+s*n+v)
    print(plus+minus*N+plus+minus*N+plus)

print_grid(3)
print_grid(15)

# PART 3
print("PART 3 START")
plus = "+ "
minus = "- "
v = "|"
s = " "

def print_grid2(n1,n2):
    n_s = int(n2*2+1)
    for i in range(0,n1):
        print((plus+minus*n2)*n1+plus)
        for i in range(0,n2):
            print((v+s*n_s)*n1+v)
    print((plus+minus*n2)*n1+plus)

print_grid2(3,4)
print_grid2(5,3)











