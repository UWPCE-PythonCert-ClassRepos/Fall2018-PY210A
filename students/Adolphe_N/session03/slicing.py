#! python3

a_string = 'this is a string'
a_tuple = (2,54,13,12,5,32)
name = 'Seattle'

'''
prints the list with the last item first and first item last
'''
def exchange_first_last():
    
    #this will exchange the first and last character of the string
    print(a_string)
    print ('{}{}{}'.format(a_string[-1], a_string[1:-1], a_string[0]))
    
    print(a_tuple)
    print ('({}, {}, {}, {}, {}, {})'.format(a_tuple[-1], a_tuple[1],a_tuple[2], a_tuple[3],a_tuple[4],
                                               a_tuple[0]))
'''
first and last 4 items removed along with every other item 
'''
def remove(n):
    
    len_str = len(n)
    print (a_string)
    print (n[4:(len_str-4):2])
'''
prints the reversed list
'''
def reverse(n):
    len_str = len(n)
    print(a_string)
    print (n[::-1])
'''
prints the last third of the list first, then the first third then the middle third
'''
def new_order(n):
    len_str = len(n)
    third = (len_str // 3)
    print(a_string)
    print("{}, {}, {}".format(n[(third)::], n[0:third], n[third:(third)]))
    print("{}, {}, {}".format(n[(third * 2)::], n[0:third], n[third:(third*2)]))
    
if __name__ == '__main__':
    exchange_first_last()
    remove(a_string)
    reverse(a_string)
    new_order(name)