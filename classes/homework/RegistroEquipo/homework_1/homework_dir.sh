#! /bin/bash

# ----------------------------------------
# Con este one-liner, extraje los nombres
# de los equipos y generé un directorio
# con el mismo nombre dentro de homework.
# ¿Qué es lo que hace mi expresión regular? 
#     - \. escapa el punto
#     - [^\.]+ selecciona todas las cadenas
#             que no contienen un punto en
#             su composición
#     - ^[^\.]+ selecciona solo el inicio de
#             de la cadena.
#     - E es para expresiones extendidas
#     - o es para ¿?
#
# ¿Por qué es necesario el primer ^?
# piensa en el string: aaa.bbb.ccc
#   - Porque solo selecciona la primera cadena aaa
#     sin ^ seleccionaríamos aaa,bbb,ccc
#     En este caso fue útil porque la mayoría
#     subimos nuestro equipo en formato txt
#     entonces con la regex solo tomamos aquella info
#     antes de .txt, que es lo que nos interesa
# ----------------------------------------

for students in $(ls ../../course_generals/teams/ | grep -Eo '^[^\.]+' ); do mkdir $students; mkdir "$students/homework_1/"; done
