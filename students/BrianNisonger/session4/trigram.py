"""
trigrams
"""
"""
set default
"""
def make_words(source):
    words=""
    with open(source) as f:
        lines=f.readlines()
    punct=[",",".","-","(",")","\n","!","'s","'","?","_",";"]   
    for line in lines:
        for punc in punct:
            line=line.replace(punc," ")
        words=words+line
    words=words.replace("  "," ")
    words=words.replace('"', '')
    words=words.lower()
    return words.split()
        


def make_trigrams(words):
    tris ={}
    for w1,w2,w3 in zip(words[:-2],words[1:-1],words[2:]):
        pair=(w1,w2)
        if pair in tris:
            tris[pair].append(w3)
        else:    
            tris[(w1, w2)]=[w3]
    return tris

def make_story(tris,new_words,story):
    new_list=new_words.split()
    new_tuple=tuple(new_list)
    if new_tuple in tris:
        next_word=str(tris[new_tuple])
        punct=[",",".","-","(",")","\n","[","]","'"]   
        for punc in punct:
            next_word=next_word.replace(punc,"")
        new_words=f'{new_tuple[1]} {next_word}'
        story=f'{story} {next_word}'
        tris1=tris
        make_story(tris1,new_words,story)
    else:
        print(story)
        
    
            
    
source="ghosts.txt"
words=make_words(source)
tris=make_trigrams(words)
new_words=input("Please enter new_words:")
story=new_words
make_story(tris,story,new_words)



