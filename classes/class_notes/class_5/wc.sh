#!/bin/bash

# ----------------------------------------
# This code replicates the functionality
# of linux wc util.
# ----------------------------------------

cat $1 | tr '\r' ' ' | awk '{OFS="\t"; C += length($0) + 1; W += NF} END {print "L", "W", "C"; print NR, W, C}'
