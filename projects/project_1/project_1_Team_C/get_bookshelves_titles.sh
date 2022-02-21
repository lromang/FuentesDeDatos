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

# El primer sed (sed -nE '/.*booklink.*/,/.*extra.*/s/.*href=([^ ]*).*/\1/gp;/.*booklink.*/,/.*extra.*/s/<.*>(.*)<.*>/\1/gp')
# Extrae todos los detalles de los libros que se del directorio seleccionado, y regresa su url, su título, su género y las descargas que ha tenido en los últimos 30 días.

# El segundo sed (sed  -Ee 's/.*ebooks\/([0-9]+)\"/https:\/\/www.gutenberg.org\/cache\/epub\/\1\/pg\1.txt/')
# Otorga la url de la que se puede descargar la versión epub de cada libro en el directorio.

# El último sed (sed 's/https/\|https/g')
# Solo sustituye los https por |https en las urls de los libros.
