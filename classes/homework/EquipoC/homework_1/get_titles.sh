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
# por tanto: \".
# - 1. Juega con la las opciones de grep
#      ¿qué pasa si quitas la 'E' o la 'o'?
# + R1. Si quitamos la 'E', se deja de entender la expresión 
# 	siguiente como una expresión regular. Si quitamos la
# 	'o' imprimiremos la línea completa que contiene el 
# 	patrón que buscamos
# - 2. Juega con la expresión regular.
#      ¿qué pasa si quitas el '+'? ¿por qué?
# + R2. Solo se regresaría el primer valor que encaje con la
#	expresión regular, en lugar de todos los valores deseados
# Tal vez sea buena idea almacenar el resultado
# de curl, en un archivo, para no saturar el sitio.
# ¿recuerdas cómo hacerlo? Hint: redirecciona curl,
# y despliega los contenidos del archivo con cat.
# + R3.
curl https://stackexchange.com/ -o stackex.txt
cat stackex.txt | grep -oE 'title=\"[^\"]+\"' 
# ----------------------------------------

# curl https://stackexchange.com/
curl https://stackexchange.com/ | grep -oE 'title=\"[^\"]+\"'
