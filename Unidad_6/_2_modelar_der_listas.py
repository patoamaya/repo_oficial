# ============================================================
# ESTRUCTURAS DE DATOS PARA UN SISTEMA DE RECOMENDACIÓN
# Entidades: Tema · Usuario · Rating
# Programación I | UADE
# ============================================================
#
# En esta actividad vamos a representar en código Python las
# tres entidades del DER de nuestro sistema de recomendación:
#
#   tema ──(1:N)── rating ──(N:1)── usuario
#
# Atributos de cada entidad:
#   tema    → id_tema, tema, autor, genero, lanzamiento
#   usuario → id_usuario, nombre, apellido, email
#   rating  → id_rating, id_tema, id_usuario, rating, fecha
#
# Vamos a ver la evolución de las estructuras:
#   Parte 1 → con listas (simple pero poco legible)
#   Parte 2 → con diccionarios (legible y robusto)
#   Parte 3 → relaciones entre entidades
#   Parte 4 → consultas combinadas (actividades)
# ============================================================


# ============================================================
# PARTE 1 — REPRESENTACIÓN CON LISTAS
# ============================================================

# Una entidad puede representarse como una lista donde
# cada posición corresponde a un atributo.
# PROBLEMA: hay que recordar el índice de cada campo.

# Atributos de tema (en orden):
# [0] id_tema | [1] tema | [2] autor 
tema_1 = [1, "Dai Dai",        "Shakira"]
tema_2 = [2, "Swim",           "BTS"]
tema_3 = [3, "MIA",            "Bad Bunny"]
tema_4 = [4, "SFTU",           "Drake"]

temas_lista = [tema_1, tema_2, tema_3]

# Acceder al autor del tema 1: hay que saber que es el índice 2
print("Autor del tema 1 (con lista):", tema_1[2])  # → Shakira

# Mostrar todos los temas
print("\nTemas (con listas):")
for t in temas_lista:
    print(t)

# Atributos de usuario (en orden):
# [0] id_usuario | [1] nombre
usuario_1 = [1, "Franco"]
usuario_2 = [2, "Valentin"]
usuario_3 = [3, "Keyla"]

usuarios_lista = [usuario_1, usuario_2, usuario_3]

# Atributos de rating (en orden):
# [0] id_rating | [1] id_usuario | [2] id_tema | [3] rating
rating_1 = [1, 1, 1, 4]   # Franco → Dai Dai
rating_2 = [2, 1, 4, 5]   # Franco → MIA
rating_3 = [3, 2, 1, 3]   # Valentin → Dai Dai
rating_4 = [4, 2, 4, 5]   # Valentin → MIA
rating_5 = [5, 3, 2, 5]   # Keyla → Swim

ratings_lista = [rating_1, rating_2, rating_3, rating_4, rating_5]

print("\n¿Qué rating dio el usuario Franco al tema Dai Dai?", rating_1[3])  # → 4
# Pero... ¿cómo sabemos que [3] es el rating y no otra cosa?
# Ese es el problema de las listas.
