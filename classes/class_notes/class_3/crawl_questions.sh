#! /bin/bash

# ----------------------------------------
# This code extracts the *list of Questions*
# From StackExchange:
# https://worldbuilding.stackexchange.com/questions?tab=newest&page=$page
# 1.- Iterate over n urls and download the html.
# TODO
# ....
# DONE
# 2.- In class we saw how to Extract the list of 'Hot Topic Questions'
#     Key Concepts to bear in mind:
#     - gsed pattern logic: '/init_pattern/,/end_pattern/action/flags'
#          init_pattern : any regular expression.
#          + Class examples:
#            1) Printing
#               # Prints lines containing 'N', 'n', or 'w'
#               echo -e 'Hello world!\nGoodBye World!\nNot a Blank line\n not a Blank line with space\n23423' | gsed -nE '/(N|n|w)/p'
#            2) Substitution
#               # First, sets the scope of analysis between the *first line* that begining with 'this' and the *last line*
#               # begining with 'up' with printing pattern.
#               # Second, shifts number sequences with non number sequences.
# echo -e 'Hello 123423 world!\nGoodBye World!\n23423numbers\nNot a Blank line\nthis_line_change23423423\n not a Blank line with space\nalso_325654654_ this_line23423423\nup to here!!\nnotthis2342342 lineplease243423432' | gsed -En '/^this/,/^up/p' | gsed -nE '/[0-9]+$/s/^([^0-9]+)([0-9]+)/\2 \1/gp'
# TODO
#    Extract the urls of regular (non 'Hot Topic Questions')
#     HINT:
#     In class we used
#     - gsed -nE '/.*hot-network-questions.*/,/.*<\/ul>.*/p'
#     followed by
#     - gsed -nE '/.*<li.*>.*/,/.*<\/li>.*/p'
#     to narrow the scope of the anlysis
#     (is the second filter necessary? Explain your reasoning---for extra credit provide a working script with your example)
#     Finally we extracted the content with:
#     gsed -E '/</s/.*title=\"([^\"]+)\"[^href]+href=\"([^\"]+)\".*/\1 \t \2/gp'
# ----------------------------------------
download_pages="${1:y}"
n_pages="${2:-10}"

if [[ $download_pages =~ (y|Y) ]]
then
    for page in $(seq $n_pages)
    do
        curl "https://worldbuilding.stackexchange.com/questions?tab=newest&page=$page" >> all_questions.txt
    done
fi

sleep 1

cat all_questions.txt #  your code goes here.
