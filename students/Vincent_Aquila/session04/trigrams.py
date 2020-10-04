"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Trigrams Assignment in Session 4 

Note - Some items are commented out.  Depending on what input is requested - a line of text 
from def make_trigrams, or an entire an entire document from sherlocktest.txt can be run
"""



#test with trigrams
"""
words = "I wish I may I wish I might".split()

print(words)

def make_trigrams(words):
    tris = {}
    for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
        print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris

tris = make_trigrams(words)

"""



"""
opens a text file called sherlock, which is located in the same directory as 
this python file; disregard comments, they serve to remind me what the code does
"""
#this function can any argument, in this case it is being called text_file 
def file_to_word_list(text_file):    
    #opens the text file in read (r) mode and assigns txt file to variable called f (white font 
    #is argument)
    with open(text_file, 'r') as f: 
        #this is an empty list, the "container" which will hold the text
        word_list = [] 
        #find all the lines in the file, and go line by line, to build up a larger list
        for line in f.readlines(): 
            #words is a new container temporary container; splitting each line on the white space
            words = line.split() 
            #"appending" - actually "extending" words to container word list; extend is like append, 
            #except extend adds in everything
            word_list.extend(words) 
        return word_list    

        #opens the text file
        #f_contents = f.readlines() 
        #prints the sherlock file
        #print(f_contents) 

#f_contents.split()



#f_contents is the sherlock.txt file
def make_trigrams_sherlock(word_list): 
    tris = {}
    for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):
        #print(w1, w2, w3)
        pair = (w1, w2)
        if pair in tris:
            tris[pair].append(w3)
        else:
            tris[pair] = [w3]

    return tris  #this prints a very long return

#print(make_trigrams_sherlock) 
#tris = make_trigrams_sherlock(word_list)	



if __name__ == "__main__":
    # inside the () is where the actual name of the text files goes
    word_list = file_to_word_list('sherlocktest.txt')
    tris = make_trigrams_sherlock(word_list)    
    print(tris)



