import src.interface as interface
def crear_usuario(usuarios):
    """
    Da de alta un usuario.
    Se encarga de colectar los campos de la terminal
    Validarlos
    Arma un diccionario y lo guarda en la lista global usuarios
    Retorna True:False
    """
    id_usuario = interface.get_id_usuario()
    nombre = interface.get_nombre()
    email = interface.get_email()
    usuario = {
        "id_usuario" : id_usuario,
        "nombre": nombre,
        "email": email
    }
    usuarios.append(usuario)
    

def buscar_usuario_por_id(usuarios):
    """
    Solicita el id del usuario a buscar
    retorna el diccionario del usuario o None
    """
    id_usuario = interface.get_id_usuario()
    return next((u for u in usuarios if u["id_usuario"]==id_usuario), None)