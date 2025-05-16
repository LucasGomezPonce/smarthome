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


def eliminar_dispositivos():
    elim = input("Desea eliminar un dispositivo? (s/n): ")
    
    if elim.lower() == "s":
        try:
            id_buscar = int(input("Ingrese el ID del dispositivo a eliminar: "))
            for i, dispositivos in enumerate(dispositivos):
                if dispositivos["id"] == id_buscar:
                    del dispositivos[i]
                    print("Dispositivo eliminado")
                    return dispositivos
            print("No se encontró el dispositivo")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    else:
        print("No se eliminará ningún dispositivo")
    return dispositivos
   
    # Valentino
    # elimina un dispositivo existente.
