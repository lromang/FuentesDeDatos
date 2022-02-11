#! /bin/bash

cat all_questions.txt | gsed -En '/.*hot-network-questions.*/,/.*\/ul>.*/p' | sed -E 's/^ +//g' | gsed -E '/</s/.*title=\"([^\"]+)\"[^href]+href=\"([^\"]+)\".*/\1 \t \2/gp' | uniq | tr '\r' '\n' | grep -E '^\w+'
