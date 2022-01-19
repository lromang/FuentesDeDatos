#! /bin/bash

# https://www.gutenberg.org/ebooks/bookshelf/302

# curl https://www.gutenberg.org/ebooks/bookshelf/302 | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/'


# Issues with downloads

# curl https://www.gutenberg.org/ebooks/bookshelf/302 | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/' | tr '\n' '|' | sed -E 's/https/$https/g' | tr '$' '\n'

# ALmost done without exception case.

# cat tests/US_bookshelf.txt | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/' | tr '\n' '\t' | sed 's/https/\|https/g' | tr '|' '\n' | tr '\t' ',' | tail -n +2


# Solution but issues with commas
# cat tests/US_bookshelf.txt | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/' | tr -d '\r' |  tr '\n' '\t' | sed 's/https/\|https/g' | tr '|' '\n' | tr '\t' ',' | tail -n +2  > tests/sol_book_shelfs.csv

# Use Awk to debug

# cat tests/US_bookshelf.txt | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/' | tr -d '\r' |  tr '\n' '\t' | sed 's/https/\|https/g' | tr '|' '\n' | awk -F '\t' 'NF != 5 {print NR "\t" $0 }'

# Best alternatvie, use gnu-sed with option -E.
