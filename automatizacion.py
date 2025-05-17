from utils import filtrar_lista
from dispositivos import listar_dispositivos

def activar_modo_ahorro(lista_dispositivos):
    contador = 0
<<<<<<< HEAD
    while contador in range (len(lista_dispositivos)):
=======
    while contador in  range (len(lista_dispositivos)):
>>>>>>> 2d5c204ff9f36512f60b9a515fa9d59c281ad648
        dispositivo = lista_dispositivos[contador]
        if dispositivo["tipo"] == "no_esencial":
            dispositivo["estado"] = "apagado"
        contador += 1
<<<<<<< HEAD
    print("\n Modo 'Ahorro de Energia' Activado \n")
=======
    print("\n Modo 'Ahorro de energia' Activado \n")
>>>>>>> 2d5c204ff9f36512f60b9a515fa9d59c281ad648
    #Octavio
    # apaga todos los dispositivos no esenciales.
    # O, si elegís otra automatización(por ejemplo, “modo noche”), una función que aplique esa lógica.


def reglas_de_automatizacion(lista_dispositivos):
    print ("\n al activar el modo 'Ahorro de Energia' se desactivaran los dispositivos  de tipo no escenciales:\n")
    listar_dispositivos (filtrar_lista(lista_dispositivos, "tipo" , "no_esencial"))
    #Octavio
    # indicar los dispositivos a apagarse 
