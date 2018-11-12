#! python3


fruits = ['Apples', 'pears', 'oranges', 'peaches']

insert_fruit = 'strawberry'
def main():
    print (fruits)
    fruit = input("what fruit would you like to add to the fruits list: ") # prompt user to enter a fruit item to add to list
    #while fruit != " " :
    fruits.append(fruit)
        #fruit = input(" =>")
    fruit.strip()
    print (fruits)
    
    number = input("Enter a number: ") # prompt user to enter a number to see the corresponding item in the list
    print (number)
    number.strip()
    if int (number) < 0:
        print('nagative numbers are not supported')
    else:
        
        
        item_fruit = fruits[int(number) - 1]
        print ('item {} you entered correspond to this fruit item: {}'.format(number, item_fruit))
        other_fruit = ['mango']
        prompt_line = input('Press Enter to add mango to the list')
        the_fruits = other_fruit + fruits
#         print(the_fruits)
#         prompt_line = input('Press Enter to add Kiwi to the list')
#         print (['Kiwi']+ the_fruits)
#         prompt_line = input('Press Enter to add Strawberry to the list')
#         the_fruits.insert(0, insert_fruit)
#         print (the_fruits)
#         prompt_line = input('Press Enter to display fruits that start with "P" ')
#     
#     for item in the_fruits:
#         
#         if item[0] == 'p':
#             print('the fruit that start with p are displayed below: {}' .format(item))
#            

    print('series 2')
    
    print('the current fruit list contains: {}'.format(the_fruits))
    prompt_line = input('Press Enter to display the fruit list with last item removed')
    print ('{}'.format(the_fruits[:-1]))
    fruit_delete = input('What fruit would you like to delete: ')
    fruit_delete.strip()
    the_fruits.remove(fruit_delete)
    print(the_fruits)
    
    print('series 3')
    
    for item in the_fruits[:]:
        fruit_choice = input('Do you like {}? (y/n): '.format(item)).lower()
#         while fruit_choice not in ['y' or 'n']:
#             fruit_choice = input('Please choose y or n')
#         
#         if fruit_choice == 'n':
#             the_fruits.remove()
        
        if fruit_choice == 'y':
            continue
        elif fruit_choice == 'n':
            the_fruits.remove(item)
            print('{} has been removed from the list: '.format(item))
            print(the_fruits)
            #fruit_choice = input('Do you like {}? (y/n): '.format(item))
#         else:
#             print('Please choose y or n')
#             fruit_choice = input('Do you like {}? (y/n): '.format(item))
            
            
    print('Series 4')
    
    n = len(the_fruits)
    reverse_fruits = []
    for fruit in the_fruits:
        r_fruit = fruit[::-1] 
        reverse_fruits.append(r_fruit)
        
    print(the_fruits)
    print(reverse_fruits)
    print("The original list is {} minus the last item.".format(the_fruits[0:n-1]))
    print("The original list items spelled backwards is {}: ".format(reverse_fruits))
   
    

    
    
if __name__ == "__main__":
    main()