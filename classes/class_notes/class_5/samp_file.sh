#!/bin/bash

# ----------------------------------------
# This script samples lines from a file
# default: 10% of lines.
# ----------------------------------------

samp_size=${2:-.1}

cat $1 | awk  -v samp_size=$samp_size  'BEGIN {srand()} rand() < samp_size {print $0}'
