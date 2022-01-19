#! /bin/bash


if [ $1 -gt 0 ]
then
    echo "abs($1) = $1"
else
    echo "abs($1) = $((-1*$1))"
fi
