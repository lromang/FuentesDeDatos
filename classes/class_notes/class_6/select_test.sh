#! /bin/bash

# ----------------------------------------
# This script demonstrates the logic
# behind select using a regex filter.
# ¿Can you figure out the logic?
# - NOTE: You can use pipelines within
#         function calls (as in select in thi example).
#         this might be extremely powerful.
# TASK 1: Go through JQ documentation
# TASK 2: Think of an application of this principle.
# TASK 3: Take a look at the commented script. It is
#         yet a more challenging application.
#         Explain what each chunk of code is doing.
# cat basic_test.json | jq '[. | to_entries | .[] | select(.value | test("^v.*", "ix"))]' | jq 'from_entries'
# ----------------------------------------

cat b2.json | jq '.[] | select(.name | test("^F.*"; "ix"))'
