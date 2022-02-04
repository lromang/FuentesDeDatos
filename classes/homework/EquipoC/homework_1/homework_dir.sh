#! /bin/bash

# ----------------------------------------
# Con este one-liner, extraje los nombres
# de los equipos y generé un directorio
# con el mismo nombre dentro de homework.
# ¿Qué es lo que hace mi expresión regular?
# 	Hace que se revise el primer carácter de una expresión buscando que no sea un punto: '.'
# 	Si una o más ocurrencias de lo señalado suceden regresa las partes de la expresión solicitadas.
# ¿Por qué es necesario el primer ^?
# 	Para saber que pedimos que solo se examine el primer caractér con la condición: [^\.]
# piensa en el string: aaa.bbb.ccc
#	Este string debería regresar aaa, gracias al + no regresa una sola a.
# ----------------------------------------

for students in $(ls ../../course_generals/teams/ | grep -Eo '^[^\.]+' ); do mkdir $students; mkdir "$students/homework_1/"; done
