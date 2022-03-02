#! /Users/luis/anaconda3/envs/nlu/bin/python

import string
import time
import numpy as np

if __name__ == '__main__':

    letters = string.ascii_letters

    # ----------------------------------------
    # This script iterates over letters and
    # gets the following output:
    # aA
    # abBA
    # abcCBA
    # ...
    # abc..xyzZYX...cba
    # TASK:
    # Think about the following solution:
    # [ letters[:i+1] + letters[M+i:M-1:-1] for i in range(M)]
    # Time the two solutions on a random string of 1M characters.
    # How to time a func:
    # t1 = time.time()
    # func
    # t2 = time.time()
    # print(t2 - t1)
    # ----------------------------------------
    letters = ''.join(np.random.choice(list(letters), 100000))

    M = len(letters)//2

    lcomp = [ letters[:i+1] + letters[M+i:M-1:-1] for i in range(M)]

    regular = []
    for i in range(M):
        regular.append(letters[:i+1] + letters[M+i:M-1:-1])  # array2[::-1][:i+1]
    t2 = time.time()


