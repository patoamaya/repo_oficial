AUD1 = [
    [30,  40,  55,  50,  35, 25],
    [35,  90, 170, 180,  80, 30],
    [40, 150, 230, 220, 140, 35],
    [25,  45,  70,  65,  40, 20]
]


def gen_matriz_nula(n_filas, n_columnas):
    matriz_nula = []
    # Completar
    return matriz_nula

def gen_binaria(matriz, umbral):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    matriz_binaria = gen_matriz_nula(n_filas, n_columnas)
    for i in range(n_filas):
        for j in range(n_columnas):
            # Completar
    return matriz_binaria


def gen_mirror_vertical(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    mirror_vertical = gen_matriz_nula(n_filas, n_columnas)
    for i in range(n_filas):
        for j in range(n_columnas):
            mirror_vertical[i][j] = matriz[n_filas-1-i][j]
    return mirror_vertical

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def procesar_AUD1():
    matriz = AUD1
    print(f"\nMatriz original")
    mostrar_matriz(matriz)

    matriz_negativo = gen_binaria(matriz, 128)
    print(f"\nMatriz negativo")
    mostrar_matriz(matriz_negativo)

    matriz_mirror_horizontal = gen_mirror_vertical(matriz)
    print(f"\nMatriz mirror horizontal")
    mostrar_matriz(matriz_mirror_horizontal)
