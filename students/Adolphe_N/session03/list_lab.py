#! python3


fruits = ['Apples', 'pears', 'oranges', 'peaches']
insert_fruit = 'strawberry'
def main():
    print (fruits)
    fruit = input("what fruit would you like to add: ")
    #while fruit != " " :
    fruits.append(fruit)
        #fruit = input(" =>")
    fruit.strip()
    print (fruits)
    
    number = input("Enter a number: ")
    print (number)
    number.strip()
    if int (number) < 0:
        print('nagative numbers are not supported')
    else:
        
        
        item_fruit = fruits[int(number) - 1]
        print (item_fruit)
        other_fruit = ['mango']
        the_fruits = other_fruit + fruits
        print(the_fruits)
    
    the_fruits.insert(0, insert_fruit)
    print (the_fruits)
        
if __name__ == "__main__":
    main()