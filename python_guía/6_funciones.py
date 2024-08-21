# Guía de Funciones en Python

# Las funciones en Python son bloques de código reutilizables que se pueden definir una vez y utilizar en varias partes del programa.

# Definición de Funciones
# Una función se define utilizando la palabra clave `def`, seguida por el nombre de la función y paréntesis `()`.

# Ejemplo básico de una función:
def saludar():
    print("¡Hola, mundo!")

# Para llamar (invocar) la función:
saludar()

# Salida:
# ¡Hola, mundo!

# Funciones con Parámetros
# Las funciones pueden aceptar parámetros para recibir datos y trabajar con ellos dentro del cuerpo de la función.

# Ejemplo: Función con un parámetro
def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")

saludar_a("Juan")

# Salida:
# ¡Hola, Juan!

# Ejemplo: Función con múltiples parámetros
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"El resultado de la suma es: {resultado}")

# Salida:
# El resultado de la suma es: 8

# Valores por Defecto en Parámetros
# Se pueden definir valores por defecto para los parámetros, que se usarán si no se proporciona un valor al llamar a la función.

# Ejemplo: Parámetro con valor por defecto
def saludar_con_nombre(nombre="invitado"):
    print(f"¡Hola, {nombre}!")

saludar_con_nombre()  # No se pasa argumento, se usa el valor por defecto
saludar_con_nombre("María")

# Salida:
# ¡Hola, invitado!
# ¡Hola, María!

# Funciones con Retorno
# Las funciones pueden devolver valores utilizando la palabra clave `return`. El valor retornado puede ser capturado en una variable para su uso posterior.

# Ejemplo: Función con retorno
def multiplicar(a, b):
    return a * b

producto = multiplicar(4, 7)
print(f"El producto es: {producto}")

# Salida:
# El producto es: 28

# Funciones Lambda (Funciones Anónimas)
# Python permite crear funciones anónimas (sin nombre) usando la palabra clave `lambda`.

# Ejemplo: Función lambda para sumar dos números
suma = lambda x, y: x + y
print(suma(2, 3))

# Salida:
# 5

# `lambda` se usa frecuentemente en funciones que requieren un pequeño bloque de código que no necesita un nombre formal, como en funciones `map()`, `filter()` y `sorted()`.

# Ejemplo: Uso de lambda con `sorted()` para ordenar una lista de tuplas por el segundo valor
lista = [(1, 2), (3, 1), (5, 4)]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)

# Salida:
# [(3, 1), (1, 2), (5, 4)]

# Argumentos *args y **kwargs
# `*args` y `**kwargs` permiten que una función acepte un número variable de argumentos.

# Ejemplo: Uso de `*args` para aceptar múltiples argumentos
def suma_varios(*args):
    return sum(args)

print(suma_varios(1, 2, 3, 4))

# Salida:
# 10

# Ejemplo: Uso de `**kwargs` para aceptar múltiples argumentos nombrados (diccionario)
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")

# Salida:
# nombre: Ana
# edad: 30
# ciudad: Madrid

# Documentación de Funciones (Docstrings)
# Es buena práctica documentar las funciones usando docstrings. Esto se hace agregando una cadena de texto justo después de la definición de la función.

# Ejemplo: Función con docstring
def dividir(a, b):
    """
    Esta función divide el número 'a' por 'b'.
    Retorna el resultado de la división.
    """
    return a / b

# Se puede acceder al docstring de la función con `help()` o `.__doc__`
print(dividir.__doc__)

# Salida:
# Esta función divide el número 'a' por 'b'.
# Retorna el resultado de la división.

# Funciones Recursivas
# Una función es recursiva si se llama a sí misma dentro de su definición. Las funciones recursivas son útiles para resolver problemas que se pueden descomponer en subproblemas más pequeños.

# Ejemplo: Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Salida:
# 120
