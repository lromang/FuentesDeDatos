## Introducción a la línea de comandos

Manejar la línea de comandos de manera adecuada es una herramienta fundamental que nos permite:

    * Interactuar con el sistema de archivos de manera eficiente,
    * controlar y vincular procesos

Todo esto a través del lenguaje interpretado [**BASH**](https://en.wikipedia.org/wiki/Bash_(Unix_shell)). Si bien la complejidad relativa que presenta aprender toda una nueva serie de *comandos* en un ambiente poco amigable, contra una interfáz gráfica, pudiera resultar abrumadora. Con la práctica y uso constante, el trabajo con una terminal se volverá una segunda naturaleza.

#### Ubicación dentro del sistema de archivos

El primer paso funcional cuando nos encontramos dentro de un sistema linux por primera vez es identificar en donde estamos ubicados. Saber movernos de manera eficiente así como crear ambientes de trabajo. 

El comando ```pwd``` nos permite identificar nuestra posición actual.

<span style="color:blue">Nota: Lo más probable es que tu ruta tenga la forma ```/dir_1/dir_2/dir_.../.```. Las rutas que comienzan con ```/``` son rutas absolutas, pues parten del directorio raíz ```/```. Las rutas de la forma ```./``` son rutas relativas que parten del directorio en el cual estás ubicad@. </span>


```ls``` imprime el contenido de dicha ubicación. 

En Bash, los comandos pueden recibir parámetros, en este caso podemos utilizar la opción ```-a``` para listar todos los archivos. Incluso archivos ocultos.

```{BASH}
ls -a
```

Pregunta 1.1: ¿Qué significan ```.``` y ```..```.?

Para movernos dentro del sistema usamos el comando  ```cd``` seguido de la ruta (absoluta o relativa) que lleva a la ubicación deseada.

Por ejemplo:

```{BASH}
cd /user/bin
```

## Variables

Es fundamental para todo programa no trivial poder almacenar entradas y salidas de información dentro de variables. Si bien la gran mayoría de las operaciones que realizaremos en BASH serán sobre texto, las operaciones aritméticas son sumamente importantes. Para esto, la terminal provee un ambiente que permite realizar este tipo de operacioens. ```$((...))```. 

Las variables se asignan usando el signo de ```=``` y pueden ser referidas usando el prefijo ```$```. Nota la ausencia de espacios en la asignación. 

```shell
a=$((20 + 3.5))
echo $a
```

Dos comandos útiles que nos permiten verificar si una variable existe y es no nula.  ```${var:-val}```, ```${var:=val}```. En ambos casos, de existir y ser no nula, se regresa el valor de la variable. En caso contrario, con el primer comando regresamos el valor alternativo *val* y con el segundo comando se asigna *val* a *var*.

```shell
b=''
echo ${b:-3}
echo ${b:=5}
echo $b
```

Dentro de un script de bash o dentro de una función, los parámetros pueden ser referenciados utilizando la sintaxis ```${num_var}``` en donde *num_var* es el número del argumento. De igual forma podemos referirnos al último argumento usando ```${!#}```. Finalmente hay una serie de comandos que nos permiten hacer referencias más generales.  De la misma forma, podemos obtener el número total de argumentos usando la sintaxis 

* ```$#```: Nos indica el número de argumentos.
* ```$*```: Obtiene el total de argumentos.
* ```"$@"```: Representa todos los argumentos como strings individuales. 

Después de ejecutar un script podemos acceder al estatus de ejecución con ```$?```, en caso de éxito será 0, cualquier otro valor implica error. 

## Decisiones

Para que un programa pueda realizar operaciones interesantes, es necesario contar con la capacidad de tomar decisiones basadas en condiciones. Estas condiciones pueden depender del valor de una variable o del resultado de ejecución de un programa. La estructura fundamental para el control de flujo es la sentencia ``ìf```. La estructura general es la siguiente: 

```shell
if expresion
then
exec true
elif expresion
then 
exec true
else
exec false
fi
```

Para negar el valor de una proposición se usa el caracter ```!```. De la misma manera, podemos estar interesados en probar múltiples condiciones. Para esto contamos con los símbolos ```&&``` y ```||```. 


Así mismo, existe un comando de conveniencia llamado ```test```. Este realiza la función de correr y determinar la salida de ejecucón de una instrucción. 


## Iteraciones - bucles


## I/O


## Expresiones Regulares

> Since regular expressions are a fundamental part of the Unix tool-using and tool-building paradigms, any investment you make in learning how to use them, and use them well, well be amply rewarded, multifold, time after time.


#### Metacaracteres

- ```\d``` match con cualquier dígito. ```\D```` match con cualquier no dígito. 
-  ```\w``` hace match con cualquier palabra. ```\W``` hace match con cualquier carcater que no sea una palabra: Los caracteres de palabras incluyen alfanuméricos (-, - and -) y guión bajo (_).
- ```|``` se alterna entre un grupo de posibles expresiones. NOTA: este caracter tiene la menor precedencia dentro de las expresiones regulares. 


Además de los patrones que hemos investigado hasta ahora, hay una manera de aumentar signficativamente el poder de las expresiones regulares. Esto es, agregando memoria. En forma de patraones que upeden ser referenciados. Esto se logra encerrando la expresión deseada entre ```\(, \)```. Estas expresiones pueden ser referidas utilizando la sintáxis ```\digit``` en donde digit es el orden de agrupación de la expresión (con un máximo de nueve referencias)

con los caracteres ```^``` y ```$``` sirven para anclar las expresiones, ya sea al principio o al final de una expresión. `

## Proyecto

- Análisis semántico de stack exchange. Generar un crawler de preguntas y respuestas. 



Recursos

- https://regexr.com/
