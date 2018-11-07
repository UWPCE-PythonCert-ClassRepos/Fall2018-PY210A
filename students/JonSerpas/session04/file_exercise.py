import os

# Write a program which prints the full path for all files in the current directory, one per line

for i in os.listdir():
	print(i)

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).

infile = open('students.txt' , 'rb')
os.system('touch copied_file.txt')
outfile = infile.readlines()
with open('copied_file.txt' , 'w') as f:
	for line in outfile:
		f.write(line)

# Write a little script that reads that file, and generates a list of all the languages that have been used.

languages = []
with open('students.txt' ,'r') as infile:
	infile = infile.readlines()[1:]
	for line in infile:
		line = line.split()
		for i in line:
			i = (i.strip("\n").replace(",", "").replace(":",""))
			if i[0].islower() == True:
				languages.append(i)
languages = list(set(languages))
print("There are {} unique languages in the class.".format(len(languages)))



