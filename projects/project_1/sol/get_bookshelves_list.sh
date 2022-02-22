#! /bin/bash

# ----------------------------------------
# In this script we download the full list
# of bookshelfs available at:
# https://www.gutenberg.org/ebooks/bookshelf/
# TODO: explore the output of the script as it is
# make sure that the structure of the final
# file is correct.
# n_bookshelf = number of row in file
# id = id of the bookshelf
# title = title of the bookshelf
# url = link that takes you directly to the
#       bookshelf.
# HINT: use awk
# REMEMBER TO CHECK YOUR IMPLEMENTATION
# ----------------------------------------

bookshelves_path="$1/bookshelves"

# echo -e 'id\ttitle\turl' > "$bookshelves_path/bookshelves.txt"

curl -s https://www.gutenberg.org/ebooks/bookshelf/  | gsed -nEf get_bookshelves_list_sed | gsed  -e '/.*title=.*/d' -e 's/\"\"/,\"/g' | awk -F ',' '{print $1"\t" $2"\t" "https://www.gutenberg.org/ebooks/bookshelf/"$1}' >>  "$bookshelves_path/bookshelves.txt"

# CHECK YOUR IMPLEMENTATION. RUN: 
# cat "$path/titles.txt" | awk -F '\t' '{print NF}' | sort | uniq -c  # expected output: 339 4
