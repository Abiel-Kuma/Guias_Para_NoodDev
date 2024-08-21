# Bucle

# En Python, los bucles permiten ejecutar un bloque de código varias veces de manera repetitiva.
# Los bucles principales en Python son: `for` y `while`.

# Bucle `for`
# El bucle `for` itera sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de caracteres).

# Ejemplo: Iterando sobre una lista
animales = ["perro", "gato", "ratón"]
for animal in animales:
    print(animal)

# Salida:
# perro
# gato
# ratón

# Ejemplo: Iterando sobre una cadena de caracteres
palabra = "Python"
for letra in palabra:
    print(letra)

# Salida:
# P
# y
# t
# h
# o
# n

# La función `range()`
# `range()` se utiliza comúnmente en los bucles `for` para generar una secuencia de números.

# Ejemplo: Usando `range()` en un bucle `for`
for i in range(5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

# `range()` también puede tomar un valor inicial, un valor final, y un paso.
# Ejemplo: `range()` con valor inicial, final, y paso
for i in range(2, 10, 2):
    print(i)

# Salida:
# 2
# 4
# 6
# 8

# Bucle `while`
# El bucle `while` ejecuta un bloque de código siempre que la condición especificada sea True.

# Ejemplo: Bucle `while` básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa el contador en 1 en cada iteración

# Salida:
# 0
# 1
# 2
# 3
# 4

# Declaraciones `break` y `continue`
# `break` se utiliza para salir de un bucle antes de que termine todas sus iteraciones.
# `continue` se utiliza para saltar el resto del código dentro del bucle para la iteración actual y pasar a la siguiente iteración.

# Ejemplo: Uso de `break`
for i in range(10):
    if i == 5:
        break
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

# Ejemplo: Uso de `continue`
for i in range(10):
    if i % 2 == 0:  # Salta los números pares
        continue
    print(i)

# Salida:
# 1
# 3
# 5
# 7
# 9

# Bucle `else`
# Python permite asociar una cláusula `else` con los bucles. El bloque `else` se ejecutará cuando el bucle termine su iteración normalmente (sin haber sido interrumpido por `break`).

# Ejemplo: Uso de `else` en un bucle `for`
for i in range(5):
    print(i)
else:
    print("El bucle ha terminado sin interrupciones.")

# Salida:
# 0
# 1
# 2
# 3
# 4
# El bucle ha terminado sin interrupciones.

# Ejemplo: Uso de `else` con `break`
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Este mensaje no se mostrará porque el bucle fue interrumpido.")

# Salida:
# 0
# 1
# 2

# Conclusión
# Los bucles en Python son herramientas poderosas para realizar tareas repetitivas de manera eficiente.
# Comprender cómo usar `for`, `while`, y las declaraciones `break`, `continue`, y `else` te permitirá escribir código más flexible y controlado.