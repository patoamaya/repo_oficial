import random

# Append
"""
lst = [1, 2, 3]

lst.append(4 )

print(lst)
"""

# Extend
# Toma un iterable (como otra lista) y agrega cada uno de sus elementos al final, en vez de agregarlos como un paquete (append)
"""
list = [1, 2]

list.extend([3, 4])

print(list)

list_A = [1, 2]
list_A.extend([3,4])

list_B = [1, 2]
list_B.append([3, 4])

print("Lista A: ", list_A)
print("Lista B: ", list_B)
"""

# insert
# Insertar en una posición específica, desplazando el resto hacia la derecha
# lista.insert(indice, valor)
"""
list = [1, 2, 3]
list.insert(1, 1.5)

print(list)
"""

# remove
# Elimina la PRIMERA ocurrencia del valor indicado. Si el valor indicado no existe, arroja un "ValueError"
"""
list = [1, 2, 3, 4]
list.remove(2)
print(list)
"""

# pop
# Elimina y devuelve un elemento para que puedas usarlo
# Sin argumento: Elimina el último elemento
# Con índice: elimina el elemento en esa posición
"""
list = [1, 2, 3]
ultimo = list.pop()
print("Eliminando sin argumento, el último valor", ultimo)
print("Lista resultante: ", list)
"""
"""
# Con índice
list = [10, 20, 30, 40]
indice = list.pop(1)
print("Eliminando en el indice 1 el número: ", indice)
print("Lista resultante ", list)
"""

# index
# Busca la posición de la primera aparición de un valor. Si el valor ingresado no existe, devuelve un "ValueError"
"""
list = [1, 2, 3]
pos = list.index(2)
print("El indice 2 esta en la posición: ", pos)
"""

# count
# Cuenta cuántas veces aparece un valor en la lista
"""
list = [1, 2, 3, 3, 3, 3, 4]
cantidad = list.count(3)

print("El número 3 está repetido", cantidad, " veces")
"""

# sort
# Ordena la lista (modificando el original) en orden ascendente por defecto
# sort() --> Orden ascendente
# sort(reverse = True) --> Orden descendente
"""
# Ascendente
list = [2, 5, 6, 4, 3, 1]
list.sort()
print("Lista ordenada ascendente: ", list)
"""
"""
# Descendente
list = [2, 5, 6, 4, 3, 1]
list.sort(reverse=True)
print("Lista ordenada descendente: ", list)
"""

# reverse
# Invierte el orden de los elementos de la lista, pero no las ordena
"""
list = [1, 3, 5, 7, 9]
print("Lista original: ", list)
list.reverse()
print("Lista en reverso: ", list)
"""

# Funciones Built-in para listas
# Funciones globales (no son metodos de lista) útiles para trabajar con colecciones
"""
list = [4, 7, 2, 9, 1]

print("Lista original: ", list)
print("Cantidad de números con len()---> ", len(list))
print("Suma total con sum()---> ", sum(list))
print("Valor mínimo()---> ", min(list))
print("Valor máximo()---> ", max(list))
"""

# list
# Convierte otro iterable en una lista
"""
tupla = (1, 2, 3)

print("Tupla original ---> ", tupla)
print("Convirtiendo la tupla en una lista con list()---> ", list(tupla))
"""

# Acceso por índice
# Los índices en python empiezan en 0. También se pueden usar índices negativos negativos para contar desde el final
"""
list = [10, 20, 30, 40, 50]

print("Lista original---> ")
print("Primer elemento con list[0]", list[0])
print("Primer elemento con list[2]", list[2])
print("Último elemento con list[-1]", list[-1])
print("Anteultimo elemento con list[-2]", list[-2])
"""

# slicing (rebanado)
# Permite usar una sublista usando la sintaxis lista[inicio:fin:paso]
# El índice 'inicio' está incluido
# El índice 'fin' está excluido
"""
list = [0, 1, 2, 3, 4, 5]

print("Lista original---> ", list)
print("Desde el indice 1 al 3 con list[1:4]--->", list[1:4])
print("Desde el inicio con list[:3]--->", list[:3])
print("Hasta el final desde 3 con list[3:]--->", list[3:])
print("De a 2 pasos con list[::2]--->", list[::2])
print("Invertida con list[::-1]--->", list[::-1])
"""

# Concatenación y copia
# Concatenación con '+'

"""
list1 = [1, 2]
list2 = [3, 4]
print("Suma de listas con '+'---> ", list1 + list2)
"""

# Repetición con '*'
"""
list = [2]
print("Repitiendo el contenido de la lista 4 veces con list*4---> ", list*4)
"""

# Copia superficial con .copy()
"""
original = [1, 2, 3]
copia = original.copy()
copia.append(99)

print("Lista original---> ", original)
print("Lista copiada---> ", copia)
"""

# Desempaquetado (Unpacking)
# Permite asignar los elementos de una lista a variables individuales en una sola línea
"""
a, b, c = [1, 2, 3]
print("a-->", a, "b-->", b, "c-->", c)
"""

# Desempaquetado con '*' (captura al resto)
"""
primero, *resto = [10, 20, 30, 40, 50]
print("Primero --> ", primero)
print("Resto --> ", resto)
"""

notas = [7, 5, 9, 6, 8, 4, 10]


# Ej 1
"""
promedio = sum(notas) / len(notas)
print("Promedio--->", promedio)

print("Nota máxima--->", max(notas))
print("Nota mínima--->", min(notas))
"""
# Ej 2
"""
list=[]
nros = [1, 2, 3, 4, 5]
list.extend(nros)
print("Lista cargada--->", list)
list.insert(0, 0)
list.insert(6, 6)
print("Lista con 0 y 6 insertados--->", list)
list.sort(reverse=True)
print("Lista ordenada en reverso--->", list)
"""
# Ej 3
"""
datos = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sliced = datos[2:6]
print(sliced)
"""