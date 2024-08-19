# Guía Completa de Python

## Introducción a Python

Python es un lenguaje de programación interpretado, de alto nivel y de propósito general, creado por Guido van Rossum y lanzado por primera vez en 1991. Es conocido por su sintaxis clara y legible, lo que facilita el aprendizaje y la escritura de código. Python es ampliamente utilizado en diversos campos como desarrollo web, análisis de datos, inteligencia artificial, automatización, entre otros.

## Índice

1. [Variables y Tipos de Datos](#variables-y-tipos-de-datos)
2. [Datos Compuestos](#datos-compuestos)
3. [Operadores](#operadores)
4. [Condicionales](#condicionales)
5. [Bucles](#bucles)
6. [Funciones](#funciones)
7. [Manejo de Excepciones](#manejo-de-excepciones)
8. [Estructuras de Datos Avanzadas](#estructuras-de-datos-avanzadas)
9. [Módulos y Paquetes](#módulos-y-paquetes)
10. [Programación Orientada a Objetos](#programación-orientada-a-objetos)
11. [Manejo de Archivos](#manejo-de-archivos)
12. [Bibliotecas y Frameworks Populares](#bibliotecas-y-frameworks-populares)
13. [Conclusión](#conclusión)

## Variables y Tipos de Datos

### Variables
Las variables en Python son contenedores para almacenar valores. No es necesario declarar el tipo de variable explícitamente, ya que Python lo infiere automáticamente.

```python
x = 5
nombre = "Juan"
```

### Tipos de Datos
Python soporta varios tipos de datos fundamentales:

- **Números Enteros (`int`)**: Ej. `x = 5`
- **Números Decimales (`float`)**: Ej. `y = 3.14`
- **Cadenas de Texto (`str`)**: Ej. `nombre = "Juan"`
- **Booleanos (`bool`)**: Ej. `es_mayor = True`

## Datos Compuestos

### Listas
Una lista es una colección ordenada y mutable de elementos.

```python
numeros = [1, 2, 3, 4, 5]
```

### Tuplas
Una tupla es similar a una lista, pero es inmutable.

```python
coordenadas = (10, 20)
```

### Conjuntos
Un conjunto es una colección no ordenada de elementos únicos.

```python
frutas = {"manzana", "naranja", "banana"}
```

### Diccionarios
Un diccionario es una colección no ordenada de pares clave-valor.

```python
persona = {"nombre": "Juan", "edad": 30}
```

## Operadores

### Operadores Aritméticos

```python
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5
```

### Operadores de Comparación

```python
es_igual = 10 == 5
es_diferente = 10 != 5
```

### Operadores Lógicos

```python
y_logico = True and False
o_logico = True or False
```

### Operadores de Asignación

```python
x += 5
x -= 5
```

## Condicionales

Las estructuras condicionales permiten la ejecución de código basado en condiciones.

```python
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")
```

## Bucles

### Bucle `while`

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Bucle `for`

```python
for i in range(5):
    print(i)
```

## Funciones

Las funciones permiten agrupar código reutilizable.

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")
```

## Manejo de Excepciones

Las excepciones se utilizan para manejar errores en tiempo de ejecución.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto siempre se ejecuta")
```

## Estructuras de Datos Avanzadas

### Listas por Compresión

```python
cuadrados = [x**2 for x in range(10)]
```

### Diccionarios por Compresión

```python
cuadrados = {x: x**2 for x in range(10)}
```

## Módulos y Paquetes

Python permite organizar el código en módulos y paquetes para su reutilización.

### Importar un Módulo

```python
import math
print(math.sqrt(16))
```

### Crear un Módulo

```python
# archivo: mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}"
```

### Paquetes

Un paquete es una colección de módulos.

```markdown
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```

## Programación Orientada a Objetos

### Clases y Objetos

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")

juan = Persona("Juan", 30)
juan.saludar()
```

### Herencia

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
```

## Manejo de Archivos

### Leer Archivos

```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```

### Escribir Archivos

```python
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola Mundo")
```

## Bibliotecas y Frameworks Populares

- **NumPy**: Manipulación de arrays y matrices.
- **Pandas**: Análisis de datos.
- **Flask/Django**: Desarrollo web.
- **Matplotlib**: Visualización de datos.
- **TensorFlow**: Aprendizaje automático.

## Conclusión
Python es un lenguaje poderoso y versátil que permite desarrollar una amplia gama de aplicaciones. Con una sintaxis sencilla y una gran cantidad de bibliotecas, es una excelente opción tanto para principiantes como para desarrolladores experimentados.
