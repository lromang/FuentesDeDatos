#!/bin/bash

home_dir=${1:-"/Users/luis/Documents/Projects/Teaching/ITAM/FuentesDeDatos"}
team_dir="$home_dir/course_generals/teams"
part_file="$home_dir/course_generals/teams/.all_teams.txt"
# Check if it is a valid directory
while [[ ! -d $home_dir ]]
do
    echo 'not a valid path. Please provide a valid path'
    read home_dir
done

# List all files in teams and get team name
# 1. What type of file name could break this code?
# 2. Any other precaution?
echo $part_file
if [[ -f $part_file ]]
then
    echo 'The file already exists, do you wish to replace it? (y/n)'
    read ans
    if [[ $ans =~ ^(Y|y).* ]]
    then
        echo '' > $part_file
    fi
fi

for team in $( ls $team_dir | grep -Eo '^[^\.]+')
do
    echo "$team,0" >> $part_file
done
