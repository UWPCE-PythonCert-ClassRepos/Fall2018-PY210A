import pathlib
import collections

def file_1():
    pth=pathlib.Path("./")
    for f in pth.iterdir():
        print(f'{pth.absolute()}\{f}')

def file_2(source,dest):        
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())

def file_3(source):
    name_dict={}
    lang_list=[]
    with open(source) as f:
        lines=f.readlines()
    for line in lines:
        line_out=line.split(":")
        if line_out[0] !="Name":
            name_dict[line_out[0]]=line_out[1]
    for name in name_dict:
        if name_dict[name] !="":
            languages=(name_dict[name].split(","))
            for language in languages:
                if language.islower():
                    language=language.strip()
                    lang_list.append(language)
    c=collections.Counter(lang_list)
    return c
    
            
    
    
if __name__ == "__main__":    
   source1='test.txt'
   source2='evil_kermit.png'
   dest1='test2.txt'
   dest2='test2.png'
   source3='students.txt'
   file_1()
   file_2(source1,dest1)
   file_2(source2,dest2)
   print(file_3(source3))