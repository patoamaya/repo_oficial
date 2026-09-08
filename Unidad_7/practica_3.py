# Cadenas de caracteres (str)

### Acceso y operaciones basicas ###
# Las cadenas se comportan como secuencias: Se puede acceder por índice, hacer slicing, concatenar y repetir, al igual que con las listas

"""
s = "hello"
#      01234  <-- índices

Se puede acceder por índice:

print("s[0] ---> 'h'", s[0])
print("s[1] ---> 'e'", s[1])
print("s[2] ---> 'l'", s[2])
etc

# slicing
print("de 0 a 2 --> 'he'", s[0:2])
print("En reverso con s[::-1]", s[::-1])
# concatenación con +

s1 = "hello"
s2 = "world"

print("Concatenando con '+' -->", s1 + "", s2)

# Repetición con *

print("Repetición con '*'-->", s1 * 3)

# Longitud

print("Longitud -->", len(s1))

# Las cadenas son inmutables. No se puede modificar un caracter directamente
s = "hello"
s[0] = "H" --> typeError: 'str' object does not support item assignment
# Para modificar una cadena, hay que crear una nueva
"""

### Metodos esenciales ###
"""
texto = "hOLA mUNDO"  

print("Todo mayúscula ---> ", texto.upper())
print("Todo minúscula ---> ", texto.lower())
print("Primera letra en mayúscula ---> ", texto.capitalize())
print("Primera letra de cada palabra en mayúscula ---> ", texto.title())
print("Invierte mayúsculas con minúsculas ---> ", texto.swapcase())
"""

# strip() ---> Elimina espacios u otros caracteres de ambos extremos
"""
s = "   hello   "

print("Strip base-->", s.strip())
print("Strip izquierdo--> ", s.lstrip())
print("Strip derecho--> ", s.rstrip())

# también elimina carácteres específicos

print("Eliminando '-' con strip('-') -->", "---hola---".strip('-'))
"""

# replace
"""
s = "hello"
# replace(viejo, nuevo) reemplaza TODAS las ocurrencias 
print("Reemplazando 'l' por 'r'-->  ", s.replace('l', 'r'))

# con un tercer argumento, limitamos la cantidad de veces que queremos que reemplace
print("Reemplazando 'l' por 'r', pero solo una vez --> ", s.replace('l', 'r', 1))
"""

# find
# Indice de la primera ocurrencia (-1 si no existe)

s = "Hola, mundo"

print("Find de 'mundo'--> ", s.find('mundo'))
print("Find de 'xyz'--> ", s.find('xyz'))

# rfind()
# Busca desde el final y muestra la ultima ocurrencia, no la primera como el find comun
s2 = "Hola, mundo, mundo"
print("Buscando desde el final 'mundo", s2.rfind('mundo'))

# starswith() / endswith()
# Verifican extremos de la cadena

print("La cadena arranca con 'hola' ? --> si -- > ", s.startswith('Hola'))
print("La cadena arranca con 'hola' ? --> no --> ", s.startswith('hola'))
print("La cadena termina con 'Mundo' ? --> si --> ", s.endswith('mundo'))