#! /bin/bash

path=$1

curl -s https://www.gutenberg.org/ebooks/bookshelf/ | gsed -nEf get_libraries_sed | gsed  -e '/.*title=.*/d' -e 's/\"\"/,\"/g' > "$path/titles.txt"
