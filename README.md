# problema_tres

(<[lista de salida]>, <error>) = get_list_of_infections(<ruta del archivo json>, <[lista de palabras para filtrar]>)

Entrada de "get_list_of_infections":
    1. json_file: ruta de un archivo json valido.
    2. filter: lista de palabras claves para filtrar. Opcional.

Salida de "get_list_of_infections":
    1. output: lista de resultados.
    2. error. Objeto de error si sucede un evento excepcional.


Si la funcion recive un json mal formado o la ruta del file no exite, entonces la salida es una tupla
donde output retorna una lista vacia y error un objeto de la excepcion.

El parametro filter en el input es opcional. Es una lista de palabras ej: ['salmonella', 'escherichia coli']

