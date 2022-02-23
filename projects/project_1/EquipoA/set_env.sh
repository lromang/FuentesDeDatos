#! /bin/bash

# ----------------------------------------
# This script provides all the setup steps
# for generating a working environment,
# downloading bookshelves (at least two), as
# well as the main texts of books belonging
# to each bookshelf.
# ----------------------------------------
# Get current dir
current_dir=`pwd`
# Ask if user wants to create a new environment
echo "Do you want to setup an environment? (y/n)"
read set_env
# Until valid y/n answer
while [ "$set_env" != "y" ] && [ "$set_env" != "n" ]
do
    echo 'ENV'
    echo $set_env
    echo "Please answer: (y/n)"
    read set_env
done
# If new environment
if [ "$set_env" = "y" ]
   then
       echo -e "Choose a location for project setup: (default: $current_dir)"
       echo -e "If you don't enter anything it will be default"
       read new_dir
       while [ 1 ]
       do
           # ----------------------------------------
           # Ask the user to provide a valid path for
           # the environment.
           # ----------------------------------------

           #Si está vacío asignamos default.
           if [ -z $new_dir ]
           then
           	new_dir=$current_dir
           #Si no está vacío nos aseguramos que la ubicación para crear text_comp exista
           else
           	while [[ ! -d "$new_dir" ]]
           	do
           		echo -e "The given path is wrong, please enter a valid one"
           		read new_dir
           	done
           fi
           
           # ----------------------------------------
           # Check if the entered path is empty
           # ----------------------------------------

           ###################################################
           # YOUR CODE GOES HERE
           # TODO: check if the entered directory is empty,
           # default it to current_dir.
           ###################################################

           # ----------------------------------------
           # Check if the directory already exists
           # ----------------------------------------
           
           #This checks if text_comp directory already exists.
           if [ -d "$new_dir/text_comp" ] 
           then
               echo "The directory already exists, do you wish to replace it (y/n)"
               read remove
               if [ "$remove" = 'y' ]
               then
                   rm -r "$new_dir/text_comp"
                   break
               else
                   new_dir='NAN'
               fi
           else
               break
           fi
       done

       # ----------------------------------------
       # Create directory structure
       # ----------------------------------------
       echo "Creating directory project: $new_dir/text_comp"
       mkdir "$new_dir/text_comp"
       mkdir "$new_dir/text_comp/bookshelves"
       mkdir "$new_dir/text_comp/texts"
       mkdir "$new_dir/text_comp/results"

       # ----------------------------------------
       # Download bookshelves
       # ----------------------------------------
       ./get_bookshelves_list.sh "$new_dir/text_comp" &
       sleep 1
else
    echo "Please provide dir location"
    read new_dir
    if [ -z $new_dir ]
    then
        new_dir=$current_dir
    fi
fi

# ----------------------------------------
# Compare text. Hay que quitar el útlimo asterisco
# ----------------------------------------
./get_bookshelves.sh "$new_dir/text_comp"
