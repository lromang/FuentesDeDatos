#! /Users/luis/anaconda3/envs/nlu/bin/python

# ----------------------------------------
# This script
# Generates 10K random strings
# of random length: 3-5
# - Get a dict with the following structure {w_i: c_i}
# Valid functions:
# - np.random.choice(collection, sample_size)
# - random.choice(collection)
# - random.choices(collection, k=sample_size)
# - if
# Extras:
# - Largest keys
# max(word_dict.keys(), len)
# - Words with largest number of vowels
# max(list(word_dict.keys()), key=lambda x: len(set(x) & set('aeiou')))
# - Alternative
# reduce(lambda x, acc: x if len(set(x) & set('aeiou')) > len(set(acc) & set('aeiou')) else acc, word_dict.keys())
# plotting distribution of wordlengths.
# Task1: What are your observations.
# import matplotlib.pyplots as plt
# plt.hist([len(word) for word in word_dict.keys()])
# plt.show()
# ----------------------------------------

for _ in range(M):
    r_w = ''.join(random.choices(list(letters), k=random.randint(3, 5)))
    if r_w in word_dict:
        word_dict[r_w] += 1
   else:
       word_dict[r_w] = 1
