#! /bin/bash


n_arguments=$#
first_arg=$1

echo "$# commands were passed to this script"
echo "$first_arg this is the first arg"
echo "${!#} this is the last arg"
echo "$@ all the arguments"
echo ""$@" all the arguments as individual strings"


