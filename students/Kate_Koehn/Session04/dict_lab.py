#!/usr/bin/env python3

"""
Dictionary Lab
"""

#create dictionary
cake_pref = {"name": "Chris", "city": "Seattle", "cake": "ChocolaTe"}
print(cake_pref)

# #delete the entry for cake
# del cake_pref["cake"]
# print(cake_pref)

# #add entry for "fruit" with "Mango" and display dict
# cake_pref["fruit"] = "Mango"
# print(cake_pref)

# #display whether or not "cake" is in dict
# print("cake" in cake_pref)

# #display whether or not "Mango" is in dict
# print("Mango" in cake_pref.values())

#t_count = {}
for keys, letter in cake_pref.items():
    keys = cake_pref.keys()
    if "t" in letter or "T" in letter:
        print(letter)
###next steps are count the Ts in each value, rewrite the values as just those numbers (0,2,1)




