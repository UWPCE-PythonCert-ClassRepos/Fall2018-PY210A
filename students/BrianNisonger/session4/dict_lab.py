def dictionary_1(food_dict):
    print(food_dict)
    del food_preferences["cake"]
    print(food_preferences)
    food_preferences["fruit"]="Mango"
    print(food_preferences)
    for items in food_preferences:
        print (items)
    for items in food_preferences:    
        print (food_preferences[items])
    print(bool("cake" in food_preferences))
    print(bool("Mango" in food_preferences.values()))

def dictionary_2(food_preferences):
      count_t={}
      for items in food_preferences:
        lower_case=food_preferences[items].lower()
        count_t[food_preferences[items]]=lower_case.count("t")
      print(count_t)

def set_1():
    s2=set()
    s3=set()
    s4=set()
    for i in range(21):  
        if not i%2:
            s2.add(i)
        if not i%3:
            s3.add(i)
        if not i%4:
            s4.add(i)    
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

def set_2():
    s_string=set("Python")
    s_string.add("i")
    fs_string=frozenset("marathon")
    print(s_string.union(fs_string))
    print(s_string.intersection(fs_string))
    
if __name__ == "__main__":
    food_preferences={
    "name":"Chris",
    "city":"Seattle",
    "cake":"Chocolate"
    }   
    dictionary_1(food_preferences)
    dictionary_2(food_preferences)
    set_1()
    set_2()    