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


# ── Entidad: usuario (ya construida para referencia) ─────────
# Cada registro es un diccionario: clave = nombre del campo
usuario_1 = {"id_usuario": 1, "nombre": "Franco"}
usuario_2 = {"id_usuario": 2, "nombre": "Valentin"}
usuario_3 = {"id_usuario": 3, "nombre": "Keyla"}
usuario_4 = {"id_usuario": 4, "nombre": "Pablo"}
usuario_5 = {"id_usuario": 5, "nombre": "Milagros"}

# La "tabla" de usuarios: una lista de diccionarios
usuarios = [usuario_1, usuario_2, usuario_3, usuario_4, usuario_5]


# ── Actividad 1 — Construir la entidad TEMA ──────────────────

# Paso 1: Construí los primeros dos temas como diccionarios.
# Usá como referencia los diccionarios de usuario de arriba.
#
# Campos de tema:
#   id_tema | tema | autor 
#
# Datos:
#   id=1, tema="Dai Dai",  autor="Shakira"
#   id=2, tema="Swim",     autor="BTS"

tema_1 = {
    "id_tema":     1,
    "tema":        "Dai Dai",
    "autor":       "Shakira"
}

tema_2 = {
    # completar...
}

# Paso 2: Armá la lista de temas con los dos registros creados arriba.
# temas =


# ********** FUNCIONES ***************

def mostrar_usuarios(usuarios):
    for registro in usuarios:
        print(registro)


def mostrar_temas(temas):
    for registro in temas:
        print(registro)


# Paso 3: Completá la función para ingresar los campos por teclado
# y agrega el registro a la lista temas usando append()
#
# Datos a ingresar:
#   id=3, tema="Chosin Texas",  autor="Ella Langley"
#   id=4, tema="MIA",           autor="Bad Bunny"
#   id=5, tema="SFTU",          autor="Drake"

def ingresar_tema():
    """Solicita los campos de un tema por teclado y retorna el diccionario."""


# Paso 4: generá un Loop en la función main que llame a la función
# ingresar_tema() - se sugiere que el usuario indique fin de carga
def main():

    """
    Tu código aquí
    """
    # mostrar_usuarios(usuarios)
    # mostrar_temas(temas)



# ── Actividad 2 — Tuplas de ids válidos para validar ─────────

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

# ids_usuarios = # Completar
# ids_temas = # Completar

# ── Actividad 3 — Construir la entidad RATING ────────────────

# Los ratings conectan un usuario con un tema y guardan
# la calificación (1 a 5) dada por ese usuario a ese tema.
#
# Campos de rating:
#   id_rating | id_usuario | id_tema | rating
#
# La función pide los tres valores al usuario, valida que
# los ids existan en las tuplas, y retorna el diccionario.

# ratings = []
# id_rating_counter = 1

# print("\nIngresá los ratings:")
# while True:
#     id_usu = input(f"\nID de usuario {ids_usuarios}: ")
#     id_usu = int(id_usu)

#     nuevo_rating = {
#         "id_rating":  id_rating_counter,
#         "id_usuario": id_usu,

#     }
    
#     ratings.append(nuevo_rating)
#     id_rating_counter += 1
#     print(f"  ✅ Rating registrado: {nuevo_rating}")

#     terminar = input("Terminar? S/N: ")
#     if terminar == "S":
#         break

# print("\nTabla RATING:")
# for r in ratings:
#     print(r)


