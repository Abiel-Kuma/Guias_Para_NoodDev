# Las variables en Python no requieren especificar un tipo de dato al declararse, lo que significa que son dinámicas.
# Sin embargo, se puede definir el tipo de dato que se espera guardar utilizando anotaciones de tipo.

# Ejemplo:

numero = 2
print(numero)

numero = "dos"
print(numero)

numero = 2.67
print(numero)

numero = True
print(numero)

# Como puedes ver, no importa el valor que asignes, Python no genera un error de tipado.

# Ejemplo de uso de anotaciones de tipo:

# str: se utiliza para valores de tipo texto.
nombre: str
nombre = "Juan"

# int: se utiliza para valores de tipo entero.
edad: int
edad = 2

# float: se utiliza para valores de tipo flotante (números decimales).
altura: float
altura = 1.60

# bool: se utiliza para valores de tipo booleano (True/False).
esta_vivo: bool
esta_vivo = True
