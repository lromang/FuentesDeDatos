#! /bin/bash

# ----------------------------------------
# In this script, we iterate over all the
# books in a bookshelf and store them.
# - Sanity check for validity of directory
# - existence of url
# - Sanity checks for outputfile format
# -
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
