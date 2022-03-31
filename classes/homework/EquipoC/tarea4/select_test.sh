#! /bin/bash

# ----------------------------------------
# This script demonstrates the logic
# behind select using a regex filter.
# ¿Can you figure out the logic?
# - NOTE: You can use pipelines within
#         function calls (as in select in thi example).
#         this might be extremely powerful.
# TASK 1: Go through JQ documentation
# R1: Done so Alonso
# TASK 2: Think of an application of this principle.
# R2: The first application for the pipeline within function
#	  that we can think of is that unlike sed or grep, you
#	  can call jq only once and within arrange your query
#	  as you like.
# TASK 3: Take a look at the commented script. It is
#         yet a more challenging application.
#         Explain what each chunk of code is doing.
# R3: The first chunk is the cat, you need this to know the
#	  file in which you will be working. The second is already
#	  a jq that does a lot of things: first it organizes the
#   contnents into a [], then it separates each pair of key and 
#   value from othes pairs of keys and values, but since this
#   circles everything onto a [[]], we need .[] to remove one [],
#   at the endo of this jq we have select(.value | test("^v.*", "ix"))]'
#   where the select searches for every pair of key-value where the regex 
#   of the value starts whit the char 'v' or contains the string "ix".
#   Finaly we reunite each key-value pair that the previous jq throwed.
# cat basic_test.json | jq '[. | to_entries | .[] | select(.value | test("^v.*", "ix"))]' | jq 'from_entries'
# ----------------------------------------

cat b2.json | jq '.[] | select(.name | test("^F.*"; "ix"))'
