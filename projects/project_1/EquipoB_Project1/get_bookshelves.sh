#! /bin/bash

# ----------------------------------------
# This script prompts the user with a
# list of bookshelves to download. And
# asks her to select two ids.
# Given a valid bookshelf, the script
# downloads the list of titles
# in that bookshelf. As well as a selection
# of books.
# ----------------------------------------

env_dir=$1
texts=0
bookshelves_dir="$env_dir/bookshelves"
bookshelves="$bookshelves_dir/bookshelves.txt"

# Print bookshelves
cat "$bookshelves"
echo "Please select a bookshelf id: "
# The user needs to provide at least 2 bookshelfs.
while [ $texts -lt 2 ] || [ ! -z $bookshelf ]
do
    read bookshelf
    # If there are more than two bookshelves selected
    # and bookshelf is empty, we exit the program.
    if [ $texts -gt 2 ] && [ -z $bookshelf ]
    then
       break
    fi
    # ----------------------------------------
    # Query library url
    # TODO: get the bookshelf url belonging
    # to the selected id.
    # ----------------------------------------
    #bookshelf_url=$(grep "$bookshelf" bookshelves.txt|awk -F ',' '{print $3}')
    bookshelf_url=https://www.gutenberg.org/ebooks/bookshelf/$bookshelf
    echo "$bookshelf_url"
    if [ ! -z $bookshelf_url ]
    then
        if [ $texts -eq 0 ]
        then
            # Download bookshelf and books content
            first_bookshelf=$bookshelf
            ./get_bookshelves_titles.sh $bookshelf_url $bookshelves_dir $bookshelf
            sleep 1
            tot_books="$(cat $env_dir/bookshelves/$bookshelf/titles.txt | wc -l)"
            echo "Select number of books to download (total books in bookshelf: $tot_books)"
            read n_books
            echo "Downloading books, this might take some time"
            ./get_books.sh $bookshelf $n_books $env_dir
            echo "please select another valid bookshelf"
        else
            if [ "$bookshelf" = "$first_bookshelf" ] && [ "$texts" -lt 2 ]
            then
                echo -e "The second bookshelf must be different from $first_bookshelf. \n Please select another valid bookshelf."
                texts=$(($texts-1))
            else
                ./get_bookshelves_titles.sh $bookshelf_url $bookshelves_dir $bookshelf
                sleep 1
                tot_books="$(cat $env_dir/bookshelves/$bookshelf/titles.txt | wc -l)"
                echo "Select number of books to download (total books in bookshelf: $tot_books)"
                read n_books
                echo "Downloading books, this might take some time"
                ./get_books.sh $bookshelf $n_books $env_dir
                echo "please select another valid bookshelf"
            fi
        fi
        texts+=1
    else
        cat "$bookshelves"
        echo "Invalid bookshelf, please select a bookshelf within the list."
    fi
done