# Datos Avanzadas

# En Python, las estructuras de datos avanzadas, como las listas y diccionarios por comprensión, 
# permiten crear y manipular datos de manera más concisa y eficiente.

# Listas por Compresión
# Las listas por comprensión son una forma compacta de crear listas a partir de secuencias o iterables.

# Ejemplo: Crear una lista de cuadrados
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

# Salida:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ejemplo: Crear una lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# Salida:
# [0, 2, 4, 6, 8]

# Las listas por comprensión pueden incluir condicionales que permiten filtrar los elementos.
# También se pueden anidar, lo que permite construir listas a partir de otras listas de forma muy compacta.

# Ejemplo: Lista de pares y sus cuadrados
pares_cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print(pares_cuadrados)

# Salida:
# [0, 4, 16, 36, 64]

# Diccionarios por Compresión
# Los diccionarios por comprensión son una forma rápida de crear diccionarios a partir de secuencias o iterables.

# Ejemplo: Crear un diccionario de números y sus cuadrados
cuadrados = {x: x**2 for x in range(10)}
print(cuadrados)

# Salida:
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Ejemplo: Crear un diccionario de números pares y sus cuadrados
pares_cuadrados = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares_cuadrados)

# Salida:
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Compresión de Conjuntos
# De manera similar a listas y diccionarios, también se pueden crear conjuntos (sets) por comprensión.

# Ejemplo: Crear un conjunto de cuadrados
cuadrados = {x**2 for x in range(10)}
print(cuadrados)

# Salida:
# {0, 1, 64, 36, 4, 9, 16, 81, 49, 25}

# Compresión de Tuplas
# Aunque no existe una "comprensión de tuplas" como tal, se puede usar la función `tuple()` junto con una comprensión de lista para crear tuplas.

# Ejemplo: Crear una tupla de cuadrados
cuadrados = tuple(x**2 for x in range(10))
print(cuadrados)

# Salida:
# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
