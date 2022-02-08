## Awk

>The simplicity and power of awk often make it just the right tool for the job, and we seldom encounter a text processing task in which we need a feature that is not already in the language, or cannot be readily implemented.

A diferencia de **grep** y  **sed**, **awk** Es un lenguaje de propósito general que ofrece todas las abstracciones que encontramos en lenguajes convencionales, tal como la capacidad para asignar variables, tomar decisiones, e iterar en bucles. Una ventaja adicional que ofrece **awk** es que nos permite trabajar con estructuras 'tabulares', identificando cada línea de un archivo como un 'registro' que está compuesto por múltiples 'campos'.  Si bien la sintaxis podría parecer un poco arcana la primera vez que nos encontramos con ella, la simplicidad en los patrones de ejecución y la flexibilidad para trabajar de manera eficiente con diversas estructuras de texto lo vuelven una herramienta muy atractiva.

### Estructura

Un script en  **awk** tiene la siguiente forma:

```
awk [-F fs] [-v var="val"] 'BEGIN {action0}; pattern1 {action1}; pattern2 {action2}; ... END {actionN} ' [file(s)]
```

* **-F** Esta opción nos permite especificar el carácter que es utilizado como 'separador de campos'. Este valor puede ser modificado usando la variable ```FS```.
    * Cada campo dentro de un program de awk puede ser referenciado con la notación "$field_num"; por ejemplo, $1 sería el primer campo, $2 el segundo, etc. Siendo "$0" la referencia al registro completo. Adicionalmente tenemos referencias al número de registros ```NR``` y número de campos ```NF```.

* **-v** con esta opción asignamos variables que podrán ser utilizadas dentro del script. Es importante notar que si estamos pasando variables de otro script, es buena práctica rodearla con comillas dobles: -v var1="$var_from_shell".

* **BEGIN** Esta sección se ejecuta después de asignación de variables, pero antes de que se lleve a cabo cualquier asignación del stream de archivos. Por ejemplo, las variable ```$0``` será vacía.

* **pattern_i {action_i}** Esta secuencia de acciones se llevarán a cabo en aquellas líneas que contengan el patrón **pattern_i**. Esto sería equivalente a ejecutar acciones que cumplan la cláusula ```if($0 ~ pattern_i)```.

* **END** Esta acción se llevará a cabo al final de la ejecución del script. Pregunta ¿Que regresará? ```echo -e 'test1\n\test2\ntest3' | awk 'END {print NR}'```

### Tipo de variables

Las cadenas de caracteres en **awk** se definen utilizando comillas al principio y fin de la expresión. Las comparaciones con strings se llevan a cabo de manera convencional: ==, !=, <=, >=, etc. Es posible extraer la longitud de un string usando la función ```length```.

* **Variables numéricas**

Todas las variables numéricas en **awk** siguen la lógica de valores de punto flotante y siguen leyes de aritmética similares a las de C. Algunas operaciones relevantes:

* **++, --** incremento y decremento
* **^** exponenciación
* **!** negación
* **+, -,*, /, %** suma, resta, división, módulo.
* **<, <=, >=, >, !=, ==** comparaciones.
* **&&, ||** and y or lógicos.
* **?, :** operadores ternarios.

* **Arreglos**

Uno de los features más interesantes de **awk** es que cuenta con arreglos asociativos. No necesitan ser declarados ni instanciados en memoria, estos crecen de manera automática conforme se incluyen elementos.

### Condiciones y bucles

Las condiciones y bucles en **awk** siguen las convenciones de C. Es necesario recordar que estas estructuras deben contenerse dentro de las llaves referentes a la acción. De la misma manera se define su scope usando llaves. En el caso del ```if```, al igual que en C, tenemos un operador ternario ```? :```.


