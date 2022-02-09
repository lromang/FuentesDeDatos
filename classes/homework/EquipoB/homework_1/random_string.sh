#!/bin/bash
r_string=''
string_length=9 #Longitud del string (10 letras pero empieza en 0, ponemos 9)
while [[ ${#r_string} -lt $string_length ]]#while la longitud del string que construimos es menor a string_length
do
    for letter in {a..z}
    do
        if [[ $(($RANDOM % 2)) == 0 ]]
        then
            r_string+="$letter" #Agrega una letra random entre a..z
            if [[ ${#r_string} -gt $string_length ]]#Si la longitud del string ya supera string_length, ahí se detiene el loop 
            then
                break
            fi
        fi
    done
   
    done
echo $r_string
