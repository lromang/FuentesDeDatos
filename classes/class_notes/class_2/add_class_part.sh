#! /bin/bash

# ----------------------------------------
# This script adds a participation point
# to a given team.
# 1.- Take a look at the bash script
#     try to put in words its functionality.
# 2.- Replace this code with a loop in plain bash.
# 3.- Which implementation is more convenient.
# ----------------------------------------

home_dir=${1:-./}
team=$2
points=${3:-1}
file_path="$home_dir/course_generals/teams/.all_teams.txt"
aux_path="$home_dir/course_generals/teams/team_aux.txt"

cat $file_path | grep -Ev '^$' | awk -F ',' -v points="$points" -v team="$team" '{if ($1 ~ team) print $1 "," $2 + points; else print $1 "," $2}' >> $aux_path

mv $aux_path $file_path
