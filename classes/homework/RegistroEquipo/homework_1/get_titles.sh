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
#       Las escapamos debido a que son caracteres
#       reservados (en este caso creo que para en-
#       capsular las regex) y para así poder ajustar
#       nuestra regex al formato en que se diseñó
#       la página web
#
# - 1. Juega con la las opciones de grep
#      ¿qué pasa si quitas la 'E' o la 'o'?
#     - o: al quitarla nos trae todo el texto y resaltado
#       el match de nuestra regex. Con ella solo nos trae las
#       coincidencias
#     - E: no nos trae nada
#
# - 2. Juega con la expresión regular.
#      ¿qué pasa si quitas el '+'? ¿por qué?
#     - Si quitamos el + no considera los caracteres
#       que hacen match por rango y están a la derecha
#       y por ende no trae nada
# Tal vez sea buena idea almacenar el resultado
# de curl, en un archivo, para no saturar el sitio.
# ¿recuerdas cómo hacerlo? Hint: redirecciona curl,
# y despliega los contenidos del archivo con cat.
#     - Agregamos >> HotQuestions.txt | cat HotQuestions.txt
# ----------------------------------------

# curl https://stackexchange.com/
curl https://stackexchange.com/ | grep -oE 'title=\"[^\"]+\"' >> HotQuestions.txt | cat HotQuestions.txt
