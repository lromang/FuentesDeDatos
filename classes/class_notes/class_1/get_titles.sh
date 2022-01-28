#!/bin/bash

# ----------------------------------------
# Este es el ejercicio que hicimos para
# extraer titulos de Stack Exchange.
# Noten:
# - Paso 1: curl trae el html de la pagina.
# - Paso 2: en un pipeline envio el html
#           a un buscador de expresiones
#           expresiones regulares.
# Dentro de la expresión regular,
# tengo que escapar las comillas (por que?)
# por esto: \".
# - 1. Juega con la las opciones de grep
#      ¿qué pasa si quitas la 'E' o la 'o'?
# - 2. Juega con la expresión regular.
#      ¿qué pasa si quitas el '+', por qué?
# Tal vez sea buena idea almacenar el resultado
# de curl, en un archivo, para no saturar el sitio.
# ¿recuerdas cómo hacerlo? Hint: redirecciona curl,
# y despliega los contenidos del archivo con cat.
# ----------------------------------------

# curl https://stackexchange.com/
curl https://stackexchange.com/ | grep -oE 'title=\"[^\"]+\"'
