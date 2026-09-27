/*
El ejercicio requiere generar una frase basada en el valor
de la columna input.
 
Casos:
- Si input contiene un nombre:
"One for <nombre>, one for me."
 
- Si input está vacío:
"One for you, one for me."
 
NULLIF(input, '')
Convierte una cadena vacía en NULL evitando que el valor quede vacio
 
COALESCE(..., 'you')
Sustituye los valores NULL por 'you'
*/


UPDATE twofer
SET response = 'One for ' || COALESCE(NULLIF(input, ''), 'you') || ', one for me.'
