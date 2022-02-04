#! /bin/bash

#----------------------------------------
# This script extracts a list of relevant
# questions from stack exchange.
# 1.- Iterate over n_pages and download the html. (due for Thursday 2022-02-03)
# https://worldbuilding.stackexchange.com/questions?tab=newest&page=1
#----------------------------------------

n_pages="${1:-10}"

for page in $(seq $n_pages)
do
    curl "https://worldbuilding.stackexchange.com/questions?tab=newest&page=$page" >>  stack_ex.txt;
done
