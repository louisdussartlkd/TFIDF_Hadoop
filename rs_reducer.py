#!/usr/bin/python


import sys
import random


key_val = set(random.sample(range(0, 10000), 10))
out_key = random.randint(0,10000)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from RS_mapper.py
    couple = line.split('\t')
    word = couple[0]
    key = int(couple[1])

    # print key_val,key
    try:
        if key in key_val:
            print '%s\t%s' % (word, out_key)
    except ValueError:
        # key was not a number, so silently
        # ignore/discard this line
        continue
