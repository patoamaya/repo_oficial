from Primer_parcial.estudiante_matrices_primer_parcial import procesar_AUD1

# ============================================================
# Estructura de datos para entidad rover
# ============================================================

ROVER_AUDACITY =
ROVER_LEGACY =  
rovers = 

# ============================================================
# UTILIDADES
# ============================================================

def validar_file_name(file_name):
    if not file_name.strip():
        return
    length = len(file_name) # Completar...
    # Completar...

    return length and upper and number and extension == "png"


def enmascarar(auth_code):
    return auth_code[:-4] + "****"


def buscar_rover_por_id(id_rover): 
    for i in range(rovers): 
        if rovers[i][0] == id_rover: 
            return rovers[i][1] 
    return None 

# ============================================================
# CRUD DE IMAGE
# ============================================================

def crear_imagen():
    id_image = gen_id_image()

    file_name = input("Ingrese el nombre de la imagen: ").strip()
    while not validar_fila_name(file_name):
        print("El nombre de la imagen no cumple con los requerimientos. Intente nuevamente...")
        file_name = input("Ingrese el nombre de la imagen: ").strip()

    access_code = input("Ingrese el código de acceso: ").strip()
    target = input("Ingrese el target de la imagen: ").strip()
    id_rover = input("Ingrese el id del rover: ").strip()

    # Guardar datos
    print("Imagen creada exitosamente!")


def mostrar_imagenes():
    print("\n--- Imagenes registrados ---")
    print(f"File Name | Access Code | Target | Rover Name") 
    # Iterar la lista imagenes 
    # file_name y target se muestran sin transformaciones 
    # access_code se enmascara con enmascarar() 
    # rover_name se obtiene con buscar_rover_por_id(id_rover) 


def main():
    """Función principal con menú interactivo."""
    while True:
        print("\n  --- Gestión de Imagenes ---")
        print("  1. Crear imagen")
        print("  2. Ver imagenes")
        print("  3. Eliminar imagen")
        print("  0. Volver")

        opcion = input("\n  Opción: ").strip()
        if opcion == "1":
            crear_imagen()
        elif opcion == "2":
            mostrar_imagenes()
        elif opcion == "3":
            eliminar_imagen()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
