#!/bin/bash

# ----------------------------------------
# This script extracts all team names in
# home_dir/course_generals/teams and
# creates a 'class_participation_file:
# .all_teams.txt'
# -> | team, score |
# ----------------------------------------

# Replace "" with absolute path to home_dir: FuentesDeDatos
home_dir=${1:-""}
team_dir="$home_dir/course_generals/teams"
part_file="$home_dir/course_generals/teams/.all_teams.txt"
# Check if it is a valid directory
while [[ ! -d $home_dir ]]
do
    echo 'not a valid path. Please provide a valid path'
    read home_dir
done

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
# ----------------------------------------
# 1. What type of file name could break this code?
# *Ans: any file with a dot in its name.*
# 2. Fix this bug with *sed*:
#   2.1.- Extract the full filename
#         (up to .txt), regardless of the file
#         having one or more dots '.'
#         HINT 1: remember how to replace a grouped expression
#         ex: echo 'this this' | gsed -nE 's/([a-z]+) \1/\1/gp'
#         HINT 2: what is this expression doing: ^(.*)\.txt$
#   2.2.- What does the option -n do?
#         g?
#         p?
# ----------------------------------------
for team in $( ls $team_dir | grep -Eo '^[^\.]+')
do
    echo "$team,0" >> $part_file
done
