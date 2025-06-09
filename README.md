#  SmartHome Solutions – Sistema Básico de Gestión de Dispositivos

Este proyecto es una simulación de un sistema para la gestión de dispositivos inteligentes dentro del hogar. El objetivo es desarrollar funcionalidades básicas en consola utilizando programación orientada a objetos y estructuras de datos (diccionarios y listas), en colaboración entre distintos integrantes del equipo.

---

##  División de Tareas

### 🔹 Lucas – Menú principal y listado de dispositivos
- Diseña e implementa un menú interactivo para que el usuario pueda acceder a las diferentes funciones del sistema.
- Muestra en pantalla todos los dispositivos registrados en una lista de diccionarios, incluyendo sus detalles.

#### Segunda etapa:
- Inplementar un	Sistema de registro e inicio de sesión haciendo uso de un archivo json

### 🔹 Franco – Agregar dispositivos y generar ID
- Implementa la función para registrar nuevos dispositivos.
- Cada dispositivo debe tener un identificador único (ID) autogenerado.
- Los datos se almacenan como diccionarios dentro de una lista general de dispositivos.

#### Segunda etapa:
- Aplicar pequeñas correciones al codigo

### 🔹 Sergio Mauricio – Búsqueda por ID o nombre
- Desarrolla funciones para buscar un dispositivo específico mediante:
  - Su ID único
  - Su nombre
- Devuelve los datos del dispositivo encontrado o un mensaje de error si no existe.

#### Segunda etapa:
- Aplicar pequeñas correciones al codigo

### 🔹 Valentino – Eliminación de dispositivos
- Permite eliminar dispositivos de la lista principal utilizando:
  - Su ID
  - Su nombre
- Confirma la eliminación o informa si no se encontró el dispositivo.

#### Segunda etapa:
- Aplicar pequeñas correciones al codigo + realizar la funcion cambiar_rol_usuario

### 🔹 Octavio – Modo Ahorro de Energía
- Desarrolla la automatización que apaga automáticamente todos los dispositivos no esenciales cuando se activa el “Modo Ahorro”.
- Puede trabajar con un atributo adicional dentro del diccionario para marcar dispositivos como esenciales o no.

#### Segunda etapa:
- Aplicar pequeñas correciones al codigo + mostrar datos del usuario mediante la funcion obtener_usuario_por_nombre
---


