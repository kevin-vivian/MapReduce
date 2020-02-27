#!/usr/bin/env python3
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys
import pandas as pd 
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    cols = ['word', 'count']
    df = pd.DataFrame(columns=cols)

    data = read_mapper_output(sys.stdin, separator=separator)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print('%s%s%d' % (current_word, separator, total_count))
            df['word'] = current_word
            df['count'] = total_count
        except ValueError:
            pass

if __name__ == '__main__':
    main()