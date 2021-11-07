## Introducción a la línea de comandos

Manejar la línea de comandos de manera adecuada es una herramienta fundamental que nos permite:

    * Interactuar con el sistema de archivos de manera eficiente,
    * controlar y vincular procesos

Todo esto a través del lenguaje interpretado [**BASH**](https://en.wikipedia.org/wiki/Bash_(Unix_shell)). Si bien la complejidad relativa que presenta aprender toda una nueva serie de *comandos* en un ambiente poco amigable, contra una interfáz gráfica, pudiera resultar abrumadora. Con la práctica y uso constante, el trabajo con una terminal se volverá una segunda naturaleza.

#### Ubicación dentro del sistema de archivos

El primer paso funcional cuando nos encontramos dentro de un sistema linux por primera vez es identificar en donde estamos ubicados. Saber movernos de manera eficiente así como crear ambientes de trabajo. 

El comando ```pwd``` nos permite identificar nuestra posición actual.

<p style="color:DodgerBlue;">Nota: Lo más probable es que tu ruta tenga la forma ```/dir_1/dir_2/dir_.../.```. Las rutas que comienzan con ```/``` son rutas absolutas, pues parten del directorio raíz ```/```. Las rutas de la forma ```./``` son rutas relativas que parten del directorio en el cual estás ubicad@. <\p>


aa

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

## Expresiones Regulares

> Since regular expressions are a fundamental part of the Unix tool-using and tool-building paradigms, any investment you make in learning how to use them, and use them well, well be amply rewarded, multifold, time after time.


