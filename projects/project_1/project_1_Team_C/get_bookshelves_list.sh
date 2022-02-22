#! /bin/bash

# ----------------------------------------
# In this script we download the full list
# of bookshelfs available at:
# https://www.gutenberg.org/ebooks/bookshelf/
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

#FINAL:
curl -s https://www.gutenberg.org/ebooks/bookshelf/  | sed -nEf get_bookshelves_list_sed_mod | grep -o '".*"' | sed 's/"/\t/g'| awk  -F '\t' '{print strtonum(substr($2, 19)) "\t""\t" $4 "\t""\t" $2}' >  "$bookshelves_path/bookshelves.txt"

#curl -s https://www.gutenberg.org/ebooks/bookshelf/  | sed -nEf get_bookshelves_list_sed_mod | # your code goes here 1 | # your code goes here 2 >  "$bookshelves_path/bookshelves.txt"
#curl -s https://www.gutenberg.org/ebooks/bookshelf/  | sed -nEf get_bookshelves_list_sed_mod | grep -o '".*"' | sed 's/"/\t/g' | awk -F '\t' '{print $4 "\t" $2}'
#awk {$1 href....$1 $2}

# CHECK YOUR IMPLEMENTATION. RUN:
# cat "$path/titles.txt" | awk -F '\t' '{print NF}' | sort | uniq -c  # expected output: 339 4

# curl -s https://www.gutenberg.org/ebooks/bookshelf/ | awk -F "</*li>" '/<\/*li>/ {print $2}' | grep -E 'title' | grep -E 'ebooks/bookshelf/'| sed -e 's/\(<[^<][^<]*>\)//g'
# curl -s https://www.gutenberg.org/ebooks/bookshelf/ | awk -F "</*li>" '/<\/*li>/ {print $2}' | grep -E 'title' | grep -E 'ebooks/bookshelf/'| sed -e 's/[^0-9][/ebooks/bookshelf/]*//g'

# curl -s https://www.gutenberg.org/ebooks/bookshelf/ | awk -F "</*li>" '/<\/*li>/ {print $2}' | sed -e 's/\([0-9][/ebooks/bookshelf/]*\)//g'
# curl -s https://www.gutenberg.org/ebooks/bookshelf/ | awk -F "</*li>" '/<\/*li>/ {print $2}' | sed -e 's/[0-9][/ebooks/bookshelf/]*//g'
# curl -s https://www.gutenberg.org/ebooks/bookshelf/ | awk -F "</*li>" '/<\/*li>/ {print $2}' | grep -E 'title' | grep -E 'ebooks/bookshelf/' | sed -e 's/[^0-9][/ebooks/bookshelf/]*//g'
