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

#item 1
print("---Item 1: with the first and last items exchanged")
def swap_first_last(list):
    x = list[:1]
    list[:1] = list[-1:]
    list[-1:] = x
    print(list)
swap_first_last(list = ([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#item 2
print("---Item 2: with every other item removed")
def remove_every_other(list2):
    print(list2[0:9:2])
remove_every_other(list2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#item 3
print("---Item 3: with the first 4 and the last 4 items removed, and then every other item in the remaining sequence")
def first_4_last_4(list3):
    y = list3[4:] #removes first four
    y1 = y[0:9:2]
    print(y1)
    z = list3[:4] #removes last four
    z1 = z[0:9:2]
    print(z1)
first_4_last_4(list3 = ([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#item 4
print("---Item 4: with the elements reversed (just with slicing)")
def reverse_list(list4):
    print(list4[::-1])
reverse_list(list4 = ([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#item 5
print("---Item 5: with the last third, then first third, then the middle third in the new order")
def thirds(list5):
    i = list5[:3]
    j = list5[3:6]
    k = list5[6:9]
    print(k,i,j)
thirds(list5 = ([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#run tests - this isn't working - will get help later
#if __name__ == "__main__":
#    assert swap_first_last([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 2, 3, 4, 5, 6, 7, 8, 1]
