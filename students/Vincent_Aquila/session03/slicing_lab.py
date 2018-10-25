"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
assignment objective: Slicing Lab

Write some functions that take a sequence as an argument, and return a copy of that sequence:

1) with the first and last items exchanged.
2) with every other item removed.
3) with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
4) with the elements reversed (just with slicing).
5) with the last third, then first third, then the middle third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

Your functions should look like:

def exchange_first_last(seq):
    return a_new_sequence
"""



#1) with the first and last items exchanged
def swap_first_last(list):
    x = len(list)
    print(x-1) #test-output test shows x = 8, or 8 indicies
    temp = list[8] #the number 9 is placed in the variable called 'temp'
    print(temp) #test-output is the number 9
    list[8] = list[0] #the number 1 is now where the number 9 is located
    print(list[8]) #test-shows that the number 1 is in index 8
    list[0] = temp #the number 9 has been shifted to the first index
    new_list = list
    print(new_list) #new list with numbers 1 and 9 swapped

swap_first_last(list = [1, 2, 3, 4, 5, 6, 7, 8, 9])



#2) with every other item removed
def remove_every_other(list):
    print(list[0:9:2])

remove_every_other(list = [1, 2, 3, 4, 5, 6, 7, 8, 9])



#3) with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
def first_4_last_4(list):
    print(list[4:]) #removes first four
    print(list[:4]) #removes last four

first_4_last_4(list = [1, 2, 3, 4, 5, 6, 7, 8, 9])



#4) with the elements reversed (just with slicing)
def reverse_list(list):
    print(list[::-1])

reverse_list(list = [1, 2, 3, 4, 5, 6, 7, 8, 9])



#5) with the last third, then first third, then the middle third in the new order
def thirds(list):
    i = list[:3]
    j = list[3:6]
    k = list[6:9]
    print(k,i,j)

thirds(list = [1, 2, 3, 4, 5, 6, 7, 8, 9])


"""
#run tests - this isn't working - will get help later
if __name__ == "__main__":
    assert swap_first_last(new_list)  == [9, 2, 3, 4, 5, 6, 7, 8, 1]
"""
