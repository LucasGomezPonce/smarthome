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


def generar_id_dispositivo(dispositivos):

    ultimo_id = dispositivos[-1]["id"]
    nuevo_id = ultimo_id + 1

    return nuevo_id


def filtrar_lista(lista, clave, valor):
 # toma una lista de directorios y la filtra segun una su clave y valor por el que lo hacemos
    contador = 0
    lista_filtrada = []
    while contador in range(len(lista)):
        dispositivo = lista[contador]
        if dispositivo[clave] == valor:
            lista_filtrada.append(dispositivo["nombre"])
        contador += 1
    return lista_filtrada


if __name__ == "__main__":
    lista = filtrar_lista(dispositivos, "tipo", "no_esencial")
    print(lista)
