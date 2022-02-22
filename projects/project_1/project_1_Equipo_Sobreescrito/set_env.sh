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
       echo -e "Choose a location for project setup: (default: $current_dir)\n"
       read new_dir
       while [ 1 ]
       do
           # ----------------------------------------
           # Ask the user to provide a valid path for
           # the environment.
           # ----------------------------------------

		while [ ! -d "$new_dir"] && [! -L "$new_dir"]
		do
			echo -e "The path doesn't exist. Please enter a valid or empty path.\n"
			read new_dir
		done

           # ----------------------------------------
           # Check if the entered path is empty
           # ----------------------------------------

		if [ ! "$(ls -A $new_dir)" ];
		then
			echo -e "$new_dir is not empty.\nDefaulting to $current_dir\n"
            new_dir=$current_dir
            echo -e "It shoud change now wtf"
		fi
            echo -e "The current directory is $current_dir"

           # ----------------------------------------
           # Check if the directory already exists
           # ----------------------------------------
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
# Compare text
# ----------------------------------------
./get_bookshelves.sh "$new_dir/text_comp"
