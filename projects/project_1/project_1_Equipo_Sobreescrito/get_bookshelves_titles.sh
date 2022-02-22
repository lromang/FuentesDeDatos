#! /bin/bash

# ----------------------------------------
# Given a bookshelf id. The script checks
# if it is a new bookshelf, in this case,
# it downloads the list of titles.
# TODO: Document what each individual sed
# script is doing.
# ----------------------------------------


bookshelf_url=$1
env_dir=$2
bookshelf_id=`echo $bookshelf_url | grep -oE "([0-9]+)$"`
output_dir="$env_dir/$bookshelf_id"

if [ ! -d $output_dir ]
then
    echo "New bookshelf, downloading data..."
    mkdir $output_dir
    curl $bookshelf_url | sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp' | sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/' | tr -d '\r' |  tr '\n' '\t' | sed 's/https/\|https/g' | tr '|' '\n' > "$output_dir/titles.txt"
else
    echo "Loading bookshelf"
fi
