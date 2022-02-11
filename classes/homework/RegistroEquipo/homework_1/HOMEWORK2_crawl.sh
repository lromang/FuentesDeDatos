 #! /bin/bash

#----------------------------------------
# This script extracts a list of relevant
# questions from stack exchange.
# 1.- Iterate over n_pages and download the html. (due for Thursday 2022-02-03)
#----------------------------------------

n_pages="${1:-10}"
texto=". "

for p in $(seq $n_pages)
do
	echo $p
	curl https://stackexchange.com/?page=$p | grep -oE 'title=\"[^\"]+\"' >> htmlsStackExchange.txt
done

