# Los datos compuestos, como su nombre indica, son estructuras que contienen uno o más datos.

# Listas
animales = ["perro", "gato", "ratón", "jaguar"]

# ¿Qué crees que sucederá si imprimimos la lista de animales?
print(f"Lista de animales: {animales}")

# En las listas también se pueden agregar y modificar valores.
animales.append("gallina")  # Agrega un valor al final de la lista.
animales[3] = "unicornio"  # Modifica el valor en la posición 3, cambiando "jaguar" por "unicornio".
print(f"Lista de animales modificada: {animales}")

# ¿Cómo hacemos para imprimir un valor específico en una lista?

# ¿Qué animal crees que imprimirá el siguiente código?
print(f"Imprimiendo un valor específico en la lista: {animales[1]}")

# Tuplas: las tuplas son similares a las listas, pero a diferencia de estas, no se pueden modificar. Es decir, son inmutables.
herramientas = ("pico", "hacha", "martillo")
print(f"Imprimiendo una tupla: {herramientas}")

# Conjuntos: los conjuntos son colecciones desordenadas de elementos únicos.
frutas = {"manzana", "naranja", "banana"}

# Diccionarios: los diccionarios usan un formato de "clave": "valor".
# Ejemplo de un diccionario:
player = {
    "nickname": "juan",
    "nivel": "23",
    "atk": "32",
    "defensa": "20"
}

print(f"Imprimiendo el diccionario player: {player}")
