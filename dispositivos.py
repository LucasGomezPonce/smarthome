from utils import generar_id_dispositivo


def agregar_dispositivo(dispositivos):
    contador_agregado = 0
    while True:

        id = generar_id_dispositivo(dispositivos)

        nombre = input("Ingrese el nombre del nuevo dispositivo: ").lower()
        if nombre == "":
            print("Error el nombre no puede estar vacio. ")
            continue

        elif nombre.isdigit():
            print("Error ha ingreasdo un numero. ")
            continue

        tipo_rta = input("¿Es un dispositivo esencial?(SI/NO): ").lower()
        if tipo_rta == "si":
            tipo = "esencial"
        elif tipo_rta == "no":
            tipo = "no_esencial"
        else:
            print("Error debe colocar (SI/NO). ")
            continue

        estado_rta = input("¿El dispositivo esta encendido?(SI/NO): ").lower()
        if estado_rta == "si":
            estado = "encendido"
        elif estado_rta == "no":
            estado = "apagado"
        else:
            print("Error debe colocar (SI/NO): ")
            continue

        dispositivo_agragado = {
            "id": id, "nombre": nombre, "tipo": tipo, "estado": estado}

        dispositivos.append(dispositivo_agragado)
        contador_agregado -= 1
        salida_bucle = input(
            "¿Desea agregar otro dispositivo?(SI/NO): ").lower()

        if salida_bucle == "no":
            break
    if contador_agregado == -1:
        print("Nuevo dispositivo agregado: ")
    else:
        print("Nuevos dispositivos agregados: ")
    for i in range(contador_agregado, 0):
        ultimo_dispositivo = dispositivos[i]
        print(
            f"ID: {ultimo_dispositivo['id']} - Nombre: {ultimo_dispositivo['nombre']} - Tipo: {ultimo_dispositivo['tipo']} - Estado: {ultimo_dispositivo['estado']}")

    return dispositivos
    # Franco
    # solicita datos al usuario y agrega un nuevo dispositivo a la lista.


def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("Dispositivos registrados:")
        for dispositivo in lista_dispositivos:
            print(
                f"ID: {dispositivo['id']} - Nombre: {dispositivo['nombre']} - Tipo: {dispositivo['tipo']} - Estado: {dispositivo['estado']}")


def buscar_dispositivos(dispositivos):
    valor_buscado = ""
    while len(valor_buscado) == 0:
        valor_buscado = input(
            "\nIngrese el id o nombre del dispositivo a buscar: ").strip()
    se_encontro = False

    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == valor_buscado.lower():
            se_encontro = True
            break
        elif valor_buscado.isdigit() and int(dispositivo["id"]) == int(valor_buscado):
            se_encontro = True
            break

    if se_encontro:
        print("\n-----Dispositivo Encontrado-----")
        print(
            f"ID: {dispositivo['id']} - Nombre: {dispositivo['nombre']} - Tipo: {dispositivo['tipo']} - Estado: {dispositivo['estado']}")
    else:
        print(
            f"\nNo fue encontrado ningún dispositivo que coincida con el id o nombre ingresado ({valor_buscado})")
    # Mauricio
    # permite buscar un dispositivo por ID o nombre.


def eliminar_dispositivos(dispositivos):
    elim = input("Desea eliminar un dispositivo (SI/NO):")

    if elim.lower() == "si":
        try:
            id_buscar = int(
                input("Ingrese el ID del dispositivo a eliminar: "))
            for i, dispositivo in enumerate(dispositivos):
                if dispositivo["id"] == id_buscar:

                    print(dispositivos[i])
                    del dispositivos[i]
                    print(f"Dispositivo eliminado")
                    return dispositivos
            print("No se encontro el dispositivo.")
        except:
            print("ERROR, el dato a ingresar debe ser numerico")
    else:
        print("No se elimina ningun dispositivo.")
    return dispositivos

    # Valentino
    # elimina un dispositivo existente.


