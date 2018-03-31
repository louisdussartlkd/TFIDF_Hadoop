#!/usr/bin/python


import sys

current_word = None
word_count = 0
document_count = 0
current_key = None
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.split('\t')
    
    # parse the input we got from IDF_mapper.py
    word = line[0]
    hash = line[1]
    key = line[2]
    
     # convert the hash and key to integers
    try:
        hash = int(hash)
    except ValueError:
        # count was not a number, so silently ignore/discard this line
        continue
    
    try:
        key = int(key)
    except ValueError:
        continue
    
    if current_word = word          # we compute the total number of words
      word_count += hash
      
    if current_key != key           # we compute the number of documents which contain this word
      document_count += 1
      
      else:
        if current_word:
            # write result to STDOUT
            tfidf = word_count/2000*log(document_count/10)
            print '%s\t%s' % (current_word,tfidf)
        current_count = count
        current_word = word 

# do not forget to output the last word if needed!
if current_word == word:
    tfidf = word_count/2000*log(document_count/10)
    print '%s\t%s' % (current_word, current_count)
