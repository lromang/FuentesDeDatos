#! /bin/bash

# ----------------------------------------
# This script generates a folder and
# a file with statistics for coulumns:
# height, weight, collage
# for every state
# in the nba dataset.
# ----------------------------------------

state_dir="./state_stats"

echo $path_to_nba


if [[ ! -d $state_dir ]]
then
    mkdir "state_stats"
fi

for state in $(cat nba.csv | csvcut -c 7 | tail -n +2 | sort | uniq | grep -E '^[A-Za-z]+$'); do echo -e "\n--------------\n$state\n----------------\n"; cat nba.csv | csvgrep -c birth_state -m $state | csvcut -c height,weight,collage | csvstat > "$state_dir/$state"; done
