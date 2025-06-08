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

def imprimir_valores (directorio, claves=None):
    #imprime los valores de un directorio con sus claves en forma de lista
    for clave in claves:
        if clave in directorio:
            valor = directorio[clave]
        print(f"- {clave.capitalize():<10}: {valor}")
