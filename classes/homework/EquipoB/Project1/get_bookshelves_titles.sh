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
#bookshelf_id=`echo $bookshelf_url | grep -oE "([0-9]+)$"`
bookshelf_id=$3
output_dir="$env_dir/$bookshelf_id"

echo "output dir is $output_dir"
echo "bookshelf_id is $bookshelf_id"
echo "bookshelf_url is $bookshelf_url"

if [ ! -d $output_dir ]
then
    echo "New bookshelf, downloading data..."
    mkdir $output_dir
    curl -s $bookshelf_url | sed -n -e 's:.*href="/ebooks/\([0-9]*\)".*:\1:p' >$output_dir/titles.txt
    #El sed va al url y busca la linea que empieza que contiene href, extrae /ebooks/un numero que está ahí y lo que sigue y lo guarda en el archivo de tittles.txt 
    cat $output_dir/titles.txt
else
    echo "Loading bookshelf"
fi