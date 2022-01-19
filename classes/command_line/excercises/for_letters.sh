#! /bin/bash


for l in {a..z}
do
    boolVar=$(($RANDOM % 2))
    if [ ! $boolVar -gt 0 ]
    then
        L=`echo $l | tr '[:lower:]' '[:upper:]'`
        echo "$boolVar $L"
    else
        echo "$boolVar $l"
    fi
done
