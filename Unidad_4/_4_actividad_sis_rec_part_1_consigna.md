# Práctica: Matrices aplicadas a un sistema de recomendación

## Objetivo

Aplicar los conceptos de **matrices implementadas mediante listas de listas en Python** a un problema inspirado en un sistema de recomendación real.

Durante la actividad se trabajará con una matriz de calificaciones de canciones, donde:

- cada **fila** representa a un estudiante;
- cada **columna** representa un tema musical;
- cada elemento de la matriz representa el rating asignado por un estudiante a un tema;
- el valor `0` indica que el estudiante todavía no escuchó o calificó ese tema.

A partir de esta estructura se construirán dos estrategias sencillas de predicción:

1. **Predicción aleatoria**.
2. **Predicción basada en popularidad**, utilizando el rating promedio de cada tema.

---

## Modalidad de trabajo

La actividad se realizará **en equipos**.

Los integrantes pueden ser los mismos grupos definidos para el TPO o pueden conformar nuevos equipos.

El desarrollo deberá realizarse de forma colaborativa utilizando:

- Git;
- GitHub;
- ramas;
- commits;
- repositorio compartido.

El archivo base para comenzar la actividad es:

```text
_3_sis_rec_part_1.py
```

No deberán modificar la estructura general del programa. El objetivo será **completar las funciones provistas**.

---

# Parte 1 — Analizar el código provisto

Antes de comenzar a programar, recorran el archivo base e identifiquen las distintas partes que componen el programa.

Analicen especialmente:

### Constantes

El programa contiene tres estructuras principales:

```python
ESTUDIANTES
TEMAS
RATINGS
```

Identifiquen qué información almacena cada una.

Observen especialmente la matriz `RATINGS`.

```python
RATINGS = [
    [4, 0, 0, 5, 0],
    [3, 0, 0, 5, 0],
    [0, 5, 0, 4, 0],
    [0, 0, 0, 2, 5],
    [0, 0, 0, 4, 5],
]
```

Respondan:

- ¿Cuántas filas tiene?
- ¿Cuántas columnas?
- ¿Qué representa cada fila?
- ¿Qué representa cada columna?
- ¿Qué representa el valor almacenado en `RATINGS[i][j]`?
- ¿Qué significado tiene un `0`?

---

## Función principal

Analicen la función:

```python
main()
```

Identifiquen:

- qué funciones secundarias utiliza;
- en qué orden son llamadas;
- qué información recibe cada función;
- qué información retorna cada una.

Antes de implementar las funciones, intenten anticipar cuál debería ser la salida general del programa.

---

# Parte 2 — Mostrar una matriz

Completar la función:

```python
def mostrar_matriz(matriz):
```

La función deberá recibir una matriz y mostrar sus elementos en consola **fila por fila**.

Por ejemplo, para:

```python
[
    [1, 2, 3],
    [4, 5, 6]
]
```

podría mostrar:

```text
1 2 3
4 5 6
```

La función deberá funcionar independientemente de la cantidad de filas de la matriz.

---

# Parte 3 — Primera estrategia: predicción aleatoria

Nuestro sistema necesita generar una predicción para aquellos temas que cada estudiante todavía no calificó.

Completar:

```python
def generar_predicciones_random(ratings):
```

La función deberá generar y retornar una **nueva matriz con las mismas dimensiones que `RATINGS`**.

Para cada posición:

- si el estudiante ya calificó ese tema, colocar `0`;
- si el rating original es `0`, generar una predicción utilizando:

```python
random.randint(1, 5)
```

Por ejemplo:

```text
RATINGS

4 0 0 5 0
3 0 0 5 0
```

podría producir:

```text
PREDICCIONES_RANDOM

0 3 5 0 2
0 4 1 0 5
```

Los valores generados podrán cambiar cada vez que se ejecute el programa.

### Para analizar

¿El algoritmo utiliza información sobre los gustos de los estudiantes para realizar las predicciones?

¿Podemos considerar que es un buen sistema de recomendación?

---

# Parte 4 — Segunda estrategia: popularidad

Ahora intentaremos mejorar la predicción.

En lugar de generar valores aleatorios, utilizaremos el **rating promedio recibido por cada tema**.

Por ejemplo, si un tema fue calificado con:

```text
4, 3, 5
```

su promedio será:

```text
4
```

Ese promedio podrá utilizarse como predicción para aquellos estudiantes que todavía no calificaron el tema.

Para construir esta estrategia deberán resolver primero algunos problemas intermedios.

---

# Parte 5 — Generar una matriz nula

Completar:

```python
def generar_matriz_nula(n_filas, n_columnas):
```

La función deberá crear y retornar una matriz de las dimensiones indicadas cuyos valores sean todos `0`.

Por ejemplo:

```python
generar_matriz_nula(3, 4)
```

deberá generar:

```python
[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

Esta función será utilizada posteriormente para construir otras matrices.

---

# Parte 6 — Trasponer la matriz

En `RATINGS`, las filas representan estudiantes y las columnas representan temas.

Sin embargo, para analizar cómodamente todas las calificaciones de un tema resulta útil intercambiar filas y columnas.

Completar:

```python
def trasponer(matriz):
```

La función deberá recibir una matriz de dimensiones:

```text
n × m
```

y retornar una nueva matriz de dimensiones:

```text
m × n
```

La relación entre ambas matrices debe cumplir:

```python
matriz_T[j][i] = matriz[i][j]
```

Por ejemplo:

```python
[
    [1, 2, 3],
    [4, 5, 6]
]
```

debe transformarse en:

```python
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

Antes de realizar la transposición, pueden utilizar la función `generar_matriz_nula()` para crear una matriz con las dimensiones necesarias.

---

# Parte 7 — Calcular el rating promedio

Completar:

```python
def calcular_ratings_avg(matriz):
```

La función deberá obtener el **rating promedio de cada tema**.

Recuerden que:

```text
0
```

representa ausencia de calificación, por lo que **no debe formar parte del cálculo del promedio**.

Por ejemplo:

```text
[4, 3, 0, 0, 0]
```

deberá producir:

```text
3.5
```

porque:

```text
(4 + 3) / 2 = 3.5
```

La función deberá retornar una lista:

```python
ratings_avg
```

cuya longitud coincida con la cantidad de temas.

Para resolver este problema puede resultar conveniente utilizar previamente la función:

```python
trasponer()
```

De esta manera, cada fila de la matriz traspuesta contendrá todas las calificaciones correspondientes a un mismo tema.

---

# Parte 8 — Predicción basada en popularidad

Finalmente, completar:

```python
def generar_predicciones_popularidad(ratings):
```

La función deberá generar una nueva matriz con las mismas dimensiones que `RATINGS`.

Para cada posición:

- si el estudiante ya calificó ese tema, colocar `0`;
- si el estudiante todavía no calificó el tema, colocar el **rating promedio correspondiente a esa canción**.

El procedimiento esperado puede pensarse como:

```text
RATINGS
   │
   ▼
trasponer()
   │
   ▼
RATINGS_T
   │
   ▼
calcular_ratings_avg()
   │
   ▼
ratings_avg
   │
   ▼
predicciones_popularidad
```

---

# Parte 9 — Ejecutar y analizar

Una vez completadas todas las funciones, ejecutar:

```python
main()
```

El programa deberá mostrar:

1. la matriz original de ratings;
2. la matriz de predicciones aleatorias;
3. la matriz de predicciones basadas en popularidad.

Comparen ambas matrices.

Analicen:

- ¿qué información utiliza `predicciones_random`?
- ¿qué información utiliza `predicciones_popularidad`?
- ¿por qué la segunda estrategia puede considerarse una mejora?
- ¿qué sucede con un tema que todavía no recibió ninguna calificación?
- ¿qué ventajas tiene trabajar con funciones independientes para cada operación?

---

# Trabajo colaborativo con Git y GitHub

## 1. Crear el repositorio local

Un integrante del equipo actuará inicialmente como responsable del repositorio.

Crear una carpeta para el proyecto e ingresar a ella:

```bash
mkdir sistema-recomendacion
cd sistema-recomendacion
```

Inicializar Git:

```bash
git init
```

Copiar dentro de la carpeta el archivo:

```text
_3_sis_rec_part_1.py
```

Agregarlo al repositorio:

```bash
git add .
```

Realizar el primer commit:

```bash
git commit -m "Agrega codigo base del sistema de recomendacion"
```

---

## 2. Crear el repositorio en GitHub

El representante deberá:

1. ingresar a GitHub;
2. seleccionar **New repository**;
3. crear un repositorio para el equipo;
4. no agregar nuevos archivos si ya existe el proyecto local;
5. copiar la URL del repositorio.

Luego asociar el repositorio local con GitHub:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Verificar:

```bash
git remote -v
```

Subir la rama principal:

```bash
git branch -M main
git push -u origin main
```

---

## 3. Agregar colaboradores

Desde GitHub:

```text
Settings
→ Collaborators
→ Add people
```

Agregar a todos los integrantes del equipo utilizando sus usuarios de GitHub.

Cada integrante deberá aceptar la invitación.

---

## 4. Crear la rama de desarrollo

El representante deberá crear una rama:

```bash
git checkout -b develop
```

Subirla a GitHub:

```bash
git push -u origin develop
```

La implementación de la práctica deberá realizarse sobre:

```text
develop
```

y no directamente sobre `main`.

---

## 5. Incorporarse al proyecto

El resto de los integrantes deberá clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta:

```bash
cd sistema-recomendacion
```

Cambiar a la rama de desarrollo:

```bash
git checkout develop
```

Antes de comenzar a trabajar deberán actualizar el repositorio:

```bash
git pull origin develop
```

---

## 6. Desarrollo colaborativo

El equipo deberá distribuir las funciones entre sus integrantes.

Por ejemplo:

```text
mostrar_matriz()
generar_predicciones_random()
generar_matriz_nula()
trasponer()
calcular_ratings_avg()
generar_predicciones_popularidad()
```

Cada integrante deberá realizar commits descriptivos.

Por ejemplo:

```bash
git add .
git commit -m "Implementa transposicion de matrices"
```

Luego subir los cambios:

```bash
git push origin develop
```

Antes de comenzar una nueva modificación se recomienda ejecutar:

```bash
git pull origin develop
```

para obtener los últimos cambios realizados por el resto del equipo.

---

# Resultado esperado

Al finalizar la práctica el equipo deberá contar con:

- todas las funciones implementadas;
- el programa ejecutándose correctamente;
- una matriz de predicciones aleatorias;
- una matriz de predicciones basada en popularidad;
- un repositorio Git;
- un repositorio remoto en GitHub;
- todos los integrantes agregados como colaboradores;
- una rama `main`;
- una rama `develop`;
- evidencia de participación mediante commits de los diferentes integrantes.

La rama `develop` deberá contener la versión funcional resultante de la práctica.