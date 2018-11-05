#Lesson##
#File Exercise ##
#
#!/usr/bin/env python3

#Import modules
from pathlib import Path

#set folder paths
data_folder = Path("C:\pythonuw\Fall2018-PY210A\students\ericstreit\session04/")

# set the variables
file_to_open = data_folder / "students.txt"
prog_set = set()
prog_dict = {}

with open(file_to_open, 'r') as infile:
    for line in infile:
        #split the line out by the colon
        split_line = line.split(':')
        #use the second half of the lines which do not contain people's names and strip out the new lines
        no_names = split_line[1].rstrip()
        #split into a new list seperated by commas
        no_names_split = no_names.split(',')
        for items in no_names_split:
            #check for strings in the list with upper case characters. If found, skip it since it is a nickname
            if items.islower():
                prog_set.add(items)
                if not items in prog_dict:
                    prog_dict[items] = 1
                else:
                    prog_dict[items] += 1

    print("The following languages are in the list:\n {}" .format(prog_set))
    print("The count for each language is: \n{}".format(prog_dict))
infile.closed

#### work to do: The results still show the colum headers so we'll want to strip that out


#define function
def myfunc(n):
    """Update the DocString"""
    pass

#for testing
if __name__=="__main__":
    pass
