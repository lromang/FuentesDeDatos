## Expresiones Regulares

> Since regular expressions are a fundamental part of the Unix tool-using and tool-building paradigms, any investment you make in learning how to use them, and use them well, will be amply rewarded, multifold, time after time.


Las expresiones regulares son clave para generar rutinas de procesamiento de texto poderosas, flexibles y eficientes. Estas representan una familia generalizada de patrones de lenguaje y, junto con el soporte de la herramienta sobre la cual las utilizas, pueden agregar, eliminar o aislar todo tipo de dato textual.

En su funcionalidad más esencial, las expresiones funcionan como un buscador de secuencias de carácteres. Por ejemplo, la expresión regular 'Hola Mundo' buscará todas las instancias de texto en donde la cadena de caracteres 'H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o' se encuentra (en ese preciso orden). El comando por excelencia que usaremos para detectar expresiones regulares es grep. Esta herramienta regresará por default todas las líneas que hagan match con la expresión regular.

```
echo 'Hello World!' | grep 'Hello'
```

Algunas opciones interesantes de grep son:

* **-E** expresiones regulares extendidas.
* **-o** regresa solo el match exacto.
* **-i** ignorar la capitalización.
* **-v** imprime todas las líneas que **no** contengan la expresión regular.

Para extender la capacidad y generalidad de las expresiones que podemos buscar es necesario recurrir a los metacaracteres.

### Metacaracteres

* **Familias de caracteres**

* Con ```[]``` podemos hacer referencia a rangos, por ejemplo [a-z], [A-Z], [0-9]. Incluye las secuencias de 'a' a 'z' (en minúsculas y mayúsculas respectivamente) así como la sucesión numérica de 0 a 9.
* El carácter ```.``` nos permite referenciar cualquier carácter imprimible.
* En versiones extendidas de regex podemos referenciar familias enteras de caracteres con: ```[:alnum:]```, ```[:alpha:]```, ```[:space:]```, ```[:digit:]```, etc.
* En versiones extendidas de regex podemos referenciar familias enteras de caracteres con:
     - ```\d``` match con cualquier dígito. ```\D```` match con cualquier no dígito.
     -  ```\w``` hace match con cualquier palabra. ```\W``` hace match con cualquier carácter que no sea una palabra: Los caracteres de palabras incluyen alfanuméricos (-, - and -) y guión bajo (_).

* **Cuantificadores**

* `*` Nos permite seleccionar **ninguna o varias** instancias del carácter (o familia de caracteres) que están a la izquierda.
* `+` Nos permite seleccionar **una o varias** instancias del carácter (o familia de caracteres) que están a la izquierda.
* `?` Nos permite seleccionar **una o ninguna** instancias del carácter (o familia de caracteres) que están a la izquierda.
* `{n,m}` Nos permite seleccionar un número de instancias que se encuentre entre n y m.

* **Posición**

* `^` buscará instancias de texto que contengan la expresión regular, al comienzo de una oración. Como nota adicional, si el circunflejo se encuentra al principio de un rango: `[^]` esto tendrá el efecto de negar el match de cualquier expresión dentro del rango.
* `$` buscará instancias de texto que contengan la expresión regular, al final de una oración.
* `\<`, `\>` equivalentes as `^` y `$` solo que el match será al principio o final de una palabra.

* **Alternancia y agrupación**

* ```|``` alterna entre un grupo de posibles expresiones. NOTA: este carácter tiene la menor precedencia dentro de las expresiones regulares.


Además de los patrones que hemos investigado hasta ahora, hay una manera de aumentar significativamente el poder de las expresiones regulares. Esto es, agregando memoria. En forma de patrones que pueden ser referenciados. Esto se logra encerrando la expresión deseada entre ```\(, \)```. Estas expresiones pueden ser referidas utilizando la sintaxis ```\digit``` en donde digit es el orden de agrupación de la expresión (con un máximo de nueve referencias)

## Sed

Hasta ahora podemos buscar patrones dentro de un archivo de texto, sin embargo, estamos algo limitados en cuanto a las operaciones que podemos hacer sobre los mismos. Con tal de solventar estas limitantes usaremos la herramienta ```sed```.

Las instrucciones en ```sed``` tienen la forma general: ```/address1/,/address2/instruction/pattern/flags```.

- **address1** y **address2** son expresiones regulares que determinan a partir de donde y hasta donde se deben llevar a cabo las operaciones.
- **instruction** puede ser eliminar: d, sustituir: s, agregar: a, imprimir: p, etc.
- **pattern** el patrón sobre el que se llevarán a cabo las operaciones de la instrucción.
- **banderas** pueden especificar: el scope (global) g o si es necesario imprimir las líneas modificadas: p.


