'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''
import re
if __name__ == '__main__':
    pass

def add(i,j):
    return i+j

# we don't care about case sensitivity and therefore use lower:
ulysses_txt = open("books/james_joyce_ulysses.txt").read().lower()

words = re.findall(r"\b[\w-]+\b", ulysses_txt)
print("The novel ulysses contains " + str(len(words)))


for word in ["the", "while", "good", "bad", "ireland", "irish"]:
    print("The word '" + word + "' occurs " + \
          str(words.count(word)) + " times in the novel!" )

novels = ['sons_and_lovers_lawrence.txt', 
          'metamorphosis_kafka.txt', 
          'the_way_of_all_flash_butler.txt', 
          'robinson_crusoe_defoe.txt', 
          'to_the_lighthouse_woolf.txt', 
          'james_joyce_ulysses.txt', 
          'moby_dick_melville.txt']

for novel in novels:
    txt = open("books/" + novel).read().lower()
    words = re.findall(r"\b[\w-]+\b", txt)
    diff_words = set(words)
    n = len(diff_words)
    print("{name:38s}: {n:5d}".format(name=novel[:-4], n=n))
    


    
    
    