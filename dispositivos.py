from utils import generar_id_dispositivo

def agregar_dispositivo(dispositivos):

    while True:
 
        id = generar_id_dispositivo(dispositivos)
        
        nombre = input("Ingrese el nombre del nuevo dispositivo: ").lower()
        if nombre == "" :
            print("Error el nombre no puede estar vacio. ")
            continue
        
        elif nombre.isdigit():
            print("Error ha ingreasdo un numero. ")
            continue
    
        tipo_rta = input("¿Es un dispositivo esencial?(SI/NO): ").lower()
        if tipo_rta == "si" :
            tipo = "esencial"
        elif tipo_rta == "no" :
            tipo = "no_esencial"
        else:    
            print("Error debe colocar (SI/NO). ")
            continue

        estado_rta = input("¿El dispositivo esta encendido?(SI/NO): ").lower()
        if estado_rta == "si" :
            estado = "encendido"
        elif estado_rta == "no" :
            estado = "apagado"
        else:    
            print("Error debe colocar (SI/NO): ")
            continue

        dispositivo_agragado = {"id": id, "nombre": nombre, "tipo": tipo, "estado": estado }

        dispositivos.append(dispositivo_agragado)

        salida_bucle = input("¿Desea agregar otro dispositivo?(SI/NO): ").lower()
        if salida_bucle == "no" :
            break 

    
    print("Nuevo dispositivo agregado: ")    

    for dispositivo in dispositivos:
        if dispositivo == dispositivos[-1]:
            print(f"ID: {dispositivo['id']} - Nombre: {dispositivo['nombre']} - Tipo: {dispositivo['tipo']} - Estado: {dispositivo['estado']}")
            break
    
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
