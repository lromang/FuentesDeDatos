#! /bin/bash

# ----------------------------------------
# This code reads hot topic questions and
# structures the output using sed and awk.
# ----------------------------------------

cat all_questions.txt | gsed -En '/.*hot-network-questions.*/,/.*\/ul>.*/p' | sed -E 's/^ +//g' | gsed -E '/</s/.*title=\"([^\"]+)\"[^href]+href=\"([^\"]+)\".*/\1 \t \2/gp' | uniq | tr '\r' '\n' | grep -E '^\w+' | awk -F '\t' 'BEGIN {OFS = "\t"} NF == 2 {last = $0} NF == 1 {print last, $0}'
