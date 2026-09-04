# Declarar e Inicializar - opcion 1
# matriz = [
#     [1, 3, 2],
#     [3, 5, 1]
# ]

# Declarar e Inicializar - opcion 2
# matriz = []
# fila1 = [1, 3, 2]
# fila2 = [3, 5, 1, 5]
# matriz.append(fila1)
# matriz.append(fila2)
# print(matriz)

# Iterar una lista (puede ser una fila de una matriz)
fila1 = [1, 3, 2]
# Iterar con range
# for i in range(len(fila1)):
#     print(fila1[i])

# Iterar con for .. in
# for f in fila1:
#     print(f)

# Iterar con Enumerate
""" enumerate recibe una lista
    retorna una tupla, formada por:
    - indice
    - valor
"""
for i, f in enumerate(fila1):
    print(f"Indice: {i+1}: Valor: {f}")