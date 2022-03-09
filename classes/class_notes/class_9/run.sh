#! /bin/bash

source env.sh

py_env=${1:-"$py_env"}
home_dir=${2:-"$(pwd)"}

$py_env main.py --home_dir $home_dir --author_id 65