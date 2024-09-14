### Guía Completa de FastAPI

---

#### **Introducción**

FastAPI es un moderno y potente framework web para la creación de aplicaciones web y APIs en Python. Se destaca por su rendimiento, basado en ASGI (Asynchronous Server Gateway Interface), y su diseño orientado a facilitar el desarrollo rápido y eficiente de APIs. Su enfoque en la tipificación y validación automática de datos lo convierte en una herramienta ideal tanto para principiantes como para desarrolladores experimentados.

FastAPI no solo es fácil de usar sino también extremadamente rápido, aprovechando las capacidades asincrónicas de Python, lo que lo hace una opción preferida para construir aplicaciones de alta performance y escalables.

---

#### **Índice**

##### **Parte 1: Principiante**
1. [Introducción a FastAPI](#1-introducción-a-fastapi)
2. [Instalación y configuración del entorno](#2-instalación-y-configuración-del-entorno)
3. [Creación de la primera aplicación con FastAPI](#3-creación-de-la-primera-aplicación-con-fastapi)
4. [Rutas y métodos HTTP](#4-rutas-y-métodos-http)
5. [Validación de datos con Pydantic](#5-validación-de-datos-con-pydantic)
6. [Manejo de errores y respuestas personalizadas](#6-manejo-de-errores-y-respuestas-personalizadas)
7. [Operaciones avanzadas con parámetros](#7-operaciones-avanzadas-con-parámetros)
8. [Documentación automática y Swagger UI](#8-documentación-automática-y-swagger-ui)
9. [Introducción a la asincronía en FastAPI](#9-introducción-a-la-asincronía-en-fastapi)
##### **Parte 2: Intermedio**
1. [Gestión de bases de datos con FastAPI y SQLAlchemy](#1-gestión-de-bases-de-datos-con-fastapi-y-sqlalchemy)
2. [Creación de modelos y esquemas](#2-creación-de-modelos-y-esquemas)
3. [Autenticación y autorización](#3-autenticación-y-autorización)
4. [Middleware y gestión de CORS](#4-middleware-y-gestión-de-cors)
5. [Creación y uso de dependencias](#5-creación-y-uso-de-dependencias)
6. [Manejo de archivos y formularios](#6-manejo-de-archivos-y-formularios)
7. [Implementación de WebSockets](#7-implementación-de-websockets)

##### **Parte 3: Experto**
1. [Optimización y escalabilidad](#1-optimización-y-escalabilidad)
2. [Despliegue en producción con Docker](#2-despliegue-en-producción-con-docker)
3. [Testing avanzado y CI/CD](#3-testing-avanzado-y-cicd)
4. [Integración con otras tecnologías (Celery, Redis)](#4-integración-con-otras-tecnologías-celery-redis)
5. [Arquitecturas orientadas a microservicios](#5-arquitecturas-orientadas-a-microservicios)
6. [Gestión de permisos y roles complejos](#6-gestión-de-permisos-y-roles-complejos)
7. [Creación de plugins y extensiones](#7-creación-de-plugins-y-extensiones)

##### **Parte 4: Estructura de Carpetas**
1. [Estructura de carpetas para una Api usando FastApi](#estructura-de-carpetas-para-una-api-en-fastapi)

---
### Parte 1: Principiante

#### **1. Introducción a FastAPI**
![FastApi](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
FastAPI es un framework moderno y de alto rendimiento para construir APIs en Python, creado por Sebastián Ramírez. Se caracteriza por ser fácil de usar y producir aplicaciones rápidas y eficientes, apoyándose en la tipificación estática de Python para generar documentación y validaciones automáticas.

##### **¿Por qué elegir FastAPI?**

1. **Velocidad**: FastAPI es uno de los frameworks más rápidos disponibles para Python, comparable en rendimiento a frameworks como Node.js y Go.

2. **Simplicidad**: Su diseño permite que los desarrolladores se concentren en la lógica de la aplicación sin preocuparse por configuraciones complicadas.

3. **Productividad**: Gracias a la generación automática de documentación y las validaciones integradas, los desarrolladores pueden ser más productivos.

4. **Documentación automática**: FastAPI genera automáticamente una interfaz web interactiva para la API usando Swagger UI y ReDoc, facilitando la interacción y prueba de los endpoints.

5. **Soporte para asincronía**: FastAPI es totalmente compatible con Python asíncrono, lo que permite la creación de aplicaciones altamente concurrentes.

##### **Características clave**

- **Basado en estándares**: FastAPI se construye sobre estándares como OpenAPI y JSON Schema, asegurando interoperabilidad y facilidad de integración.
  
- **Tipado de datos**: Utiliza Pydantic para validar datos de entrada basados en las anotaciones de tipo de Python, lo que ayuda a evitar errores comunes y a mejorar la claridad del código.
  
- **Escalabilidad**: Diseñado para manejar desde pequeñas aplicaciones hasta grandes proyectos de producción con miles de usuarios concurrentes.

##### **Casos de uso**

FastAPI es ideal para proyectos como:

- **APIs RESTful**: Permite crear APIs escalables y fáciles de mantener.
- **Microservicios**: Gracias a su eficiencia y simplicidad, es excelente para desarrollar microservicios.
- **Aplicaciones de Machine Learning**: Su capacidad para manejar peticiones rápidas lo hace una excelente opción para servir modelos de machine learning en producción.

##### **Quién debería usar FastAPI**

- **Principiantes**: Es una excelente opción para aquellos nuevos en el desarrollo web, debido a su simplicidad y buena documentación.
- **Desarrolladores experimentados**: Ofrece herramientas avanzadas que permiten crear aplicaciones sofisticadas de manera eficiente.
- **Equipos de desarrollo**: La generación automática de documentación y validación reduce errores y facilita la colaboración entre miembros del equipo.

---

#### **2. Instalación y configuración del entorno**

Antes de empezar a desarrollar con FastAPI, es necesario configurar el entorno de desarrollo. En esta sección, aprenderás a instalar FastAPI y las herramientas necesarias para empezar a crear aplicaciones.

##### **Requisitos previos**

- **Python 3.7 o superior**: FastAPI requiere Python 3.7 o versiones posteriores para funcionar. Puedes verificar la versión de Python instalada ejecutando el siguiente comando en tu terminal:

    ```bash
    python --version
    ```

##### **Paso 1: Crear un entorno virtual**

Es recomendable crear un entorno virtual para tu proyecto para evitar conflictos entre dependencias de diferentes proyectos. Para crear un entorno virtual, sigue estos pasos:

1. Abre tu terminal y navega a la carpeta donde quieres crear tu proyecto.

2. Crea un entorno virtual usando `venv`:

    ```bash
    python -m venv env
    ```

3. Activa el entorno virtual:

    - En Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - En macOS/Linux:

        ```bash
        source env/bin/activate
        ```

    Verás que el nombre del entorno virtual aparece al inicio de la línea de tu terminal, indicando que el entorno está activado.

##### **Paso 2: Instalar FastAPI y Uvicorn**

Una vez que el entorno virtual esté activado, puedes instalar FastAPI y Uvicorn. Uvicorn es un servidor ASGI ligero y rápido que FastAPI utiliza para servir tus aplicaciones.

1. Ejecuta el siguiente comando para instalar FastAPI:

    ```bash
    pip install fastapi
    ```

2. Luego, instala Uvicorn:

    ```bash
    pip install "uvicorn[standard]"
    ```

##### **Paso 3: Crear tu primer archivo FastAPI**

Ahora que tienes FastAPI y Uvicorn instalados, puedes crear tu primera aplicación. Sigue estos pasos:

1. En tu editor de texto o IDE favorito, crea un nuevo archivo llamado `main.py`.

2. Dentro de `main.py`, añade el siguiente código para crear una aplicación simple de FastAPI:

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello, FastAPI!"}
    ```

Este código crea una instancia de FastAPI y define una ruta (`/`) que retorna un mensaje de bienvenida.

##### **Paso 4: Ejecutar la aplicación con Uvicorn**

Finalmente, puedes ejecutar tu aplicación utilizando Uvicorn. En tu terminal, asegúrate de estar en la misma carpeta donde se encuentra `main.py` y ejecuta:

```bash
uvicorn main:app --reload
```

- `main:app` hace referencia al archivo `main.py` y a la instancia `app` de FastAPI que definimos.
- `--reload` indica que el servidor se reiniciará automáticamente cuando detecte cambios en el código, lo que es útil durante el desarrollo.

Si todo está bien, deberías ver un mensaje en la terminal indicando que el servidor está corriendo, y podrás acceder a la aplicación en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

##### **Verificación**

Abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000). Deberías ver un JSON con el mensaje `{"message": "Hello, FastAPI!"}`.

---

#### **3. Creación de la primera aplicación con FastAPI**

Ahora que tienes FastAPI y Uvicorn instalados, es hora de profundizar un poco más y crear una aplicación básica. En esta sección, expandiremos la aplicación que empezamos en la sección anterior y exploraremos algunas de las funcionalidades básicas de FastAPI.

##### **Paso 1: Definir rutas adicionales**

En FastAPI, puedes definir múltiples rutas para manejar diferentes tipos de solicitudes HTTP. Vamos a crear un par de rutas más para ilustrar cómo funcionan.

1. Abre el archivo `main.py` que creaste anteriormente.
2. Añade el siguiente código:

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    # Ruta principal (GET)
    @app.get("/")
    def read_root():
        return {"message": "Welcome to FastAPI!"}

    # Ruta para obtener un ítem por ID (GET)
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "query": q}

    # Ruta para crear un nuevo ítem (POST)
    @app.post("/items/")
    def create_item(name: str, price: float):
        return {"name": name, "price": price}
    ```

##### **Explicación del código:**

1. **Ruta principal `/`**:
   - **Método HTTP:** `GET`
   - **Descripción:** Devuelve un mensaje de bienvenida.

2. **Ruta `/items/{item_id}`**:
   - **Método HTTP:** `GET`
   - **Parámetros de ruta:** `item_id` (int) es un parámetro dinámico de la URL.
   - **Parámetros de consulta:** `q` (opcional) permite pasar un valor extra a través de la URL como una consulta (`?q=valor`).
   - **Descripción:** Devuelve el ID del ítem solicitado y, opcionalmente, el valor de la consulta `q`.

3. **Ruta `/items/`**:
   - **Método HTTP:** `POST`
   - **Parámetros de cuerpo:** `name` (str) y `price` (float) se pasan en el cuerpo de la solicitud.
   - **Descripción:** Crea un nuevo ítem con un nombre y un precio, y devuelve los datos del ítem creado.

##### **Paso 2: Ejecutar y probar la aplicación**

1. Ejecuta nuevamente la aplicación usando Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Probar las rutas:**

    - Visita [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador para ver la ruta principal.
    - Para probar la ruta `/items/{item_id}`, abre la siguiente URL en tu navegador: [http://127.0.0.1:8000/items/42?q=test](http://127.0.0.1:8000/items/42?q=test). Deberías ver una respuesta como `{"item_id": 42, "query": "test"}`.
    - Para probar la ruta `POST /items/`, puedes utilizar herramientas como **Postman** o **cURL** para enviar una solicitud POST. Por ejemplo, con cURL:

      ```bash
      curl -X POST "http://127.0.0.1:8000/items/" -d "name=Apple&price=0.99"
      ```

      Deberías obtener una respuesta como `{"name": "Apple", "price": 0.99}`.

##### **Paso 3: Explorar la documentación automática**

FastAPI genera automáticamente la documentación de la API y la expone en dos rutas:

- **Swagger UI**: Visita [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver una interfaz interactiva generada con Swagger UI, donde puedes probar las rutas de la API directamente desde el navegador.

- **ReDoc**: Visita [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) para ver la documentación generada con ReDoc, que ofrece una vista más detallada de la API.

---

#### **4. Rutas y métodos HTTP**

En FastAPI, las rutas son las URL a las que pueden acceder los usuarios para interactuar con tu aplicación. Cada ruta está asociada a un método HTTP, como `GET`, `POST`, `PUT`, `DELETE`, etc., que define qué tipo de acción se realizará.

En esta sección, exploraremos cómo manejar diferentes métodos HTTP y cómo trabajar con rutas en FastAPI.

##### **Métodos HTTP comunes**

- **GET**: Recupera información del servidor. Por ejemplo, obtener datos de un ítem específico o una lista de ítems.
- **POST**: Envía datos al servidor para crear un nuevo recurso. Por ejemplo, crear un nuevo ítem en una base de datos.
- **PUT**: Actualiza un recurso existente en el servidor. Por ejemplo, modificar los detalles de un ítem.
- **DELETE**: Elimina un recurso del servidor. Por ejemplo, eliminar un ítem de una base de datos.

##### **Definiendo rutas con diferentes métodos HTTP**

Vamos a crear un conjunto de rutas que ejemplifiquen el uso de estos métodos HTTP en FastAPI.

1. Abre el archivo `main.py` y añade o modifica el siguiente código:

    ```python
    from fastapi import FastAPI, HTTPException

    app = FastAPI()

    # Base de datos ficticia para ejemplos
    fake_items_db = {"item1": {"name": "Item 1", "price": 50.5},
                     "item2": {"name": "Item 2", "price": 99.9}}

    # Ruta GET para obtener información de un ítem
    @app.get("/items/{item_id}")
    def read_item(item_id: str):
        if item_id in fake_items_db:
            return fake_items_db[item_id]
        raise HTTPException(status_code=404, detail="Item not found")

    # Ruta POST para crear un nuevo ítem
    @app.post("/items/")
    def create_item(item_id: str, name: str, price: float):
        if item_id in fake_items_db:
            raise HTTPException(status_code=400, detail="Item already exists")
        fake_items_db[item_id] = {"name": name, "price": price}
        return fake_items_db[item_id]

    # Ruta PUT para actualizar un ítem existente
    @app.put("/items/{item_id}")
    def update_item(item_id: str, name: str, price: float):
        if item_id not in fake_items_db:
            raise HTTPException(status_code=404, detail="Item not found")
        fake_items_db[item_id].update({"name": name, "price": price})
        return fake_items_db[item_id]

    # Ruta DELETE para eliminar un ítem
    @app.delete("/items/{item_id}")
    def delete_item(item_id: str):
        if item_id in fake_items_db:
            del fake_items_db[item_id]
            return {"message": "Item deleted successfully"}
        raise HTTPException(status_code=404, detail="Item not found")
    ```

##### **Explicación del código:**

1. **GET `/items/{item_id}`**:
   - Este endpoint permite obtener información de un ítem específico de la base de datos ficticia `fake_items_db`.
   - Si el `item_id` existe en la base de datos, retorna los detalles del ítem. Si no, lanza una excepción HTTP 404 con un mensaje "Item not found".

2. **POST `/items/`**:
   - Este endpoint permite crear un nuevo ítem en la base de datos.
   - Verifica si el `item_id` ya existe. Si es así, lanza una excepción HTTP 400 con el mensaje "Item already exists". Si no, añade el nuevo ítem a la base de datos.

3. **PUT `/items/{item_id}`**:
   - Este endpoint permite actualizar un ítem existente en la base de datos.
   - Si el `item_id` no existe, lanza una excepción HTTP 404. Si existe, actualiza el nombre y el precio del ítem.

4. **DELETE `/items/{item_id}`**:
   - Este endpoint permite eliminar un ítem de la base de datos.
   - Si el `item_id` existe, lo elimina y retorna un mensaje de éxito. Si no, lanza una excepción HTTP 404.

##### **Paso 2: Ejecutar y probar los métodos HTTP**

1. Ejecuta la aplicación con Uvicorn si no lo has hecho ya:

    ```bash
    uvicorn main:app --reload
    ```

2. **Prueba las rutas:**

   - **GET**: Prueba obtener un ítem existente usando la URL [http://127.0.0.1:8000/items/item1](http://127.0.0.1:8000/items/item1).
   - **POST**: Usa herramientas como Postman o cURL para crear un nuevo ítem. Por ejemplo, con cURL:

     ```bash
     curl -X POST "http://127.0.0.1:8000/items/" -d "item_id=item3&name=Item 3&price=25.0"
     ```

   - **PUT**: Actualiza un ítem existente usando cURL:

     ```bash
     curl -X PUT "http://127.0.0.1:8000/items/item3" -d "name=Updated Item 3&price=30.0"
     ```

   - **DELETE**: Elimina un ítem usando cURL:

     ```bash
     curl -X DELETE "http://127.0.0.1:8000/items/item3"
     ```

##### **Documentación automática**

No olvides que puedes acceder a la documentación automática en:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

#### **5. Validación de datos con Pydantic**

Una de las características más poderosas de FastAPI es su integración con Pydantic, que permite la validación y serialización de datos de manera sencilla y eficiente. Pydantic aprovecha las anotaciones de tipo de Python para definir y validar la estructura de los datos que manejan las rutas de tu aplicación.

En esta sección, aprenderás a usar Pydantic para validar los datos de entrada y crear modelos que representen la estructura de tus datos.

##### **Paso 1: Creación de modelos con Pydantic**

Los modelos Pydantic son clases que definen la estructura de los datos que quieres validar. Vamos a crear un modelo simple para representar un ítem.

1. Abre tu archivo `main.py` y añade o modifica el siguiente código:

    ```python
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    # Modelo Pydantic para un ítem
    class Item(BaseModel):
        name: str
        price: float
        description: str | None = None
        tax: float | None = None

    # Base de datos ficticia para ejemplos
    fake_items_db = {}

    # Ruta POST para crear un nuevo ítem usando el modelo Pydantic
    @app.post("/items/")
    def create_item(item: Item):
        if item.name in fake_items_db:
            raise HTTPException(status_code=400, detail="Item already exists")
        fake_items_db[item.name] = item.dict()
        return item
    ```

##### **Explicación del código:**

1. **Definición del modelo Pydantic**:
   - Creamos una clase `Item` que hereda de `BaseModel`.
   - Los atributos de la clase definen el nombre, precio, descripción y el impuesto (`tax`) de un ítem.
   - `description` y `tax` son opcionales, como se indica con `str | None` y `float | None`.

2. **Uso del modelo en una ruta**:
   - La ruta `POST /items/` acepta un objeto de tipo `Item` en el cuerpo de la solicitud.
   - FastAPI valida automáticamente que los datos enviados cumplan con la estructura y tipos definidos en el modelo `Item`.
   - Si el ítem ya existe en la base de datos ficticia, lanza una excepción HTTP 400.
   - Si los datos son válidos y el ítem no existe, se guarda en la base de datos ficticia.

3. **Conversión a diccionario**:
   - El método `item.dict()` convierte el objeto `Item` en un diccionario, lo que es útil para almacenarlo o manipularlo.

##### **Paso 2: Validar datos en solicitudes**

FastAPI validará automáticamente los datos enviados en la solicitud basada en el modelo Pydantic. Vamos a agregar una ruta para actualizar un ítem, validando los datos de entrada.

1. Añade el siguiente código a tu archivo `main.py`:

    ```python
    # Ruta PUT para actualizar un ítem existente usando el modelo Pydantic
    @app.put("/items/{item_name}")
    def update_item(item_name: str, item: Item):
        if item_name not in fake_items_db:
            raise HTTPException(status_code=404, detail="Item not found")
        fake_items_db[item_name] = item.dict()
        return {"message": "Item updated successfully", "item": item}
    ```

##### **Explicación del código:**

1. **Ruta PUT `/items/{item_name}`**:
   - Esta ruta permite actualizar un ítem existente en la base de datos.
   - Valida que `item_name` exista en la base de datos.
   - Los datos del ítem son validados según el modelo `Item`.
   - Si todo es correcto, el ítem se actualiza y se devuelve un mensaje de éxito junto con los datos actualizados.

##### **Paso 3: Ejecutar y probar la validación de datos**

1. Asegúrate de que tu aplicación esté ejecutándose con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Probar la validación:**

    - **POST**: Usa cURL o Postman para crear un nuevo ítem.

      ```bash
      curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d "{\"name\": \"Laptop\", \"price\": 1000.0, \"description\": \"A powerful laptop\", \"tax\": 100.0}"
      ```

    - **PUT**: Actualiza un ítem existente.

      ```bash
      curl -X PUT "http://127.0.0.1:8000/items/Laptop" -H "Content-Type: application/json" -d "{\"name\": \"Laptop\", \"price\": 1100.0, \"description\": \"A powerful laptop with updated specs\", \"tax\": 120.0}"
      ```

3. **Comprobación de errores:**
   - Intenta enviar una solicitud con un tipo de dato incorrecto o dejando un campo obligatorio en blanco. FastAPI retornará un error con detalles sobre qué datos no son válidos.

##### **Ventajas de usar Pydantic en FastAPI**

- **Validación automática**: FastAPI valida automáticamente los datos entrantes basados en los modelos Pydantic.
- **Documentación clara**: Los modelos Pydantic son utilizados por FastAPI para generar documentación clara y detallada de la API.
- **Simplicidad**: Definir modelos y validar datos se hace de manera declarativa y concisa.

---

#### **6. Manejo de errores y respuestas personalizadas**

FastAPI facilita la captura y gestión de errores, permitiéndote devolver respuestas personalizadas a los usuarios cuando algo no sale como se esperaba. En esta sección, aprenderás a manejar errores comunes y a devolver respuestas personalizadas utilizando las herramientas que FastAPI proporciona.

##### **Manejo de excepciones con `HTTPException`**

FastAPI tiene una clase llamada `HTTPException` que te permite lanzar errores HTTP de manera fácil. Veamos cómo se utiliza.

1. Abre tu archivo `main.py` y revisa el siguiente código:

    ```python
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    # Modelo Pydantic para un ítem
    class Item(BaseModel):
        name: str
        price: float
        description: str | None = None
        tax: float | None = None

    # Base de datos ficticia para ejemplos
    fake_items_db = {"item1": {"name": "Item 1", "price": 50.5}}

    # Ruta GET para obtener información de un ítem
    @app.get("/items/{item_name}")
    def read_item(item_name: str):
        if item_name not in fake_items_db:
            raise HTTPException(status_code=404, detail="Item not found")
        return fake_items_db[item_name]

    # Ruta POST para crear un nuevo ítem usando el modelo Pydantic
    @app.post("/items/")
    def create_item(item: Item):
        if item.name in fake_items_db:
            raise HTTPException(status_code=400, detail="Item already exists")
        fake_items_db[item.name] = item.dict()
        return item

    # Ruta DELETE para eliminar un ítem
    @app.delete("/items/{item_name}")
    def delete_item(item_name: str):
        if item_name not in fake_items_db:
            raise HTTPException(status_code=404, detail="Item not found")
        del fake_items_db[item_name]
        return {"message": "Item deleted successfully"}
    ```

##### **Explicación del código:**

1. **`HTTPException`**:
   - La clase `HTTPException` te permite lanzar una respuesta HTTP con un código de estado específico y un mensaje de error.
   - Por ejemplo, en la ruta `GET /items/{item_name}`, si el `item_name` no se encuentra en la base de datos, se lanza una `HTTPException` con un código de estado 404 (Not Found) y un mensaje `"Item not found"`.

2. **Uso en múltiples rutas**:
   - Se utiliza `HTTPException` en varias rutas (`GET`, `POST`, `DELETE`) para manejar casos como un ítem que no se encuentra, un ítem que ya existe, o la eliminación de un ítem que no está en la base de datos.

##### **Paso 2: Respuestas personalizadas con `Response`**

FastAPI también te permite personalizar las respuestas que se devuelven desde las rutas, incluyendo el tipo de contenido, los encabezados y el código de estado.

1. Añade o modifica el siguiente código en tu archivo `main.py`:

    ```python
    from fastapi import FastAPI, HTTPException, Response

    app = FastAPI()

    # Ruta para crear un ítem con respuesta personalizada
    @app.post("/custom-response/", status_code=201)
    def custom_create_item(item: Item):
        if item.name in fake_items_db:
            return Response(content="Item already exists", status_code=400)
        fake_items_db[item.name] = item.dict()
        return Response(content="Item created successfully", status_code=201)
    ```

##### **Explicación del código:**

1. **Personalización de respuestas**:
   - Usamos `Response` para devolver una respuesta personalizada con un contenido específico y un código de estado.
   - En la ruta `POST /custom-response/`, si el ítem ya existe, se devuelve una respuesta con un código de estado 400 y un mensaje personalizado.
   - Si el ítem es creado exitosamente, se devuelve una respuesta con un código de estado 201 y un mensaje de éxito.

##### **Paso 3: Manejo global de excepciones**

Además de manejar errores en rutas individuales, FastAPI te permite capturar y gestionar excepciones a nivel global. Esto es útil para manejar errores de forma consistente en toda la aplicación.

1. Añade o modifica el siguiente código en tu archivo `main.py`:

    ```python
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import JSONResponse

    app = FastAPI()

    # Manejo global de excepciones
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": f"Oops! {exc.detail}"}
        )

    # Ruta de ejemplo que lanza una excepción
    @app.get("/cause-error/")
    def cause_error():
        raise HTTPException(status_code=418, detail="I'm a teapot")
    ```

##### **Explicación del código:**

1. **`@app.exception_handler`**:
   - Se define un manejador global de excepciones para `HTTPException`.
   - Este manejador captura todas las excepciones `HTTPException` que ocurran en la aplicación y devuelve una respuesta JSON personalizada.

2. **Ruta de ejemplo**:
   - La ruta `GET /cause-error/` lanza una excepción con un código de estado 418 (I'm a teapot), demostrando cómo el manejador global captura la excepción y devuelve una respuesta personalizada.

##### **Paso 4: Ejecutar y probar el manejo de errores**

1. Ejecuta la aplicación con Uvicorn si no lo has hecho:

    ```bash
    uvicorn main:app --reload
    ```

2. **Prueba el manejo de errores:**

    - Visita la URL [http://127.0.0.1:8000/items/nonexistent](http://127.0.0.1:8000/items/nonexistent) para ver cómo se maneja una excepción 404.
    - Prueba la ruta [http://127.0.0.1:8000/cause-error/](http://127.0.0.1:8000/cause-error/) para ver el manejador global en acción.

3. **Revisa las respuestas personalizadas:**

    - Usa cURL o Postman para probar la ruta `POST /custom-response/` y observa las respuestas personalizadas basadas en los datos enviados.

---

#### **7. Operaciones avanzadas con parámetros**

FastAPI permite trabajar con parámetros de rutas, consultas y cuerpos de una manera muy flexible, proporcionando herramientas para manejar casos más complejos de una manera sencilla. En esta sección, exploraremos cómo realizar operaciones avanzadas con estos parámetros para tener un control más fino sobre las entradas que recibe tu aplicación.

##### **Paso 1: Parámetros de ruta con validaciones avanzadas**

Los parámetros de ruta no solo pueden capturar valores de las URLs, sino también aplicar validaciones o transformar esos valores antes de que sean utilizados en las rutas.

1. Abre tu archivo `main.py` y añade o modifica el siguiente código:

    ```python
    from fastapi import FastAPI, Path, HTTPException

    app = FastAPI()

    # Ruta con un parámetro de ruta avanzado
    @app.get("/items/{item_id}")
    def read_item(item_id: int = Path(..., title="The ID of the item", ge=1)):
        if item_id not in fake_items_db:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"item_id": item_id, "item": fake_items_db[item_id]}
    ```

##### **Explicación del código:**

1. **Uso de `Path` para parámetros avanzados**:
   - El parámetro `item_id` se define como un entero (`int`) y se establece como obligatorio (`...`) utilizando `Path`.
   - `title` añade un título descriptivo para el parámetro, que será visible en la documentación automática.
   - La validación `ge=1` asegura que el valor de `item_id` sea mayor o igual a 1.

2. **Validación personalizada**:
   - Si el `item_id` no se encuentra en la base de datos ficticia, se lanza una `HTTPException` con un código de estado 404.

##### **Paso 2: Parámetros de consulta opcionales y requeridos**

FastAPI permite manejar parámetros de consulta (query parameters) que pueden ser opcionales o requeridos, dependiendo de cómo definas su valor por defecto.

1. Añade o modifica el siguiente código en tu archivo `main.py`:

    ```python
    from fastapi import FastAPI, Query

    app = FastAPI()

    # Ruta con parámetros de consulta opcionales y requeridos
    @app.get("/search/")
    def search_items(q: str = Query(None, title="Query string for the search"), limit: int = 10):
        results = {"items": []}
        if q:
            results["items"] = [item for item in fake_items_db.values() if q in item["name"]]
        return {"query": q, "results": results, "limit": limit}
    ```

##### **Explicación del código:**

1. **Parámetros de consulta (`Query`)**:
   - `q` es un parámetro de consulta opcional (`None` como valor por defecto) y se utiliza para buscar ítems cuyo nombre contenga el valor de `q`.
   - `limit` es un parámetro opcional con un valor por defecto de 10, que determina cuántos resultados devolver.

2. **Búsqueda en la base de datos ficticia**:
   - Si se proporciona un valor para `q`, se filtran los ítems en la base de datos que coinciden con el valor de búsqueda.

##### **Paso 3: Combinación de parámetros de ruta, consulta y cuerpo**

FastAPI permite combinar parámetros de ruta, consulta y cuerpo en la misma ruta, lo que te brinda gran flexibilidad para definir cómo se reciben y procesan los datos.

1. Añade o modifica el siguiente código en tu archivo `main.py`:

    ```python
    from fastapi import FastAPI, Path, Query, Body
    from pydantic import BaseModel

    app = FastAPI()

    # Modelo Pydantic para un ítem
    class Item(BaseModel):
        name: str
        price: float
        description: str | None = None
        tax: float | None = None

    # Ruta que combina parámetros de ruta, consulta y cuerpo
    @app.put("/items/{item_id}")
    def update_item(
        item_id: int = Path(..., title="The ID of the item to update", ge=1),
        q: str | None = Query(None, max_length=50),
        item: Item = Body(...),
    ):
        results = {"item_id": item_id, "item": item}
        if q:
            results["query"] = q
        return results
    ```

##### **Explicación del código:**

1. **Combinación de parámetros**:
   - `item_id` es un parámetro de ruta que debe ser mayor o igual a 1.
   - `q` es un parámetro de consulta opcional con una longitud máxima de 50 caracteres.
   - `item` es un parámetro de cuerpo que representa un objeto `Item` definido por el modelo Pydantic.

2. **Devolución de resultados**:
   - La ruta combina la información del `item_id`, el resultado de la consulta `q` (si se proporciona), y los detalles del ítem a actualizar.

##### **Paso 4: Ejecutar y probar operaciones avanzadas con parámetros**

1. Asegúrate de que tu aplicación esté ejecutándose con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Probar las rutas avanzadas:**

   - **Ruta con parámetros de ruta avanzados**: Visita [http://127.0.0.1:8000/items/1](http://127.0.0.1:8000/items/1) para ver cómo funciona la validación de `item_id`.
   - **Parámetros de consulta**: Prueba la búsqueda con [http://127.0.0.1:8000/search/?q=Item](http://127.0.0.1:8000/search/?q=Item).
   - **Combinación de parámetros**: Usa cURL o Postman para probar la ruta `PUT /items/1`, enviando datos en el cuerpo de la solicitud.

    ```bash
    curl -X PUT "http://127.0.0.1:8000/items/1?q=example" -H "Content-Type: application/json" -d "{\"name\": \"Item 1\", \"price\": 150.0, \"description\": \"Updated Item 1\", \"tax\": 15.0}"
    ```
---

#### **8. Documentación automática y Swagger UI**

Una de las características más destacadas de FastAPI es su capacidad para generar documentación automática y visualmente atractiva para tu API. Esta documentación no solo es útil para los desarrolladores, sino también para cualquier persona que necesite interactuar con la API, como clientes o equipos de control de calidad. En esta sección, aprenderás cómo FastAPI genera esta documentación y cómo puedes personalizarla según tus necesidades.

##### **Paso 1: Introducción a la documentación automática**

FastAPI genera dos interfaces de documentación automáticamente:

1. **Swagger UI**: Una interfaz interactiva y amigable para probar tu API en el navegador.
2. **Redoc**: Una interfaz de documentación elegante y fácil de navegar, orientada a la lectura.

Por defecto, FastAPI genera estas interfaces automáticamente basándose en los modelos, rutas, y validaciones que defines en tu aplicación.

1. Ejecuta tu aplicación si aún no lo has hecho:

    ```bash
    uvicorn main:app --reload
    ```

2. Abre tu navegador y navega a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver Swagger UI.

3. Para ver Redoc, navega a [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

##### **Paso 2: Personalización del título y la descripción de la documentación**

Puedes personalizar el título, la descripción y la versión de la API para que aparezcan en la documentación automática.

1. Modifica tu archivo `main.py` de la siguiente manera:

    ```python
    from fastapi import FastAPI

    # Personalización del título y descripción de la API
    app = FastAPI(
        title="Mi API con FastAPI",
        description="Esta es una API de ejemplo utilizando FastAPI. Aquí puedes aprender a crear una API rápida y eficiente con documentación automática.",
        version="1.0.0",
        terms_of_service="http://example.com/terms/",
        contact={
            "name": "Support Team",
            "url": "http://example.com/contact/",
            "email": "support@example.com",
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT",
        },
    )
    ```

2. Guarda los cambios y recarga la página de Swagger UI para ver la documentación personalizada.

##### **Explicación del código:**

1. **Personalización de `FastAPI`**:
   - **`title`**: Cambia el título que aparece en la documentación.
   - **`description`**: Proporciona una descripción detallada de la API, que aparecerá en la parte superior de la documentación.
   - **`version`**: Define la versión de la API.
   - **`terms_of_service`**: Un enlace a los términos de servicio de la API.
   - **`contact`**: Proporciona información de contacto para el soporte.
   - **`license_info`**: Incluye información sobre la licencia de la API.

##### **Paso 3: Personalización de las etiquetas de las rutas**

FastAPI permite agrupar rutas bajo etiquetas específicas para mejorar la organización de la documentación.

1. Modifica tu archivo `main.py` para añadir etiquetas a las rutas:

    ```python
    @app.get("/items/", tags=["items"])
    def read_items():
        return [{"name": "Item 1"}, {"name": "Item 2"}]

    @app.post("/items/", tags=["items"])
    def create_item(item: dict):
        return {"name": item["name"], "price": item["price"]}

    @app.get("/users/", tags=["users"])
    def read_users():
        return [{"username": "user1"}, {"username": "user2"}]
    ```

2. Recarga Swagger UI y observa cómo las rutas ahora están agrupadas bajo las etiquetas "items" y "users".

##### **Explicación del código:**

1. **`tags` en rutas**:
   - Cada ruta se asocia con una o más etiquetas mediante el parámetro `tags`.
   - Estas etiquetas aparecen en la documentación y permiten a los usuarios navegar más fácilmente por las diferentes secciones de la API.

##### **Paso 4: Añadir ejemplos en la documentación**

FastAPI permite definir ejemplos de datos en la documentación para ayudar a los usuarios a entender qué tipo de datos se espera en las solicitudes y respuestas.

1. Añade ejemplos en el modelo Pydantic o directamente en las rutas:

    ```python
    from fastapi import FastAPI, Body
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        price: float
        description: str | None = None
        tax: float | None = None

    @app.post("/items/")
    def create_item(item: Item = Body(..., example={
        "name": "FastAPI Tutorial",
        "price": 29.99,
        "description": "A complete guide to FastAPI.",
        "tax": 5.0,
    })):
        return item
    ```

2. Revisa Swagger UI para ver cómo el ejemplo aparece en la documentación de la ruta.

##### **Explicación del código:**

1. **Añadir ejemplos con `example`**:
   - El parámetro `example` en `Body` permite definir un ejemplo de solicitud que aparecerá en la documentación.
   - Esto ayuda a los usuarios a entender rápidamente qué tipo de datos deben enviar.

##### **Paso 5: Protección de la documentación con autenticación**

En algunos casos, puede ser necesario proteger la documentación de tu API para que solo usuarios autorizados puedan acceder a ella.

1. Modifica tu archivo `main.py` para incluir la protección de la documentación:

    ```python
    from fastapi import FastAPI, Depends
    from fastapi.security import OAuth2PasswordBearer

    app = FastAPI()

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def get_current_user(token: str = Depends(oauth2_scheme)):
        return {"username": "fakeuser"}

    @app.get("/items/")
    def read_items(token: str = Depends(oauth2_scheme)):
        return [{"name": "Item 1"}, {"name": "Item 2"}]

    app = FastAPI(docs_url=None, redoc_url=None)

    @app.get("/docs", include_in_schema=False)
    def custom_swagger_ui_html(token: str = Depends(get_current_user)):
        return get_swagger_ui_html(openapi_url="/openapi.json", title="Mi API", oauth2_redirect_url="/docs/oauth2-redirect", swagger_favicon_url="https://example.com/favicon.ico")
    ```

2. Accede a la documentación en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) y observa cómo ahora se requiere autenticación para acceder.

##### **Explicación del código:**

1. **Protección con OAuth2**:
   - El uso de `OAuth2PasswordBearer` permite proteger la documentación de la API, requiriendo un token para acceder.
   - `docs_url` y `redoc_url` se establecen en `None` para deshabilitar el acceso directo a la documentación.
---

#### **9. Introducción a la asincronía en FastAPI**

La asincronía es una característica clave en FastAPI que permite mejorar el rendimiento y la escalabilidad de tus aplicaciones web. En esta sección, exploraremos qué es la asincronía, cómo se utiliza en FastAPI y cómo puede beneficiar a tu aplicación al manejar operaciones concurrentes de manera más eficiente.

##### **Paso 1: ¿Qué es la asincronía?**

La asincronía es una técnica que permite que una aplicación realice múltiples operaciones simultáneamente sin bloquear la ejecución de otras tareas. Esto es especialmente útil en aplicaciones web que necesitan manejar muchas solicitudes concurrentes o realizar operaciones de entrada/salida (I/O) que pueden llevar tiempo, como consultas a bases de datos o solicitudes a APIs externas.

1. **Síncrono vs. Asíncrono**:
   - **Síncrono**: En un modelo síncrono, cada operación se completa antes de que comience la siguiente. Esto puede llevar a bloqueos si una operación tarda mucho tiempo.
   - **Asíncrono**: En un modelo asíncrono, las operaciones pueden comenzar y completarse de manera independiente. La aplicación puede continuar ejecutando otras tareas mientras espera que una operación termine.

##### **Paso 2: Uso de funciones `async` y `await` en FastAPI**

FastAPI soporta completamente la programación asincrónica en Python mediante el uso de `async` y `await`. Estas palabras clave permiten definir y ejecutar funciones de manera asíncrona.

1. **Definir funciones asíncronas**:
   - Las funciones asíncronas se definen utilizando la palabra clave `async` antes de `def`.

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/async-endpoint/")
    async def async_endpoint():
        return {"message": "This is an asynchronous endpoint"}
    ```

2. **Esperar (await) en funciones asíncronas**:
   - Dentro de una función asíncrona, puedes usar la palabra clave `await` para esperar la finalización de otras funciones asíncronas.

    ```python
    import asyncio
    from fastapi import FastAPI

    app = FastAPI()

    async def fake_db_query():
        await asyncio.sleep(1)  # Simula una operación I/O que tarda 1 segundo
        return {"data": "fake data"}

    @app.get("/async-db/")
    async def async_db_endpoint():
        data = await fake_db_query()
        return {"data": data}
    ```

##### **Paso 3: Beneficios de la asincronía en FastAPI**

La asincronía puede ofrecer varios beneficios para tu aplicación FastAPI:

1. **Rendimiento Mejorado**:
   - Las operaciones de entrada/salida (I/O) como consultas a bases de datos o solicitudes a APIs externas pueden realizarse de manera no bloqueante, permitiendo que la aplicación maneje más solicitudes concurrentemente.

2. **Escalabilidad**:
   - Al manejar operaciones de manera asincrónica, tu aplicación puede escalar mejor al manejar un mayor número de conexiones simultáneas sin bloquear el servidor.

3. **Experiencia del Usuario**:
   - Las operaciones que requieren mucho tiempo se pueden realizar en segundo plano, mejorando la capacidad de respuesta de la aplicación y la experiencia del usuario.

##### **Paso 4: Ejemplos prácticos de asincronía**

1. **Consulta a una base de datos asíncrona**:

    ```python
    from fastapi import FastAPI
    from databases import Database

    app = FastAPI()
    database = Database("sqlite+aiosqlite:///./test.db")

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    @app.get("/async-data/")
    async def async_data_endpoint():
        query = "SELECT * FROM items"
        results = await database.fetch_all(query)
        return {"results": results}
    ```

    - En este ejemplo, usamos `databases`, una biblioteca asíncrona para consultas a bases de datos. Las funciones `startup` y `shutdown` se encargan de conectar y desconectar la base de datos al iniciar y detener la aplicación.

2. **Realización de solicitudes HTTP asíncronas**:

    ```python
    import httpx
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/async-request/")
    async def async_request():
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.example.com/data")
        return {"data": response.json()}
    ```

    - Aquí usamos `httpx`, una biblioteca asíncrona para hacer solicitudes HTTP. La función `async_request` realiza una solicitud a una API externa de manera asíncrona.

##### **Paso 5: Ejecución y pruebas**

1. Ejecuta tu aplicación con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Prueba los endpoints asíncronos**:
   - Visita [http://127.0.0.1:8000/async-endpoint](http://127.0.0.1:8000/async-endpoint) y [http://127.0.0.1:8000/async-db/](http://127.0.0.1:8000/async-db/) para verificar que los endpoints asincrónicos funcionen correctamente.

---

#### **1. Gestión de bases de datos con FastAPI y SQLAlchemy**

En esta sección, aprenderás a integrar y gestionar bases de datos en tus aplicaciones FastAPI utilizando SQLAlchemy, una biblioteca ORM (Object-Relational Mapping) que facilita la interacción con bases de datos SQL. Cubriremos desde la configuración inicial hasta la realización de operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar).

##### **Paso 1: Instalación de dependencias**

Para trabajar con SQLAlchemy y FastAPI, primero necesitas instalar las bibliotecas necesarias:

```bash
pip install sqlalchemy databases asyncpg
```

- **`sqlalchemy`**: Biblioteca ORM para Python.
- **`databases`**: Biblioteca asíncrona para consultas a bases de datos.
- **`asyncpg`**: Driver asíncrono para PostgreSQL (puedes reemplazarlo con el driver adecuado para tu base de datos).

##### **Paso 2: Configuración de SQLAlchemy con FastAPI**

1. **Configura la conexión a la base de datos**:

    Crea un archivo `database.py` para manejar la configuración de la base de datos.

    ```python
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import sessionmaker

    DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    metadata = MetaData()
    ```

    - **`DATABASE_URL`**: Reemplaza con la URL de conexión a tu base de datos.
    - **`create_engine`**: Crea una instancia del motor de base de datos.
    - **`sessionmaker`**: Crea una clase de sesión para interactuar con la base de datos.

2. **Configura el esquema de la base de datos**:

    Crea un archivo `models.py` para definir tus modelos de datos.

    ```python
    from sqlalchemy import Column, Integer, String
    from database import metadata

    class User(metadata):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        email = Column(String, unique=True, index=True)
        full_name = Column(String)
    ```

    - **`__tablename__`**: Define el nombre de la tabla en la base de datos.
    - **`Column`**: Define las columnas de la tabla.

##### **Paso 3: Crear y aplicar migraciones**

Para crear y aplicar migraciones en tu base de datos, puedes usar `Alembic`, una herramienta de migraciones para SQLAlchemy.

1. **Instala Alembic**:

    ```bash
    pip install alembic
    ```

2. **Inicializa Alembic**:

    ```bash
    alembic init alembic
    ```

    Esto creará una carpeta `alembic` con la configuración necesaria.

3. **Configura Alembic**:

    Edita el archivo `alembic.ini` y establece el `sqlalchemy.url`:

    ```ini
    sqlalchemy.url = postgresql+asyncpg://user:password@localhost/dbname
    ```

4. **Genera una nueva migración**:

    ```bash
    alembic revision --autogenerate -m "Create users table"
    ```

5. **Aplica las migraciones**:

    ```bash
    alembic upgrade head
    ```

##### **Paso 4: Operaciones CRUD básicas**

1. **Crear una nueva entrada**:

    Modifica tu archivo `main.py` para incluir las operaciones CRUD.

    ```python
    from fastapi import FastAPI, Depends
    from sqlalchemy.orm import Session
    from models import User
    from database import SessionLocal

    app = FastAPI()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.post("/users/")
    def create_user(username: str, email: str, full_name: str, db: Session = Depends(get_db)):
        db_user = User(username=username, email=email, full_name=full_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    ```

2. **Leer entradas existentes**:

    ```python
    @app.get("/users/{user_id}")
    def read_user(user_id: int, db: Session = Depends(get_db)):
        return db.query(User).filter(User.id == user_id).first()
    ```

3. **Actualizar una entrada**:

    ```python
    @app.put("/users/{user_id}")
    def update_user(user_id: int, username: str, email: str, full_name: str, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.username = username
            user.email = email
            user.full_name = full_name
            db.commit()
            db.refresh(user)
            return user
        return {"error": "User not found"}
    ```

4. **Eliminar una entrada**:

    ```python
    @app.delete("/users/{user_id}")
    def delete_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return {"message": "User deleted"}
        return {"error": "User not found"}
    ```

##### **Paso 5: Pruebas y verificación**

1. Ejecuta tu aplicación con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. Prueba las operaciones CRUD en Swagger UI visitando [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Parte 2: Intermedio

---

#### **2. Creación de modelos y esquemas**

En esta sección, exploraremos cómo crear y gestionar modelos y esquemas en FastAPI utilizando SQLAlchemy y Pydantic. Los modelos representan las estructuras de datos en la base de datos, mientras que los esquemas definen cómo se estructuran los datos que se envían y reciben a través de la API.

##### **Paso 1: Definición de modelos con SQLAlchemy**

Los modelos de SQLAlchemy representan las tablas en la base de datos y sus columnas. Cada modelo debe heredar de `Base` y definir sus columnas como atributos de clase.

1. **Definir un modelo de SQLAlchemy**:

    Crea o modifica el archivo `models.py` para definir un modelo de usuario:

    ```python
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        email = Column(String, unique=True, index=True)
        full_name = Column(String)
    ```

    - **`Base`**: Clase base para todos los modelos.
    - **`__tablename__`**: Nombre de la tabla en la base de datos.
    - **`Column`**: Define las columnas de la tabla y sus tipos.

##### **Paso 2: Definición de esquemas con Pydantic**

Los esquemas de Pydantic se utilizan para validar y documentar los datos que entran y salen de tu API. Los esquemas son modelos de datos que definen cómo se espera que los datos estén estructurados.

1. **Definir un esquema con Pydantic**:

    Crea un archivo `schemas.py` para definir los esquemas de datos:

    ```python
    from pydantic import BaseModel
    from typing import Optional

    class UserBase(BaseModel):
        username: str
        email: str
        full_name: Optional[str] = None

    class UserCreate(UserBase):
        pass

    class UserRead(UserBase):
        id: int

        class Config:
            orm_mode = True
    ```

    - **`UserBase`**: Define los campos básicos de un usuario.
    - **`UserCreate`**: Esquema utilizado al crear un nuevo usuario.
    - **`UserRead`**: Esquema utilizado para leer la información de un usuario, incluyendo el ID.
    - **`orm_mode`**: Permite a Pydantic convertir los datos de SQLAlchemy en modelos Pydantic.

##### **Paso 3: Integrar modelos y esquemas con FastAPI**

Integra los modelos y esquemas en tus rutas para manejar la entrada y salida de datos.

1. **Crear un nuevo usuario usando esquemas**:

    Modifica tu archivo `main.py` para usar los esquemas en las operaciones CRUD:

    ```python
    from fastapi import FastAPI, Depends
    from sqlalchemy.orm import Session
    from models import User
    from schemas import UserCreate, UserRead
    from database import SessionLocal

    app = FastAPI()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.post("/users/", response_model=UserRead)
    def create_user(user: UserCreate, db: Session = Depends(get_db)):
        db_user = User(username=user.username, email=user.email, full_name=user.full_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @app.get("/users/{user_id}", response_model=UserRead)
    def read_user(user_id: int, db: Session = Depends(get_db)):
        return db.query(User).filter(User.id == user_id).first()
    ```

    - **`response_model`**: Define el esquema que se utilizará para la respuesta de la ruta.
    - **`UserCreate`**: Esquema para validar los datos de entrada al crear un usuario.
    - **`UserRead`**: Esquema para formatear la respuesta al leer un usuario.

##### **Paso 4: Validación y documentación de datos**

Pydantic proporciona validación automática y documentación para los datos que se envían y reciben en las rutas de tu API.

1. **Validación**:
   - Si los datos enviados en una solicitud no cumplen con el esquema definido, FastAPI devolverá automáticamente un error 422 (Unprocessable Entity) con detalles sobre la validación fallida.

2. **Documentación**:
   - Los esquemas se utilizan para generar la documentación automática de la API en Swagger UI, proporcionando información clara sobre los datos esperados y devueltos por cada ruta.

##### **Paso 5: Ejemplos prácticos**

1. **Definir modelos y esquemas adicionales**:

    Puedes definir modelos y esquemas adicionales para otras entidades en tu aplicación. Por ejemplo, un modelo para `Item` y sus esquemas correspondientes:

    ```python
    # models.py
    class Item(Base):
        __tablename__ = "items"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        price = Column(Integer)

    # schemas.py
    class ItemBase(BaseModel):
        name: str
        description: Optional[str] = None
        price: int

    class ItemCreate(ItemBase):
        pass

    class ItemRead(ItemBase):
        id: int

        class Config:
            orm_mode = True
    ```

2. **Actualizar rutas para manejar nuevos modelos**:

    ```python
    @app.post("/items/", response_model=ItemRead)
    def create_item(item: ItemCreate, db: Session = Depends(get_db)):
        db_item = Item(name=item.name, description=item.description, price=item.price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @app.get("/items/{item_id}", response_model=ItemRead)
    def read_item(item_id: int, db: Session = Depends(get_db)):
        return db.query(Item).filter(Item.id == item_id).first()
    ```

---

#### **3. Autenticación y autorización**

En esta sección, abordaremos cómo implementar autenticación y autorización en FastAPI para proteger tus rutas y controlar el acceso a los recursos. La autenticación permite verificar la identidad de los usuarios, mientras que la autorización define qué recursos pueden acceder esos usuarios.

##### **Paso 1: Introducción a la autenticación y autorización**

1. **Autenticación**: El proceso de verificar la identidad del usuario. En FastAPI, se puede implementar mediante tokens JWT (JSON Web Tokens) o autenticación básica.
2. **Autorización**: El proceso de determinar qué acciones puede realizar un usuario autenticado. Esto se basa en los roles o permisos asignados.

##### **Paso 2: Instalación de dependencias**

Para manejar autenticación y autorización, necesitaremos algunas bibliotecas adicionales:

```bash
pip install passlib[bcrypt] pyjwt
```

- **`passlib[bcrypt]`**: Biblioteca para el hashing de contraseñas.
- **`pyjwt`**: Biblioteca para trabajar con JSON Web Tokens.

##### **Paso 3: Configuración de autenticación básica con JWT**

1. **Configuración de JWT**:

    Crea un archivo `auth.py` para manejar la autenticación.

    ```python
    from datetime import datetime, timedelta
    from typing import Union

    from jose import JWTError, jwt
    from passlib.context import CryptContext
    from pydantic import BaseModel

    SECRET_KEY = "your-secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    class Token(BaseModel):
        access_token: str
        token_type: str

    class TokenData(BaseModel):
        username: str

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(token: str) -> TokenData:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise JWTError
            token_data = TokenData(username=username)
        except JWTError:
            raise JWTError
        return token_data
    ```

    - **`SECRET_KEY`**: Clave secreta utilizada para firmar el JWT.
    - **`ALGORITHM`**: Algoritmo de cifrado para el JWT.
    - **`create_access_token`**: Función para crear un token JWT.
    - **`verify_token`**: Función para verificar la validez de un token JWT.

2. **Agregar autenticación a las rutas**:

    Modifica tu archivo `main.py` para incluir las funciones de autenticación.

    ```python
    from fastapi import FastAPI, Depends, HTTPException, status
    from sqlalchemy.orm import Session
    from auth import create_access_token, verify_token, get_password_hash, verify_password
    from schemas import UserCreate, UserRead
    from database import SessionLocal
    from models import User

    app = FastAPI()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def authenticate_user(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.password):
            return False
        return user

    @app.post("/token", response_model=Token)
    def login(form_data: UserCreate, db: Session = Depends(get_db)):
        user = authenticate_user(db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def get_current_user(token: str = Depends(oauth2_scheme)):
        token_data = verify_token(token)
        return token_data

    @app.get("/users/me", response_model=UserRead)
    def read_users_me(current_user: TokenData = Depends(get_current_user)):
        return current_user
    ```

    - **`/token`**: Ruta para obtener un token JWT.
    - **`authenticate_user`**: Función para autenticar al usuario.
    - **`get_current_user`**: Dependencia que valida el token y obtiene la información del usuario.

##### **Paso 4: Implementar autorización basada en roles**

Para agregar autorización basada en roles, puedes modificar la función `get_current_user` y las rutas para verificar los permisos del usuario.

1. **Agregar roles a los modelos**:

    Modifica tu modelo de usuario para incluir roles.

    ```python
    # models.py
    from sqlalchemy import Column, Integer, String, Enum
    from enum import Enum as PyEnum

    class Role(PyEnum):
        user = "user"
        admin = "admin"

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        email = Column(String, unique=True, index=True)
        full_name = Column(String)
        password = Column(String)
        role = Column(Enum(Role), default=Role.user)
    ```

2. **Verificar roles en las rutas**:

    Modifica tus rutas para verificar roles de usuario.

    ```python
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def get_current_user(token: str = Depends(oauth2_scheme)):
        token_data = verify_token(token)
        return token_data

    def get_current_active_user(current_user: TokenData = Depends(get_current_user)):
        if current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions",
            )
        return current_user

    @app.get("/admin", response_model=UserRead)
    def read_admin_data(current_user: TokenData = Depends(get_current_active_user)):
        return {"message": "Admin data accessed"}
    ```

    - **`get_current_active_user`**: Dependencia que verifica si el usuario tiene el rol adecuado para acceder a ciertas rutas.

##### **Paso 5: Pruebas y verificación**

1. Ejecuta tu aplicación con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Prueba la autenticación y autorización**:

    - **Obtener un token**: Realiza una solicitud POST a `/token` con las credenciales del usuario.
    - **Acceder a rutas protegidas**: Usa el token obtenido para acceder a rutas protegidas y verifica que las rutas funcionen según los permisos del usuario.

---

#### **4. Middleware y gestión de CORS**

En esta sección, aprenderás a configurar middleware y manejar CORS (Cross-Origin Resource Sharing) en FastAPI. El middleware permite modificar las solicitudes y respuestas globalmente, mientras que CORS controla qué dominios externos pueden interactuar con tu API.

##### **Paso 1: Configuración básica de Middleware**

Middleware en FastAPI permite interceptar y modificar las solicitudes y respuestas. Puedes usar middleware para tareas como el manejo de sesiones, la adición de encabezados personalizados, o el registro de actividades.

1. **Crear un middleware personalizado**:

    Puedes crear middleware personalizado para agregar funcionalidad a tu aplicación. A continuación, se muestra un ejemplo de un middleware que registra cada solicitud y respuesta:

    ```python
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.requests import Request
    from starlette.responses import Response
    import logging

    logging.basicConfig(level=logging.INFO)

    class CustomMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request: Request, call_next):
            logging.info(f"Request: {request.method} {request.url}")
            response = await call_next(request)
            logging.info(f"Response status: {response.status_code}")
            return response

    app.add_middleware(CustomMiddleware)
    ```

    - **`CustomMiddleware`**: Define un middleware que registra solicitudes y respuestas.
    - **`dispatch`**: Método que maneja las solicitudes y respuestas.

##### **Paso 2: Gestión de CORS**

CORS permite a las aplicaciones web en un dominio acceder a recursos en otro dominio. Para habilitar CORS en FastAPI, utiliza el middleware de CORS.

1. **Instalar `fastapi.middleware.cors`**:

    La biblioteca `fastapi.middleware.cors` proporciona el middleware necesario para manejar CORS.

    ```bash
    pip install fastapi[all]
    ```

2. **Configurar CORS**:

    Configura el middleware de CORS para permitir solicitudes desde ciertos orígenes.

    ```python
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permitir todos los orígenes
        allow_credentials=True,
        allow_methods=["*"],  # Permitir todos los métodos HTTP
        allow_headers=["*"],  # Permitir todos los encabezados
    )
    ```

    - **`allow_origins`**: Lista de orígenes permitidos. Usa `["*"]` para permitir todos los orígenes, o especifica dominios concretos.
    - **`allow_credentials`**: Permite el uso de cookies y otros credenciales.
    - **`allow_methods`**: Lista de métodos HTTP permitidos.
    - **`allow_headers`**: Lista de encabezados permitidos.

##### **Paso 3: Uso avanzado de Middleware y CORS**

1. **Agregar encabezados personalizados**:

    Puedes modificar las respuestas para incluir encabezados personalizados, como para la seguridad:

    ```python
    class CustomSecurityMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request: Request, call_next):
            response = await call_next(request)
            response.headers["X-Content-Type-Options"] = "nosniff"
            response.headers["X-Frame-Options"] = "DENY"
            return response

    app.add_middleware(CustomSecurityMiddleware)
    ```

    - **`CustomSecurityMiddleware`**: Middleware que agrega encabezados de seguridad a las respuestas.

2. **Configurar CORS para diferentes entornos**:

    Es común tener configuraciones de CORS diferentes para desarrollo y producción. Puedes ajustar la configuración según el entorno:

    ```python
    import os

    if os.getenv("ENV") == "production":
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["https://yourproductiondomain.com"],
            allow_credentials=True,
            allow_methods=["GET", "POST"],
            allow_headers=["Authorization"],
        )
    else:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ```

    - **`os.getenv("ENV")`**: Lee el entorno de ejecución y aplica la configuración de CORS correspondiente.

##### **Paso 4: Pruebas y verificación**

1. Ejecuta tu aplicación con Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. **Verifica el middleware**:

    - Realiza solicitudes a tu API y verifica que los mensajes de registro aparezcan en los logs.
    - Verifica que los encabezados personalizados se incluyan en las respuestas.

3. **Verifica la configuración de CORS**:

    - Realiza solicitudes desde un origen diferente y asegúrate de que los encabezados de CORS se ajusten según la configuración.

---

#### **5. Creación y uso de dependencias**

En FastAPI, las dependencias permiten reutilizar y compartir lógica entre las rutas de tu API de manera modular y eficiente. Las dependencias pueden ser utilizadas para manejar tareas comunes, como la autenticación de usuarios, la validación de datos, y la configuración de conexiones a bases de datos.

##### **Paso 1: Introducción a las dependencias**

Las dependencias en FastAPI son funciones que se definen para proporcionar datos o realizar tareas antes de que se ejecute la función de vista (endpoint). Se utilizan para:

- **Inyección de dependencias**: Proporcionar datos o servicios a las rutas.
- **Modularización**: Compartir lógica común entre varias rutas.
- **Validación**: Validar datos y manejar errores de manera centralizada.

##### **Paso 2: Definir y utilizar dependencias simples**

1. **Crear una dependencia simple**:

    Una dependencia es una función que se puede usar en las rutas para proporcionar datos o realizar tareas. Por ejemplo, puedes crear una dependencia para obtener una base de datos.

    ```python
    from fastapi import Depends
    from sqlalchemy.orm import Session
    from database import SessionLocal

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    ```

    - **`get_db`**: Crea una sesión de base de datos y la cierra al finalizar.

2. **Usar la dependencia en una ruta**:

    Puedes usar la dependencia `get_db` en una ruta para obtener acceso a la base de datos.

    ```python
    from fastapi import FastAPI, Depends
    from sqlalchemy.orm import Session
    from models import User
    from schemas import UserRead

    app = FastAPI()

    @app.get("/users/{user_id}", response_model=UserRead)
    def read_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.id == user_id).first()
        return user
    ```

    - **`Depends(get_db)`**: Inyecta la dependencia en la ruta para obtener la sesión de la base de datos.

##### **Paso 3: Crear dependencias avanzadas**

1. **Dependencia para autenticación**:

    Puedes crear una dependencia para autenticar usuarios usando JWT.

    ```python
    from fastapi import HTTPException, Depends, status
    from auth import verify_token, TokenData

    def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            token_data = verify_token(token)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return token_data
    ```

    - **`get_current_user`**: Dependencia para obtener y verificar el usuario actual a partir del token JWT.

2. **Usar la dependencia de autenticación**:

    Aplica la dependencia `get_current_user` para proteger rutas que requieren autenticación.

    ```python
    @app.get("/users/me", response_model=UserRead)
    def read_users_me(current_user: TokenData = Depends(get_current_user)):
        return current_user
    ```

    - **`Depends(get_current_user)`**: Inyecta la dependencia de autenticación en la ruta.

##### **Paso 4: Manejar dependencias con parámetros**

1. **Dependencia con parámetros**:

    Puedes crear dependencias que acepten parámetros y usarlas en las rutas.

    ```python
    from fastapi import Query

    def get_query_param(q: str = Query(..., min_length=3, max_length=50)):
        return q
    ```

    - **`Query`**: Define parámetros de consulta para la dependencia.

2. **Usar la dependencia con parámetros**:

    Aplica la dependencia `get_query_param` en una ruta.

    ```python
    @app.get("/items/")
    def read_items(query_param: str = Depends(get_query_param)):
        return {"query_param": query_param}
    ```

    - **`Depends(get_query_param)`**: Inyecta la dependencia que maneja el parámetro de consulta en la ruta.

##### **Paso 5: Dependencias en aplicaciones complejas**

1. **Composición de dependencias**:

    Puedes combinar varias dependencias en una sola ruta para crear comportamientos más complejos.

    ```python
    def common_dependency(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
        return db, current_user

    @app.get("/protected-data/")
    def get_protected_data(deps: tuple = Depends(common_dependency)):
        db, current_user = deps
        # Lógica para manejar datos protegidos
        return {"user": current_user.username}
    ```

    - **`common_dependency`**: Dependencia que combina otras dependencias.

---

#### **6. Manejo de archivos y formularios**

En esta sección, aprenderás a manejar archivos y formularios en FastAPI. Aprenderás a recibir archivos subidos por el usuario, procesar datos de formularios y enviar archivos como respuesta.

##### **Paso 1: Manejo de archivos subidos**

1. **Recibir archivos en FastAPI**:

    Puedes recibir archivos subidos por el usuario usando el tipo `UploadFile`. FastAPI permite manejar archivos de manera eficiente sin necesidad de guardarlos en disco.

    ```python
    from fastapi import FastAPI, File, UploadFile

    app = FastAPI()

    @app.post("/uploadfile/")
    async def upload_file(file: UploadFile = File(...)):
        return {"filename": file.filename, "content_type": file.content_type}
    ```

    - **`UploadFile`**: Tipo de archivo que permite manejar archivos subidos.
    - **`File(...)`**: Indicador de que el archivo es obligatorio.

2. **Leer contenido del archivo**:

    Puedes leer el contenido del archivo subido de diferentes maneras:

    ```python
    @app.post("/uploadfile/")
    async def upload_file(file: UploadFile = File(...)):
        content = await file.read()
        return {"filename": file.filename, "content_type": file.content_type, "file_content": content.decode("utf-8")}
    ```

    - **`await file.read()`**: Lee el contenido del archivo de manera asíncrona.

##### **Paso 2: Procesar datos de formularios**

1. **Recibir datos de formularios en FastAPI**:

    Para recibir datos de formularios, puedes usar el tipo `Form` de FastAPI. Puedes combinar datos de formularios con archivos si es necesario.

    ```python
    from fastapi import FastAPI, Form, File, UploadFile

    app = FastAPI()

    @app.post("/submit-form/")
    async def submit_form(name: str = Form(...), age: int = Form(...), file: UploadFile = File(...)):
        return {"name": name, "age": age, "filename": file.filename}
    ```

    - **`Form(...)`**: Indicador de que el campo del formulario es obligatorio.

2. **Procesar datos y archivos juntos**:

    Puedes combinar el manejo de datos del formulario con archivos para crear endpoints más complejos.

    ```python
    @app.post("/submit-form/")
    async def submit_form(name: str = Form(...), age: int = Form(...), file: UploadFile = File(...)):
        file_content = await file.read()
        return {"name": name, "age": age, "filename": file.filename, "file_content": file_content.decode("utf-8")}
    ```

    - **`file_content.decode("utf-8")`**: Decodifica el contenido del archivo como texto.

##### **Paso 3: Enviar archivos como respuesta**

1. **Enviar archivos como respuesta**:

    Puedes enviar archivos como respuesta en FastAPI usando el tipo de respuesta `FileResponse`.

    ```python
    from fastapi import FastAPI
    from fastapi.responses import FileResponse

    app = FastAPI()

    @app.get("/download-file/")
    async def download_file():
        file_path = "path/to/your/file.txt"
        return FileResponse(file_path, media_type='text/plain', filename="file.txt")
    ```

    - **`FileResponse`**: Envía un archivo como respuesta HTTP.
    - **`media_type`**: Tipo de contenido del archivo.
    - **`filename`**: Nombre del archivo que se descarga.

##### **Paso 4: Validación y manejo de errores**

1. **Validación de archivos**:

    Puedes agregar validación para asegurarte de que los archivos subidos cumplan con ciertos criterios.

    ```python
    from fastapi import HTTPException

    @app.post("/uploadfile/")
    async def upload_file(file: UploadFile = File(...)):
        if file.content_type != 'text/plain':
            raise HTTPException(status_code=400, detail="Invalid file type")
        content = await file.read()
        return {"filename": file.filename, "content_type": file.content_type, "file_content": content.decode("utf-8")}
    ```

    - **`HTTPException`**: Lanza una excepción HTTP si el archivo no cumple con los requisitos.

2. **Manejo de errores al leer archivos**:

    Maneja posibles errores al procesar archivos, como problemas al leer el contenido.

    ```python
    @app.post("/uploadfile/")
    async def upload_file(file: UploadFile = File(...)):
        try:
            content = await file.read()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
        return {"filename": file.filename, "content_type": file.content_type, "file_content": content.decode("utf-8")}
    ```

    - **`try` / `except`**: Maneja errores al leer el archivo.

---

#### **7. Implementación de WebSockets**

Los WebSockets permiten la comunicación bidireccional entre el servidor y el cliente en tiempo real. FastAPI soporta WebSockets de manera eficiente, lo que te permite construir aplicaciones interactivas y en tiempo real, como chats en vivo, notificaciones, y actualizaciones de datos en tiempo real.

##### **Paso 1: Introducción a WebSockets en FastAPI**

1. **Instalación y requisitos**:

    No necesitas instalar paquetes adicionales para usar WebSockets con FastAPI si ya tienes `fastapi` y `uvicorn`. Asegúrate de que `uvicorn` esté instalado para correr el servidor.

    ```bash
    pip install fastapi uvicorn
    ```

2. **Estructura básica de WebSockets**:

    FastAPI proporciona una manera sencilla de definir y manejar conexiones WebSocket. La comunicación se realiza a través de métodos `send` y `receive` en una conexión WebSocket.

##### **Paso 2: Crear un WebSocket básico**

1. **Definir un endpoint WebSocket**:

    Puedes definir un endpoint WebSocket que maneje la comunicación en tiempo real. A continuación se muestra un ejemplo simple de un servidor WebSocket que recibe mensajes del cliente y los devuelve.

    ```python
    from fastapi import FastAPI, WebSocket

    app = FastAPI()

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    ```

    - **`websocket.accept()`**: Acepta la conexión WebSocket.
    - **`websocket.receive_text()`**: Recibe un mensaje de texto del cliente.
    - **`websocket.send_text()`**: Envía un mensaje de texto al cliente.

##### **Paso 3: Interacción con el cliente**

1. **Cliente WebSocket en HTML**:

    Puedes usar JavaScript en el lado del cliente para conectarte al WebSocket y enviar/recibir mensajes.

    ```html
    <!DOCTYPE html>
    <html>
    <body>
        <h2>WebSocket Example</h2>
        <textarea id="messages" cols="30" rows="10" readonly></textarea><br>
        <input id="messageInput" type="text"><br>
        <button onclick="sendMessage()">Send</button>

        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");

            ws.onmessage = function(event) {
                const messages = document.getElementById("messages");
                messages.value += '\n' + event.data;
            };

            function sendMessage() {
                const input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
    </html>
    ```

    - **`WebSocket`**: Crea una conexión WebSocket al servidor.
    - **`ws.onmessage`**: Maneja los mensajes recibidos del servidor.
    - **`ws.send`**: Envía mensajes al servidor.

##### **Paso 4: Manejo de múltiples clientes**

1. **Crear un servidor WebSocket que maneje múltiples clientes**:

    Puedes mantener una lista de conexiones WebSocket activas y enviar mensajes a todos los clientes conectados.

    ```python
    from fastapi import FastAPI, WebSocket
    from typing import List

    app = FastAPI()
    connections: List[WebSocket] = []

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        connections.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                for connection in connections:
                    if connection is not websocket:
                        await connection.send_text(f"Message from another user: {data}")
        except:
            connections.remove(websocket)
    ```

    - **`connections`**: Lista que almacena las conexiones WebSocket activas.
    - **`for connection in connections`**: Envía mensajes a todos los clientes conectados, excepto al remitente.

##### **Paso 5: Seguridad y autenticación**

1. **Autenticación de WebSockets**:

    Puedes agregar autenticación a tus conexiones WebSocket para asegurar que solo usuarios autorizados se conecten.

    ```python
    from fastapi import Depends, WebSocket, HTTPException
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        # Lógica para verificar el token
        if token != "valid_token":
            raise HTTPException(status_code=401, detail="Invalid token")
        return token

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_current_user)):
        await websocket.accept()
        # Resto de la lógica del WebSocket
    ```

    - **`Depends(oauth2_scheme)`**: Dependencia que maneja la autenticación.
    - **`get_current_user`**: Verifica el token para autenticar la conexión.

---


#### **1. Optimización y escalabilidad**

En esta sección, exploraremos técnicas avanzadas para optimizar el rendimiento de tu aplicación FastAPI y escalarla para manejar una mayor carga de tráfico. Aprenderás sobre cómo aprovechar el poder de las configuraciones asíncronas, cómo implementar técnicas de caché y balanceo de carga, y cómo utilizar herramientas de monitoreo para asegurarte de que tu aplicación se mantenga rápida y estable bajo presión.

##### **Optimización del rendimiento**

1. **Configuración asíncrona avanzada**:
    - Aprovecha la asincronía para manejar más solicitudes simultáneas sin bloquear el servidor.
    - Usa `async` y `await` correctamente para mejorar la eficiencia de las operaciones de I/O.

2. **Caché y almacenamiento en memoria**:
    - Implementa estrategias de caché con Redis o Memcached para reducir la carga en la base de datos.
    - Usa `fastapi_cache` o técnicas personalizadas para cachear resultados de consultas frecuentes.

3. **Minimización de latencia**:
    - Usa HTTP/2 para mejorar la velocidad de transferencia de datos.
    - Implementa Compresión Gzip para reducir el tamaño de las respuestas.

##### **Escalabilidad**

1. **Balanceo de carga**:
    - Configura un balanceador de carga como Nginx o HAProxy para distribuir las solicitudes entre múltiples instancias de tu aplicación.
    - Implementa políticas de balanceo de carga como Round Robin o Least Connections.

2. **Escalado horizontal**:
    - Usa herramientas como Kubernetes o Docker Swarm para escalar horizontalmente tu aplicación.
    - Implementa autoescalado basado en métricas de uso (CPU, memoria).

3. **Uso de servicios en la nube**:
    - Aprovecha servicios en la nube como AWS Lambda, Google Cloud Run, o Azure Functions para escalar de manera dinámica.
    - Configura bases de datos escalables como Amazon Aurora o Google Cloud SQL.

##### **Monitoreo y análisis**

1. **Monitoreo del rendimiento**:
    - Usa herramientas como Prometheus y Grafana para monitorear el rendimiento en tiempo real.
    - Configura alertas basadas en métricas clave (tiempo de respuesta, uso de recursos).

2. **Análisis de registros**:
    - Implementa soluciones de gestión de logs como ELK Stack (Elasticsearch, Logstash, Kibana) para analizar y visualizar registros.
    - Configura logging asíncrono para reducir el impacto en el rendimiento.

3. **Pruebas de carga**:
    - Realiza pruebas de carga con herramientas como Locust o Apache JMeter para simular tráfico y medir la capacidad de tu aplicación.
    - Identifica cuellos de botella y optimiza el código o la infraestructura en consecuencia.

---

#### **2. Despliegue en producción con Docker**

El despliegue en producción es un paso crítico para asegurar que tu aplicación FastAPI funcione de manera eficiente y segura en un entorno real. Docker se ha convertido en una herramienta estándar para empaquetar aplicaciones, facilitando su despliegue en cualquier entorno, independientemente de las diferencias en configuraciones del sistema operativo o software instalado.

##### **Paso 1: Crear un Dockerfile para FastAPI**

1. **Estructura básica del Dockerfile**:

    Un Dockerfile define el entorno en el que se ejecutará tu aplicación. Aquí tienes un ejemplo básico para una aplicación FastAPI:

    ```dockerfile
    # Utiliza una imagen base ligera de Python
    FROM python:3.11-slim

    # Establece el directorio de trabajo en el contenedor
    WORKDIR /app

    # Copia los archivos necesarios al contenedor
    COPY . /app

    # Instala las dependencias de la aplicación
    RUN pip install --no-cache-dir --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt

    # Expone el puerto en el que la aplicación correrá
    EXPOSE 8000

    # Comando para ejecutar la aplicación
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

    - **`FROM python:3.11-slim`**: Usa una imagen base ligera de Python.
    - **`WORKDIR /app`**: Establece el directorio de trabajo en el contenedor.
    - **`COPY . /app`**: Copia los archivos de la aplicación al contenedor.
    - **`RUN pip install`**: Instala las dependencias listadas en `requirements.txt`.
    - **`EXPOSE 8000`**: Expone el puerto 8000, donde se ejecutará la aplicación.
    - **`CMD ["uvicorn", "main:app"]`**: Comando que inicia la aplicación usando Uvicorn.

2. **Optimización del Dockerfile**:

    Optimiza el Dockerfile para crear imágenes más ligeras y rápidas:

    - **Usar capas intermedias**: Cada comando en el Dockerfile crea una nueva capa, por lo que es importante combinar comandos relacionados.
    - **Eliminar archivos innecesarios**: Usa `.dockerignore` para excluir archivos que no son necesarios en la imagen final.

    ```dockerfile
    # Añadir optimizaciones al Dockerfile
    FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt /app/
    RUN pip install --no-cache-dir --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt

    COPY . /app

    EXPOSE 8000

    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

##### **Paso 2: Construir y correr el contenedor Docker**

1. **Construir la imagen Docker**:

    Usa el comando `docker build` para construir la imagen:

    ```bash
    docker build -t myfastapiapp .
    ```

    - **`-t myfastapiapp`**: Etiqueta la imagen como `myfastapiapp`.
    - **`.`**: Indica que el Dockerfile está en el directorio actual.

2. **Correr el contenedor Docker**:

    Una vez construida la imagen, puedes correr el contenedor:

    ```bash
    docker run -d --name myfastapiapp_container -p 8000:8000 myfastapiapp
    ```

    - **`-d`**: Corre el contenedor en segundo plano (detached).
    - **`--name myfastapiapp_container`**: Nombra el contenedor `myfastapiapp_container`.
    - **`-p 8000:8000`**: Mapea el puerto 8000 del contenedor al puerto 8000 del host.

##### **Paso 3: Despliegue en producción**

1. **Configuración para producción**:

    Asegúrate de que tu aplicación esté configurada para correr en un entorno de producción:

    - **Usar Gunicorn**: Aunque Uvicorn es excelente para desarrollo, Gunicorn es más robusto para producción.
    - **Optimizar la configuración de Uvicorn**: Usa múltiples workers y threads para manejar más solicitudes concurrentes.

    ```dockerfile
    FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt /app/
    RUN pip install --no-cache-dir --upgrade pip \
        && pip install --no-cache-dir -r requirements.txt

    COPY . /app

    EXPOSE 8000

    CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--workers", "4", "--bind", "0.0.0.0:8000"]
    ```

2. **Integración con Docker Compose**:

    Docker Compose permite definir y correr aplicaciones multi-contenedor. Aquí tienes un ejemplo básico de cómo usarlo:

    ```yaml
    version: '3.8'
    services:
      web:
        build: .
        ports:
          - "8000:8000"
        environment:
          - ENV=production
    ```

    - **`services`**: Define los servicios que correrán en contenedores.
    - **`build: .`**: Construye la imagen Docker usando el Dockerfile en el directorio actual.
    - **`ports`**: Mapea el puerto 8000 del contenedor al puerto 8000 del host.
    - **`environment`**: Define variables de entorno para la aplicación.

##### **Paso 4: Monitoreo y manejo de logs**

1. **Gestión de logs**:

    Configura el manejo de logs en producción:

    - **Volúmenes para logs**: Usa volúmenes Docker para guardar logs persistentes.
    - **Integración con servicios de logs**: Configura la exportación de logs a servicios como ELK, Datadog, o AWS CloudWatch.

    ```yaml
    services:
      web:
        build: .
        ports:
          - "8000:8000"
        volumes:
          - ./logs:/app/logs
        logging:
          driver: "json-file"
          options:
            max-size: "10m"
            max-file: "3"
    ```

    - **`volumes`**: Mapea un directorio en el host para almacenar logs.
    - **`logging`**: Configura la gestión de logs con limitación de tamaño y rotación.

---


#### **3. Testing avanzado y CI/CD**

El testing avanzado y la integración continua/despliegue continuo (CI/CD) son componentes esenciales para mantener la calidad y la estabilidad de las aplicaciones en producción. En esta sección, exploraremos cómo implementar pruebas avanzadas en FastAPI, automatizar el proceso de despliegue, y cómo utilizar herramientas de CI/CD para asegurar que cada cambio en el código sea probado y desplegado de manera eficiente.

##### **Paso 1: Testing avanzado en FastAPI**

1. **Pruebas unitarias y de integración**:

    - **Pruebas unitarias**: Se enfocan en probar funciones individuales. Puedes usar `pytest` para escribir pruebas unitarias en FastAPI.

    ```python
    from fastapi.testclient import TestClient
    from .main import app

    client = TestClient(app)

    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}
    ```

    - **Pruebas de integración**: Verifican cómo diferentes partes de la aplicación trabajan juntas. Puedes probar endpoints completos, incluyendo la interacción con bases de datos.

    ```python
    def test_create_item():
        response = client.post("/items/", json={"name": "Test item", "price": 10.0})
        assert response.status_code == 200
        assert response.json()["name"] == "Test item"
    ```

2. **Mocking y pruebas aisladas**:

    - **Uso de `pytest-mock`**: Para simular dependencias externas como bases de datos o servicios externos.

    ```python
    from unittest.mock import patch

    @patch("app.database.get_db")
    def test_read_item(mock_db):
        mock_db.return_value.query.return_value.filter.return_value.first.return_value = {"id": 1, "name": "Mocked item"}
        response = client.get("/items/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Mocked item"
    ```

    - **Simulación de respuestas HTTP**: Utiliza `responses` para simular respuestas de APIs externas.

    ```python
    import responses

    @responses.activate
    def test_external_api_call():
        responses.add(responses.GET, 'http://api.example.com/data', json={"key": "value"}, status=200)
        response = client.get("/external-data")
        assert response.status_code == 200
        assert response.json() == {"key": "value"}
    ```

3. **Pruebas de rendimiento y carga**:

    - **Uso de `locust`**: Para simular tráfico y medir el rendimiento bajo carga.

    ```python
    from locust import HttpUser, task, between

    class LoadTestUser(HttpUser):
        wait_time = between(1, 5)

        @task
        def load_test(self):
            self.client.get("/items/")
    ```

    - **Integración con `pytest-benchmark`**: Para medir y comparar el rendimiento de diferentes partes de la aplicación.

    ```python
    def test_benchmark_endpoint(benchmark):
        result = benchmark(client.get, "/items/")
        assert result.status_code == 200
    ```

##### **Paso 2: Configuración de CI/CD**

1. **Configurar un pipeline de CI/CD**:

    - **Uso de GitHub Actions**: GitHub Actions permite automatizar el proceso de testing y despliegue directamente desde tu repositorio.

    ```yaml
    name: CI/CD Pipeline

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2

        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.11'

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
            pip install pytest pytest-cov

        - name: Run tests
          run: |
            pytest --cov=app tests/

      deploy:
        needs: test
        runs-on: ubuntu-latest
        if: github.ref == 'refs/heads/main'

        steps:
        - uses: actions/checkout@v2

        - name: Deploy to Production
          run: |
            echo "Deploying application..."
            # Añadir comandos de despliegue (ej. Docker, SSH)
    ```

    - **Integración con Docker**: Configura tu pipeline para construir y publicar imágenes Docker automáticamente.

    ```yaml
    - name: Build and push Docker image
      uses: docker/build-push-action@v2
      with:
        context: .
        push: true
        tags: user/repo:latest
    ```

2. **Despliegue continuo**:

    - **Uso de servicios como Heroku, AWS, GCP**: Configura tu pipeline para que el despliegue ocurra automáticamente después de que se pasen todos los tests.

    - **Monitoreo de despliegue**: Implementa monitoreo para detectar errores y revertir despliegues fallidos automáticamente.

##### **Paso 3: Estrategias avanzadas de CI/CD**

1. **Despliegue progresivo (Canary releases)**:

    - **Despliegue controlado**: Despliega una nueva versión de la aplicación a un subconjunto de usuarios antes de lanzarla completamente.

    ```yaml
    - name: Canary Release
      run: |
        # Comandos para despliegue canario
    ```

2. **Pruebas automáticas de regresión**:

    - **Configuración de pruebas de regresión**: Asegura que nuevas actualizaciones no rompan funcionalidades existentes.

3. **Integración con herramientas de seguridad**:

    - **Análisis de seguridad en el pipeline**: Usa herramientas como `bandit` o `safety` para detectar vulnerabilidades en el código.

    ```yaml
    - name: Security check
      run: |
        pip install bandit
        bandit -r app/
    ```

---

#### **4. Integración con otras tecnologías (Celery, Redis)**

Integrar FastAPI con tecnologías como Celery y Redis te permite manejar tareas en segundo plano y gestionar datos de manera eficiente, lo que es crucial para aplicaciones avanzadas que requieren un procesamiento asíncrono y una gestión rápida de sesiones y caché. En esta sección, aprenderás cómo integrar estas tecnologías en tu aplicación FastAPI.

##### **Paso 1: Integración con Celery para tareas en segundo plano**

1. **Configurar Celery en FastAPI**:

    - **Instalación de Celery y librerías necesarias**:

    ```bash
    pip install celery[redis] fastapi[celery]
    ```

    - **Configuración básica de Celery**: Crea un archivo `celery_app.py` para configurar Celery.

    ```python
    from celery import Celery

    celery_app = Celery(
        "myapp",
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0"
    )

    @celery_app.task
    def add(x, y):
        return x + y
    ```

    - **Integración con FastAPI**: En tu aplicación FastAPI, importa y usa Celery para ejecutar tareas en segundo plano.

    ```python
    from fastapi import FastAPI
    from .celery_app import celery_app

    app = FastAPI()

    @app.post("/process/")
    def process_task(x: int, y: int):
        task = celery_app.send_task("myapp.add", args=[x, y])
        return {"task_id": task.id, "status": "Processing"}
    ```

2. **Manejo de resultados de tareas**:

    - **Recuperar resultados**: Usa el ID de la tarea para recuperar el resultado.

    ```python
    from fastapi import HTTPException

    @app.get("/result/{task_id}")
    def get_result(task_id: str):
        result = celery_app.AsyncResult(task_id)
        if result.state == "PENDING":
            raise HTTPException(status_code=202, detail="Task still processing")
        elif result.state != "SUCCESS":
            raise HTTPException(status_code=400, detail="Task failed")
        return {"status": result.state, "result": result.result}
    ```

    - **Manejo de errores**: Implementa un manejo de errores adecuado para tareas fallidas.

    ```python
    @celery_app.task(bind=True)
    def faulty_task(self, x, y):
        try:
            # Simulate a faulty task
            result = x / y
        except Exception as exc:
            raise self.retry(exc=exc)
        return result
    ```

##### **Paso 2: Integración con Redis para caché y gestión de sesiones**

1. **Configurar Redis como caché**:

    - **Instalación de Redis y librerías necesarias**:

    ```bash
    pip install redis fastapi-cache2
    ```

    - **Configuración básica de Redis**: Configura Redis como backend de caché en FastAPI.

    ```python
    from fastapi import FastAPI
    from fastapi_cache import FastAPICache
    from fastapi_cache.backends.redis import RedisBackend
    import redis

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    ```

    - **Caché en endpoints**: Usa decoradores para cachear respuestas de endpoints.

    ```python
    from fastapi_cache.decorator import cache

    @app.get("/items/{item_id}")
    @cache(expire=60)
    async def read_item(item_id: int):
        return {"item_id": item_id, "value": "This is a cached response"}
    ```

2. **Gestión de sesiones con Redis**:

    - **Implementación de sesiones**: Usa Redis para almacenar y gestionar sesiones de usuario.

    ```python
    from fastapi import Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer
    import redis

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def get_current_user(token: str = Depends(oauth2_scheme)):
        user = redis_client.get(token)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return user
    ```

    - **Almacenar sesiones**: Guarda tokens de sesión en Redis cuando el usuario se autentica.

    ```python
    @app.post("/token")
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        token = create_access_token(user)
        redis_client.setex(token, 3600, user)  # Expira en una hora
        return {"access_token": token, "token_type": "bearer"}
    ```

##### **Paso 3: Casos de uso avanzados**

1. **Procesamiento masivo de datos**:

    - **Usar Celery para procesar grandes volúmenes de datos en segundo plano**: Celery es ideal para tareas que requieren un procesamiento intensivo y no pueden ser manejadas en tiempo real.

    ```python
    @celery_app.task
    def process_large_dataset(dataset):
        # Procesamiento de grandes volúmenes de datos
        processed_data = [process_item(item) for item in dataset]
        return processed_data
    ```

    - **Usar Redis para almacenar temporalmente los resultados**: Almacena resultados intermedios en Redis para su acceso rápido.

    ```python
    def save_intermediate_results(task_id, data):
        redis_client.setex(task_id, 3600, data)  # Expira en una hora
    ```

2. **Notificaciones en tiempo real**:

    - **Implementar notificaciones push usando Redis**: Redis puede ser usado para manejar canales de publicación/suscripción (`pub/sub`) para notificaciones en tiempo real.

    ```python
    def send_notification(channel, message):
        redis_client.publish(channel, message)
    ```

---

#### **5. Arquitecturas orientadas a microservicios**

Las arquitecturas orientadas a microservicios dividen una aplicación en servicios pequeños, independientes y desplegables, cada uno de los cuales ejecuta una función específica. Esta aproximación facilita el escalado, la mantenibilidad y la resiliencia de las aplicaciones modernas. En esta sección, aprenderás cómo estructurar tu aplicación FastAPI como una colección de microservicios y cómo gestionarlos eficazmente.

##### **Paso 1: Descomposición de la aplicación en microservicios**

1. **Identificación de dominios y servicios**:

    - **Dividir la aplicación en módulos independientes**: Analiza las funciones principales de tu aplicación y divídelas en servicios independientes, como autenticación, gestión de usuarios, inventario, etc.

    ```plaintext
    - Auth Service: Maneja la autenticación y autorización.
    - User Service: Gestiona la información y operaciones relacionadas con usuarios.
    - Product Service: Gestiona productos, inventario, etc.
    - Order Service: Maneja pedidos y transacciones.
    ```

    - **Desarrollo de servicios independientes**: Cada microservicio debe tener su propio repositorio, base de datos y entorno de despliegue.

    ```plaintext
    - auth_service/
    - user_service/
    - product_service/
    - order_service/
    ```

2. **Comunicación entre microservicios**:

    - **API Gateway**: Implementa un API Gateway como un punto de entrada único para todas las solicitudes, que enruta las peticiones a los microservicios correspondientes.

    ```python
    from fastapi import FastAPI, HTTPException, Request

    app = FastAPI()

    @app.get("/{service}/{path:path}")
    async def gateway(service: str, path: str, request: Request):
        if service == "auth":
            # Redirigir a auth_service
        elif service == "user":
            # Redirigir a user_service
        # y así sucesivamente...
        else:
            raise HTTPException(status_code=404, detail="Service not found")
    ```

    - **Mensajería y colas**: Usa sistemas de mensajería como RabbitMQ o Redis para comunicar eventos entre microservicios de forma asincrónica.

    ```python
    import pika

    def send_message(queue, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=message)
        connection.close()
    ```

##### **Paso 2: Gestión de microservicios**

1. **Orquestación con Kubernetes**:

    - **Despliegue y gestión de microservicios**: Usa Kubernetes para orquestar los microservicios, gestionando su escalabilidad, disponibilidad y actualización.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: auth-service
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: auth-service
      template:
        metadata:
          labels:
            app: auth-service
        spec:
          containers:
          - name: auth-service
            image: user/auth-service:latest
            ports:
            - containerPort: 80
    ```

    - **Servicios de descubrimiento**: Usa Kubernetes para habilitar el descubrimiento de servicios, permitiendo que los microservicios se encuentren y comuniquen entre sí.

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: auth-service
    spec:
      selector:
        app: auth-service
      ports:
      - protocol: TCP
        port: 80
        targetPort: 80
    ```

2. **Gestión de la configuración y secretos**:

    - **Uso de ConfigMaps y Secrets**: Almacena y gestiona la configuración de los microservicios usando ConfigMaps y Secrets en Kubernetes.

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: app-config
    data:
      DB_HOST: "database-service"
      DB_PORT: "5432"
    ```

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-secret
    type: Opaque
    data:
      DB_PASSWORD: <base64-encoded-password>
    ```

3. **Monitorización y logging**:

    - **Implementación de herramientas de monitorización**: Usa Prometheus y Grafana para monitorizar los microservicios y visualizar métricas en tiempo real.

    - **Centralización de logs**: Implementa ELK Stack (Elasticsearch, Logstash, Kibana) para la centralización y análisis de logs.

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: fluentd-config
    data:
      fluent.conf: |
        <source>
          @type tail
          path /var/log/containers/*.log
          pos_file /var/log/fluentd-containers.log.pos
          tag kubernetes.*
        </source>
    ```

##### **Paso 3: Estrategias avanzadas de microservicios**

1. **Tolerancia a fallos y recuperación**:

    - **Implementación de patrones de resiliencia**: Usa circuit breakers, retries, y timeouts para manejar fallos de manera eficiente.

    ```python
    import requests
    from requests.exceptions import RequestException

    def call_service(url):
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            return response.json()
        except RequestException:
            # Implementar lógica de retry o fallback
            pass
    ```

    - **Replicación y alta disponibilidad**: Asegura que los microservicios críticos estén replicados y disponibles en múltiples zonas.

2. **Versionado de servicios**:

    - **Manejo de versiones de API**: Define y gestiona versiones de los microservicios para mantener la compatibilidad hacia atrás mientras evolucionas tu API.

    ```python
    app = FastAPI()

    @app.get("/v1/items/")
    async def read_items_v1():
        return [{"item_id": 1, "name": "Item V1"}]

    @app.get("/v2/items/")
    async def read_items_v2():
        return [{"item_id": 1, "name": "Item V2", "price": 100}]
    ```

    - **Estrategias de despliegue con versiones**: Implementa despliegues canarios o blue-green para introducir nuevas versiones de servicios sin interrumpir el servicio actual.

3. **Seguridad y autenticación entre microservicios**:

    - **Autenticación mutua TLS**: Usa certificados para autenticar y asegurar la comunicación entre microservicios.

    - **Implementación de OAuth2/OpenID**: Usa OAuth2 o OpenID Connect para la autenticación segura entre microservicios.

    ```python
    from fastapi import Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def authenticate_microservice(token: str = Depends(oauth2_scheme)):
        # Verificar token y autenticación del microservicio
        pass
    ```
---

#### **6. Gestión de permisos y roles complejos**

La gestión de permisos y roles complejos es esencial en aplicaciones que requieren control granular sobre las acciones que los usuarios pueden realizar. Implementar un sistema de roles y permisos en FastAPI te permite definir quién puede acceder a qué recursos y con qué nivel de privilegio. En esta sección, exploraremos cómo configurar y manejar roles y permisos de manera eficiente en FastAPI.

##### **Paso 1: Definición de roles y permisos**

1. **Estructuración de roles**:

    - **Definir roles básicos**: Empieza definiendo roles básicos como `admin`, `user`, `moderator`, etc. Cada rol tiene un conjunto de permisos asociados.

    ```python
    roles_permissions = {
        "admin": ["read", "write", "delete", "update"],
        "user": ["read", "update"],
        "moderator": ["read", "update", "delete"]
    }
    ```

    - **Roles jerárquicos**: Puedes implementar roles jerárquicos donde un rol superior (como `admin`) hereda los permisos de roles inferiores.

    ```python
    def get_permissions(role):
        if role == "admin":
            return roles_permissions["admin"]
        elif role == "moderator":
            return roles_permissions["moderator"]
        elif role == "user":
            return roles_permissions["user"]
        return []
    ```

2. **Asignación de roles a usuarios**:

    - **Almacenar roles en la base de datos**: Los roles deben estar asociados a los usuarios en la base de datos para facilitar su gestión.

    ```python
    from sqlalchemy import Column, String, Integer, ForeignKey
    from sqlalchemy.orm import relationship

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        role = Column(String, ForeignKey("roles.name"))
        role_relationship = relationship("Role", back_populates="users")

    class Role(Base):
        __tablename__ = "roles"

        name = Column(String, primary_key=True)
        users = relationship("User", back_populates="role_relationship")
    ```

##### **Paso 2: Implementación de permisos en FastAPI**

1. **Middleware para manejo de permisos**:

    - **Creación de un middleware de permisos**: Implementa un middleware para verificar si el usuario tiene los permisos necesarios antes de permitir el acceso a un recurso.

    ```python
    from fastapi import Request, HTTPException
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    async def check_permissions(request: Request, call_next):
        token = await oauth2_scheme(request)
        # Recuperar el usuario a partir del token
        user = get_user_from_token(token)
        if not user:
            raise HTTPException(status_code=403, detail="Invalid credentials")

        # Verificar permisos del usuario
        endpoint = request.url.path
        method = request.method.lower()
        if not has_permission(user.role, endpoint, method):
            raise HTTPException(status_code=403, detail="Insufficient permissions")

        response = await call_next(request)
        return response
    ```

2. **Decoradores para proteger endpoints**:

    - **Uso de decoradores para verificar permisos**: Usa decoradores para proteger los endpoints, asegurándote de que solo los usuarios con los permisos adecuados puedan acceder a ellos.

    ```python
    from functools import wraps
    from fastapi import HTTPException

    def require_permission(permission):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                user = get_current_user()
                if permission not in get_permissions(user.role):
                    raise HTTPException(status_code=403, detail="You do not have permission to perform this action")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @app.get("/admin/data")
    @require_permission("read")
    async def read_admin_data():
        return {"data": "This is admin data"}
    ```

3. **Gestión dinámica de permisos**:

    - **Asignación dinámica de permisos**: Permite la asignación dinámica de permisos a roles mediante un panel de administración o comandos específicos.

    ```python
    def assign_permission_to_role(role, permission):
        roles_permissions[role].append(permission)

    def revoke_permission_from_role(role, permission):
        roles_permissions[role].remove(permission)
    ```

##### **Paso 3: Integración con OAuth2 y JWT**

1. **Autenticación con OAuth2 y manejo de tokens**:

    - **Generación de tokens con JWT**: Implementa un sistema de autenticación con JWT, donde los tokens incluyen información sobre los roles y permisos del usuario.

    ```python
    from jose import JWTError, jwt

    SECRET_KEY = "your_secret_key"
    ALGORITHM = "HS256"

    def create_access_token(data: dict):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Token is invalid or expired")
    ```

    - **Verificación de permisos a través del token**: Al decodificar el token, extrae los roles y permisos del usuario y verifica que sean suficientes para acceder al recurso solicitado.

    ```python
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        payload = verify_token(token)
        user = get_user_from_payload(payload)
        return user
    ```

2. **Autorización granular con scopes**:

    - **Uso de scopes para manejar permisos específicos**: Los scopes permiten definir acciones específicas que un token puede autorizar, permitiendo un control más granular.

    ```python
    from fastapi.security import OAuth2PasswordBearer

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", scopes={"read": "Read access", "write": "Write access"})

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        payload = verify_token(token)
        user = get_user_from_payload(payload)
        if "read" not in payload.get("scopes", []):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    ```

---

#### **7. Creación de plugins y extensiones**

Desarrollar plugins y extensiones para FastAPI permite extender las funcionalidades de la aplicación sin modificar su núcleo, promoviendo la modularidad y la reutilización de código. En esta sección, exploraremos cómo diseñar, implementar, y gestionar plugins y extensiones que añadan capacidades adicionales a tu aplicación FastAPI.

##### **Paso 1: Diseño de la arquitectura de un plugin**

1. **Estructura básica de un plugin**:

    - **Directorio del plugin**: Cada plugin debe tener su propio directorio, lo que facilita la organización y la integración en el proyecto principal.

    ```plaintext
    /my_fastapi_project/
    ├── /app/
    ├── /plugins/
    │   ├── /my_plugin/
    │   │   ├── __init__.py
    │   │   ├── main.py
    │   │   ├── routes.py
    │   │   └── dependencies.py
    └── main.py
    ```

    - **Definición de la clase del plugin**: Cada plugin puede ser representado por una clase que encapsula sus rutas, dependencias y otras configuraciones.

    ```python
    from fastapi import FastAPI

    class MyPlugin:
        def __init__(self, app: FastAPI):
            self.app = app
            self.register_routes()

        def register_routes(self):
            @self.app.get("/plugin-endpoint")
            def plugin_endpoint():
                return {"message": "Hello from the plugin!"}
    ```

2. **Configuración de dependencias**:

    - **Registrar dependencias del plugin**: Si tu plugin requiere dependencias, debes asegurarte de registrarlas y gestionarlas de manera modular.

    ```python
    from fastapi import Depends

    def my_plugin_dependency():
        return {"dependency_data": "Important data"}

    class MyPlugin:
        def __init__(self, app: FastAPI):
            self.app = app
            self.register_routes()

        def register_routes(self):
            @self.app.get("/plugin-endpoint")
            def plugin_endpoint(dep=Depends(my_plugin_dependency)):
                return {"message": "Hello from the plugin!", "data": dep}
    ```

##### **Paso 2: Implementación de plugins en FastAPI**

1. **Integración del plugin en la aplicación principal**:

    - **Carga de plugins en el arranque**: Los plugins deben cargarse durante la inicialización de la aplicación principal, permitiendo que sus rutas y dependencias se integren de manera automática.

    ```python
    from fastapi import FastAPI
    from plugins.my_plugin.main import MyPlugin

    app = FastAPI()

    # Cargar el plugin
    MyPlugin(app)
    ```

2. **Uso de eventos para inicializar plugins**:

    - **Inicialización en eventos de FastAPI**: Usa eventos de FastAPI para inicializar o configurar los plugins en momentos específicos, como al iniciar la aplicación.

    ```python
    @app.on_event("startup")
    async def startup_event():
        MyPlugin(app)
    ```

    - **Eventos para cleanup**: Implementa eventos para limpiar o liberar recursos que el plugin pueda estar utilizando.

    ```python
    @app.on_event("shutdown")
    async def shutdown_event():
        # Realizar cleanup del plugin si es necesario
        pass
    ```

##### **Paso 3: Creación de extensiones reutilizables**

1. **Extensiones modulares**:

    - **Diseño de extensiones reutilizables**: Las extensiones deben ser modulares y fácilmente integrables en diferentes proyectos FastAPI. Pueden incluir funcionalidades como autenticación, gestión de archivos, o manejo de cache.

    ```python
    class AuthExtension:
        def __init__(self, app: FastAPI):
            self.app = app
            self.setup_auth()

        def setup_auth(self):
            @self.app.post("/auth/login")
            def login():
                # Lógica de autenticación
                pass

            @self.app.get("/auth/user")
            def get_user():
                # Lógica para obtener datos del usuario
                pass
    ```

    - **Distribución de extensiones**: Puedes empaquetar tus extensiones y publicarlas en PyPI para que otros desarrolladores las usen.

    ```plaintext
    setup(
        name="fastapi-auth-extension",
        version="0.1.0",
        description="A reusable authentication extension for FastAPI",
        packages=find_packages(),
        install_requires=[
            "fastapi",
            "pydantic",
        ],
    )
    ```

2. **Gestión de configuraciones y opciones**:

    - **Configuración flexible**: Permite que las extensiones acepten configuraciones específicas del proyecto donde se integran, asegurando su flexibilidad.

    ```python
    class AuthExtension:
        def __init__(self, app: FastAPI, auth_config: dict):
            self.app = app
            self.auth_config = auth_config
            self.setup_auth()

        def setup_auth(self):
            # Usar self.auth_config para personalizar la autenticación
            pass
    ```

    - **Sobrecarga de configuraciones por el usuario**: Asegúrate de que las configuraciones predeterminadas puedan ser sobreescritas por las configuraciones del proyecto.

    ```python
    app = FastAPI()

    auth_config = {
        "jwt_secret": "mysecretkey",
        "token_expiration": 3600,
    }

    AuthExtension(app, auth_config=auth_config)
    ```

### **Estructura de Carpetas para una API en FastApi**

Aquí tienes una guía para estructurar las carpetas de una API basada en una arquitectura modular y escalable. Esta estructura es adecuada para APIs pequeñas y medianas.

![EstructuraDeUnApi](/img/EstructuraFastApi.svg)

##### Estructura de Carpetas para una API

```
/api-project
│
├── /app
│   ├── /models            # Definición de modelos (p. ej., SQLAlchemy o Mongoose)
│   ├── /schemas           # Validación de datos y serialización (p. ej., Pydantic o Joi)
│   ├── /services          # Lógica de negocio y servicios (interacciones con los modelos)
│   ├── /routes            # Endpoints de la API
│   ├── /controllers       # Lógica de controladores, maneja las rutas y solicitudes
│   ├── /middlewares       # Middlewares personalizados (autenticación, logging, CORS)
│   ├── /utils             # Funciones auxiliares (helpers, constantes, formateadores)
│   ├── /tests             # Pruebas unitarias y de integración
│   ├── /static            # Archivos estáticos (imágenes, CSS, JS)
│   └── __init__.py        # Inicialización de la aplicación
│
├── /config                # Configuraciones (base de datos, entorno, API keys)
│   ├── settings.py        # Configuración de variables de entorno
│   ├── db.py              # Configuración de la base de datos
│   └── logging.py         # Configuración del logging
│
├── /migrations            # Scripts de migración de la base de datos (Alembic, LeamBic)
│
├── /docs                  # Documentación de la API (Swagger, OpenAPI)
│
├── .env                   # Variables de entorno (NO subir a producción)
├── .gitignore             # Archivos y carpetas a ignorar en Git
├── README.md              # Documentación inicial del proyecto
└── main.py                # Archivo principal que inicia la aplicación
```
##### Explicación de las carpetas

1. **app**: Directorio principal que contiene la lógica de la aplicación.
   - **models**: Define los modelos de la base de datos.
   - **schemas**: Maneja la validación y serialización de datos de entrada y salida.
   - **services**: Lógica de negocio que interactúa con los modelos.
   - **routes**: Definición de las rutas o endpoints de la API.
   - **controllers**: Maneja la lógica de cada ruta y delega tareas a servicios o modelos.
   - **middlewares**: Funciones que se ejecutan antes o después de las solicitudes (autenticación, CORS, etc.).
   - **utils**: Funciones auxiliares que se utilizan en distintas partes de la aplicación.
   - **tests**: Pruebas para garantizar que la API funciona como se espera.

2. **config**: Archivo para las configuraciones globales del proyecto.
   - **settings.py**: Aquí irían las variables de entorno, configuraciones de la API, etc.
   - **db.py**: Configuración de la conexión a la base de datos.
   - **logging.py**: Configuración de los logs para seguimiento y depuración.

3. **migrations**: Carpeta donde se colocan las migraciones de base de datos (Alembic, LeamBic).

4. **docs**: Espacio para la documentación de la API, como el archivo Swagger u OpenAPI.

5. **.env**: Archivo de variables de entorno (clave API, conexión a la DB).

6. **main.py**: El punto de entrada de la aplicación. Aquí se configuran los servidores, middlewares y las rutas.
