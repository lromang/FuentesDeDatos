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
# HINT:  Classic Shell Scripting
#        Table 6-6. test expressions
#
# ----------------------------------------

r_string=''
for letter in {a..z}
do
    if [[ $(($RANDOM % 2)) == 0 ]]
    then
        r_string+="$letter"
    fi
done

echo $r_string
