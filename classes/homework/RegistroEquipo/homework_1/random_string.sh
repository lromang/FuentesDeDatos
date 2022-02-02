#! /bin/bash

# ----------------------------------------
# Con este script construimos strings
# aleatorios. Conceptualmente, lo más importante
# es recordar que se puede iterar sobre el resultado
# de cualquier comando.{a..z}, $(ls), $(echo ...)
# El loop while es una mezcla de if y for
# Iteras hasta cumplir una condición.
#
# While [[condition]]
# do
# ....exec....
# done
#
# 1.- Modifica este script para garantizar
#     strings 'aleatorios' de longitud
#     10.
#
# HINT1:  Classic Shell Scripting
#        Table 6-6. test expressions
# HINT2: Puedes salir de un loop con break.
# ----------------------------------------

r_string=''

# ----------------------------------------
# Your code goes here:
# Begin while
# test condition ${#r_string} -lt X.
# ----------------------------------------
while [[ ${#r_string} -lt  10 ]]
do
for letter in {a..z}
do
if [[ $(($RANDOM % 2)) == 0 ]]
then
r_string+="$letter"
if [[ ${#r_string} -eq 10 ]]
then
break
fi
fi
done
done
# ----------------------------------------
    # End while
    # Your code goes here
# ----------------------------------------

echo $r_string

