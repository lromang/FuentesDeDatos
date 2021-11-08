#! /Users/luis/anaconda3/envs/courses/bin/python

import re
import sys

def validate_coord(coord):
    '''
    :param coord: a string to validate
    :return: Valid if it is a validate coordinate, Invalid in any other case
    '''
    lat_pattern =  # Your code goes here
    lon_pattern =  # Your code goes here
    pattern = fr'{lat_pattern}, {lon_pattern}'
    if bool(re.search(pattern, coord)):
        return 'Valid'
    return 'Invalid'

if __name__ == '__main__':
    n_iters = int(sys.stdin.readline())
    output = []
    for i in range(n_iters):
        print(validate_coord(sys.stdin.readline()))


