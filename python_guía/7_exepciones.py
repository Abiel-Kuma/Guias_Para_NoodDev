# Excepciones

# Las excepciones en Python son errores detectados durante la ejecución del programa.
# El manejo de excepciones permite controlar el flujo del programa cuando ocurren errores,
# evitando que el programa termine abruptamente.

# Manejo Básico de Excepciones
# En Python, las excepciones se manejan usando las palabras clave `try`, `except`, `else`, y `finally`.

# Ejemplo básico:
try:
    # Código que podría generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción de tipo ZeroDivisionError
    print("Error: No se puede dividir entre cero.")

# Salida:
# Error: No se puede dividir entre cero.

# Múltiples Except
# Se pueden manejar diferentes tipos de excepciones utilizando múltiples cláusulas `except`.

# Ejemplo:
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Entrada inválida. Debes ingresar un número.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# Salida si se ingresa texto no numérico:
# Error: Entrada inválida. Debes ingresar un número.

# Salida si se ingresa 0:
# Error: No se puede dividir entre cero.

# Cláusula `else`
# La cláusula `else` se ejecuta si el bloque `try` no genera ninguna excepción.

# Ejemplo:
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")

# Salida si no ocurre ninguna excepción:
# Ingresa un número: 2
# El resultado es: 5.0

# Cláusula `finally`
# La cláusula `finally` se ejecuta siempre, ocurra o no una excepción.
# Es útil para realizar tareas de limpieza, como cerrar archivos o liberar recursos.

# Ejemplo:
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
finally:
    archivo.close()  # Se ejecuta siempre, independientemente de si ocurrió una excepción
    print("El archivo ha sido cerrado.")

# Salida:
# Error: El archivo no fue encontrado.
# El archivo ha sido cerrado.

# Lanzar Excepciones
# Se pueden lanzar excepciones manualmente utilizando la palabra clave `raise`.

# Ejemplo:
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Salida:
# Error: El divisor no puede ser cero.

# Excepciones Personalizadas
# Puedes crear tus propias excepciones personalizadas creando una clase que herede de `Exception`.

# Ejemplo:
class MiExcepcion(Exception):
    pass

def verificar_positivo(numero):
    if numero < 0:
        raise MiExcepcion("El número no puede ser negativo.")

try:
    verificar_positivo(-5)
except MiExcepcion as e:
    print(f"Error: {e}")

# Salida:
# Error: El número no puede ser negativo.
