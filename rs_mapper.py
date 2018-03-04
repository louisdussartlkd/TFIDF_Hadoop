#!/usr/bin/python

import sys
import string
import re


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace, punctuation and caps
    line = line.strip()
    line = re.sub('['+string.punctuation+']', '', line)
    line = line.lower()

    # split the line into words
    words = line.split()

    for word in words:
        print '%s\t%s' % (word, 1)
