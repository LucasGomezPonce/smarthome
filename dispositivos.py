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


def eliminar_dispositivo():
    pass
    elim = input("que ")
    # Valentino
    # elimina un dispositivo existente.
