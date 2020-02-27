#!/usr/bin/env python3

"""mapper.py"""

import sys
import pandas as pd

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from stdin
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print('%s%s%d'%(word, separator, 1))
         


if __name__ == '__main__':
    main()