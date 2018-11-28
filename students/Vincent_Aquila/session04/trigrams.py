"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Trigrams Assignment in Session 4 - needs further work, but functions with the sherlock text file and a string of text
     --- please disregard items that are commented out, this is still in progress ---

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
#opens a text file called sherlock, which is located in the same directory as this python file
def file_to_word_list(text_file): #this function can any argument, in this case it is being called text_file   
    with open(text_file, 'r') as f: #opens the text file in read (r) mode and assigns txt file to variable called f (white font is argument)
        word_list = [] #this is an empty list, the "container" which will hold the text
        for line in f.readlines(): #find all the lines in the file, and go line by line, to build up a larger list
            words = line.split() #words is a new container temporary container; splitting each line on the white space
            word_list.extend(words) #"appending" - actually "extending" words to container word list; extend is like append, except extend adds in everything
        return word_list    


        #f_contents = f.readlines() #opens the text file
        #print(f_contents) #prints the sherlock file

#f_contents.split()

def make_trigrams_sherlock(word_list): #f_contents is the sherlock.txt file
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
    word_list = file_to_word_list('sherlocktest.txt')# inside the () is where the actual name of the text files goes
    tris = make_trigrams_sherlock(word_list)    
    print(tris)

#this returns a dictionary

