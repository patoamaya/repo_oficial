# 🎵 Actividad Integradora — Sistema de Recomendación Musical (Parte 1)
### Programación I | UADE

---

## Contexto

A lo largo del cuatrimestre estuvimos construyendo un **Sistema de Recomendación de Temas Musicales**. En esta actividad integradora vamos a unificar todos los contenidos vistos hasta ahora para construir la capa de datos del sistema: las entidades, el CRUD de usuarios y la gestión de calificaciones.

El resultado de esta parte va a ser la **matriz de ratings** que alimentará el motor de recomendación visto en clase (`_6_sis_rec_part_1_resuelto.py`).

---

## Modalidad

- Se puede trabajar de manera **grupal** (mismo grupo del TPO) o individual.
- Se recomienda trabajar de manera **individual** para prepararse para el primer parcial.
- El código debe estar versionado en **GitHub** siguiendo las instrucciones de la sección 1 (Unidades 1 y 2).

---

## Sección 1 — Git y GitHub

### 1.1 Configuración del repositorio

1. Crea una carpeta en tu pc con el nombre `582477-actividad-integradora` y pega el template `_4_actividad_integradora_template.py`:
2. Creá un repositorio en GitHub con el nombre `582477-actividad-integradora`.
3. Seguí los pasos de Github para inicializar y sincronizar el repo local con la nube.
3. Creá la rama `develop` a partir de `main`:
   ```bash
   git checkout -b develop
   ```
4. Trabajá siempre en la rama `develop`. Solo mergeás a `main` cuando la parte esté completa y funcional.

### 1.2 Flujo de trabajo

Cada vez que completes una función o sección, hacé un commit descriptivo:

```bash
git add .
git commit -m "feat: agrega función crear_usuario con validaciones"
git push origin develop
```

Al finalizar toda la actividad, mergeá `develop` en `main` (o generá pull-request desde Github):

```bash
git checkout main
git merge develop
git push origin main
```

### 1.3 Criterio de evaluación Git

| Criterio | Descripción |
|---|---|
| Uso de ramas | Trabajo en `develop`, merge final a `main` |
| Commits atómicos | Al menos un commit por función completada |
| Mensajes descriptivos | El mensaje describe qué se hizo (no "cambios" o "fix") |

---

## Sección 2 — Modelo de datos

El sistema se basa en el siguiente Diagrama Entidad-Relación:

```
tema ──(1:N)── rating ──(N:1)── usuario
```

### Atributos de cada entidad

| Entidad | Atributos |
|---|---|
| `tema` | `id_tema`, `tema`, `autor` |
| `usuario` | `id_usuario`, `nombre`, `apellido`, `email` |
| `rating` | `id_rating`, `id_tema`, `id_usuario`, `rating`, `fecha` |

### Estructura en memoria

Cada entidad se representa como una **lista de diccionarios** (tabla en memoria):

```python
# Ejemplo de estructura
temas    = [{"id_tema": 1, "tema": "Dai Dai", "autor": "Shakira"}, ...]
usuarios = [{"id_usuario": 1, "nombre": "...", ...}, ...]
ratings  = [{"id_rating": 1, "id_tema": 1, "id_usuario": 1, "rating": 5, "fecha": "..."}, ...]
```

---

## Sección 3 — Entidad TEMA (estática)

La entidad `temas` se carga de manera **estática** al inicio del programa con los siguientes registros:

| id_tema | tema | autor |
|---|---|---|
| 1 | Dai Dai | Shakira |
| 2 | Swim | BTS |
| 3 | Chosin Texas | Ella angley |
| 4 | DTMF | Bad Bunny |
| 5 | SFTU | Drake |

No se implementa CRUD para temas: la lista es fija durante toda la ejecución.

---

## Sección 4 — CRUD de USUARIOS

Implementá las siguientes funciones para gestionar la entidad `usuario`.  
El `id_usuario` por ahora lo ingresa el usuario, luego lo vamos a automatizar.

### 4.1 `crear_usuario(usuarios)`

Solicita los datos por teclado y agrega el nuevo usuario a la lista.

**Validaciones requeridas (Unidad 7 — métodos de string):**
- `nombre` y `apellido`: solo deben contener letras y espacios (`.isalpha()` o equivalente). Normaliza los datos, convirtiendo a title.
- `email`: debe contener `@` y al menos un `.` después del `@`
- Ningún campo puede estar vacío

### 4.2 `buscar_usuario_por_id(usuarios, id_usuario)`

Recibe la lista de usuarios y un id, y retorna el diccionario del usuario encontrado o `None` si no existe.

### 4.3 `ver_usuarios(usuarios, pagina, tamaño_pagina)`

Muestra los usuarios paginados usando **slicing** (Unidad 7).

- Explorá opciones con slice para mostrar los primeros 5 registros, por ejemplo

### 4.4 `eliminar_usuario(usuarios, id_usuario)`

Elimina el usuario con ese id usando `.pop()` o `.remove()` sobre la lista (Unidad 7 — métodos de lista).  
Si el usuario no existe, muestra un mensaje de error.  
**Consideración:** al eliminar un usuario, también deben eliminarse todos sus ratings asociados.

---

## Sección 5 — Gestión de RATINGS

### 5.1 `registrar_rating(ratings, id_usuario, id_tema, valor_rating, fecha)`

Registra una calificación de un usuario para un tema.

**Regla de negocio:** si el usuario ya calificó ese tema, se **actualiza** el rating existente en lugar de crear uno nuevo. No puede haber dos ratings del mismo `(id_usuario, id_tema)`.

**Validaciones:**
- `valor_rating` debe ser un entero entre 1 y 5
- `id_usuario` debe existir en la lista de usuarios
- `id_tema` debe existir en la lista de temas

### 5.2 `leer_ratings(ratings, temas, usuarios)`

Muestra todos los ratings registrados con el nombre del tema y del usuario (JOIN manual), en formato de tabla legible.

---

## Sección 6 — Matriz de ratings

### 6.1 `construir_matriz_ratings(usuarios, temas, ratings)`

A partir de las tres listas, construí la **matriz de doble entrada** donde:
- Cada **fila** corresponde a un usuario
- Cada **columna** corresponde a un tema
- El valor es el rating dado (o `0` si el usuario no calificó ese tema)

Esta matriz es la que se pasa como argumento a las funciones de `_6_sis_rec_part_1_resuelto.py`.

### 6.2 `mostrar_matriz(matriz, usuarios, temas)`

Muestra la matriz con encabezados de filas (nombres de usuarios) y columnas (nombres de temas), usando el mismo formato que `mostrar_matriz` del archivo de referencia.

---

## Sección 7 — Función principal

La función `main()` debe implementar un **menú interactivo** con las siguientes opciones:

```
========================================
  Sistema de Recomendación Musical
========================================
1. Ver temas disponibles
2. Gestionar usuarios
   2.1. Crear usuario
   2.2. Ver usuario por ID
   2.3. Ver todos los usuarios (con slicing)
   2.4. Eliminar usuario
3. Gestionar ratings
   3.1. Registrar rating
   3.2. Ver todos los ratings
4. Ver matriz de ratings
0. Salir
```

---

## Entrega

| Ítem | Descripción |
|---|---|
| Repositorio GitHub | URL del repositorio con ramas `main` y `develop` |
| Archivo `.py` | Código completo y funcionando |
| Al menos 5 commits | Uno por cada sección completada |

---


---

> 💡 **Tip:** podés usar el archivo `_6_sis_rec_part_1_resuelto.py` como referencia para las funciones `mostrar_matriz`, `generar_predicciones_random` y `generar_predicciones_popularidad`. En la Parte 2 vamos a integrar ambos archivos.
