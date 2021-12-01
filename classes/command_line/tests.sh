#! /bin/bash

if (( 5 < 3 ))
then
    echo 'Success 1'
elif (( 5 < 4 ))
then
     echo 'Success 2'
else
    echo 'Failure'
fi
