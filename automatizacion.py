from utils import filtrar_lista
from dispositivos import listar_dispositivos


def activar_modo_ahorro(lista_dispositivos):
    contador = 0
    while contador in range(0, len(lista_dispositivos)):
        dispositivo = lista_dispositivos[contador]
        if dispositivo["tipo"] == "no_esencial":

            dispositivo["estado"] = "apagado"
        contador += 1
    print("\n Modo 'Ahorro de Energia' activado \n")
    print(
        f"Dispositivos desactivados {filtrar_lista(lista_dispositivos, "tipo", "no_esencial")}")
    # Octavio
    # apaga todos los dispositivos no esenciales.
    # O, si elegís otra automatización(por ejemplo, “modo noche”), una función que aplique esa lógica.


def reglas_de_automatizacion(lista_dispositivos):
    print(
        f"\n Al activar el modo 'Ahorro de Energia' se desactivaran los dispositivos  de tipo no escenciales: {filtrar_lista(lista_dispositivos, "tipo", "no_esencial")}\n")
    # Octavio
    # indicar los dispositivos a apagarse
