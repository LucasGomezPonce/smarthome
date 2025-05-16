from dispositivos import listar_dispositivos
from dispositivos import eliminar_dispositivos
dispositivos = [
    {"id": 1, "nombre": "Luz living", "tipo": "no_esencial", "estado": "apagado"},
    {"id": 2, "nombre": "Televisor", "tipo": "no_esencial", "estado": "encendido"},
    {"id": 3, "nombre": "Heladera", "tipo": "esencial", "estado": "encendido"},
    {"id": 4, "nombre": "Aire acond", "tipo": "no_esencial", "estado": "apagado"},
    {"id": 5, "nombre": "Cámaras", "tipo": "esencial", "estado": "encendido"},
    {"id": 6, "nombre": "Cafetera", "tipo": "no_esencial", "estado": "apagado"},
    {"id": 7, "nombre": "Calefactor", "tipo": "no_esencial", "estado": "apagado"},
    {"id": 8, "nombre": "Router WiFi", "tipo": "esencial", "estado": "encendido"},
    {"id": 9, "nombre": "Lavarropas", "tipo": "no_esencial", "estado": "apagado"},
]


def mostrar_menu_principal():
    print("\n¿Qué desea hacer?")
    print("1. Gestión de dispositivos")
    print("2. Automatizaciones")
    print("3. Salir\n")


def mostrar_menu_dispositivos():
    print("\nGestión de dispositivos:")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Volver al menú principal")


def mostrar_menu_automatizaciones():
    print("\nAutomatizaciones disponibles:")
    print("1. Activar modo ahorro de energía")
    print("2. Ver reglas de automatización")
    print("3. Volver al menú principal")


def gestionar_dispositivos():
    while True:
        mostrar_menu_dispositivos()
        op = input("Seleccione una opcion: ")

        if op == "1":
            print("Funcion agregar dispositivos")
            pass
        elif op == "2":
            print("Funcion listar dispositivos\n")
            listar_dispositivos(dispositivos)

        elif op == "3":
            print("Funcion buscar dispositivo")
        elif op == "4":
            print("Funcion eliminar dispositivo")
            eliminar_dispositivos(dispositivos)
        elif op == "5":
            menu()
        else:
            print("Opcion inorrecta")


def gestionar_automatizacion():
    while True:
        mostrar_menu_automatizaciones()
        op = input("Seleccione una opcion: ")

        if op == "1":
            print("Funcion modo ahorro de energia")

        elif op == "2":
            print("Reglas de automatización")

        elif op == "3":
            menu()
        else:
            print("Opcion inorrecta")


def menu():
    mostrar_menu_principal()

    while True:
        op = input("Seleccione una opcion: ")
        if op == "1":
            gestionar_dispositivos()
        elif op == "2":
            gestionar_automatizacion()
        elif op == "3":
            break
        else:
            print("Opcion inorrecta")


if __name__ == "__main__":
    menu()
