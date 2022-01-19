#! /bin/bash

## This function attempts to replicate the behaviour of
## 'cd'. With a twist...
## - If the user inserts a path => take her home.
## - If the user changes to home => taker to the current directory.
## CHALLENGE
## - Take the user to random directories.
## Why it is not possible
if [ -z $1 ]
then
    curr_dir=`pwd`
    echo $curr_dir
else
    echo '.'
fi
