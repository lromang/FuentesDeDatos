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

Además de esto es fundamental poder interactuar con archivos. Los comandos más utilizados son:

* ```touch```: permite crear un archivo bajo un nombre específico. 
* ```cat```, ```head```, ```tail```: muestran contenido parcial o total del archivo.
* ```mv```, ```cp```, ```rm```: mueven, copian y eliminan archivos.

Uno de los conceptos más fundamentales dentro de bash (y muchos otros lenguajes que cubriremos en el curso) es el *pipelining* de instrucciones. En terminos generales, esto nos permite concatenar la ejecución de multiples subrutinas. El commando que nos permite llevar esto a cabo es ```|```. 

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


Así mismo, existe un comando de conveniencia llamado ```test```. Este realiza la función de correr y determinar la salida de ejecucón de una instrucción. Esto es equivalent a usar `[]` para profundizar en las diferencias entre ```[]``` y  ```[[]]``` ver este [hilo](https://stackoverflow.com/questions/3427872/whats-the-difference-between-and-in-bash). 


## Iteraciones - bucles

El bucle ```for``` itera sobre una lista de objetos, ejecutando el cuerpo de instrucciones para cada objeto de manera individual. 

```shell
for i in expression
do
exec
done
```

El bucle ```while``` por su parte, itera hasta que cierta condición deja de cumplirse. 

```shell
while expression
do
exec
done
```

Es posible interrumpir un bucle de manera prematura usando la instrucción ```break```. 

## I/O

Cuando nuestros scripts crecen demasiado en tamaño y complejidad, deja de ser conveniente ejecutarlos sobre la línea de comandos, en lugar de esto, definimos archivos que contengan las instrucciones y puedan ser ejecutados directamente desde la consola. 

El header de estos archivos debe tener la siguiente forma: "#! /path/to/interpreter" en donde el interprete es el programa que consumirá el archivo.

Dentro de un script, se puede leer insumos del usuario usando la sentencia ```read``` y  los argumentos de usuario pueden ser referenciados utilizando la sintaxis ```${num_var}``` en donde *num_var* es el número del argumento. De igual forma podemos referirnos al último argumento usando ```${!#}```. Finalmente hay una serie de comandos que nos permiten hacer referencias más generales.  De la misma forma, podemos obtener el número total de argumentos usando la sintaxis 

* ```$#```: Nos indica el número de argumentos.
* ```$*```: Obtiene el total de argumentos.
* ```"$@"```: Representa todos los argumentos como strings individuales. 

Después de ejecutar un script podemos acceder al estatus de ejecución con ```$?```, en caso de éxito será 0, cualquier otro valor implica error. 
