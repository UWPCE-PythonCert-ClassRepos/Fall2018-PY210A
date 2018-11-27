my_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(my_dict)
my_dict.pop("cake")
print(my_dict)
my_dict["fruit"] = "Mango"
my_dict.keys()
my_dict.values()
"cake" in my_dict # now False
"Mango" in my_dict.values() # True

dict_keys = {}
for k , v in my_dict.items():
	dict_keys[k] = v.count("t")

s2 = set()
s3 = set()
s4 = set()

for i in range(1,21):
	if i % 3 == 0:
		s2.add(i)
	if i % 2 == 0:
		s3.add(i)
	if i % 4 == 0:
		s4.add(i)

# Sets

s3 is subset of s2 #False
s4 is subset of s2 #True

#Sets 2

x = ("p","y","t","h","o","n")
python = set()
for i in x:
	python.add(i)
python.add("i")

y = ("m","a","r","a","t","h","o","n")
marathon = frozenset(y)

#union of two sets
marathon | python
# frozenset({'r', 'a', 'y', 'o', 'm', 'i', 'n', 't', 'p', 'h'})

#intersection of two sets
marathon & python
# frozenset({'n', 't', 'o', 'h'})

