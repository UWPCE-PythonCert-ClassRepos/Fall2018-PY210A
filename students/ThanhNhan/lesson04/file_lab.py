import pathlib
import io

#Paths and File Processing
# Write a program which prints the full path for all files in the current directory, one per line

pth = pathlib.Path('./')
print(pth)
print(pth.absolute())

for f in pth.iterdir():
	print(pth.absolute() / f)

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
##???

# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
f = io.StringIO()
f.write ("some stufff")
f.seek(0)
f.read()
f.getvalue()
f.close()


# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.



# Test it with both text and binary files (maybe jpeg or something of your choosing).
f_student = open('students.txt')
students_data = f_student.read()
print(students_data)
f.close()
