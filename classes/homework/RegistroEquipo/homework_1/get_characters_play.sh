#! /bin/bash

# ----------------------------------------
# Get the top N (default 10) characters
# in Macbeth.
# Why it is necessary to sort twice?
#   Supongo que el primer sort le facilita el trabajo 
    de búsqueda al uniq -c y el segundo sort hace que
    los datos aparezcan legibles y listo para 
    interpretarse al presentarlos en orden numérica
    invertida
# What does 'uniq -c' do?
#   Cuenta las apariciones de todos los
    valores únicos
# Relace the regex with: '\w+'. Explain.
    Cuenta todas las palabras y sus apariciones en el texto
    porque los personajes terminan en punto por lo que me
    imagino.
# ----------------------------------------

# top characters
top=${1:-10}

cat mac.txt | tr '\r' '\n' | grep -Eo '^[A-Z]+\.$' | sort | uniq -c | sort -nr | head -n $top
