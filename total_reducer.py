#!/usr/bin/python


import sys

current_doc = None
current_count = 0
word_count = 0
doc = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from wc_mapper.py with the id (thus having 2 spaces, we need to split from the end to keep the id) 
    doc, words, count = line.rsplit('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    word_count += words
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_doc == doc:
        current_count += 1
    else:
        if current_doc:
            # write result to STDOUT
            print '%s\t%s' % (current_count, word_count)
        current_count = 1
        current_doc = doc
        
# do not forget to output the last word if needed!
if current_doc == doc:
    print '%s\t%s' % (current_count, word_count)
