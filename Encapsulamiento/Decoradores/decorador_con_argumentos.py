# Definimos un decorador que acepta una lista variable de roles como argumentos
def roles_requeridos(*roles):
    # El decorador real que envuelve la función
    def decorador(funcion):
        # El wrapper que se ejecuta antes de la función original
        def wrapper(usuario, *args, **kwargs):
            # Verifica si el usuario tiene alguno de los roles requeridos
            if usuario["rol"] in roles:
                # Si tiene los roles requeridos, ejecuta la función original con los argumentos recibidos
                return funcion(usuario, *args, **kwargs)
            else:
                # Si no tiene los roles requeridos, lanza una excepción
                raise PermissionError("Usuario no tiene los roles requeridos")

        # Devuelve el wrapper que contiene la lógica de verificación de roles
        return wrapper

    # Devuelve el decorador que envuelve la función original
    return decorador


# Simulamos un usuario con roles
usuario = {"nombre": "Juan", "rol": "admin"}


# Definimos una función que requiere roles específicos para ejecutarse
@roles_requeridos("admin", "editor")
def editar_articulo(usuario, articulo_id, contenido):
    # Lógica para editar el artículo
    print(f"El usuario {usuario['nombre']} está editando el artículo {articulo_id} con contenido: {contenido}")


# Intentamos editar un artículo con el usuario simulado
try:
    editar_articulo(usuario, 123, "Nuevo contenido del artículo")
except PermissionError as e:
    # Capturamos la excepción si el usuario no tiene los roles requeridos
    print(f"No se pudo editar el artículo: {e}")
