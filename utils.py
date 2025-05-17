def generar_id_dispositivo(dispositivos):
    
    ultimo_id = dispositivos[-1]["id"] 
    nuevo_id = ultimo_id + 1     
    
    return nuevo_id


def mostrar_mensaje_error():
    pass
    # para centralizar los errores.


if __name__ == "__main__":
    print(generar_id_dispositivo())
