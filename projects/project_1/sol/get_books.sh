# ----------------------------------------
# This script downloads n random books from
# a given library.
# Input:
# - library_id: id of library to download.
# - n: number of random books to download.
#   NOTE1: (n < number of books in library)
#   NOTE2: do not download unnecesary books!
# - env_dir: path to: [./PROJECT HOME]/text_comp/.
# - Hint1: take a look at $RANDOM
# - Hint2: (n % (b-a+1) + a) belongs to [a, b].
# ----------------------------------------

bookshelf_id=$1
n=$2
env_dir=$3
samp=1

##################################################
# YOUR CODE GOES HERE
##################################################
if [ ! -d "$env_dir/texts/$bookshelf_id" ]
then
    mkdir "$env_dir/texts/$bookshelf_id"
fi

n_books="$(cat $env_dir/bookshelves/$bookshelf_id/titles.txt | wc -l)"

if [ "$n" -gt "$n_books" ]
then
    # Deterministic case
    n=$n_books
    samp=0
    echo 'Downloading all books'
fi

for i in `seq $n`
do
    book=$(($samp*(($RANDOM % $n_books) + 1) + $i*(1-$samp)))
    book_data=`cat $env_dir/bookshelves/$bookshelf_id/titles.txt | grep -vE '^$' | awk -F '\t' -v book="$book" 'NR == book {print $0}'`
    book_url="$(echo $book_data | grep -Eo 'https[^ ]+')"
    book_id="$(echo $book_data | grep -Eo '/[0-9]+/' | sed -E 's/\/([0-9]+)\//\1/g')"
    book_path="$env_dir/texts/$bookshelf_id/$book_id"
    if [ ! -d "$book_path" ]
    then
        mkdir $book_path
        curl $book_url > "$book_path/main_text.txt"
    fi
done
