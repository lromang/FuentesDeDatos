#! /bin/bash


if [ `echo "Hello World" | grep -o $1` ]
then
    echo 'Pattern found'
else
    echo 'Pattern not found'
fi
