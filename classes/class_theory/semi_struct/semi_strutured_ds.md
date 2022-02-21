# Estructura en los datos

Hasta ahora hemos trabajado con fuentes de datos libres de estructura, principalmente en la forma de texto libre. Cuando empezamos a trabajar con **AWK** notamos que en ocasiones es conveniente introducir abstracciones que nos permitan ordenar y accesar a los datos de manera estructurada; por ejemplo, en la forma de campos (fields) y registros (registers).


## CSV, TSV, PSV, ...

Este es sin duda el formato tabular más utilizado en  la actualidad. La idea es separar cada campo de un registro por un caracter especial. Este puede ser: ',', ' ', 't', '|', etc. La manera en la que separamos los registros es a través de salto de línea. Cómo hemos visto previamente **AWK** posee una interfáz que nos permite trabajar de manera cómoda con esta estructura. Adicionalmente a este lenguaje, hay una serie de librerías que facilitan la búsqueda y manipulación de este tipo de formatos sobre la línea de comandos. En este curso nos enfocaremos en dos: 

### CUT



### CSVKIT

Las principales razones por las cuales es útil:

* Nos permite explorar de manera ágil la estructura de un archivo.

     - Las primeras 10 líneas de un archivo sin traslapar columnas

    ```
    head data.csv | csvlook | less -S
    ```

    - El nombre de las columnas en un archivo.

  ```
  csvcut -n data.csv
  ```

    - Despliega columnas específicas (tanto por índice como de manera lexicográfica.).

```
csvcut -c 2,4,5 data.csv
```

* Podemos obtener obtener estadísticas sobre nuestros datos. 

```
csvcut -c c1, c2, c3 data.csv | csvstat
```

* Se puede focalizar el rango de las operaciones 

```
head data.csv | csvgrep -c col -r regex
```


Más importante de todo. Te ayuda a deshacerte de excel. 

```
in2csv ne_1033_data.xlsx > data.csv
```

Pero lo más importante es comprender, que a pesar de esto, la línea de comandos no es la herramienta ideal para llevar a cabo análisis de datos. Para esto necesitamos un software que contenga de forma nativa o heredada a través de liberías, las herramientas básicas de explotación de datos. 

> Sometimes (almost always), the command-line isn’t enough. It would be crazy to try to do all your analysis using command-line tools.


## JSON

Una de las principales ventajas de este tipo de estructuras es que soportan jerarquías anidadas. Esto simplifica la representación de relaciones complejas entre los datos. Por ejemplo, supongamos que queremos encontrar todas las publicaciones de todos los amigos de todas las personas que le dieron like a una publicación. Más aún, podríamos estar interesados en todos los retweets y comentarios. De la misma manera, el soporte para listas de objetos simplifica varias queries que de otra manera serían demasiado complicadas en un esquema relacional. 


### JQ

> **jq** is like sed for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that sed, awk, grep and friends let you play with text.
