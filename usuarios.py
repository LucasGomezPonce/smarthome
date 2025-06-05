import json
import os

archivo = "usuarios.json"


def registrar_usuario(nombre, usuario, clave, rol):

    usuarios = json.load(open(archivo)) if os.path.exists(archivo) else []

    usuarios.append({
        "nombre": nombre,
        "usuario": usuario,
        "clave": clave,
        "rol": rol
    })

    with open(archivo, "w") as f:
        json.dump(usuarios, f, indent=2)
    # registrar usuario de acuerdo a su nombre, usuario, clave y rol, pasar datos como parametro
    #LUCAS


def iniciar_sesion(usuario, clave):
    if not os.path.exists(archivo):
        return None
    usuarios = json.load(open(archivo))
    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == clave:
            return u
    return None
    # Usar datos de archivo json, mostrando el menu correspondiente si es usuario estandar o admin, pasar datos como parametro
    # LUCAS


def cambiar_rol_usuario():
    # opcion valida solo para administrador, puede cambiar a usuarios estandar a administrador, se puede crear una funcion para listar a todos los usuarios, pasar datos como parametro
    #VALENTINO
    pass


def obtener_usuario_por_nombre():
    # muestra datos del usuario, pasar datos como parametro
    #SERGIO 
    pass
