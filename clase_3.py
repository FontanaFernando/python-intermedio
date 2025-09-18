# Calcular Mayor
def numero_mayor(num1, num2):
    return num1 if num1 > num2 else num2

try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))

    print(f"El numero mayor es: {numero_mayor(num1, num2)}")

except ValueError:
    print("Error! ingrese numeros enteros")


# Buscar Palabra
def buscar_palabra(palabra_a_buscar, *lista_de_palabras):
    for palabra in lista_de_palabras:
        if palabra_a_buscar == palabra:
            return f"La palabra < {palabra_a_buscar} > fue encontrada"
    return f"La palabra < {palabra_a_buscar} > no existe en esta lista"

try:
    palabra_buscada = input("Ingrese la palabra que desae buscar: ")
    lista_de_palabras = ("python", "foo", "bar", "hola", "argumento", "Sol", "Flor", "Juan", "Juli",)
    resultado = buscar_palabra(palabra_buscada, *lista_de_palabras)
    print(resultado)
except ValueError:
    print("Error! Ingrese una palabra")


# Par o Impar
def es_par (num):
    return num % 2 == 0

try:
    num = int(input("Ingrese un numero: "))
    print(f"el numero {num} es par" if es_par(num) else f"el numero {num} es impar")

except ValueError:
    print("Error! ingrese numeros enteros")


# Calcular Promedio
def promedio(*numeros):
    return sum(numeros) / len(numeros) if numeros else "Error: No se pasaron suficientes argumentos"

print(promedio(1, 2, 3, 4, 5))
print(promedio())