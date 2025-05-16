def agregar_dispositivo():
    pass
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


def buscar_dispositivo():
    pass
    # Mauricio
    # permite buscar un dispositivo por ID o nombre.


def eliminar_dispositivos(dispositivos):
    elim = input("Desea eliminar un dispositivo (s/n):")

    if elim.lower() == "s":
            id_buscar = int(input("Ingrese el ID del dispositivo a eliminar: "))
            for i, dispositivo in enumerate(dispositivos):
                if dispositivo["id"] == id_buscar:
                    del dispositivos[i]  
                    print("Dispositivo eliminado")
                    return dispositivos
            print("No se encontro el dispositivo.")
    else:
        print("No se elimina ningun dispositivo.")
    return dispositivos

    # Valentino
    # elimina un dispositivo existente.
