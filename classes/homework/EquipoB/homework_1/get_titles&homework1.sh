#!/bin/bash
#Get titles
curl https://stackexchange.com/ | grep -oE 'title=\"[^\"]+\"'>titulos
#grep sin E
curl https://stackexchange.com/ | grep -o 'title=\"[^\"]+\"'>titulosSinE
#Crea un archivo vacío 
curl https://stackexchange.com/ | grep -E 'title=\"[^\"]+\"'>titulosSinO
#Regresa todo aunque no sea un match exacto 
curl https://stackexchange.com/ | grep -oE 'title=\"[^\"]\"'>titulosSin+
#Crea un archivo vacío, ya que el + trae todo lo que está en medio de comillas y sin él no trae nada 

#Homework1
for students in $(ls ../../course_generals/teams/ | grep -Eo '^[^\.]+' ); do mkdir $students; mkdir "$students/homework_1/"; done
#¿Qué hace la expresión regular?
#Agarra todos los strings que no comiencen con un punto para extraer los nombres de los equipos y hacer un directorio en homework
#Para qué se necesita el el primer ^?
#Para que el grep busque todo lo que no contenga punto al inicio del string
