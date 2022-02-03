#! /bin/bash

# ----------------------------------------
# Con este one-liner, extraje los nombres
# de los equipos y generé un directorio
# con el mismo nombre dentro de homework.
# ¿Qué es lo que hace mi expresión regular?
#	Busca las ocurrencias de un punto en el string
#	dado y regresa todo lo que esta a la izquierda
#	de la primera.	
# ¿Por qué es necesario el primer ^?
# piensa en el string: aaa.bbb.ccc
#	Sin el, regresara todas las ocurrencias de 
#	caracteres antes de un punto en vez de solo
#	la primera (osea, en vez de regresar 'aaa'
#	regresara 'aaa' 'bbb' y 'ccc'.
# ----------------------------------------

for students in $(ls ../../course_generals/teams/ | grep -Eo '^[^\.]+' ); do mkdir $students; mkdir "$students/homework_1/"; done
