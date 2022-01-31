#! /bin/bash

# ----------------------------------------
# Con este one-liner, extraje los nombres
# de los equipos y generé un directorio
# con el mismo nombre dentro de homework.
# ¿Qué es lo que hace mi expresión regular?
# ¿Por qué es necesario el primer ^?
# piensa en el string: aaa.bbb.ccc
# ----------------------------------------

for students in $(ls ../../course_generals/teams/ | grep -Eo '^[^\.]+' ); do mkdir $students; mkdir "$students/homework_1/"; done
