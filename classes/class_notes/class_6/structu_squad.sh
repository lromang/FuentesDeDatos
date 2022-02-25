#! /bin/bash


# ----------------------------------------
# This script extracts the contexts
# Questions and answers for the
# Reading comprehension task.
# TASK: This script has a flaw, it outputs
# as many nulls as answers per context.
# Fix this.
# HINT: Find a better structure for .ans
# ----------------------------------------


cat train-v2.0.json | jq '[. | .data | .[] | .t=(.title) | .paragraphs | .[] | .questions=([.qas | .[] | .question]) | .ans=([.qas | .[] | .. | .text?]) | {context: .context, questions:.questions, ans:.ans}]'
