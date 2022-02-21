#!/bin/bash

# ----------------------------------------
# This code removes duplicates from
# a file provided by the user.
# ----------------------------------------

cat $1 | sort | awk '$0 == Last {OFS="\t"; print $0} {Last = $0} '
