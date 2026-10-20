
"""
ratings = [5, 3, 4, 1, 5, 2]
ratings_altos = [] # lista a retornar
for r in ratings: # iteracion
    if r >= 4: # evaluacion de la condicion
        ratings_altos.append(r)

print("Forma tradicional:", ratings_altos)
"""



# ratings_altos = []
# for r in ratings: # iteracion
#     ratings_altos.append(r**2)

ratings = [5, 3, 4, 1, 5, 2] # lista de numeros
# Lista por comprension - generar los cuadrados de los ratings
ratings_cuadrados_lxc = [r**2 for r in ratings ]
print(f"ratings_altos_lxc: {ratings_cuadrados_lxc}")

# funcion tradicional
def elevar_cuadrado(x):
    return x**2

# funcion lambda
lambda  x : x**2

# Map + Lambda - generar los cuadrados de los ratings
# aplica una funcion a cada elemento de la lista
ratings_cuadrados_map = list( map ( lambda  x : x**2 , ratings) )
print(f"\nratings_cuadrados_map: {ratings_cuadrados_map}")

def cuadrados_con_lambda(lista):
    return list( map ( lambda  x : x**2 , lista) )

# ------------------------------------------------
# FILTER

# funcion tradicional
# retorna True si x >= 4 o False caso contrario
def mayor_4(x):
    return x >= 4

# funcion lambda
lambda  x : x >= 4

# Filtro tradicional
ratings_altos = [] # lista a retornar
for r in ratings: # iteracion
    if r >= 4: # evaluacion de la condicion
        ratings_altos.append(r)
print("Forma tradicional:", ratings_altos)

# Filtro con Filter & lambda
# Sintaxis: filter ( funcion , iterable)
ratings_altos_lambda = list (filter (lambda  x : x >= 4 , ratings))
print("Forma Filter & lambda:", ratings_altos_lambda)