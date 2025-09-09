def dividir_1(numerador, denominador):
    try:
        a = int(numerador)
        b = int(denominador)
        return a / b
    except ZeroDivisionError:
        print("¡Error! No puedes dividir por cero.")


def suma(num, cadena):
    try:
        a = int(num)
        b = str(cadena)
        return a + b
    except TypeError:
        print("¡Error! No puedes sumar un número y una cadena directamente.")


def clave_diccionario(diccionario, key):
    try:
        return diccionario[key]
    except KeyError:
        print(f"¡Error! La clave '{key}' no existe en el diccionario.")


def buscar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r"):
            print(f"El archivo '{nombre_archivo}' fue abierto exitosamente.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. Creándolo ahora...")
        try:
            with open(nombre_archivo, "w") as nuevo_archivo:
                nuevo_archivo.write(
                    "Este es un archivo de prueba creado automáticamente."
                )
            print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")
        except IOError as e:
            print(f"¡Error al intentar crear el archivo! Detalles: {e}")


def dividir_2(numerador, denominador):
    try:
        num = float(numerador)
        den = float(denominador)
        resultado = num / den
    except (ZeroDivisionError, ValueError) as e:
        print("¡Ha ocurrido un error!")
        if isinstance(e, ZeroDivisionError):
            print("El error específico es: No puedes dividir por cero.")
        elif isinstance(e, ValueError):
            print("El error específico es: La entrada no es un número válido.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    else:
        print(f"El resultado de la división es: {resultado}")
