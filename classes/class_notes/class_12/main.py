import time
import numpy as np
import pandas as pd
import string
import argparse

if __name__ == '__main__':
    # Instantiate parser.
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_words', help='Number of random words to generate.')
    parser.add_argument('--n_tests', help='Number of tests to perform.')



M = 1000000
n_tests = 1000
word_size = 4
letters = string.ascii_lowercase

# Times
regular_time = []
sorted_time = []

gen_series = lambda size: pd.Series(np.arange(size),
                                    index=[''.join(np.random.choice(list(letters),
                                                                    word_size))
                                           for _ in range(M)])
s1 = gen_series(M)
# Sorting time
sort_t1 = time.time()
s2 = s1.sort_index().copy()
sort_t2 = time.time()
print(f'Sorting time: {sort_t2 - sort_t1}')

for _ in range(n_tests):
    search_string = s1.sample().index[0]

    no_sort_t1 = time.time()
    s1.loc[search_string]
    no_sort_t2 = time.time()
    regular_time.append(no_sort_t2 - no_sort_t1)


    sort_t1 = time.time()
    s2.loc[search_string]
    sort_t2 = time.time()
    sorted_time.append(sort_t2 - sort_t1)

print(f'Regular mean retreiving time for ({n_tests} trials): {np.array(regular_time).mean()}')
print(f'Sorted mean retreiving time for ({n_tests} trials): {np.array(sorted_time).mean()}')