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
echo -e "Choose a location for project setup: (default: $current_dir)\n"
read new_dir

###################################################
# YOUR CODE GOES HERE
while [ ! -z $new_dir ] && [ ! -d  $new_dir ]
do
    echo -e "The provided path doesn't exist. Please provide a valid path:\n"
    read new_dir
done
###################################################

if [ ! -z $new_dir ]
then
    current_dir=$new_dir
fi

# ----------------------------------------
# Create directory structure
# ----------------------------------------

echo "Creating directory project: $current_dir"

mkdir "$current_dir/text_comp"
mkdir "$current_dir/text_comp/titles"
mkdir "$current_dir/text_comp/texts"
mkdir "$current_dir/text_comp/results"

# ----------------------------------------
# Download titles
# ----------------------------------------

./get_libraries.sh "$current_dir/text_comp/titles"
