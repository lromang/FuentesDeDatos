#! /bin/bash

st=''
for c in {a..z}
do
    if [ $(($RANDOM % 2)) -eq 0 ]
    then
        st+=" $c"
    fi
done
echo $st
