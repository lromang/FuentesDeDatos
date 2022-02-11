#! /bin/bash

# ----------------------------------------
# This code gets the top n most frequent
# words in crime.txt.
# PARAMS:
# - top = top words to print, defaults to 10
# This code reads and validates a letter from
# the user.
# Your task is to read, understand and
# execute this code. Make sure you try
# to break this code (enter invalid 'letters').
# ----------------------------------------

# Top letters
top=${1:-10}

# 	Este deja como default el valor de esta variable (usada como
# 	primer parámetro) de 10 para sacar las top 10 palabras más usadas
# 	con esa letra. Si ejecuto el script con otro número, será el "top
# 	$número de palabras que empiezan con esa letra y sus ocurrencias. 

# Ask user for a letter
echo 'Please enter a letter to find: '
# Check it is in fact a letter HINT: use an if =~
read letter
while [[ ! $letter =~ ^[a-zA-Z]{1}$ ]]
#	Verifica que  la letra ingresada cumpla con el regex puesto:
#	Que empieze con cualquier letra ASCII de la a-z (mayúscula o
#	minúscula) y que fuera un solo dígito antes de su final.
do
    echo 'please enter a valid letter'
    read letter
done
# Get top words.
cat crime.txt | sed -E 's/[^A-Za-z ]//g' | grep -v '^$' | grep -ioE '[a-z]+' | tr '[:upper:]' '[:lower:]' | grep -E "^$letter.+" | sort | uniq -c | sort -nr | head -n $top
