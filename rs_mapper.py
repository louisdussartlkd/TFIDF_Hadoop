#!/usr/bin/python

import sys
from random import randint
import string
import re


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace and punctuation
    line = line.strip()
    line = re.sub('['+string.punctuation+']', '', line)

    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
    #add a random number between 0 and 10000 as a key
        print '%s\t%s' % (word, randint(0,10000))
