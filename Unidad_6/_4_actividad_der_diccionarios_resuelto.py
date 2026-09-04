# ============================================================
# ESTRUCTURAS DE DATOS PARA UN SISTEMA DE RECOMENDACIÓN
# Entidades: Tema · Usuario · Rating
# Programación I | UADE
# ============================================================
#
# En esta actividad vamos a representar las entidades del
# sistema de recomendación usando listas y diccionarios.
#
#   tema ──(1:N)── rating ──(N:1)── usuario
#
# ============================================================


# ============================================================
# PARTE 2 — REPRESENTACIÓN CON DICCIONARIOS
# ============================================================

# Refactorizamos: cada registro ahora es un diccionario.
# Los atributos se acceden por nombre (clave), no por posición.

print("\n" + "=" * 60)
print("PARTE 2 — Con diccionarios")
print("=" * 60)

# ── Entidad: usuario (ya construida para referencia) ─────────
# Cada registro es un diccionario: clave = nombre del campo
usuario_1 = {"id_usuario": 1, "nombre": "Lorenzo"}
usuario_2 = {"id_usuario": 2, "nombre": "Mariano"}
usuario_3 = {"id_usuario": 3, "nombre": "Ignacio"}
usuario_4 = {"id_usuario": 4, "nombre": "Agustin"}
usuario_5 = {"id_usuario": 5, "nombre": "Tatiana"}

# La "tabla" de usuarios: una lista de diccionarios
usuarios = [usuario_1, usuario_2, usuario_3, usuario_4, usuario_5]

print("\nTabla USUARIO:")
for u in usuarios:
    print(u)

# Acceder a un campo por nombre: legible y robusto
print("\nNombre del usuario 1:", usuario_1["nombre"])     # → Lorenzo
print("Id del usuario 3:    ", usuario_3["id_usuario"])  # → 3


# ── Actividad 1 — Construir la entidad TEMA ──────────────────
print("\n--- Actividad 1: Entidad TEMA ---")

# Paso 1: Construí los primeros dos temas como diccionarios.
# Usá como referencia los diccionarios de usuario de arriba.
#
# Campos de tema:
#   id_tema | tema | autor 
#
# Datos:
#   id=1, tema="Dai Dai",  autor="Shakira"
#   id=2, tema="Dynamite", autor="BTS"

tema_1 = {
    "id_tema":     1,
    "tema":        "Dai Dai",
    "autor":       "Shakira"
}

tema_2 = {
    # completar...
    "id_tema":     2,
    "tema":        "Dynamite",
    "autor":       "BTS"
}

# Paso 2: Armá la lista de temas con los dos registros creados arriba.
temas = [ tema_1, tema_2]

print("\nTabla TEMA (primeros 2):")
for t in temas:
    print(t)

# Paso 3: Completá la función para ingresar los campos por teclado
# y agregá los temas 3, 4 y 5 usando append().
#
# Datos a ingresar:
#   id=3, tema="DTMF",           autor="Bad Bunny"
#   id=4, tema="Dont start now", autor="Dua Lipa"
#   id=5, tema="Positions",      autor="Ariana Grande"

def ingresar_tema():
    """Solicita los campos de un tema por teclado y retorna el diccionario."""
    tema = {}
    id = int(input("Ingrese el id: "))
    nombre_tema = input("Ingrese nombre del tema: ")
    autor = input("Ingrese el autor: ")
    tema["id_tema"] = id
    tema["tema"] = nombre_tema
    tema["autor"] = autor
    temas.append(tema) # Inserto el diccionario a la lista

while True:
    ingresar_tema()
    continuar = input("Continua ? S/N:")
    if continuar != "S":
        break


print("\nTabla TEMA (completa):")
for t in temas:
    print(t)


# ── Actividad 2 — Tuplas de ids válidos para validar ─────────
print("\n--- Actividad 2: Tuplas de ids válidos ---")

# Para la Actividad 3 vamos a necesitar validar que el usuario
# ingrese ids que realmente existen.
#
# Usamos TUPLAS porque son inmutables: una vez que cargamos
# los datos, los ids de referencia no deberían cambiar.
#
# Construí dos tuplas a partir de las entidades usuarios y temas:
#   ids_usuarios → todos los id_usuario de la lista usuarios
#   ids_temas    → todos los id_tema de la lista temas

# Podes crear una lista vacia o set vacio, iterar la entidad y completarlos
# Luego converti a tupla con la funcione tuple()

lista_ids_usuarios = []
for usuario in usuarios:
    lista_ids_usuarios.append(usuario["id_usuario"])
ids_usuarios = tuple(lista_ids_usuarios)

lista_ids_temas = []
for tema in temas:
    lista_ids_temas.append(tema["id_tema"])
ids_temas = tuple(lista_ids_temas)

print("IDs de usuarios:", ids_usuarios)
print("IDs de temas:", ids_temas)

# ── Actividad 3 — Construir la entidad RATING ────────────────
print("\n--- Actividad 3: Entidad RATING ---")

# Los ratings conectan un usuario con un tema y guardan
# la calificación (1 a 5) dada por ese usuario a ese tema.
#
# Campos de rating:
#   id_rating | id_usuario | id_tema | rating
#
# La función pide los tres valores al usuario, valida que
# los ids existan en las tuplas, y retorna el diccionario.

ratings = []
id_rating_counter = 1

print("\nIngresá los ratings:")
while True:
    id_usu = int(input(f"\nID de usuario {ids_usuarios}: "))
    while id_usu not in ids_usuarios:
        print("ID de usuario inválido.")
        id_usu = int(input(f"ID de usuario {ids_usuarios}: "))

    id_tema = int(input(f"ID de tema {ids_temas}: "))
    while id_tema not in ids_temas:
        print("ID de tema inválido.")
        id_tema = int(input(f"ID de tema {ids_temas}: "))

    rating = int(input("Rating entre 1 y 5: "))
    while rating < 1 or rating > 5:
        print("El rating debe estar entre 1 y 5.")
        rating = int(input("Rating entre 1 y 5: "))

    nuevo_rating = {
        "id_rating": id_rating_counter,
        "id_usuario": id_usu,
        "id_tema": id_tema,
        "rating": rating,
    }

    ratings.append(nuevo_rating)
    id_rating_counter += 1
    print(f"  ✅ Rating registrado: {nuevo_rating}")

    terminar = input("Terminar? S/N: ")
    if terminar.upper() == "S":
        break

print("\nTabla RATING:")
for r in ratings:
    print(r)


# ── Actividad 4 — Buscar tema por id ─────────────────────────
print("\n--- Actividad 4: Buscar tema por id ---")

# Completá la función que, dado un id_tema, recorra la lista
# de temas y retorne el diccionario correspondiente.
# Si no lo encuentra, que retorne None.

def buscar_tema_por_id(temas, id_tema):
    """Retorna el diccionario del tema con ese id, o None si no existe."""
    for tema in temas:
        if tema["id_tema"] == id_tema:
            return tema

    return None


# Prueba
id_buscar = int(input("\n¿Qué id de tema querés buscar? "))
resultado  = buscar_tema_por_id(temas, id_buscar)

if resultado:
    print("\nTema encontrado:")
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")
else:
    print(f"\nNo se encontró ningún tema con id {id_buscar}.")
