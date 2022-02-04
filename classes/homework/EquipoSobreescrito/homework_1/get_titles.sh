#!/bin/bash

# ----------------------------------------
# Este es el ejercicio que hicimos para
# extraer titulos de Stack Exchange.
# Noten:
# - Paso 1: curl trae el html de la página.
# - Paso 2: en un pipeline envio el html
#           a un buscador de expresiones
#           expresiones regulares.
# Dentro de la expresión regular,
# tengo que escapar las comillas (por que?)
# 	Porque si no lo hace, no irá por los matches
#	de los títulos y no imprimirá nada.
# por tanto: \".
# - 1. Juega con la las opciones de grep
#      ¿qué pasa si quitas la 'E' o la 'o'?
#		La Regex esta usando el set Extendido de
#		caracteres. Si quitamos la 'E', grep no
#		los va a usar y no ejecutara la expresion.
#
#		Si quitamos la o, no regresara el match 
#		exacto. Por lo tanto, nos regresara todos
#		los strings entre comillas, no solo los que
#		tengan title.
# - 2. Juega con la expresión regular.
#      ¿qué pasa si quitas el '+'? ¿por qué?
#		El + hace que incluya los caracteres
#		a la izquierda de la expresion. Si no
#		lo pones, no te regresara nada ya que
#		ignorara la parte de title, pero la
#		seguira buscando. 
# Tal vez sea buena idea almacenar el resultado
# de curl, en un archivo, para no saturar el sitio.
# ¿recuerdas cómo hacerlo? Hint: redirecciona curl,
# y despliega los contenidos del archivo con cat.
# ----------------------------------------

curl https://stackexchange.com/ > titles.html
cat titles.html | grep -oE 'title=\"[^\"]+\"'
