"""
Consigna:
Un cliente necesita desarrollar un programa en Python
para gestionar la información de los recitales realizados en un festival de música.

1. cargar bandas
generar la función cargar_bandas() con los siguientes requerimientos:
a. el usuario ingresa el nombre de la banda
b. el programa genera de forma random entradas_vendidas y monto_recaudado de la banda
c. los datos se almacenan en una matriz
d. la carga finaliza con -1

2. visualizar datos
generar la función mostrar_bandas() que imprime en consola las bandas ingresadas
y las métricas simuladas

3. ordenar los datos
generar la funcion ordenar_bandas() que ordena la matriz por monto recaudado descendiente

"""

import random


def cargar_bandas():
    bandas = []
    nombre_banda = None
    nombre_banda = input("Ingrese el nombre de la banda: ")
    while nombre_banda != "-1":
        if not nombre_banda:
            print("No se admite campo vacío")
            nombre_banda = input("Ingrese el nombre de la banda: ")
            continue
        entradas_vendidas = random.randint(1000, 1500)
        precio_promedio = random.randint(150, 300)
        monto_recaudado = entradas_vendidas * precio_promedio
        banda = [nombre_banda, entradas_vendidas, monto_recaudado]
        bandas.append(banda)
        nombre_banda = input("Ingrese el nombre de la banda: ")
    return bandas


def mostrar_bandas(bandas):
    for banda in bandas:
        print(banda)


def ordenar_bandas_burbujeo(bandas):
    bandas_sorted = bandas.copy()
    n = len(bandas_sorted)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if bandas_sorted[j][2] < bandas_sorted[j + 1][2]:
                aux = bandas_sorted[j]
                bandas_sorted[j] = bandas_sorted[j + 1]
                bandas_sorted[j + 1] = aux
    return bandas_sorted


def ordenar_bandas_sorted(bandas):
    bandas_sorted = sorted(bandas, key=lambda banda: banda[1], reverse=True)
    return bandas_sorted


def main():
    # Cargar bandas
    bandas = cargar_bandas()

    if not bandas:
        print("No hay bandas registradas")
        return

    # Mostrar bandas ingresadas
    print("Bandas ingresadas: ")
    mostrar_bandas(bandas)
    # Ordenar datos
    print("Bandas ordenadas por entradas vendidas: ")
    mostrar_bandas(ordenar_bandas_burbujeo(bandas))


if __name__ == "__main__":
    main()
