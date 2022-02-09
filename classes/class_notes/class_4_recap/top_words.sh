#! /bin/bash

# ----------------------------------------
# This code gets the top n most frequent
# words in crime.txt.
# PARAMS:
# - top = top words to print, defaults to 10
# This code reads and validates a letter from
# the user.
# Your task is to read, understand and
# execute this code. Make sure you try
# to break this code (enter invalid 'letters').
# ----------------------------------------

# Top letters
top=${1:-10}

# Ask user for a letter
echo 'Please enter a letter to find: '
# Check it is in fact a letter HINT: use an if =~
read letter
while [[ ! $letter =~ ^[a-zA-Z]{1}$ ]]
do
    echo 'please enter a valid letter'
    read letter
done
# Get top words.
cat crime.txt | gsed -E 's/[^A-Za-z ]//g' | grep -v '^$' | grep -ioE '[a-z]+' | tr '[:upper:]' '[:lower:]' | grep -E "^$letter.+" | sort | uniq -c | sort -nr | head -n $top
