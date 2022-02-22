#! /bin/bash

# ----------------------------------------
# This script downloads n random books (with replacement)
# from a given bookshelf. If n > number of
# books in library, you should deterministaclly
# download all books.
# Input:
# - library_id: id of library to download.
# - n: number of random books to download.
#   NOTE1: (n < number of books in library)
#   NOTE2: do not download unnecesary books!
# - env_dir: path to: [./PROJECT HOME]/text_comp/.
# - Hint1: take a look at $RANDOM
# - Hint2: (n % (b-a+1) + a) belongs to [a, b].
# ----------------------------------------

bookshelf_id=$1	#Bookshelf id
n=$2			#Number of books to download
env_dir=$3		#Path to text_comp
samp=1

if [ ! -d "$env_dir/texts/$bookshelf_id" ]
then
    mkdir "$env_dir/texts/$bookshelf_id"
fi

n_books="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | wc -l)"

if [ "$n" -ge "$n_books" ]		#If n >= n_books --> Imprimimos todos los libros.
then
    # Deterministic case
    n=$n_books
    samp=0
    echo 'Downloading all books'
    
    #TODO Descarga todos los libros.
    for i in `seq $n`
    do
    	url="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | tr '\t' ' ' | awk -v book=$i 'NR == book+1 {print $1}')"
    	title="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | awk -F '\t' '{print $2}' | awk -v book=$i 'NR == book+1 {print $0}')"
    	curl $url > $env_dir/texts/$bookshelf_id/"$title.txt"
    done
    

else
	for i in `seq $n`
	do
		nr=$RANDOM
		a=$(expr $n_books - 1 + 1)
		b=$(expr $nr % $a)
		rand_book=$(expr $b + 1)
		
		#Extraemos el url
		url="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | tr '\t' ' ' | awk -v book=$rand_book 'NR == book+1 {print $1}')"
		
		#Extraemos el título
		title="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | awk -F '\t' '{print $2}' | awk -v book=$rand_book 'NR == book+1 {print $0}')"
		
		#Guardamos el archivo
		curl $url > $env_dir/texts/$bookshelf_id/"$title.txt"
	done
fi
