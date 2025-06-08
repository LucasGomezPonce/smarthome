from utils import generar_id_dispositivo
from lista_dispositivos import dispositivos
def menu_agregar_dispositivo():
    
    nombre = input("Ingrese el nombre del nuevo dispositivo: ").lower().strip()

    esencial = input("¿Es un dispositivo esencial?(SI/NO): ").lower().strip()

    encendido = input("¿El dispositivo esta encendido?(SI/NO): ").lower().strip()

    salida_bucle = input(
            "¿Desea agregar otro dispositivo?(SI/NO): ").lower().strip()
    
    return nombre, esencial, encendido, salida_bucle

def agregar_dispositivo(dispositivos):
    contador_agregado = 0
    while True:

        nombre, esencial, encendido, salida_bucle = menu_agregar_dispositivo()

        id = generar_id_dispositivo(dispositivos)

        if nombre == "":
            print("Error el nombre no puede estar vacio. ")
            continue

        if nombre.isdigit():
            print("Error ha ingreasdo un numero. ")
            continue

        if esencial == "si":
            tipo = "esencial"
        elif esencial == "no":
            tipo = "no_esencial"
        else:
            print("Error debe colocar (SI/NO). ")
            continue

        if encendido == "si":
            estado = "encendido"
        elif encendido == "no":
            estado = "apagado"
        else:
            print("Error debe colocar (SI/NO): ")
            continue

        dispositivo_agregado = {
            "id": id, "nombre": nombre, "tipo": tipo, "estado": estado}

        dispositivos.append(dispositivo_agregado)
        contador_agregado += 1
        

        if salida_bucle == "no":
            break
        if salida_bucle == "" :
            break

    if contador_agregado == 1:
        print("Nuevo dispositivo agregado: ")
    else:
        print("Nuevos dispositivos agregados: ")
    for dispositivo in dispositivos[-contador_agregado:]:
        print(
            f"ID: {dispositivo['id']} - Nombre: {dispositivo['nombre']} - Tipo: {dispositivo['tipo']} - Estado: {dispositivo['estado']}")

    return
    # FRANCO
    # solicita datos al usuario y agrega un nuevo dispositivo a la lista.
    # CORRECCIONES: QUITAR LOS PRINT E INPUT Y PONERLOS COMO DATOS DE ENTRADA O PARAMETROS


def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("Dispositivos registrados:")
        for dispositivo in lista_dispositivos:
            print(
                f"ID: {dispositivo['id']} - Nombre: {dispositivo['nombre']} - Tipo: {dispositivo['tipo']} - Estado: {dispositivo['estado']}")


def buscar_dispositivos(valor_buscado):
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == valor_buscado.lower():
            return dispositivo
        elif valor_buscado.isdigit() and int(dispositivo["id"]) == int(valor_buscado):
            return dispositivo
    return None
    # SERGIO
    # permite buscar un dispositivo por ID o nombre.
    # #CORRECCIONES: QUITAR LOS PRINT E INPUT Y PONERLOS COMO DATOS DE ENTRADA O PARAMETROS


def eliminar_dispositivos(dispositivos, eliminar, id_a_eliminar):
    
    if eliminar.lower() == "si":
        for i, dispositivo in enumerate(dispositivos):
            if dispositivo["id"] == id_a_eliminar:
                del dispositivos[i]
                return True  # Eliminado correctamente
        return False  # No se encontró el dispositivo
    else:
        return False  # No se pudo eliminar
    
    # VALENTINO
    # elimina un dispositivo existente.
    # #CORRECCIONES: QUITAR LOS PRINT E INPUT Y PONERLOS COMO DATOS DE ENTRADA O PARAMETROS
