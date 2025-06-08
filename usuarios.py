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


def cambiar_rol_usuario(numero_usuario):

    f = open("usuarios.json", "r")
    texto = f.read()
    f.close()

    usuarios = json.loads(texto)

    pos = numero_usuario - 1
    if 0 <= pos < len(usuarios):
        if usuarios[pos]["rol"] == "admin":
            usuarios[pos]["rol"] = "estandar"
        else:
            usuarios[pos]["rol"] = "admin"
        f = open("usuarios.json", "w")
        f.write(json.dumps(usuarios, indent=2))
        f.close()
        return True
    else:
        return False
    
    # opcion valida solo para administrador, puede cambiar a usuarios estandar a administrador, se puede crear una funcion para listar a todos los usuarios, pasar datos como parametro
    #VALENTINO

def obtener_usuario_por_nombre(nombre_usuario ,identificador, datos_a_mostrar):
        
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
    if identificador in ['nombre','usuario']:
        usuario = next((usuario for usuario in usuarios if usuario[identificador] == nombre_usuario), "Usuario no encontrado")

    if usuario and datos_a_mostrar:

        usuario_filtrado = {dato: usuario[dato] for dato in datos_a_mostrar if dato in usuario}
        return usuario_filtrado
    else:
        return usuario  # Devuelve el usuario completo si no se especifican campos
    
    # muestra datos del usuario, pasar datos como parametro
    #OCTAVIO

if __name__ == "__main__":
   print(obtener_usuario_por_nombre("lucas gomez ponce",'nombre', {'usuario'}))
