from Primer_parcial.catedra_matrices_primer_parcial import procesar_aud1

# ============================================================
# DATOS INICIALES
# ============================================================

# ── Registro user admin
IMAGE = {
    "id_image": 1,
    "file_name": "AUD1.png",
    "access_code": "88888888",
    "target": "rock",
    "id_rover": 1,
}

# ── Entidad: usuarios (se gestiona con CRUD) ─
images = [IMAGE]

# ── Entidad: rover (hardcoded)
rovers = [{"id_rover": 1, "rover_name": "audacity"}, 
          {"id_rover": 2, "rover_name": "legacy"}]


# ============================================================
# UTILIDADES GENERALES CRUD IMAGE
# ============================================================

def gen_id_image():
    ids = [image["id_image"] for image in images]
    return max(ids) + 1

def validar_file_name(file_name):
    # 8 caracteres de minimo: length
    # el punto separa nombre de extension
    # nombre:
    # - 3 caracteres en mayúscula
    # - al menos 1 némero
    # extension:
    # "png"
    if not file_name.strip():
        return
    length = len(file_name) >= 8
    nombre, extension = file_name.split(".")
    n_upper = n_digit = 0

    for c in nombre:
        if c.isupper():
            n_upper += 1
        elif c.isdigit():
            n_digit += 1

    upper = n_upper == 3
    number = n_digit >= 1

    return length and upper and number and extension == "png"


def validar_access_code(access_code):
    return access_code.isdigit() and len(access_code) == 8


def validar_target(target):
    targets = ["terrain", "crater", "rock"]
    return target.lower() in targets


def buscar_rover_por_id(id_rover):
    for rover in rovers:
        if rover["id_rover"] == int(id_rover):
            return rover["rover_name"]
    return None


def validar_id_rover(id_rover):
    return id_rover.isdigit and buscar_rover_por_id(id_rover)


def buscar_image_por_id(id_image):
    for image in images:
        if image["id_image"] == id_image:
            return image
    return None


def enmascarar(auth_code):
    return auth_code[:-4] + "****"


# ============================================================
# CRUD DE IMAGE
# ============================================================

def crear_imagen():
    id_image = gen_id_image()

    file_name = input("Ingrese el nombre de la imagen: ").strip()
    while not validar_file_name(file_name):
        print("El nombre de la imagen no cumple con los requerimientos. Intente nuevamente...")
        file_name = input("Ingrese el nombre de la imagen: ").strip()

    access_code = input("Ingrese el código de acceso: ").strip()
    while not validar_access_code(access_code):
        print("El código de acceso no cumple con los requerimientos. Intente nuevamente...")
        access_code = input("Ingrese el código de acceso: ").strip()

    target = input("Ingrese el target de la imagen: ").strip()
    while not validar_target(target):
        print("No corresponde a ningún target permitido. Intente nuevamente...")
        target = input("Ingrese el target de la imagen: ").strip()
    
    id_rover = input("Ingrese el id del rover: ").strip()
    while not validar_id_rover(id_rover):
        print("El id_role ingresado en inválido. Intente nuevamente...")
        id_rover = input("Ingrese el id del rover: ").strip()

    # Construir el diccionario del usuario
    nueva_imagen = {
        "id_image": id_image,
        "file_name": file_name,
        "access_code": access_code,
        "target": target,
        "id_rover": int(id_rover),
    }

    images.append(nueva_imagen)
    print("Imagen agregada exitosamente!")


def mostrar_imagenes():
    print("\n--- Imagenes registrados ---")
    for image in images:
        print(f"file_name: {image["file_name"]}")
        print(f"access_code: {enmascarar(image["access_code"])}")
        print(f"target: {image["target"]}")
        print(f"rover: {buscar_rover_por_id(image["id_rover"])}")


def eliminar_imagen():
    print("\n--- Procesando eliminar imagen ---")
    id_image = int(input("Ingrese el ID de la imagen a eliminar: "))
    image = buscar_image_por_id(id_image)
    if not image:
        print(f"No se encontró ninguna imagen con ID {id_image}.")
        return
    access_code = input("Ingrese el código de acceso para confirmar: ").strip()
    while not validar_access_code(access_code):
        print("Código de acceso inválido. Intente nuevamente...")
        access_code = input("Ingrese el código de acceso para confirmar: ").strip()
    if image["access_code"] == access_code:
        images.remove(image)
        print(f"Imagen eliminada correctamente.")
    else:
        print("Código inválido - no se ha podido eliminar.")


def main():
    """Función principal con menú interactivo."""
    while True:
        print("\n  --- Gestión de Imagenes ---")
        print("  1. Crear imagen")
        print("  2. Ver imagenes")
        print("  3. Eliminar imagen")
        print("  4. Procesar imagen AUD1.png")
        print("  0. Terminar")

        opcion = input("\n  Opción: ").strip()
        if opcion == "1":
            crear_imagen()
        elif opcion == "2":
            mostrar_imagenes()
        elif opcion == "3":
            eliminar_imagen()
        elif opcion == "4":
            procesar_aud1()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
