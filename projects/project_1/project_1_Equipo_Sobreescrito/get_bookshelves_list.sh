#! /bin/bash

# ----------------------------------------
# In this script we download the full list
# of bookshelfs available at:
# https://www.gutenberg.org/ebooks/bookshelf/
# TODO:
# 1) Explore the output of the script as it is.
# 2) Strip unnecessary output.
# 3) Structure the output:
# bookshelf_id \t bookshelf_title \t bookshelf_url
# HINT 1: check how to format the bookshelf_url
# HINT 2: use awk for ouput formatting
# 4) Run code validation 
# ----------------------------------------

bookshelves_path="$1/bookshelves"

curl -s https://www.gutenberg.org/ebooks/bookshelf/  | grep -noE "/bookshelf\/.+<\/a" | sed -nE "s@bookshelf/@@gp" | sed -nE 's;"\W*title=;\t;gp' | sed -nE 's;>.+$;;gp' | sed -nE 's;.+:/;;gp' | awk -F '\t' '{print $1"\t"$2"\thttps://www.gutenberg.org/ebooks/bookshelf/"$1}' > "$bookshelves_path/bookshelves.txt"

# CHECK YOUR IMPLEMENTATION. RUN:
#cat "$path/titles.txt" | awk -F '\t' '{print NF}' | sort | uniq -c  # expected output: 339 4
