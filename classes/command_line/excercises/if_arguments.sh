#! /bin/bash

echo "$#"

if [ $# -le 1  ]
then 
    echo "Need arguments to compute the sum"
elif [ $# -gt 2 ]
then
     echo "Only know how to operate with two sumands"
fi


