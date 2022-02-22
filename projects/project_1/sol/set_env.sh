#! /bin/bash

# ----------------------------------------
# Get project location
# - Ask the user for a valid path to create
#   the project (stop asking whenever the path is valid or empty).
#   If the path entered is
#   empty, default to current directory.
# - HINT: -d path
# ----------------------------------------
current_dir=`pwd`
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
           ###################################################
           # YOUR CODE GOES HERE
           ###################################################
           while [ ! -z $new_dir ]  && [ ! -d  $new_dir ]
           do
               echo -e "The provided path doesn't exist. Please provide a valid path:\n"
               read new_dir
           done
           ###################################################

           # ----------------------------------------
           # Check if the entered directory is empty (defaults home directory)
           # ----------------------------------------
           if [ -z $new_dir ]
           then
               new_dir=$current_dir
           fi

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
       # Download titles
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
