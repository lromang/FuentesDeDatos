
## SED

Hasta este momento hemos visto como identificar y extraer patrones específicos sobre archivos de texto. El paso más inmediato sería adquirir la posibilidad de realizar modificaciones específicas. Una herramienta escencial para este tipo de tareas es el editor de flujos (stream editor) o Sed. 

El uso más básico de sed es el siguiente ```sed 's[delimiter][pattern][delimiter][new_pattern][delimiter]'``` en donde el caracter delimitador puede ser cualquier printable. 

Recuerda que para hacer referencia hacia atrás es necesario que los parentesis que engloban la expresión referenciada estén escapados. En el caso particular de la expresión de substitución, el caracter ```&``` significa, reemplaza en este punto el texto identificado con la expresión regular. 

El sufijo g, hace que las modificaciones sean globales. De la misma manera, se puede especificar la instancia que se desea modificar poniendo el número de ocurrencia como sufijo. Las instrucciones se pueden concatenar con ```-e``` o simplemente escribiendolas en un archivo y pasando la opción ```-f```. 
