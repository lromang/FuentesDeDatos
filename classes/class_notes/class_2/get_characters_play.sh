#! /bin/bash

# ----------------------------------------
# Get the top N (default 10) characters
# in Macbeth.
# Why it is necessary to sort twice?
# What does 'uniq -c' do?
# Relace the regex with: '\w+'. Explain.
# ----------------------------------------

# top characters
top=${1:-10}

cat mac.txt | tr '\r' '\n' | grep -Eo '^[A-Z]+\.$' | sort | uniq -c | sort -nr | head -n $top
